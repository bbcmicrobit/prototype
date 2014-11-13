// These are all of the controls that we're going to be using.
// Selecting them at the top here means we don't have to ever
//   request them from JQuery again.
var tutorial_back_button = $('#tutorial_back');
var tutorial_forward_button = $('#tutorial_forward');

function enablePageInteraction() {
    var editor_tabs = $('#editor_tabs');
    editor_tabs.tab();
    console.log("Tabs enabled on ", editor_tabs)

    // Wire up the Build Code button if it's available.
    var build_code_btn = $('#buildCode')
    if (build_code_btn.length) {
        console.log("Activating buildCode on ",build_code_btn);
        build_code_btn.click(function () {
            console.log("Building code");
            compileBlockly();
        })
    } else {
        console.log("No buildCode button, skipping");
    }

    // Wire up the Create Program button if it's available.
    var create_program_btn = $('#createProgram')
    if (create_program_btn.length) {
        console.log("Activating create program on ", create_program_btn);
        create_program_btn.click(function () {
            console.log("Building code");
            compileBlockly(function(program_id) {
                window.location.replace('/microbug/program/'+program_id);
            });
        })
    } else {
        console.log("No createCode button, skipping");
    }

    // Wire up the Blockly UI if it's working
    setupBlockly();

    // Wire up the nifty rename button trickery
    setupNameRename();

    setupTutorial();
}

function setupTutorial() {
    var tutorial_elem = $('#tutorial');
    if (tutorial_elem.length) {
        console.log("Setting up tutorial");

        // Move 'tutorial_content' into 'tutorial'.
        var tutorial_content_elem = $('#tutorial_content');
        tutorial_content_elem.appendTo($('#tutorial'));

        // Connect the buttons
        var page_number = 1;
        tutorial_back_button.click(function() {
            page_number -= 1;
            showTutorialPage(page_number);
        });
        tutorial_forward_button.click(function() {
            page_number += 1;
            showTutorialPage(page_number);
        });

        // Show the first page
        showTutorialPage(page_number);
    } else {
        console.log("No tutorial on page");
    }
}

function showTutorialPage(page_id) {
    var tutorial_content_elem = $('#tutorial_content');

    // Show only the page we're after.
    tutorial_content_elem.children().hide();
    selected_page = tutorial_content_elem.find(':nth-child('+page_id+')')
    selected_page.show();

    // Disable the back button only on the first page
    if (page_id==1) {
        tutorial_back_button.addClass('disabled');
    } else {
        tutorial_back_button.removeClass('disabled');
    }

    // Disable the forward button only for the last page
    console.log("on page ",page_id," of ",tutorial_content_elem.children().length);
    if (page_id == tutorial_content_elem.children().length) {
        tutorial_forward_button.addClass('disabled');
    } else {
        tutorial_forward_button.removeClass('disabled');
    }

    // Find the XML from the selected page, it's the Blockly toolbox.
    blockly_xml = selected_page.find('xml')[0];
    Blockly.updateToolbox(blockly_xml);
}

function setupNameRename() {
    // Store these in closure so we don't have to keep finding them again
    var program_name_elem = $('#program_name');
    var original_name_elem = $('#original_program_name');
    var rename_button_elem = $('#program_rename');

    var was_same = true;
    var program_id, program_name;

    // Check if we have the rename controls
    if (original_name_elem.length) {
        // Get the program ID, we can store it in a closure.
        var program_id_elem = $('#program_id');
        if (program_id_elem.length) {
            program_id = program_id_elem.text();
            console.log("Program ID is ",program_id,", storing for later use");
        } else {
            console.error("Cannot set of rename box, no '#program_id' element")
        }

        // Link up the behavior for the rename button
        console.log("Setitng up rename bar functionality");

        rename_button_elem.on('click', function() {
            var program_name = program_name_elem[0].value;
            var original_program_name = original_name_elem[0].value;

            // Cannot rename to an empty value.  TODO: Regular expression version!
            if (program_name == '' || typeof(program_name)=='undefined') {
                bootbox.alert("You need to provide a name");
                return;
            }
            // Auto-accept if there's no current name
            if (original_program_name == '') {
                //programRenameAjax()
                //original_name_elem[0].value = program_name_elem[0].value;
                //program_name_elem.removeClass('changed_name');
                //rename_button_elem.removeClass('changed_button');
                //was_same = true;
                //return true;
            }
            bootbox.confirm("This will rename your program\nAre you sure?", function(result) {
                if (result) {
                    programRenameAjax(program_id, program_name_elem, original_name_elem, rename_button_elem);
                    //original_name_elem[0].value = program_name_elem[0].value;
                    //program_name_elem.removeClass('changed_name');
                    //rename_button_elem.removeClass('changed_button');
                    //was_same = true;
                }
            });
        });

        program_name_elem.on("change keyup paste", function() {
            console.log("Click");
            if (program_name_elem[0].value == original_name_elem[0].value) {
                if (!was_same) {
                    program_name_elem.removeClass('changed_name');
                    rename_button_elem.removeClass('changed_button');
                    console.log("SAME");
                    was_same = true;

                }
            } else {
                if (was_same) {
                    program_name_elem.addClass('changed_name');
                    rename_button_elem.addClass('changed_button');
                    console.log("DIFFERENT");
                    was_same = false;
                }
            }
        })
    } else {
        console.log("No rename bar, skipping")
    }
}

// Wrapper round the Ajax part of the program renaming.
function programRenameAjax(program_id, program_name_elem, original_program_name_elem, rename_button_elem) {
    var program_name = program_name_elem[0].value;
    var original_program_name = original_program_name_elem[0].value;

    console.log("Renaming program ",program_id," to '",program_name,"', (Was '",original_program_name,"')")

    $.ajax({
        type: "POST",
        url: "/microbug/rename_program/",
        data: JSON.stringify({
            "program_id": program_id,
            "program_name": program_name,
            "original_program_name": original_program_name
        }),
        success: function (data) {
            console.log("Rename successful.")
            // We've successfully renamed the object, but need to recheck equality to make sure
            // it's not changed since the submission.
            original_program_name_elem[0].value = program_name;
            if (program_name == program_name_elem[0].value) {
                program_name_elem.removeClass('changed_name');
                rename_button_elem.removeClass('changed_button');
            } else {
                console.log("Name changed since request,  ",program_name," vs. ",program_name_elem[0].value);
                program_name_elem.addClass('changed_name');
                rename_button_elem.addClass('changed_button');
            }
        },
        error: function(data) {
            bootbox.alert("Something went wrong, could not rename the program");
        }
    });
}

function setupBlockly() {
    if (document.getElementById('blockly')) {
        Blockly.inject(document.getElementById('blockly'),
            {
                path: '/static/microbug/blockly/',
                toolbox: document.getElementById('toolbox'),
                trashcan: false
            });

        // Load the XML from blocklyXmlSrc, if it exists.
        xml_src = $('#blocklyXmlSrc')
        if (xml_src.length) {
            console.log("Loading XML from BlocklyXmlSrc");
            var blockly_xml_text = xml_src.text();
            console.log("XML Text: ",blockly_xml_text);
            var blockly_xml = Blockly.Xml.textToDom(blockly_xml_text);
            console.log("XML: ",blockly_xml);
            Blockly.Xml.domToWorkspace( Blockly.mainWorkspace, blockly_xml);
        } else {
            console.log("No BlocklyXmlSrc, not loading");
        }
    }
}

// Gets the name of the program whether or not we're using the rename bar.
function getProgramName() {
    // Get the program name from the original_program_name box if it exists,
    //  if not go for the program_name box
    var original_program_name_elem = $('#original_program_name');
    var program_name_elem = $('#program_name');

    if (original_program_name_elem.length) {
        return original_program_name_elem[0].value;
    } else {
        return program_name_elem[0].value;
    }

}
function compileBlockly(successCallback) {
    var code = Blockly.Python.workspaceToCode();

    var xml = Blockly.Xml.workspaceToDom(Blockly.mainWorkspace);
    var xml_text = Blockly.Xml.domToText(xml);

    var program_name = getProgramName();

    console.log("Program name is: ",program_name);
    console.log("Code is ", code);
    console.log("XML is ", xml_text);

    $("#code").html("<P><PRE>" + code + "</PRE>");

    $.ajax({
        type: "POST",
        url: "/microbug/build_code/",
        data: JSON.stringify({
            "program_name": program_name,
            "repr": {
                "code": code,
                "xml": xml_text
            }
        }),
        success: function (data) {
            console.log("Success, data is "+data);
            if (successCallback) {
                successCallback(data);
            }
            //var someid = data["id"];
            //text = '<P>Link to this version - <a href="/blockly_reload.html?id=' + someid + '"> ' + someid.toString() + ' </a>';
            //$("#resultblock").html(text);
        }
    });
}

console.log("Loaded test page");
enablePageInteraction();
console.log("All done")

