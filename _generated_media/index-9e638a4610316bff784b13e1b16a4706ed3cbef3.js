console.info('index.js loaded');
$(window).load(function () {
  $('#mandala').on('transitionend webkitTransitionEnd oTransitionEnd otransitionend', function(e){
    $('#mandala-text').css('opacity', 1);
    $('#mandala-sections a').on('mouseenter', function(e){
      $("#sub-nav span").hide();
      $("#"+$(this).data('nav')).show();
    });
    // $('#mandala-sections a').on('mouseleave', function(e){
    //   $("#sub-nav span").hide();
    //   $("#nav-default").show();
    // });
    $('.transition-hidden').fadeIn(400, function(){
      $('#planets').show();
    });
  });
  // Hide elements below the manadala until it's expanded for performance
  // debugger;
  $('#root_footer, #footer, #sub-nav').addClass('transition-hidden');
  setTimeout(function () {
    $('#mandala').addClass('active');
  }, 1000);
});
// $('#mandala').on('mouseenter', function(e){
//   $('#mandala').addClass('active');
// });
// $('#mandala').on('mouseleave', function(e){
//   $('#mandala').removeClass('active');
// });