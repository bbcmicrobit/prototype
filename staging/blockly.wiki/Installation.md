# Introduction

Blockly is designed to easily install into your web application.  Users drag blocks around, Blockly generates code, your application does something with that code.  From your application's point of view Blockly is just a textarea in which the user types syntactically perfect JavaScript, Python, Dart, or other language.

Blockly is 100% client-side, requiring no support from the server (unless one wants to use the cloud-storage or realtime collaboration features).  There are no 3rd party dependencies (unless one wants to recompile the core).  Everything is open source.

If you do not need to modify the code, you can use our public server at https://blockly-demo.appspot.com.  Installation is only recommended for developers who wish to modify or add source code.

## Get the Code

First, download the source code.  Use [Subversion](http://subversion.apache.org/) to pull a copy of Blockly off of Google Code:

```
svn checkout http://blockly.googlecode.com/svn/trunk/ blockly
```

Once you have the code, point your browser at ` apps/maze/index.html ` and test out the maze app.  Verify that clicking "Run Program" will make the man move forward.

## Injecting Blockly

With your installation of Blockly verified as working, inject Blockly into a web page using either a fixed-size ` div ` or a resizable ` iframe `.

→ More info on [injecting fixed-sized Blockly](InjectingFixedSize)...

→ More info on [injecting resizable Blockly](InjectingResizable)...

## Configuration

The ` Blockly.inject ` line contains as its second argument a dictionary of name-value pairs.  These are used for configuration.  The following options are supported:

| Name | Type | Description |
|--------------|--------|---------------------------------------------------------------------------------------------------------------------|
| ` collapse: ` | boolean | Allows blocks to be collapsed or expanded.  Defaults to ` true ` if the toolbox has categories, ` false ` otherwise. |
| ` comments: ` | boolean | Allows blocks to have comments.  Defaults to ` true ` if the toolbox has categories, ` false ` otherwise.            |
| ` disable: `  | boolean | Allows blocks to be disabled.  Defaults to ` true ` if the toolbox has categories, ` false ` otherwise.              |
| ` maxBlocks: ` | number  | Maximum number of blocks that may be created.  Useful for student exercises. Defaults to ` Infinity `.               |
| ` path: `     | string  | Path from page (or frame) to the Blockly root directory. Defaults to ` "./" `.                                       |
| ` readOnly: ` | boolean | If ` true `, prevent the user from editing.  Supresses the toolbox and trashcan.  Defaults to ` false `.             |
| ` rtl: `      | boolean | If ` true `, mirror the editor for Arabic or Hebrew locales.  See [RTL demo](https://blockly-demo.appspot.com/static/demos/rtl/index.html).  Defaults to ` false `. |
| ` scrollbars: ` | boolean | If ` false `, supress scrollbars that appear if the toolbox has categories.  Defaults to ` true `.                   |
| ` sound: `    | boolean | If ` false `, don't play sounds (e.g. click and delete).  Defaults to ` true `.                                      |
| ` toolbox: `  | XML nodes or string | Tree structure of categories and blocks available to the user.  See [Defining the Toolbox](Toolbox) for more information. |
| ` trashcan: ` | boolean | Displays or hides the trashcan.  Defaults to ` true ` if the toolbox has categories, ` false ` otherwise.            |

Blockly's library of blocks is highly configurable.  The blocks shown to the user can be customized so that users only see blocks that are relevant to the task.  Browse the ` blocks/ ` directory for block categories that you want to include.  The categories and blocks shown in the toolbox (the side menu) is specified using an [XML tree](Toolbox).

Additionally, custom blocks need to be built to call your web application's API.  An example is the [Maze application](https://blockly-demo.appspot.com/static/apps/maze/index.html) which has custom blocks for movement.  More info on [Creating custom blocks](CustomBlocks)...

## Language Generators

Blockly is not a programming language, one cannot 'run' a Blockly program.  Instead, Blockly can translate the user's program into JavaScript, Python, Dart, or some other language.

→ More info on [Language Generators](LanguageGenerators)...

## Importing and Exporting Blocks

If your application needs to save and store the user's blocks and restore them at a later visit, use this call for export to XML:

```
  var xml = Blockly.Xml.workspaceToDom(Blockly.mainWorkspace);
  var xml_text = Blockly.Xml.domToText(xml);
```

This will produce a minimal (but ugly) string containing the XML for the user's blocks.  If one wishes to obtain a more readable (but larger) string, use ` Blockly.Xml.domToPrettyText ` instead.

Restoring from an XML string to blocks is just as simple:

```
  var xml = Blockly.Xml.textToDom(xml_text);
  Blockly.Xml.domToWorkspace(Blockly.mainWorkspace, xml);
```

## Cloud Storage

Blockly comes with an optional cloud-storage feature.  It enables users to save, load, share, and publish their programs.  If your project is hosted on App Engine you can take advantage of this service.

→ More info on [Cloud Storage](CloudStorageWithAppEngine)...
