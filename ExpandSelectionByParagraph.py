import sublime, sublime_plugin

def has_selection(sel):
  return sel.begin() != sel.end()

def cursor_at_top_of_selection(sel):
  return sel.b == sel.begin()

def cursor_at_bottom_of_selection(sel):
  return sel.b == sel.end()

def change_up_selection(view, upward):
  current_sel = view.sel()[0]
  view.run_command('move', {"by": "stops", "empty_line": True, "forward": not upward})
  new_sel = view.sel()[0]
  view.sel().add(
    sublime.Region( current_sel.end(), new_sel.begin() )
  )

def change_down_selection(view, upward):
  current_sel = view.sel()[0]
  view.run_command('move', {"by": "stops", "empty_line": True, "forward": not upward})
  new_sel = view.sel()[0]
  view.sel().add(
    sublime.Region( current_sel.begin(), new_sel.end() )
  )

class ExpandSelectionByParagraphUpCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    ParagraphSelection.expand(self, True)

class ExpandSelectionByParagraphDownCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    ParagraphSelection.expand(self, False)

class ParagraphSelection():
  def expand(self, up):
    for sel in self.view.sel():
      if has_selection(sel):
        if cursor_at_top_of_selection(sel):
          change_up_selection(self.view, up)
        elif cursor_at_bottom_of_selection(sel):
          change_down_selection(self.view, up)
      else:
        if cursor_at_top_of_selection(sel):
          change_up_selection(self.view, up)
        elif cursor_at_bottom_of_selection(sel):
          change_down_selection(self.view, up)