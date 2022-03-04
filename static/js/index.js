// Script to the INDEX page

// Function to change the hero section img on mobile screens, making the mobile UI improved
$(window).resize(function(){
    var width = $(window).width(); 
    if (width < 450) {
      $(".first-slide-img").attr("src","https://res.cloudinary.com/arthurvg/image/upload/v1646352737/jakub-dziubak-iOHJKJqO6E0-unsplash_vxmtc8_lhkmwg.jpg");
      $(".second-slide-img").attr("src","https://res.cloudinary.com/arthurvg/image/upload/v1646352737/jakub-dziubak-iOHJKJqO6E0-unsplash_vxmtc8_lhkmwg.jpg");
    }
    else {
      $(".first-slide-img").attr("src","https://res.cloudinary.com/arthurvg/image/upload/v1638584754/jakub-dziubak-iOHJKJqO6E0-unsplash_vxmtc8.jpg");
      $(".second-slide-img").attr("src","https://res.cloudinary.com/arthurvg/image/upload/v1638584754/jakub-dziubak-iOHJKJqO6E0-unsplash_vxmtc8.jpg");
    }
}); 

$(window).ready(function(){
    var width = $(window).width(); 
    if (width < 450) {
      $(".first-slide-img").attr("src","https://res.cloudinary.com/arthurvg/image/upload/v1646352737/jakub-dziubak-iOHJKJqO6E0-unsplash_vxmtc8_lhkmwg.jpg");
      $(".second-slide-img").attr("src","https://res.cloudinary.com/arthurvg/image/upload/v1646352737/jakub-dziubak-iOHJKJqO6E0-unsplash_vxmtc8_lhkmwg.jpg");
    }
}); 