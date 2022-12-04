
// $(window).scroll(function(){
//     $(".theFixed").css("top", Math.max(0, 250 - $(this).scrollTop()));
// });

$(function(){
    // console.log("FUNCTIONAL");
    $('.fade-out').click(function(){
        // console.log($(this).attr('id'));
        url = $(this).attr('value');
        // $(this).toggleClass("fade-out");
        $(this).animate({
            "right": "-40%",
            opacity:0
        }, function(){
            window.open(url, "_blank");
        });
    });
    $('.fade-down').click(function(){
        // console.log($(this).attr('id'));
        url = $(this).attr('value');
        // $(this).toggleClass("fade-out");
        $(this).animate({
            "top": "+=50px",
            opacity:0
        }, function(){
            // window.location = url;
            window.open(url, "_blank");
        });
    });

    $( ".show-more" ).click(function() {
        slider = $(this).attr('value');
        $( "#"+slider ).slideToggle( "slow", function() {
          // Animation complete.
        });
      });


});
