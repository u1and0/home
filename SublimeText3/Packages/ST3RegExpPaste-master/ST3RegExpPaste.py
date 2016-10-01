import sublime
import sublime_plugin
import re

class myfuncRegCommand(sublime_plugin.TextCommand):
    def run(self, edit):

        for region in self.view.sel():
            txt = sublime.get_clipboard()
            esc_txt = re.sub(r'([\\])', r'/', txt)
            # esc_txt = re.sub(r'([\.\\\+\*\?\[\^\]\$\(\)\{\}\=\!\|])', r'\\\1', txt)

            #クオート内を何でもありにする
            #いらなかったらコメントアウトしてください
            esc_txt = re.sub(r'".+?"', '"(.+?)"', esc_txt)

            sublime.set_clipboard(esc_txt)
            self.view.window().run_command("paste")
