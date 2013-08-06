![Demo](http://https://raw.github.com/natew/ExpandSelectionByParagraph/master/demo.gif)

Select text blocks by paragraphs in Sublime.  Supports version 2 and 3.


# About
Being used to vims paragraph navigation using Shift+[ and Shift+] I had found an equivalent for Sublime:

```
    { "keys": ["alt+down"], "command": "move", "args": {"by": "stops", "empty_line": true, "forward": true} },
    { "keys": ["alt+up"], "command": "move", "args": {"by": "stops", "empty_line": true, "forward": false} },
```

But I kept getting frustrated that I couldn't add the shift modifier to select blocks of text by paragraph, thus this plugin.


# Installation

Add using Sublime Package Control. Or, git clone this repo into your sublime Packages Directory.

To set up shortcuts, just add something like this:

```
    // Select by paragraph
    { "keys": ["alt+shift+down"], "command": "expand_selection_by_paragraph_down" },
    { "keys": ["alt+shift+up"], "command": "expand_selection_by_paragraph_up" }
```
