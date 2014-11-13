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
}

function setupNameRename() {
    // Store these in closure so we don't have to keep finding them again
    var program_name_elem = $('#program_name')
    var original_name_elem = $('#original_program_name')
    var rename_button_elem = $('#program_rename');
    var was_same = true;
    var program_name;

    // Check if we have the rename controls
    if (original_name_elem.length) {
        // Link up the behavior for the rename button
        console.log("Setitng up rename bar functionality");
        console.log("ONE: ", original_name_elem);

        rename_button_elem.on('click', function() {
            // Cannot rename to an empty value.  TODO: Regular expression version!
            if (program_name_elem[0].value == '') {
                bootbox.alert("You need to provide a name");
                return;
            }
            // Auto-accept if there's no current name
            if (original_name_elem[0].value == '') {
                original_name_elem[0].value = program_name_elem[0].value;
                program_name_elem.removeClass('changed_name');
                rename_button_elem.removeClass('changed_button');
                was_same = true;
                return true;
            }
            bootbox.confirm("This will rename your program\nAre you sure?", function(result) {
                if (result) {
                    original_name_elem[0].value = program_name_elem[0].value;
                    program_name_elem.removeClass('changed_name');
                    rename_button_elem.removeClass('changed_button');
                    was_same = true;
                }
            });
        });

        console.log("PNE: ",program_name_elem);
        console.log("ONE: ",original_name_elem);

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

function setupBlockly() {
    if (document.getElementById('blockly')) {
        Blockly.inject(document.getElementById('blockly'),
            {
                path: '/static/microbug/blockly/',
                toolbox: document.getElementById('toolbox'),
                trashcan: false
            });
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

