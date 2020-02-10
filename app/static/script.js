$(document).ready(function () {
    $('input[type=checkbox][name=cruise]').change(function() {
        $('#buffet').toggle()
    });
})