**[Installation](Installation): Cloud Storage**

# Introduction

If your application is hosted on App Engine, a cloud storage service is available that allows users to save, load, share, and publish their programs.

_Note that the [RealtimeCollaboration](RealtimeCollaboration) feature provides an alternate way to save, load, share, and publish programs.  It does, however, currently require users to have a Google Account._

## Setting up App Engine

The first step is to get your own copy of Blockly running on App Engine.

  1. Download and install the [Python SDK](https://developers.google.com/appengine/downloads).
  1. Log into [Google App Engine](https://appengine.google.com/) and create an application.
  1. Edit ` appengine/app.yaml ` and change the application ID from ` blockly-demo ` to the application name you created in the previous step.
  1. Copy (or soft-link) the following files and directories into ` appengine/static/ `:
    * ` apps/ `
    * ` demos/ `
    * ` msg/ `
    * ` media/ `
    * ` tests/ `
    * ` *_compressed.js `
  1. Optional: If you'd like to use ` blockly_uncompressed.js ` on the server, also copy that into ` appengine/static/ ` and copy ` closure-library-read-only/ ` into the parent directory, ` appengine/ `.
  1. Optional: If you'd like to run the Blockly Playground, you'll have to add links for the ` blocks `, ` core `, ` generators `, and ` tests ` directories, as well as the files in step 5.
  1. Run the Google App Engine Launcher from the GUI, add your ` appengine ` directory as an existing application, and press the "Deploy" button.  If you prefer to use the command line, run: ` appcfg.py --oauth2 update appengine/ `.

Once Blockly is uploaded you can point a browser to the URL you created in step 2.  You should see a list of demos, including the cloud storage demo.

## Talking to the Cloud

Examine the [storage demo](https://blockly-demo.appspot.com/static/demos/storage/index.html)'s source at [demos/storage/index.html](https://github.com/google/blockly/tree/master/demos/storage/index.html) and note the following features.  First, there is a script include that loads the cloud storage API:

```
  <script type="text/javascript" src="/storage.js"></script>
```

There are also these message definitions, which you should modify as desired:
```
  BlocklyStorage.HTTPREQUEST_ERROR = 'There was a problem with the request.\n';
  BlocklyStorage.LINK_ALERT = 'Share your blocks with this link:\n\n%1';
  BlocklyStorage.HASH_ERROR = 'Sorry, "%1" doesn\'t correspond with any saved Blockly file.';
  BlocklyStorage.XML_ERROR = 'Could not load your saved file.\n'+
      'Perhaps it was created with a different version of Blockly?';
```
Translations into other languages can be found at [apps/json](https://github.com/google/blockly/tree/master/apps/json).

Saving the current blocks is a single call to ` BlocklyStorage.link() `:

```
  <button onclick="BlocklyStorage.link()">Save Blocks</button>
```

To restore saved blocks on page load, just call ` BlocklyStorage.retrieveXml ` with the URL's hash after Blockly has been injected:

```
  if ('BlocklyStorage' in window && window.location.hash.length > 1) {
    BlocklyStorage.retrieveXml(window.location.hash.substring(1));
  }
```

## Local Storage

The ` storage.js ` API also offers the ability to save a single set of blocks in the browser's local storage.  This may be implemented instead of cloud storage, or in addition with cloud storage (though in the latter case one has to be careful of both types of storage attempting to restore at once).

To restore blocks from local storage, call ` BlocklyStorage.restoreBlocks ` in a timeout right after Blockly has been injected.

```
  window.setTimeout(BlocklyStorage.restoreBlocks, 0);
```

To automatically backup the blocks into local storage when the user leaves the page, call ` BlocklyStorage.backupOnUnload ` and it will register an event listener on the page's unload event.

```
  BlocklyStorage.backupOnUnload();
```

## Example

Here is [a live demo](https://blockly-demo.appspot.com/static/demos/storage/index.html) of cloud storage.
