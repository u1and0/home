# -*- coding: UTF-8 -*-

import errno
import re
import threading
import traceback

import sublime

import SublimeHaskell.internals.proc_helper as ProcHelper
import SublimeHaskell.internals.logging as Logging
import SublimeHaskell.internals.settings as Settings
import SublimeHaskell.internals.output_collector as OutputCollector
import SublimeHaskell.parseoutput as ParseOutput
import SublimeHaskell.ghci_backend as GHCIMod


def show_hdevtools_error_and_disable():
    # Looks like we can't always get an active window here,
    # we use sublime.error_message() instead of
    # output_error(sublime.active_window().
    sublime.set_timeout(lambda: sublime.error_message(
        "SublimeHaskell: hdevtools was not found!\n"
        "It's used for 'symbol info' and type inference\n"
        "Install it with 'cabal install hdevtools',\n"
        "or adjust the 'add_to_PATH' setting for a custom location.\n"
        "'enable_hdevtools' automatically set to False in the User settings."), 0)

    Settings.PLUGIN.enable_hdevtools = False


def call_hdevtools_and_wait(arg_list, filename=None, cabal=None):
    """
    Calls hdevtools with the given arguments.
    Shows a sublime error message if hdevtools is not available.
    """
    ghc_opts_args = GHCIMod.get_ghc_opts_args(filename, cabal=cabal)
    hdevtools_socket = Settings.PLUGIN.hdevtools_socket
    source_dir = ProcHelper.get_source_dir(filename)

    if hdevtools_socket:
        arg_list.append('--socket={0}'.format(hdevtools_socket))

    try:
        exit_code, out, err = ProcHelper.ProcHelper.run_process(['hdevtools'] + arg_list + ghc_opts_args, cwd=source_dir)
        if exit_code != 0:
            show_hdevtools_error_and_disable()
            raise Exception("hdevtools exited with status %d and stderr: %s" % (exit_code, err))
        return out

    except OSError as os_exc:
        if os_exc.errno == errno.ENOENT:
            show_hdevtools_error_and_disable()
        return None


def admin(cmds, wait=False, **popen_kwargs):
    if not Settings.PLUGIN.enable_hdevtools:
        return None

    hdevtools_socket = Settings.PLUGIN.hdevtools_socket

    if hdevtools_socket:
        cmds.append('--socket={0}'.format(hdevtools_socket))

    command = ["hdevtools", "admin"] + cmds

    try:
        if wait:
            exit_code, stdout, stderr = ProcHelper.ProcHelper.run_process(command, **popen_kwargs)
            return stdout if exit_code == 0 else 'error running {0}: {1}'.format(command, stderr)
        else:
            proc = ProcHelper.ProcHelper(command, **popen_kwargs)
            OutputCollector.DescriptorDrain('hdevtools stdout', proc.process.stdout).start()
            OutputCollector.DescriptorDrain('hdevtools stderr', proc.process.stderr).start()
            return ''

    except OSError as os_exc:
        if os_exc.errno == errno.ENOENT:
            show_hdevtools_error_and_disable()

        Settings.PLUGIN.enable_hdevtools = False

        return None
    except Exception:
        Logging.log('hdevtools.admin failed with exception, see console window traceback')
        traceback.print_exc()
        return None


def is_running():
    hdevtool = admin(['--status'], wait=True)
    return hdevtool and re.search(r'running', hdevtool)


def start_server():
    if not is_running():
        admin(["--start-server"])


def hdevtools_info(filename, symbol_name, cabal=None):
    """
    Uses hdevtools info filename symbol_name to get symbol info
    """
    contents = call_hdevtools_and_wait(['info', filename, symbol_name], filename=filename, cabal=cabal)
    return ParseOutput.parse_info(symbol_name, contents) if contents else None


def hdevtools_check(filename, cabal=None):
    """
    Uses hdevtools to check file
    """
    return call_hdevtools_and_wait(['check', filename], filename=filename, cabal=cabal)


def hdevtools_type(filename, line, column, cabal=None):
    """
    Uses hdevtools to infer type
    """
    return call_hdevtools_and_wait(['type', filename, str(line), str(column)], filename=filename, cabal=cabal)


def start_hdevtools():
    thread = threading.Thread(target=start_server)
    thread.start()


def stop_hdevtools():
    admin(["--stop-server"])
