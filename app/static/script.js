$(document).ready(function () {
    $('input[type=radio][name=cruise]').change(function() {
        if (document.getElementById('cruise').checked) {
            $('#buffet').show()
        } else {
            $('#buffet').hide()
        }
    });
})