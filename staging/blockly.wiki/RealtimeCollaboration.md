### Introduction
The Blockly library supports realtime collaboration of Blockly programs similar to realtime collaboration of documents in Google Drive, i.e. multiple users can edit the same program at the same time, with all the users seeing each others changes in real time.

Using Blockly's realtime collaboration feature will provide your users with a sharable link which they can send to a friend or colleague.  That link contain the ID of a 'document' which is saved in Google Drive and stores the Blockly program that is being edited.  Note that this implies that using Blockly's realtime collaboration feature also provides for persistent storage of a Blockly program (as an alternative to the mechanism described in [CloudStorageWithAppEngine](CloudStorageWithAppEngine)) and therefore is useful even if you don't necessarily care about realtime collaboration.  Also note that another benefit of using the realtime collaboration feature will be the ability to 'undo' and 'redo' editing operations.  'Undo' and 'redo' are not currently supported due to a bug (in Blockly code) but hopefully that will soon be fixed.

Blockly's realtime collaboration is built using [Google Drive's Realtime API](https://developers.google.com/drive/realtime/): a service provided by Google that enables 3rd party developers to incorporate realtime collaboration into their own web applications.

> _Note that Google Drive's Realtime API currently requires users to have (or create) Google Accounts, so please consider that when deciding to enable realtime collaboration into your app._

By default realtime collaboration is currently disabled in Blockly.  This wiki page tells you how to enable it.  Note that these instructions are for the developer using Blockly for their web application, not for the end user.

There are two major steps to take in order to enable realtime collaboration in Blockly.  One is to [put the appropriate code in your application](#Code_to_enable_realtime_collaboration).  The other is to use the [Google Developer Console](https://cloud.google.com/console/project) to [register your application](Registering_with_the_Google_Developer_Console) to use Google Drive's Realtime API.

### Code to enable realtime collaboration
To enable realtime collaboration in your application's code add a 'realtime: true' option to your Blockly.inject() method call.  There are also a set of 'realtimeOptions: ...' that you can add, as well.  Here, for example, is the code in for this in [playground.html](https://github.com/google/blockly/tree/master/tests/playground.html) in the Blockly Playground application (which is part of the standard Blockly test codebase):

```
function start() {
  var toolbox = document.getElementById('toolbox');
  Blockly.inject(document.getElementById('blocklyDiv'),
          {rtl: rtl, path: '../', toolbox: toolbox, realtime: true,
           realtimeOptions:
            {clientId: 'YOUR CLIENT ID GOES HERE',
             chatbox: {elementId: 'chatbox'},
             collabElementId: 'collaborators'}});
  if (Blockly.Realtime.isEnabled()) {
    enableRealtimeSpecificUi();
  }
}
```

The clientId string (i.e  'YOUR CLIENT ID GOES HERE') needs to be replaced by the Client ID that you will obtain when registering your application in the Google Developers Console.  That ID should look something like ` '12345678901.apps.googlecontent.com' `

The 'chatbox' option is used if you want to have a collaborative chat in you app.  Within that option you must specify an 'elementId' suboption which tells the realtime code the id of a textarea that is defined in your app and which will be used for the chat.  You can also specify the initial text to be placed in your chatbox by adding an 'initText' suboption.  If you don't specify an 'initText' it will default to the value of Blockly.Msg.CHAT, which has the value _'Chat with your collaborator by typing in this box!'_ for english users but can be localized.

The 'collabElementId' option is used if you want to view thumbnail images (with alt/hover text containing the users' name) of all the users (with available profiles that are accessible to the user) currently collaborating on a particular Blockly-based program.  The value of the 'collabElementId' option should be the id of a div in your application where the thumbnails will be placed.  See the [playground.html](https://github.com/google/blockly/tree/master/tests/playground.html) for an example of this.

### Registering with the Google Developer Console
To register your application with the Google Developers Console, please use the instructions that can be found in the [activation section of the Google Drive Realtime API Quickstart documentation](https://developers.google.com/drive/realtime/realtime-quickstart#step_1_activate_the_drive_api).

### Example
Here's [a simple live demo](https://blockly-realtime-collab.appspot.com/static/demos/realtime/index.html) of Blockly realtime collaboration in action.  For something more extensive, here's [a live demo of the Blockly Playground](https://blockly-realtime-collab.appspot.com/static/tests/playground.html) enabled for realtime collaboration.

The first time you view them you may need to click the 'You must authorize' button.