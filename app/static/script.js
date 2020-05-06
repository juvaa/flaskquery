
$(document).ready(function () {
    $('input[type=checkbox][name=greeting]').change(function() {
        if (document.getElementById('greeting').checked) {
            $('#greeting_box').show();
        } else {
            $('#greeting_box').hide();
        }
    });
    $('input[type=checkbox][name=avek]').change(function() {
        if (document.getElementById('avek').checked) {
            $('#avek_box').show();
        } else {
            $('#avek_box').hide();
        }
    });
});