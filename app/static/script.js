
$(document).ready(function () {
    $('input[type=checkbox][name=greeting]').change(function() {
        if (document.getElementById('greeting').checked) {
            $('#greeting_box').show();
        } else {
            $('#greeting_box').hide();
        }
    });
    $('input[type=radio][name=drink]').change(function() {
        if (document.getElementById('drink-0').checked) {
            $('#alcohol_box').show()
            $('#none_box').hide()
        } else {
            $('#alcohol_box').hide()
            $('#none_box').show()
        }
    });
    $('input[type=checkbox][name=avec]').change(function() {
        if (document.getElementById('avec').checked) {
            $('#avec_box').show();
        } else {
            $('#avec_box').hide();
        }
    });
    $('input[type=radio][name=avec_drink]').change(function() {
        if (document.getElementById('avec_drink-0').checked) {
            $('#avec_alcohol_box').show()
            $('#avec_none_box').hide()
        } else {
            $('#avec_alcohol_box').hide()
            $('#avec_none_box').show()
        }
    });
    (function() {
        var canvas = document.getElementById('background'),
                context = canvas.getContext('2d');
    
        // resize the canvas to fill browser window dynamically
        window.addEventListener('resize', resizeCanvas, false);
    
        function resizeCanvas() {
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
    
                /**
                 * Your drawings need to be inside this function otherwise they will be reset when 
                 * you resize the browser window and the canvas goes will be cleared.
                 */
                drawStuff(); 
        }
        resizeCanvas();
    
        function drawStuff() {
                // do your drawing stuff here

        }
    })();
});