$(document).ready( function() {
    $("#template_select").change(function() {
        var selectedTemplate = $('#template_select').find(":selected").text();
    });
});

function sendTemplatePing() {
    var templateBody = $('#template_select').find(":selected").text();
    var company = $('#company_select').find(":selected").text();
    var guest = $('#guest_select').find(":selected").text();
    var timeOfDay = getTimeOfDay()
    var greeting = "Good " + timeOfDay + ", "

    templateBody = substituteBodyValues(templateBody, company, guest);

    alert(
    "Successfully sent the following Ping: \n" +
    "\nSender: " + company +
    "\nRecipient: " + guest +
    "\nMessage: \n" + greeting + "\n" + templateBody
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

function getTimeOfDay() {
    var time = new Date().getHours();
    var timeOfDay = (
        time < 12 ? "Morning" :
        time < 18 ? "Afternoon" :
        "Evening"
        );
    return timeOfDay
}
