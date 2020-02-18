$(document).ready(function () {
    $('input[type=checkbox][name=cruise]').change(function() {
        if (document.getElementById('cruise').checked) {
            $('#buffet').show();
        } else {
            $('#buffet').hide();
        }
    });
    $('input[type=checkbox][name=sitsit]').change(function() {
        if (document.getElementById('sitsit').checked) {
            $('#alcohol').show();
            $('#specialneeds').show();
        } else {
            $('#alcohol').hide();
            $('#specialneeds').hide();
        }
    });
})