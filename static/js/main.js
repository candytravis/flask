function main($center) {
     $('.center').hide();
   $('.center').fadeIn(4000);

}

function main($image) {
	$('.image').hide();
	$('.image').fadeIn(4000);
}

function main($navList) {
    $('navList').mouseenter(function() {
        $('navList').fadeTo('fast', 1);
    });
    $('navList').mouseleave(function() {
        $('navList').fadeTo('fast', 0.5);
    });
};

$(document).ready(main);