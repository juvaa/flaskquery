$(document).ready(function () {
    $('input[type=radio][name=alcohol]').change(function() {
        if (document.getElementById('alcohol-0').checked) {
            $('#drinks').show()
        } else {
            $('#drinks').hide()
        }
    });

    $('input[type=checkbox][name=operator]').change(function() {
        if (document.getElementById('operator').checked) {
            $('body').css('color', '#51ff00');
            $('.operatorlead').show();
            $('.nonoperatorlead').hide();
            $('.opleaf').show();
            $('.leaf').hide();
            $('.op').show();
            $('.nonop').hide();

        } else {
            $('body').css('color', 'white');
            $('.operatorlead').hide();
            $('.nonoperatorlead').show();

            $('.leaf').show();
            $('.opleaf').hide();
            $('.nonop').show();
            $('.op').hide();
        }
    });
    $('input[type=checkbox][name=avec]').change(function() {
        if (document.getElementById('avec').checked) {
            $('#avec-info').show();
            $('#avec_consent').prop("checked", false);
        } else {
            $('#avec-info').hide();
            $('#avec_consent').prop("checked", true);
        }
    });
        $('input[type=radio][name=avec_alcohol]').change(function() {
        if (document.getElementById('avec_alcohol-0').checked) {
            $('#avec-drinks').show();
        } else {
            $('#avec-drinks').hide();
        }
    })
});



