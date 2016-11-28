# https://jupyter.org/qtconsole/stable/config_options.html
# Configuration options
# =====================

# These options can be set in ``~/.jupyer/jupyter_qtconsole_config.py``, or
# at the command line when you start it.


# ConnectionFileMixin.connection_file : Unicode
#     Default: ``''``

#     JSON file in which to store connection info [default: kernel-<pid>.json]

#     This file will contain the IP, ports, and authentication key needed to connect
#     clients to this kernel. By default, this file will be created in the security dir
#     of the current profile, but can be specified by absolute path.


# ConnectionFileMixin.control_port : Int
#     Default: ``0``

#     set the control (ROUTER) port [default: random]

# ConnectionFileMixin.hb_port : Int
#     Default: ``0``

#     set the heartbeat port [default: random]

# ConnectionFileMixin.iopub_port : Int
#     Default: ``0``

#     set the iopub (PUB) port [default: random]

# ConnectionFileMixin.ip : Unicode
#     Default: ``''``

#     Set the kernel's IP address [default localhost].
#     If the IP address is something other than localhost, then
#     Consoles on other machines will be able to connect
#     to the Kernel, so be careful!

# ConnectionFileMixin.shell_port : Int
#     Default: ``0``

#     set the shell (ROUTER) port [default: random]

# ConnectionFileMixin.stdin_port : Int
#     Default: ``0``

#     set the stdin (ROUTER) port [default: random]

# ConnectionFileMixin.transport : 'tcp'|'ipc'
#     Default: ``'tcp'``

#     No description

# JupyterConsoleApp.confirm_exit : CBool
#     Default: ``True``


#     Set to display confirmation dialog on exit. You can always use 'exit' or 'quit',
#     to force a direct exit without any confirmation.

# JupyterConsoleApp.existing : CUnicode
#     Default: ``''``

#     Connect to an already running kernel

# JupyterConsoleApp.kernel_name : Unicode
#     Default: ``'python'``

#     The name of the default kernel to start.

# JupyterConsoleApp.sshkey : Unicode
#     Default: ``''``

#     Path to the ssh key to use for logging in to the ssh server.

# JupyterConsoleApp.sshserver : Unicode
#     Default: ``''``

#     The SSH server to use to connect to the kernel.


# Application.log_datefmt : Unicode
#     Default: ``'%Y-%m-%d %H:%M:%S'``

#     The date format used by logging formatters for %(asctime)s

# Application.log_format : Unicode
#     Default: ``'[%(name)s]%(highlevel)s %(message)s'``

#     The Logging format template

# Application.log_level : 0|10|20|30|40|50|'DEBUG'|'INFO'|'WARN'|'ERROR'|'CRITICAL'
#     Default: ``30``

#     Set the log level by value or name.

# JupyterApp.answer_yes : Bool
#     Default: ``False``

#     Answer yes to any prompts.

# JupyterApp.config_file : Unicode
#     Default: ``''``

#     Full path of a config file.

# JupyterApp.config_file_name : Unicode
#     Default: ``''``

#     Specify a config file to load.

# JupyterApp.generate_config : Bool
#     Default: ``False``

#     Generate default config file.

# JupyterQtConsoleApp.display_banner : CBool
#     Default: ``True``

#     Whether to display a banner upon starting the QtConsole.

c.JupyterQtConsoleApp.hide_menubar = True
# JupyterQtConsoleApp.hide_menubar : CBool
#     Default: ``False``

#     Start the console window with the menu bar hidden.

# JupyterQtConsoleApp.maximize : CBool
#     Default: ``False``

#     Start the console window maximized.

# JupyterQtConsoleApp.plain : CBool
#     Default: ``False``

#     Use a plaintext widget instead of rich text (plain can't print/save).

# JupyterQtConsoleApp.stylesheet : Unicode
#     Default: ``''``

#     path to a custom CSS stylesheet


# ConsoleWidget.ansi_codes : Bool
#     Default: ``True``

#     Whether to process ANSI escape codes.

# ConsoleWidget.buffer_size : Int
#     Default: ``500``


#     The maximum number of lines of text before truncation. Specifying a
#     non-positive number disables text truncation (not recommended).


# ConsoleWidget.execute_on_complete_input : Bool
#     Default: ``True``

#     Whether to automatically execute on syntactically complete input.

#     If False, Shift-Enter is required to submit each execution.
#     Disabling this is mainly useful for non-Python kernels,
#     where the completion check would be wrong.


# ConsoleWidget.font_family : Unicode
#     Default: ``''``

#     The font family to use for the console.
#     On OSX this defaults to Monaco, on Windows the default is
#     Consolas with fallback of Courier, and on other platforms
#     the default is Monospace.


# ConsoleWidget.font_size : Int
#     Default: ``0``

#     The font size. If unconfigured, Qt will be entrusted
#     with the size of the font.


# ConsoleWidget.gui_completion : 'plain'|'droplist'|'ncurses'
#     Default: ``'ncurses'``


#     The type of completer to use. Valid values are:

#     'plain'   : Show the available completion as a text list
#                 Below the editing area.
#     'droplist': Show the completion in a drop down list navigable
#                 by the arrow keys, and from which you can select
#                 completion by pressing Return.
#     'ncurses' : Show the completion as a text list which is navigable by
#                 `tab` and arrow keys.


# ConsoleWidget.height : Int
#     Default: ``25``

#     The height of the console at start time in number
#     of characters (will double with `vsplit` paging)


# ConsoleWidget.include_other_output : Bool
#     Default: ``False``

#     Whether to include output from clients
#     other than this one sharing the same kernel.

#     Outputs are not displayed until enter is pressed.


# ConsoleWidget.kind : 'plain'|'rich'
#     Default: ``'plain'``


#     The type of underlying text widget to use. Valid values are 'plain',
#     which specifies a QPlainTextEdit, and 'rich', which specifies a
#     QTextEdit.


# ConsoleWidget.paging : 'inside'|'hsplit'|'vsplit'|'custom'|'none'
#     Default: ``'inside'``


#     The type of paging to use. Valid values are:

#     'inside'
#        The widget pages like a traditional terminal.
#     'hsplit'
#        When paging is requested, the widget is split horizontally. The top
#        pane contains the console, and the bottom pane contains the paged text.
#     'vsplit'
#        Similar to 'hsplit', except that a vertical splitter is used.
#     'custom'
#        No action is taken by the widget beyond emitting a
#        'custom_page_requested(str)' signal.
#     'none'
#        The text is written directly to the console.


# ConsoleWidget.width : Int
#     Default: ``81``

#     The width of the console at start time in number
#     of characters (will double with `hsplit` paging)


# HistoryConsoleWidget.history_lock : Bool
#     Default: ``False``

#     No description

# FrontendWidget.banner : Unicode
#     Default: ``''``

#     No description

# FrontendWidget.clear_on_kernel_restart : Bool
#     Default: ``True``

#     Whether to clear the console when the kernel is restarted

# FrontendWidget.confirm_restart : Bool
#     Default: ``True``

#     Whether to ask for user confirmation when restarting kernel

# FrontendWidget.enable_calltips : Bool
#     Default: ``True``

#     Whether to draw information calltips on open-parentheses.

# FrontendWidget.is_complete_timeout : Float
#     Default: ``0.25``

#     Seconds to wait for is_complete replies from the kernel.

# FrontendWidget.lexer_class : DottedObjectName
#     Default: ``traitlets.Undefined``

#     The pygments lexer class to use.


# JupyterWidget.editor : Unicode
#     Default: ``''``


#     A command for invoking a system text editor. If the string contains a
#     {filename} format specifier, it will be used. Otherwise, the filename
#     will be appended to the end the command.


# JupyterWidget.editor_line : Unicode
#     Default: ``''``


#     The editor command to use when a specific line number is requested. The
#     string should contain two format specifiers: {line} and {filename}. If
#     this parameter is not specified, the line number option to the %edit
#     magic will be ignored.


# JupyterWidget.in_prompt : Unicode
#     Default: ``'In [<span class="in-prompt-number">%i</span>]: '``

#     No description

# JupyterWidget.input_sep : Unicode
#     Default: ``'\\n'``

#     No description

# JupyterWidget.out_prompt : Unicode
#     Default: ``'Out[<span class="out-prompt-number">%i</span>]: '``

#     No description

# JupyterWidget.output_sep : Unicode
#     Default: ``''``

#     No description

# JupyterWidget.output_sep2 : Unicode
#     Default: ``''``

#     No description

# JupyterWidget.style_sheet : Unicode
#     Default: ``''``


#     A CSS stylesheet. The stylesheet can contain classes for:
#         1. Qt: QPlainTextEdit, QFrame, QWidget, etc
#         2. Pygments: .c, .k, .o, etc. (see PygmentsHighlighter)
#         3. QtConsole: .error, .in-prompt, .out-prompt, etc


c.JupyterWidget.syntax_style = 'monokai'
# JupyterWidget.syntax_style : Unicode
#     Default: ``''``


#     If not empty, use this Pygments style for syntax highlighting.
#     Otherwise, the style sheet is queried for Pygments style
#     information.


# KernelManager.autorestart : Bool
#     Default: ``False``

#     Should we autorestart the kernel if it dies.

# KernelManager.kernel_cmd : List
#     Default: ``[]``

#     DEPRECATED: Use kernel_name instead.

#     The Popen Command to launch the kernel.
#     Override this if you have a custom kernel.
#     If kernel_cmd is specified in a configuration file,
#     Jupyter does not pass any arguments to the kernel,
#     because it cannot make any assumptions about the
#     arguments that the kernel understands. In particular,
#     this means that the kernel does not receive the
#     option --debug if it given on the Jupyter command line.


# Session.buffer_threshold : Int
#     Default: ``1024``

#     Threshold (in bytes) beyond which an object's buffer should be extracted to avoid pickling.

# Session.copy_threshold : Int
#     Default: ``65536``

#     Threshold (in bytes) beyond which a buffer should be sent without copying.

# Session.debug : Bool
#     Default: ``False``

#     Debug output in the Session

# Session.digest_history_size : Int
#     Default: ``65536``

#     The maximum number of digests to remember.

#     The digest history will be culled when it exceeds this value.


# Session.item_threshold : Int
#     Default: ``64``

#     The maximum number of items for a container to be introspected for custom serialization.
#     Containers larger than this are pickled outright.


# Session.key : CBytes
#     Default: ``b''``

#     execution key, for signing messages.

# Session.keyfile : Unicode
#     Default: ``''``

#     path to file containing execution key.

# Session.metadata : Dict
#     Default: ``{}``

#     Metadata dictionary, which serves as the default top-level metadata dict for each message.

# Session.packer : DottedObjectName
#     Default: ``'json'``

#     The name of the packer for serializing messages.
#     Should be one of 'json', 'pickle', or an import name
#     for a custom callable serializer.

# Session.session : CUnicode
#     Default: ``''``

#     The UUID identifying this session.

# Session.signature_scheme : Unicode
#     Default: ``'hmac-sha256'``

#     The digest scheme used to construct the message signatures.
#     Must have the form 'hmac-HASH'.

# Session.unpacker : DottedObjectName
#     Default: ``'json'``

#     The name of the unpacker for unserializing messages.
#     Only used with custom functions for `packer`.

# Session.username : Unicode
#     Default: ``'minrk'``

#     Username for the Session. Default is your system username.
