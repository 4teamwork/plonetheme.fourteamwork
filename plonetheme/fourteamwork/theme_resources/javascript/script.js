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

    // var resizer = function () {
    //     var $scrollable = $('.scrollable'),
    //         height = $scrollable.find('.focuss').height(),
    //         width = $('#content').width(),
    //         $navig = $('.browse');
    //     $scrollable.css('height', height + 30);
    //     $scrollable.css('width', width - 60);
    //     $scrollable.find('.focuss-wrapper').css('height', height);
    //     $scrollable.find('.focuss-wrapper').css('width', width - 90);

    //     // move the next/prev button
    //     $navig.css('top', (height / 2));
    // };

    // resizer();

    // $(window).resize(function(){
    //     resizer();
    // });




// TODO this is not working!!!!!!!!!!
    // $.fn.handleSwipes = function() {
    //   return this.each(function() {
    //     var api = $(this).data("scrollable");

    //     api.getRoot().addSwipeEvents()
    //        .bind('swipeleft', function() {
    //          api.next(100);
    //          window.console.log('LEFT!!!!!');
    //        })
    //        .bind('swiperight', function() {
    //          api.prev(100);
    //          window.console.log('RIGHT!!!!!');
    //        });
    //   });
    // };

    // $('.scrollable').scrollable({touch:false}).handleSwipes();


    $('.flexslider').flexslider({
        animation: 'slide'
    });

}(jQuery));