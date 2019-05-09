$(document).ready( function() {
    $("#template-form").on("change", (function() {
        var radioValue = $("[name='template']:checked").text();
        console.log('radio text:' + radioValue);
        alert($("input[name='template']:checked", "#template-form").val());
    }));
//    $("#template-form").click( function(event) {
//        console.log('you clicked somewhere in the form');
//    });
});
