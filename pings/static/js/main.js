$(document).ready( function() {
    $('#radio_value').click(function() {
        $('#result').empty();
        var value = $("input[type='radio']:checked").val();

        if ($("input[type='radio']").is(':checked')) {
            $('#result').append("Checked Radio Button Value is :<span> "+ value +" </span>");
        } else {
            alert(" Please Select any Option ");
        }
    });

    $("#template_select").change(function() {
        var selectedTemplate = $('#template_select').find(":selected").text();
        console.log("Current template subject:" + selectedTemplate);
    });
});

function sendPing() {
    var templateBody = $('#template_select').find(":selected").text();
    var company = $('#company_select').find(":selected").text();
    var guest = $('#guest_select').find(":selected").text();

    templateBody = fillTemplateValues(templateBody, company, guest);

    alert(
    "Successfully sent the following Ping: \n" +
    "\nSender: " + company +
    "\nRecipient: " + guest +
    "\nMessage: \n" + templateBody
    );
}

function fillTemplateValues(body, company, guest) {
   var mapObj = {
       COMPANY: company,
       GUEST: guest
    };
    body = body.replace(/COMPANY|GUEST/gi, function(matched){
      return mapObj[matched];
    });
    return body
}




//
//    $("#template-form").on("change", (function() {
//        var radioValue = $("[name='template']:checked").text();
//        console.log('radio text:' + radioValue);
//        alert($("input[name='template']:checked", "#template-form").val());
//    }));
//    $("#template-form").click( function(event) {
//        console.log('you clicked somewhere in the form');
//    });
