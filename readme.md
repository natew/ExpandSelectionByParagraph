# About
Being used to vims paragraph navigation using Shift+[ and Shift+] I had found an equivalent for Sublime:

```
    { "keys": ["alt+down"], "command": "move", "args": {"by": "stops", "empty_line": true, "forward": true} },
    { "keys": ["alt+up"], "command": "move", "args": {"by": "stops", "empty_line": true, "forward": false} },
```

But I kept getting frustrated that I couldn't add the shift modifier to use the same command to select blocks of text by paragraph.  This plugin does just that, allows you to select text in blocks of paragraphs.


# Installation

*Pending approval to Sublime Package Control*

Until then use package control to add this repo: `git@github.com:natew/ExpandSelectionByParagraph.git`


# Keyboard Shortcuts

```
    // Select by paragraph
    { "keys": ["alt+shift+down"], "command": "expand_selection_forward_paragraph" },
    { "keys": ["alt+shift+up"], "command": "expand_selection_backward_paragraph" }
```