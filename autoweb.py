from .tools import curl2req
import sublime
import sublime_plugin


class autowebCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        line_one = self.view.line(1)
        curl = self.view.substr(line_one)
        script = curl2req.convert(curl)
        self.view.erase(edit, line_one)
        self.view.insert(edit, 0, script)
