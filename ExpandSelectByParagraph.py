import sublime, sublime_plugin

class ExpandSelectionForwardParagraphCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    cur_pos = self.view.sel()[0]
    self.view.run_command('move', {"by": "stops", "empty_line": True, "forward": True})
    new_end = self.view.sel()[0]
    self.view.sel().add( sublime.Region( cur_pos.begin(), new_end.end() ) )

class ExpandSelectionBackwardParagraphCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    cur_pos = self.view.sel()[0]
    self.view.run_command('move', {"by": "stops", "empty_line": True, "forward": False})
    new_begin = self.view.sel()[0]
    self.view.sel().add( sublime.Region( cur_pos.end(), new_begin.end() ) )
