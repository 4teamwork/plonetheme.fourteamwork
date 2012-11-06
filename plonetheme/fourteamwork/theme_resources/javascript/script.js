(function ($) {
    $(function () {
        $('#mobile-globalnav').bind('click', function() {
            $('#portal-globalnav').toggleClass('visible');
            $('#portal-searchbox').removeClass('visible');
        });

        $('#mobile-search').bind('click', function() {
            $('#portal-searchbox').toggleClass('visible');
            $('#portal-globalnav').removeClass('visible');
        });

        $('#mobile-page-settings').bind('click', function() {
            $('#edit-bar').toggleClass('visible');
            $(this).toggleClass('selected');
        });
    });

    $('.flexslider').flexslider({
        animation: 'slide',
        manualControls: '#tabs-nav li'
    });

    $('.logo-flexslider').flexslider({
        animation: 'slide',
        direction: 'vertical',
        controlNav: false,
        directionNav: false
    });


}(jQuery));