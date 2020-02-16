$(document).ready(function () {
    $('input[type=checkbox][name=cruise]').change(function() {
        $('#buffet').toggle()
    });
    $('input[type=checkbox][name=sitsit]').change(function() {
        $('#alcohol').toggle()
        $('#specialneeds').toggle()
    });
})