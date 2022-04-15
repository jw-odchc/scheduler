
//Check all values on submit

$("[name=submit]").click(function(event) {
    var emptyError = false;
    var inputError = false;
    $('.dropdown-content').each(function() {
        var answer = $(this).val();
        var formId = $(this).attr('id');
        formId = formId.slice(1,2);
        formId = '#c'.concat(formId);f
        if (answer == '0') {
            emptyError = true;
            $(this).css("background", "red");
            $(this).focus();
        }
        if (answer == '2'){
            if ($(formId).val() == '') {
                inputError = true;
                $(formId).css("background", "yellow");
                $(formId).attr("placeholder", "When answering No, please comment.");
                $(formId).focus();
            }
        }
        else {
        $(formId).css("background", "white");
        $(formId).attr("placeholder", "Comments.");
        }
    });
    if (emptyError) {
        event.preventDefault();
        alert("Please answer all the questions before submitting, if you want to save your work and submit later, please press Save");
    }
    if (inputError) {
        event.preventDefault();
        alert("If selecting No, please leave a comment.");
    }
});
