# Introduction

Blockly is in active development with changes landing every day.  We are aware of many deficiencies and are working hard to address them.  Many of Blockly's features come from volunteer developers, so please feel free to dig into the code and send us contributions.

# Running Everywhere

It is important that everyone be able to use Blockly.  That means running in as many environments as possible:

  * [Translating Blockly](Translation) (or just some demo apps) into your language is extremely helpful.  Less that 5% of the world [speaks English](https://en.wikipedia.org/wiki/List_of_languages_by_number_of_native_speakers) natively.  Help us reach the billions of people who are missing out.
  * Touch screen support (for Android and iOS tablets in particular) is critical.  Currently Blockly kinda-sorta works, but we need to do much better.
  * Good support for IE 10 and IE 9 (IE 8 is assumed to be a lost cause).  The Google developers do not have easy access to Windows computers, so any help to improve IE is appreciated.

# New Blocks

Different applications need different blocks.  There are a few types of blocks that are repeatedly requested:

  * Text split, List join.  Split text into a list based on a delimiter, join a list into a text based on a separator.
  * List sort.  Choice of alphabetic, numeric, case-insensitive, and length modes.  Ascending or descending order.
  * 2D grids.  Arrays of arrays are clumsy and hard to visualize.  A new category of blocks that deals with grid data (spreadsheets) is needed.  Most of the existing list blocks would have grid equivalents.
  * Multi-line strings.  A block with a text area one can type paragraphs into.  Also useful would be a character picker widget that allows one to select Unicode characters.
  * Date/Time selection.  A calendar picker (similar to the existing colour picker) would allow users to choose dates and times easily.

# Improved UI

Blockly is designed to be clean and simple.  We don't want to add clutter.  But there are many ways that the UI may be improved:

  * Multi-block selection.  Hold shift to click many blocks, for group moves, collapsing, disabling or deleting.
  * Cursor control for accessibility.  Many users don't have good mouse-skills due to disabilities.  Adding keyboard shortcuts to manipulate Blockly would enable these users to participate.  The same shortcuts would also benefit power programmers.
  * Trash can contents.  Clicking on the trash can should bring up a bubble that contains everything that has been deleted.  These blocks may be dragged out of the trash and back into the workspace.
  * Improved variable rename dialog.  Shows a preview of how many variables are going to be renamed, warns of collisions, etc.

# Scalability

Writing large programs in most visual programming environments is cumbersome.  There are many interesting problems in allowing one to write large programs (many are challenging enough to produce publishable academic papers or dissertations if you feel so inclined).  The Blockly team is _currently_ focused on small educational applications, which means nobody is currently pursuing these:

  * Zooming in and out like Google Maps.  This is more than just scaling the workspace, details need to appear and disappear appropriately.
  * Multiple workspaces.  Break a large program into pieces, with parts in different tabs?
  * Variable scope.  Currently all variables are global, except for function arguments.  Large programs need some sort of scope.
  * Debugging hooks.  Being able to run a program, step forwards and backwards, inspect variables, set break points.
  * Search.  Find functions, callers, variables, and other code searching activities.  Likewise, a search and replace feature would allow for easier maintenance of code.
  * Libraries.  How does one bundle code into a reusable, publishable module that other programs may include and depend on?
  * Collaboration.  Blockly was designed from the beginning to integrate well with the [Google Drive SDK](https://developers.google.com/drive/realtime/).  This would allow real-time multi-user collaborative editing.

But most important of all, grab a copy of Blockly, integrate it with your apps, and see how your users like it.  We love to see Blockly out in the real world -- from teaching programming to students, to controlling heavy machinery in a factory.