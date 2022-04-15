// DatePicker Support


$('.datepick').datepicker({
    weekStart: 1,
    daysOfWeekHighlighted: "6,0",
    autoclose: true,
    todayHighlight: true,
    orientation: "auto",
    container: '#startDateCont'
});
$('.datepick').datepicker("setDate", new Date());


$('#firstPeriod').datepicker({
    weekStart: 1,
    daysOfWeekHighlighted: "6,0",
    autoclose: true,
    todayHighlight: true,
    orientation: "auto",
    container: '#firstPeriodCont'
});
$('#firstPeriod').datepicker("setDate", new Date());

$('#repeatPeriod').datepicker({
    weekStart: 1,
    daysOfWeekHighlighted: "6,0",
    autoclose: true,
    todayHighlight: true,
    orientation: "auto",
    container: '#endPeriodCont'
});
$('#repeatPeriod').datepicker("setDate", new Date());

// Hidding Div and Form Validation

$("#reoccurring").change(function () {
    if ($(this).val() == "Yes") {
        $('#repeatDiv').slideDown();
        $('#dateRangeDiv').slideUp();
        $('#period').attr('required', '');
        $('#period').attr('data-error', 'This field is required.');
        $('#firstPeriod').attr('required', '');
        $('#firstPeriod').attr('data-error', 'This field is required.');
        $('#repeatPeriod').attr('required', '');
        $('#repeatPereriod').attr('data-error', 'This field is required.');
    } else {
        $('#repeatDiv').slideUp();
        $('#dateRangeDiv').slideDown();
        $('#period').removeAttr('required');
        $('#period').removeAttr('data-error');
        $('#firstPeriod').removeAttr('required');
        $('#firstPeriod').removeAttr('data-error');
        $('#repeatPeriod').removeAttr('required');
        $('#repeatPeriod').removeAttr('data-error');
    }
});
$("#reoccurring").trigger("change");


$("#useProcs").change(function () {
    if ($(this).val() == "Yes") {
        $('#procDiv').slideDown();
        $('#procCodes').attr('required', '');
        $('#procCodes').attr('data-error', 'This field is required.');
    } else {
        $('#procDiv').slideUp();
        $('#procCodes').removeAttr('required');
        $('#procCodes').removeAttr('data-error');
    }
});
$("#useProcs").trigger("change");



$("#reviwerEqual").change(function () {
    if ($(this).val() == "No") {
        $('#diff-prov-types').slideDown();
        $('#diff-prov-hr').slideDown();
        $('#procCodes').attr('required', '');
        $('#procCodes').attr('data-error', 'This field is required.');
    } else {
        $('#diff-prov-types').slideUp();
        $('#diff-prov-hr').slideUp();
        $('#procCodes').removeAttr('required');
        $('#procCodes').removeAttr('data-error');
    }
});
$("#reviwerEqual").trigger("change");

$("[name=reviewerProv]").change(function () {
    if ($("#reviwerEqual").val() == "Yes") {
        var checked = $(this).attr("id");
        checked = checked.slice(12, 14);
        checked = 'revieweeProv'.concat(checked);
        if ($(this).is(':checked')) {
            document.getElementById(checked).checked = true;
        }
        else {
            document.getElementById(checked).checked = false;
        }
    }
});


$("#numQuestions").change(function () {
    var questions = $(this).val();
    for (let step = 1; step <= questions; step++) {
        var div = "#qDiv-".concat((step));
        $(div).show();
        var qs = "#q".concat(step);
        $(qs).attr('required', '');
        $(qs).attr('data-error', 'This field is required.');
    }
    questions++;
    for (let step = questions; step < 23 ; step++) {
        var div = "#qDiv-".concat(step);
       $(div).hide();
       var qs = "#q".concat(step);
       $(qs).removeAttr('required', '');
       $(qs).removeAttr('data-error', 'This field is required.');
    }
});
$("#numQuestions").trigger("change");

$(".sub-btn").mouseover( function() {
    $(".sub-btn").hide();
});

$("hr").mouseover( function() {
    $(".sub-btn").show();
});