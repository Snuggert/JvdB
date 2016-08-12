$(function() {
    $('.image-link').magnificPopup({
        type:'image',
        closeOnContentClick: true,
        callbacks: {
            open: function() {
                $('.mfp-img').css('max-height', $(window).height() * 0.9 + 'px');
                $('.mfp-img').css('max-width', $(window).width() * 0.9 + 'px');
                $('.mfp-bg').css('opacity', 1.0).css('background', '#FFFFFF');
            },
        }
    });
});