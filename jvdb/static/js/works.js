$(function() {
    $('.image-link').magnificPopup({
        type:'image',
        closeOnContentClick: true,
        callbacks: {
            open: function() {
                $('.mfp-img').css('max-height', $(document).height() * 0.8 + 'px');
                $('.mfp-bg').css('opacity', 1.0).css('background', '#FFFFFF');

            },
        }
    });
});