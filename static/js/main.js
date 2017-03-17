function main($center) {
     $('.center').hide();
   $('.center').fadeIn(4000);

}

function main($image) {
	$('.image').hide();
	$('.image').fadeIn(4000);
}

$(document).ready(function() {
    $('navigation').mouseenter(function() {
        $('navigation').fadeTo('fast', 1);
    });
    $('navigation').mouseleave(function() {
        $('navigation').fadeTo('fast', 0.5);
    });
});

$(document).ready(main);
