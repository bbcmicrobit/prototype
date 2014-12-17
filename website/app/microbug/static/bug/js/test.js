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
var update_user_details_btn = $('#update-user-details');
var create_user_button = $('#createUser');
var created_user_details = $('#createdUserDetails');
var created_user_name = $('#createdUserName');
var created_user_password = $('#createdUserPassword');
var facilitator_password_reset_request_btns = $('.facilitatorPasswordResetRequest');
var forkCodeBtn = $('.forkCode');
var needs_facilitator_email = $('#needs_facilitator_email');
var load_code_btns = $('.load-code-btn');
var clear_code_btn = $('.clear-code-btn');
var build_tutorial_btn = $('.buildTutorialProgram');

var runCodeButton = document.getElementById("RunCodeButton");
var pauseCodeButton = document.getElementById("PauseCodeButton");
var stepCodeButton = document.getElementById("StepCodeButton");
var resetCodeButton = document.getElementById("ResetCodeButton");



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
                    window.location.replace('/bug/program/'+program_id);
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

    setupUserDetailsUpdate();

    setupCreateUser();

    setupForgotPasswordButton();

    setupFacilitatorPasswordReset();

    setupForkCode();

    setupRequireFacilitatorEmail();

    setupLoadCodeBtn();

    setupClearCodeBtn();

    setupBuildTutorialButton();
}

function setupBuildTutorialButton() {
    if (build_tutorial_btn.length > 0) {
        build_tutorial_btn.click(function() {
            bootbox.dialog({
                // Lorem ipsum
                title: "Build Program from Tutorial",
                message: "Enter a name to store your program as.<br/>" +
                "<label for='program_name'>Program Name:&nbsp;</label>" +
                "<input id='program_name' name='program_name' style='width:30em' placeholder='The name for your program'></input>",
                buttons: {
                    build: {
                        label: "<i class='fa fa-cog'></i>&nbsp;Store Program",
                        className: "btn-success",
                        callback: function () {
                            //bootbox.alert(
                            //    "NAME: "+getProgramName()+"<br/>"+
                            //        "CODE: <pre>"+blocklyCode()+"</pre><br/>"+
                            //        "XML: <pre>"+blocklyCodeAsPython()+"</pre><br/>"
                            //);
                            console.log("NAME: ",getProgramName());
                            console.log("CODE: ",blocklyCode());
                            console.log("XML: ",blocklyCodeAsPython());
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
                                    bootbox.alert("Your program has been stored")
                                },
                                error: function (jqHxr, textStatus, errorText) {
                                    bootbox.alert("Error saving program, please try again later");
                                }
                            });
                        }
                    },
                    cancel: {
                        label: "<i class='fa fa-close'></i>&nbsp;Cancel",
                        className: "btn-danger"
                    }
                }
            });
        });
    } else {
        console.log("No build tutorial button, skipping");
    }
}

function setupClearCodeBtn() {
    if (clear_code_btn.length > 0) {
        console.log("Setting up clear code button");
        clear_code_btn.click(function() {            bootbox.confirm(
                // Lorem ipsum
                "Clearing your code will lose any unsaved work, continue?",
                function(result) {
                    if (result) {
                        Blockly.mainWorkspace.clear();
                    }
                }
            );
        })
    }
}

function setupLoadCodeBtn() {
    if (load_code_btns.length >0 ) {
        console.log("Setting up load code buttons");
        load_code_btns.click(function(ev) {
            bootbox.confirm(
                // Lorem ipsum
                "You will lose any unsaved work, continue?",
                function(result) {
                    if (result) {

                        var clickedOn = $(ev.currentTarget);
                        var blockly_xml_text = clickedOn.attr('data-blockly-xml');
                        var blockly_xml = Blockly.Xml.textToDom(blockly_xml_text);

                        Blockly.mainWorkspace.clear();
                        Blockly.Xml.domToWorkspace(Blockly.mainWorkspace, blockly_xml);
                    }
                }
            );

            ev.preventDefault();
        });
    } else {
        console.log("No load code buttons, skipping");
    }
}
function requestFacilitatorEmail() {
    bootbox.dialog({
        title: "Facilitator Email",
        message: "Please provide your email address so that we are able to "+
            "contact you with important facilitor updates, such as when one "+
            "of your children requires a password reset.<br/>" +
            "<label for='facilitatorEmail'>Email:&nbsp;</label>" +
            "<input id='facilitatorEmail' placeholder='Your email'></input>",
        buttons: {
            success: {
                label: "<i class='fa fa-envelope'></i>&nbsp;Update Email",
                className: "btn-success",
                callback: function () {
                    var email_address = $('#facilitatorEmail').val();
                    $.ajax({
                        type: "POST",
                        url: "/bug/set_email/",
                        data: JSON.stringify({
                            "email": email_address
                        }),
                        success: function(data) {
                            // Lorem ipsum
                            bootbox.alert("Your email has been stored, thank you.")
                        },
                        error: function (jqXhr, textStatus, errorThrown) {
                        var statusCode = jqXhr.statusCode().status;
                            switch (statusCode) {
                                case 400: // Client error
                                    // Lorem ipsum
                                    bootbox.alert("Invalid email address, please check and retry", function() {
                                        requestFacilitatorEmail();
                                    });
                                    break;
                                default:
                                    bootbox.alert("Error, cannot set email");
                                    console.log("Cannot set email: "+textStatus+", "+errorThrown);
                            }
                        }
                    });
                }
            },
            danger: {
                label: "<i class='fa fa-exclamation-triangle'></i>&nbsp;Not now",
                className: "btn-danger"
            }
        }
    });
}

function setupRequireFacilitatorEmail() {
    if (needs_facilitator_email.length > 0){
        requestFacilitatorEmail();
    }
}

function setupForkCode() {
    if (forkCodeBtn.length > 0) {
        console.log("Setting up fork code");
        forkCodeBtn.click(function(ev) {
            // Lorem ipsum.
            bootbox.confirm(
                "This will create your own version of this program, are you sure?",
                function(result) {
                    if (!result) { return }
                    $.ajax({
                        type: "POST",
                        url: "/bug/fork_code",
                        data: JSON.stringify({
                            "src_id": $(ev.currentTarget).attr('data-src-id')
                        }),
                        success: function(data) {
                            data = JSON.parse(data);
                            window.location.replace('/bug/program/'+data['fork_id'])
                        },
                        error: function (jqXhr, textStatus, errorThrown) {
                            bootbox.alert("Error, cannot create own version");
                            console.log("Cannot create own version: "+textStatus+", "+errorThrown);
                        }
                    })
                }
            )
        })
    } else {
        console.log("No fork code button, skipping");
    }
}

function setupFacilitatorPasswordReset() {
    if (facilitator_password_reset_request_btns.length > 0) {
        facilitator_password_reset_request_btns.click(function(ev) {
            child_id = $(ev.currentTarget).attr('data-child-id');
            // Lorem ipsum
            bootbox.confirm("<p>This will reset the password for this user, and it's your responsibility to pass the new password along to them.</p><p><em>Are you sure?</em></p>", function(result) {
                if (result) {
                    $.ajax({
                        type: "POST",
                        url: "/bug/confirm_password_reset",
                        data: JSON.stringify({
                            "id": child_id
                        }),
                        success: function(data) {
                            data = JSON.parse(data);
                            // Lorem ipsum
                            bootbox.alert("Password has been reset to '<em>"+data.password+"</em>'",
                                function() {
                                    location.reload();
                                });
                        },
                        error: function (jqXhr, textStatus, errorThrown) {
                            var statusCode = jqXhr.statusCode().status;
                            switch (statusCode) {
                                case 405: // Not allowed
                                    // Lorem ipsum
                                    bootbox.alert("Cannot reset password.  You must be the child's facilitator, and there must be a request pending.", function () {
                                        location.reload();
                                    });
                                    break;
                                default:
                                    bootbox.alert("An error occured, cannot reset password");
                                    console.log(textStatus,": ",errorThrown);
                            }
                        }
                    });
                }
            });
            ev.preventDefault();
        })
    } else {
        console.log("No facilitator password request buttons, skipping");
    }
}

function setupForgotPasswordButton() {
    var forgot_password_button = $('#forgotPasswordButton');
    if (forgot_password_button.length > 0) {
        console.log("Setting up Forgot Password Button");
        forgot_password_button.click(function(ev) {
            bootbox.dialog({
                // Lorem ipsum.
                title: "Forgotten Password",
                // Lorem ipsum.
                message:
                    "This will send a message to your facilitators asking them to reset your account.<br/>" +
                    "<label for='requestUsername'>Username:</label>" +
                    "<input type='text' id='requestUsername' placeholder='Your username'></input>",
                buttons: {
                    make_request: {
                        // Lorem ipsum.
                        label: '<i class="fa fa-unlock-alt"></i>&nbsp;Request password reset',
                        className: 'btn-primary',
                        callback: function() {
                            $.ajax({
                                type: "POST",
                                url: "/bug/request_password_reset",
                                data: JSON.stringify({
                                    "username": $('#requestUsername').val()
                                }),
                                success: function() {
                                    // Lorem ipsum
                                    bootbox.alert("Your facilitator has been asked to reset your password");
                                },
                                error: function() {
                                    // Lorem ipsum
                                    bootbox.alert("An error has happened, cannot request password reset.  Please try later");
                                }
                            });
                        }
                    },
                    cancel_request: {
                        // Lorem ipsum
                        label: '<i class="fa fa-close"></i>&nbsp;No, don\'t request change',
                        className: 'btn-primary'
                    }
                }
            });
            ev.preventDefault();
        })
    } else {
        console.log("No Forgot Password Button, skipping");
    }
}

function setupCreateUser() {
    if (create_user_button.length > 0) {
        console.log("Setting up Create User Button");
        create_user_button.click(function(ev) {
            console.log("Creating new user");
            $.ajax({
                type: "POST",
                url: "/bug/create_user/",
                data: '',
                dataType: 'json',
                success: function (data) {
                    created_user_name.text(data.username);
                    created_user_password.text(data.password);
                    created_user_details.show();
                }
            });
            ev.preventDefault();
        })
    } else {
        console.log("No Create User button, skipping");
    }
}
function setupUserDetailsUpdate() {
    if (update_user_details_btn.length > 0 ) {
        console.log("Setting up user details update");
        update_user_details_btn.click(function() {
            console.log("Updating user details");
            var email_input = $('#email');
            if (email_input.length > 0) {
                var email = email_input.val();
            } else {
                var email = null;
            }
            $.ajax({
                type: "POST",
                url: "/bug/update_user_details/",
                data: JSON.stringify({
                    "name": $('#name').val(),
                    "email": email,
                    "question_answers": [
                        $('#question_1').val(),
                        $('#question_2').val(),
                        $('#question_3').val(),
                        $('#question_4').val(),
                        $('#question_5').val(),
                        $('#question_6').val(),
                        $('#question_7').val(),
                        $('#question_8').val(),
                        $('#question_9').val(),
                        $('#question_10').val()
                    ]
                }),
                success: function (data) {
                    location.reload();
                },
                error: function (jqXhr, textStatus, errorThrown) {
                    var statusCode = jqXhr.statusCode().status;
                    switch (statusCode) {
                        case 400: // Client error, invalid email address
                            // Lorem ipsum
                            bootbox.alert("Invalid email address, please check and try again");
                            break;
                        case 403: // Not allowed
                            // Lorem ipsum
                            bootbox.alert("Sorry, you can only change your own details.");
                            break;
                        default:
                            // Lorem ipsum
                            bootbox.alert("An error occured while updating your info.");
                    }
                }
            })
        });
    } else {
        console.log("No update button, skipping");
    }
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
                // Lorem ipsum
                message: "This will confirm you as a facilitator for '<strong>" + child_name + "</strong>'.",
                title: "Accepting request from '<strong>" + child_name + "</strong>'.",
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
                // Lorem ipsum
                message: "This will decline the facilitator request from '<strong>" + child_name + "</strong>', and delete it from the system.",
                title: "Decling request from '<strong>" + child_name + "</strong>'.",
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
        url: "/bug/respond_to_facilitator_request",
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
                    // Lorem ipsum
                    bootbox.alert("Can't find that facilitator request, have you already replied to it?.");
                    break;
                case 403: // Not allowed
                    // Lorem ipsum
                    bootbox.alert("Sorry, this does not seem to be a request directed to you.");
                    break;
                default:
                    // Lorem ipsum
                    bootbox.alert("An error occured processing the facilitator request.");
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
            // Lorem ipsum
            message:
                "In order to add a facilitator you will need to contact them "+
                "to know their username, then enter it in the box below and "+
                "wait for them to confirm." +
                "<input type='text' id='facilitator-username' style='width:100%'>",
            title: "Add Facilitator",
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
        url: "/bug/facilitator_request",
        data: JSON.stringify({
            "facilitator_name": faciliator_name
        }),
        success: function(data) {
            // Lorem ipsum
            bootbox.alert("Your facilitator has been told of your request..");
            location.reload();
        },
        error: function (jqXhr, textStatus, errorThrown) {
            var statusCode = jqXhr.statusCode().status;
            switch(statusCode) {
                case 401: // Unauthorized
                    // Lorem ipsum
                    bootbox.alert("You must be logged in to make a facilitator request.");
                    break;
                case 404: // Not found
                    // Lorem ipsum
                    bootbox.alert("Can't find a user with that username.");
                    break;
                case 405: // Not allowed
                    // More details in body text
                    console.log("ERROR: ",jqXhr);
                    bootbox.alert("Cannot send request. "+jqXhr.responseText);
                    break;
                default:
                    // Lorem ipsum
                    bootbox.alert("An error occured making the facilitator request.");
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
        url: "/bug/sign_out",
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
        url: "/bug/login_pane",
        success: function(data) {
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
                    url: "/bug/authenticate_user/",
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
                setupForgotPasswordButton();
            })

            setupForgotPasswordButton();
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
    if (program_id == '' || program_id==undefined) {
        console.log("No program ID");
        return;
    }
    var callback = function() {
        updateProgramStatus(program_id)
    };

    $.ajax({
        type: 'GET',
        url: '/bug/queue_status/'+program_id,
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
            '<a class="btn btn-primary" href="/bug/download/'+data.id+'">' +
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
        url: "/bug/rename_program/",
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
                path: '/static/bug/blockly/',
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

            var codeParsed = false;
            var codePaused = false;
            var codeComplete = false;
            var stepMode = false;
            var stepRequest = false;

            var highlightPause = false;


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

			function highlightBlock(id)
			{
			    Blockly.mainWorkspace.highlightBlock(id);
			    highlightPause = true;
			}

            function stepCode()
            {
                var statusMsg = "Everything OK";

                while (!highlightPause)
                {
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
                            codeComplete = true;
                            codeParsed = false; //ensure we re-parse when run is pressed to restart JS emu

                            pauseCodeButton.disabled = true;
                            runCodeButton.disabled = false;

                            Blockly.mainWorkspace.highlightBlock(null);
                            return;
                        }
                    }
                }
            }

            function runCode()
            {
                // If device not ready or code paused, check back shortly
                if (!DALJS.deviceReady() || codePaused || (stepMode && !stepRequest))
                {
                    setTimeout(function()
                    {
                        runCode();
                    }, 50);
                    return;
                }

                // Step! (will keep executing until higlightPause)
                stepCode();

                if (codeComplete)
                {
                    stepMode = false;
                    return;
                }

                if (stepMode)
                {
                    stepRequest = false;
                    highlightPause = false;
                }
                else
                {
                    // A block has been highlighted.  Pause execution here.
                    var delay = parseInt(document.getElementById('pausetime').value);

                    setTimeout(function()
                    {
                        runCode();
                        highlightPause = false;
                    }, delay);
                }
            }

            function reparse()
            {
                if (!codeParsed)
                {
                    codeComplete = false;
                    if (!parseCode())
                    {
                        alert("Problem parsing code!");
                        return false;
                    }
                    Blockly.mainWorkspace.highlightBlock(1);
                }
                return true;
            }

            function runCodeHandler()
            {
                //DALJS.reset();
                if (!reparse())
                    return;//BADOSITY

                if (codePaused)
                {
                    //turn off pause, run freely with delay
                    pauseCodeHandler();
                    return;                   
                }
                if (stepMode)
                {
                    stepMode = false;
                    stepRequest = false;
                }
                console.log("runCodeHandler runCode()");
                pauseCodeButton.disabled = false;
                runCodeButton.disabled = true;
                runCode();
            }


            function stepCodeHandler()
            {
                if (!reparse())
                    return;//BADOSITY

                if (codePaused)
                {
                    pauseCodeHandler();
                    runCodeButton.disabled = false;
                    pauseCodeButton.disabled = true;
                }


                if (!stepMode)
                {
                    console.log("stepCodeHandler enabling step mode");
                    stepMode = true;
                    stepRequest = true;
                    runCode();
                    return;
                }

                console.log("stepCodeHandler stepping");
                stepRequest = true;
                runCode();
            }

            function pauseCodeHandler()
            {
                runCodeButton.disabled = codePaused;
                codePaused = !codePaused;
                console.log("Code Paused " + codePaused);
            }

            function resetCodeHandler()
            {

            }

			function parseCode()
			{
			    // Generate JavaScript code and parse it.
			    Blockly.JavaScript.STATEMENT_PREFIX = 'highlightBlock(%1);\n';
			    Blockly.JavaScript.addReservedWords('highlightBlock');
			    
			    var code = Blockly.JavaScript.workspaceToCode();
                //console.log("RUNNING: ",code);

                if (dalcode === undefined)
                    alert('dalcode undefined');

			    //alert('Ready to execute this code:\n\n' + code);
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
                codeParsed = true;
                return true;
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
            runCodeButton.addEventListener("click", runCodeHandler);
            pauseCodeButton.addEventListener("click", pauseCodeHandler);
            stepCodeButton.addEventListener("click", stepCodeHandler);
            resetCodeButton.addEventListener("click", resetCodeHandler);

			SIMIO.render();

            var jqxhr = $.get('/static/bug/js/dal_interpreter.txt', function(data, txt, err) {
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
        url: "/bug/build_code/",
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
        url: "/bug/build_code/",
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
$(document).ready(function() {
    console.log("** Document ready");
    enablePageInteraction();
});

console.log("All done")
