$(document).ready( function() {
    $("#template_select").change(function() {
        var selectedTemplate = $('#template_select').find(":selected").text();
        console.log("Current template subject:" + selectedTemplate);
    });
});

function sendTemplatePing() {
    var templateBody = $('#template_select').find(":selected").text();
    var company = $('#company_select').find(":selected").text();
    var guest = $('#guest_select').find(":selected").text();

    templateBody = substituteBodyValues(templateBody, company, guest);

    alert(
    "Successfully sent the following Ping: \n" +
    "\nSender: " + company +
    "\nRecipient: " + guest +
    "\nMessage: \n" + templateBody
    );
}

function substituteBodyValues(body, company, guest) {
   var mapObj = {
       COMPANY: company,
       GUEST: guest
    };
    body = body.replace(/COMPANY|GUEST/gi, function(matched){
      return mapObj[matched];
    });
    return body
}
