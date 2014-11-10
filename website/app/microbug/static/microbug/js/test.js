function enablePageInteraction() {
    $('#editor-tabs').tab();
    console.log("Tabs enabled on ", $('#editor-tabs'))

    $('#buildCode').click(function() {
        console.log("Building code");
        compileBlockly();
    })

}

function setupBlockly() {
    Blockly.inject(document.getElementById('blockly'),
        {
            path: '/static/microbug/blockly/',
            toolbox: document.getElementById('toolbox'),
            trashcan: false
        });
}

function compileBlockly() {
    var code = Blockly.Python.workspaceToCode();

    var xml = Blockly.Xml.workspaceToDom(Blockly.mainWorkspace);
    var xml_text = Blockly.Xml.domToText(xml);


    $("#code").html("<P><PRE>" + code + "</PRE>");
    $.ajax({
        type: "POST",
        url: "/microbug/build_code/",
        data: JSON.stringify({"repr": {"code": code, "xml": xml_text}}),
        success: function (data) {
            console.log("Success, data is "+data);
            //var someid = data["id"];
            //text = '<P>Link to this version - <a href="/blockly_reload.html?id=' + someid + '"> ' + someid.toString() + ' </a>';
            //$("#resultblock").html(text);
        }
    });
}

console.log("Loaded test page");
enablePageInteraction();
setupBlockly();

