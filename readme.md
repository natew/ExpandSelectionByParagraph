# About
Being used to vims paragraph navigation using Shift+[ and Shift+] I had found an equivalent for Sublime:

```
    { "keys": ["alt+down"], "command": "move", "args": {"by": "stops", "empty_line": true, "forward": true} },
    { "keys": ["alt+up"], "command": "move", "args": {"by": "stops", "empty_line": true, "forward": false} },
```

But I kept getting frustrated that I couldn't add the shift modifier to use the same command to select blocks of text by paragraph.  This plugin does just that, allows you to select text in blocks of paragraphs.


# Installation

*Add using Sublime Package Control*


# Keyboard Shortcuts

Now, to use this plugin just add something like this:

```
    // Select by paragraph
    { "keys": ["alt+shift+down"], "command": "expand_selection_by_paragraph_down" },
    { "keys": ["alt+shift+up"], "command": "expand_selection_by_paragraph_up" }
```
