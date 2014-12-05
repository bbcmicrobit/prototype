// These are all of the controls that we're going to be using.
// Selecting them at the top here means we don't have to ever
//   request them from JQuery again.
var program_id_elem = $('#program_id');
var tutorial_back_button = $('#tutorial_back');
var tutorial_forward_button = $('#tutorial_forward');
var program_status_update_elem = $('#program_status_update');
var build_code_btn = $('.buildCode')
var create_program_btn = $('.createProgram');
var login_div = $('#login');
var edit_phrase_elem = $('#edit_phrase');
var add_facilitator_btn = $('.add-facilitator');
var facilitator_responses = $('.facilitator-response');

function enablePageInteraction() {
    var editor_tabs = $('#editor_tabs');
    editor_tabs.tab();
    console.log("Tabs enabled on ", editor_tabs)

    // Wire up the Build Code button if it's available.
    if (build_code_btn.length) {
        var program_id = getProgramId();
        console.log("ID: ",program_id);
        console.log("Activating buildCode on ",build_code_btn);
        build_code_btn.click(function () {
            console.log("Building code");
            compileNewProgram();
        })
    } else {
        console.log("No buildCode button, skipping");
    }

    // Wire up the Create Program button if it's available.
    if (create_program_btn.length) {
        console.log("Activating create program on ", create_program_btn);
        create_program_btn.click(function () {
            console.log("Building code");
            compileNewProgram(
                function(program_id) {
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

    setupProgramStatusUpdate();

    setupLoginForm();

    setupAddFacilitator();

    setupFacilitatorResponses();
}

function setupFacilitatorResponses() {
    facilitator_responses.click(function(ev) {
        // Delete all existing modals.
        $('.modal').remove();

        // Get the button which was clicked on
        var target = $(ev.currentTarget);
        console.log("EV: ",target);

        // Accepted- true/false?
        var accepted = target.attr('data-response') == 'accept';

        // The request we're accessing
        var request_id = target.attr('data-request-id');

        // The child's name
        var child_name = target.attr('data-child-name');

        if (accepted) {
            bootbox.dialog({
                message: "This will confirm you as a facilitator for '<strong>" + child_name + "</strong>'. Lorem ipsum",
                title: "Accepting request from '<strong>" + child_name + "</strong>'.  Lorem ipsum",
                buttons: {
                    accept: {
                        label: "<i class='fa fa-check'></i>&nbsp;Confirm",
                        className: "btn-success",
                        callback: function () {
                            respondToFacilitatorRequest(request_id, true)
                        }
                    },
                    decline: {
                        label: "<i class='fa fa-close'></i>&nbsp;Not now",
                        className: "btn-danger"
                    }
                }
            });
        } else {
            bootbox.dialog({
                message: "This will decline the facilitator request from '<strong>" + child_name + "</strong>', and delete it from the system. Lorem ipsum",
                title: "Decling request from '<strong>" + child_name + "</strong>'.  Lorem ipsum",
                buttons: {
                    accept: {
                        label: "<i class='fa fa-close'></i>&nbsp;Decline",
                        className: "btn-danger",
                        callback: function () {
                            respondToFacilitatorRequest(request_id, false)
                        }
                    },
                    decline: {
                        label: "<i class='fa fa-close'></i>&nbsp;Not now",
                        className: "btn-success"
                    }
                }
            });

        }
    })
}

function respondToFacilitatorRequest(request_id, accepted) {
    if (accepted) {
        console.log("Accepting response " + request_id);
    } else {
        console.log("Declining response "+request_id);
    }
    $.ajax({
        type: "POST",
        url: "/microbug/respond_to_facilitator_request",
        data: JSON.stringify({
            "request_id": request_id,
            "is_accepted": accepted
        }),
        success: function(data) {
            location.reload();
        },
        error: function (jqXhr, textStatus, errorThrown) {
            var statusCode = jqXhr.statusCode().status;
            switch(statusCode) {
                case 404: // Not found
                    bootbox.alert("Can't find that facilitator request, have you already replied to it?. Lorem ipsum");
                    break;
                case 403: // Not allowed
                    bootbox.alert("Sorry, this does not seem to be a request directed to you. Lorem ipsum");
                    break;
                default:
                    bootbox.alert("An error occured processing the facilitator request. Lorem ipsum");
            }
            console.log("JQXHR: ",jqXhr);
            console.log("TEXTSTATUS: ",textStatus);
            console.log("ERRORTHROWN: ",errorThrown);
            console.log("CODE: ",jqXhr.statusCode().status);
        }
    });
}

function setupAddFacilitator() {
    add_facilitator_btn.click(function() {
        console.log("Clickey");
        bootbox.dialog({
            message:
                "In order to add a facilitator you will need to contact them "+
                "to know their username, then enter it in the box below and "+
                "wait for them to confirm.  Lorem ipsum." +
                "<input type='text' id='facilitator-username' style='width:100%'>",
            title: "Add Facilitator Lorem Ipsum",
            buttons: {
                send_request: {
                    label: "<i class='fa fa-check'></i>&nbsp; Send Request",
                    className: "btn-success",
                    callback: function () {
                        console.log("Sending..");
                        makeFacilitorRequest($('#facilitator-username').val());
                    }
                },
                cancel: {
                    label: "<i class='fa fa-close'></i>&nbsp;Cancel",
                    className: "btn-danger"
                }
            }
        })
    });
}

function makeFacilitorRequest(faciliator_name) {
    console.log("making facilitator request to "+faciliator_name);
    $.ajax({
        type: "POST",
        dataType: 'text',
        url: "/microbug/facilitator_request",
        data: JSON.stringify({
            "facilitator_name": faciliator_name
        }),
        success: function(data) {
            bootbox.alert("Your facilitator has been told of your request.  Lorem ipsum.");
            location.reload();
        },
        error: function (jqXhr, textStatus, errorThrown) {
            var statusCode = jqXhr.statusCode().status;
            switch(statusCode) {
                case 401: // Unauthorized
                    bootbox.alert("You must be logged in to make a facilitator request. Lorem ipsum");
                    break;
                case 404: // Not found
                    bootbox.alert("Can't find a user with that username. Lorem ipsum");
                    break;
                case 405: // Not allowed
                    // More details in body text
                    console.log("ERROR: ",jqXhr);
                    bootbox.alert("Cannot send request. "+jqXhr.responseText);
                    break;
                default:
                    bootbox.alert("An error occured making the facilitator request. Lorem ipsum");
            }
            console.log("JQXHR: ",jqXhr);
            console.log("TEXTSTATUS: ",textStatus);
            console.log("ERRORTHROWN: ",errorThrown);
            console.log("CODE: ",jqXhr.statusCode().status);
        }
    });
}

function signOut() {
    $.ajax({
        type: "GET",
        url: "/microbug/sign_out",
        success: function(data) {
            //updateLoginForm();
            location.reload();
        }
    })
}

function updateLoginForm() {
    // Close the login dropdown
    $('#login').removeClass('open');
    
    $.ajax({
        type: "GET",
        url: "/microbug/login_pane",
        success: function(data) {
            console.log("SUCCESS ON LOGIN FORM, DATA IS ",data);
            login_div.html(data);
            // Close the menu

            $('.dropdown-toggle').dropdown();
            $('.dropdown-menu').find('form').click(function (e) {
                console.log("Stopping propogation on form");
                e.stopPropagation();
            });

            $('#loginSubmit').click(function(ev) {
                ev.preventDefault();
                var username = $('#loginUsername').val();
                var password = $('#loginPassword').val();
                console.log("Logging in as Username: ",username,", Password: ",password);

                $.ajax({
                    type: "POST",
                    url: "/microbug/authenticate_user/",
                    data: JSON.stringify({
                        "username": username,
                        "password": password
                    }),
                    success: function (data) {
                        data = JSON.parse(data);
                        if (data['status']=='authenticated') {
                            console.log("LOGGED IN, DATA IS ", data);
                            //updateLoginForm();
                            location.reload();
                        } else {
                            alert("Could not log in with username and password provided");
                        }
                    },
                    error: function (jqXhr, textStatus, errorThrown) {
                        alert("Cannot Login: "+textStatus+"\n"+errorThrown)
                    }
                });
            })

            $('#loginSignOut').click(function(ev) {
                ev.preventDefault();
                console.log("Logging out");
                signOut();
            })
        }
    });
}

function setupLoginForm() {
    if (login_div.length >0) {
        console.log("Configuring login form");
        updateLoginForm();
    } else {
        console.log("No login page, skipping");
    }
}

function setupProgramStatusUpdate() {
    if (program_status_update_elem.length >0) {
        var program_id = program_status_update_elem.attr('data-program-id');
        if (program_id) {
            console.log("Configuring program status update for ",program_id);
            updateProgramStatus(program_id);
        } else {
            program_status_update_elem.html('&nbsp;');
            console.log("No program id so not configuring status update");
        }
    } else {
        console.log("No program status update, no need to update it");
    }
}

function updateProgramStatus(program_id) {
    var callback = function() { updateProgramStatus(program_id)};

    $.ajax({
        type: 'GET',
        url: '/microbug/queue_status/'+program_id,
        timeout: 2000,
        success: function(data) {
            data = JSON.parse(data);
            console.log("GOT DATA: ",data);
            program_status_update_elem.html(statusElementContent(data));
            window.setTimeout(callback, 10000);
        },
        error: function (XMLHttpRequest, textStatus, errorThrown) {
            console.log("Error fetching program status");
            window.setTimeout(callback, 10000);
        }
    });
}

function statusElementContent(data) {
    if (data.status == 'no_version') {
        return '';
    } else if (data.status == 'compiled') {
        return(
            '<a class="btn btn-primary" href="/microbug/download/'+data.id+'">' +
            '<i class="fa fa-download">&nbsp;</i>Download </a>'
        );
    } else if (data.status == 'in_compile_queue') {
        return(
            'Program being compiled, expected in <span class="eta">'+data.eta+'</span>'
        );
    }
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

    // Show only the page we're after, and everything with 'always-show' class
    tutorial_content_elem.children().hide();
    selected_page = tutorial_content_elem.find(':nth-child('+page_id+')')
    selected_page.show();
    tutorial_content_elem.find('.always-show').show();

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


		$(document).ready(function() {
            var dalcode;
			// Sim Renderer
			SIMIO.init("SIMIO");
			//DALJS.setDirtyCallback(SIMIO.render); DEPRECATED?

			//Add start blocks if defined - idea: dump them out to console?
			Blockly.Xml.domToWorkspace(Blockly.mainWorkspace, document.getElementById('startBlocks'));

		    var myInterpreter = null;
		    var myInterval = null;

			function initInterpreterApi(interpreter, scope)
			{
			    function makeWrapper(fn)
			    {
			    	return function()
			    	{
						for (var j = 0; j < arguments.length; j++) {
							arguments[j] = arguments[j].toString();
						}
			    		return interpreter.createPrimitive(fn.apply(this, arguments));
			    	}
			    }
			    function makeInterp(text, fn)
			    {
				    interpreter.setProperty(scope, text, 
				    	interpreter.createNativeFunction(
				    		makeWrapper(fn)));
			    }

			    function makeWrapperScrollImg(fn)
			    {
			    	return function()
			    	{
						arguments[2] = arguments[0].length;
						arguments[3] = arguments[0].properties[0].length;
						arguments.length = 4;

						for (var j = 0; j < arguments.length; j++) {
							arguments[j] = arguments[j].toString();
						}
			    		return interpreter.createPrimitive(fn.apply(this, arguments));
			    	}
			    }
			    function makeInterpScrollImg(text, fn)
			    {
				    interpreter.setProperty(scope, text, 
				    	interpreter.createNativeFunction(
				    		makeWrapperScrollImg(fn)));
			    }
                function makeWrapperScrollStringImg(fn)
                {
                    return function()
                    {
                        var newArgs = [undefined, undefined];
                        newArgs[0] = {
                            mPixelData: [],//??
                            mPixelPos: arguments[0].properties.mPixelPos.toNumber(),
                            mString: arguments[0].properties.mString.toString(),
                            mStrlen: arguments[0].properties.mStrlen.toNumber()
                        }
                        newArgs[1] = arguments[1].toNumber();//delay
                        return interpreter.createPrimitive(fn.apply(this, newArgs));
                    }
                }
                function makeInterpScrollStringImg(text, fn)
                {
                    interpreter.setProperty(scope, text, 
                        interpreter.createNativeFunction(
                            makeWrapperScrollStringImg(fn)));
                }


				function renderSimulator(display, left_eye_state, right_eye_state)
				{
					var leds = display.split(",");
					leds = leds.map(function(led){return parseInt(led);});
					var rows = [];
					rows[0] = leds.slice(0,5);
					rows[1] = leds.slice(5,10);
					rows[2] = leds.slice(10,15);
					rows[3] = leds.slice(15,20);
					rows[4] = leds.slice(20,25);

					left_eye_state = parseInt(left_eye_state);
					right_eye_state = parseInt(right_eye_state);
					SIMIO.render(rows, [left_eye_state, right_eye_state]);
				}

				DALJS.setDirtyCallback(SIMIO.render);

				function clog(msg)
				{
					console.log(msg);
				}
				//makeInterp('prompt', prompt);
				//makeInterp('alert', alert);

				// Utility functions
			    makeInterp('highlightBlock', highlightBlock);
			    makeInterp('renderSimulator', renderSimulator);
			    makeInterp('clog', clog);//console.log

			    // Acorn interpreter can't access DOM's setTimeout, setInterval etc
				// Callout functions that are in the API				
				makeInterp('print_message', DALJS.print_message);
				makeInterpScrollImg('scroll_image', DALJS.scroll_image);
				makeInterpScrollStringImg('scroll_string_image', DALJS.scroll_string_image);
                makeInterp('pause', DALJS.pause);

                // test function, this one
                makeInterp('scroll_string', DALJS.scroll_string);

			    function makeWrapperButt(fn)
			    {
			    	return function()
			    	{
						for (var j = 0; j < arguments.length; j++) {
							arguments[j] = arguments[j].toString();
						}
			    		return interpreter.createPrimitive(fn.apply(this, arguments));
			    	}
			    }
			    function makeInterpButt(text, fn)
			    {
				    interpreter.setProperty(scope, text, 
				    	interpreter.createNativeFunction(
				    		makeWrapper(fn)));
			    }

				makeInterpButt('get_button', DALJS.get_button);


			}	    

			var highlightPause = false;

			function highlightBlock(id)
			{
			    Blockly.mainWorkspace.highlightBlock(id);
			    highlightPause = true;
			}

			function runCode()
			{
				//DALJS.reset();
			    if (parseCode())
                {
                    stepCode();
                }
                else
                    alert("Problem parsing code");
			}

			function parseCode()
			{
			    // Generate JavaScript code and parse it.
			    Blockly.JavaScript.STATEMENT_PREFIX = 'highlightBlock(%1);\n';
			    Blockly.JavaScript.addReservedWords('highlightBlock');
			    
			    var code = Blockly.JavaScript.workspaceToCode();

                if (dalcode === undefined)
                    alert('dalcode undefined');

			    alert('Ready to execute this code:\n\n' + code);
			    code = dalcode + "reset();" + code;

                try {
                    myInterpreter = new Interpreter(code, initInterpreterApi);
                } catch (e) {

                    if (e instanceof SyntaxError) {
                        console.log(e);
                        alert(e);
                        return false;
                    } else {
                        console.log(e);
                        alert(e);
                        return false;
                    }
                }

			    highlightPause = false;
			    Blockly.mainWorkspace.traceOn(true);
			    Blockly.mainWorkspace.highlightBlock(null);
                return true;
			}

			function stepCode()
			{
                var statusMsg = "Everything OK";

			    if (!DALJS.deviceReady())
			    {
			        setTimeout(function()
			        {
			            stepCode();
			        }, 50);
			        return;
			    }

			    try
			    {
			        var ok = myInterpreter.step();
			    }
                catch (e) {
                    statusMsg = "Error: " + e;
                    console.log(statusMsg);
                    alert(statusMsg + "\n" + "Program Halted");
                }
			    finally
			    {
			        if (!ok)
			        {
			            // Program complete, no more code to execute.
                        console.log("Execution complete. " + statusMsg);
			            return;
			        }
			    }

			    if (highlightPause)
			    {
			        // A block has been highlighted.  Pause execution here.
			        var pausebutton = document.getElementById('pausetime');
			        var delay = parseInt(document.getElementById('pausetime').value);

			        highlightPause = false;
			        setTimeout(function()
			        {
			            stepCode();
			        }, delay);
			    }
			    else
			    {
			        // Keep executing until a highlight statement is reached.
			        stepCode();
			    }
			}

			// Code Build
			var buildCode = function() {
				var pycode = "you've commented the pycode out";//Blockly.Python.workspaceToCode();

				var xml = Blockly.Xml.workspaceToDom(Blockly.mainWorkspace);
				var xml_text = Blockly.Xml.domToText(xml);
				console.log(xml_text);

				$("#codeblock").html("<P><PRE>" + pycode  + "</PRE>" + "<P><PRE>" + pycode + "</PRE>");
    			$.ajax({
					type: "POST",
					url: "/cgi-bin/upload_mb.py",
					data: JSON.stringify({"repr" : { "code": pycode, "xml" : xml_text }}),
					success: function( data ) {
						var someid = data["id"];
						text = '<P>Link to this version - <a href="/blockly_reload.html?id=' +  someid + '"> ' + someid.toString() +' </a>';
						$( "#resultblock" ).html( text );
						},
				});
			};

			// document.getElementById("BuildCodeButton").addEventListener("click", buildCode);
			document.getElementById("RunCodeButton").addEventListener("click", runCode);
			SIMIO.render();

            var jqxhr = $.get('/static/microbug/js/dal_interpreter.txt', function(data, txt, err) {
                dalcode = data;
                console.log("Dalcode success");
            })
            .fail(function() {
                console.log("Dalcode error, using responseText");
                dalcode = jqxhr.responseText;
            });
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

// Gets the edit phrase the user has entered.
function getEditPhrase() {
    return edit_phrase_elem.val();
}

// Gets the edit phrase currently entered
function getProgramId() {
    return program_id_elem.text();
}

// Return the Blockly code
function blocklyCode() {
    return Blockly.Python.workspaceToCode();
}

// Return the Blockly code as Python
function blocklyCodeAsPython() {
    var xml = Blockly.Xml.workspaceToDom(Blockly.mainWorkspace);
    return Blockly.Xml.domToText(xml);
}

function populateCodeTab() {
    var code = blocklyCode();
    $('#code-tab').html("<P><PRE>" + code  + "</PRE>");
}

function compileNewProgram(successCallback) {
    // Start to update the setup as well since it's about to compile.
    updateProgramStatus(getProgramId());

    $.ajax({
        type: "POST",
        url: "/microbug/build_code/",
        data: JSON.stringify({
            "program_name": getProgramName(),
            "program_id": getProgramId(),
            "edit_phrase": getEditPhrase(),
            "repr": {
                "code": blocklyCode(),
                "xml": blocklyCodeAsPython()
            }
        }),
        success: function (data) {
            console.log("Success, data is "+data);
            if (successCallback) {
                successCallback(data);
            }
        },
        error: function (jqHxr, textStatus, errorText) {
            if (errorText == 'METHOD NOT ALLOWED') {
                bootbox.alert("Sorry, you need to either log in as the author of this program or have the edit password to edit it.")
            } else {
                bootbox.alert("Error: " + textStatus + "<br/>" + errorText)
            }
        }
    });
}

function recompileProgram(successCallback) {
    $.ajax({
        type: "POST",
        url: "/microbug/build_code/",
        data: JSON.stringify({
            "program_name": getProgramName(),
            "program_id": getProgramId(),
            "edit_phrase": getEditPhrase(),
            "repr": {
                "code": blocklyCode(),
                "xml": blocklyCodeAsPython()
            }
        }),
        success: function (data) {
            console.log("Success, data is "+data);
            if (successCallback) {
                successCallback(data);
            }
        }
    });
}

console.log("Loaded test page");
enablePageInteraction();
console.log("All done")
