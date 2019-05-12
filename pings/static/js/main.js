$(document).ready( function() { $("#template_select").change(function() { var selectedTemplate = $('#template_select').find(":selected").text(); });
});

function sendTemplatePing() {
    var templateBody = $('#template_select').find(":selected").text();
    var company = $('#company_select').find(":selected").text();
    var guest = $('#guest_select').find(":selected").text();
    var timeOfDay = getTimeOfDay()
    var greeting = "Good " + timeOfDay + " " + guest + ", "

    templateBody = substituteBodyValues(templateBody, company, guest, timeOfDay);

    alert(
    "Successfully sent the following Ping: \n" +
    "----------------------------------------------------\n" +
    "*SENDER: " + company +
    "\n*RECIPIENT: " + guest +
    "\n*MESSAGE: \n" + greeting + "\n" + templateBody +
    "\n----------------------------------------------------"
    );
}

function substituteBodyValues(body, company, guest, timeOfDay) {
   var mapObj = {
       COMPANY: company,
       GUEST: guest,
       TIMEOFDAY: timeOfDay
    };
    body = body.replace(/COMPANY|GUEST|TIMEOFDAY/gi, function(matched){
      return mapObj[matched];
    });
    return body
}

function getTimeOfDay() {
    var time = new Date().getHours();
    var timeOfDay = (
        time < 12 ? "morning" :
        time < 18 ? "afternoon" :
        "evening"
        );
    return timeOfDay
}
