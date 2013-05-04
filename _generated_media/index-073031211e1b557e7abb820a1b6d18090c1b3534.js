console.info('index.js loaded');

var rotator = function(){
  console.log('active');
  var last = $('#planets a.active');
  var active = last.next();
  // perhaps nothing is active, or there is no next()
  if (active.length === 0){
    active = $('#planets a:first-child');
  }
  // last.removeClass('active');
  active.addClass('active');
  return true;
};

$(window).load(function () {
  // do not also react to transitionEnd, this will trigger everything twice
  $('#mandala').one('webkitTransitionEnd oTransitionEnd', function(e){
    $('#mandala-text').css('opacity', 1);
    $('#mandala-sections a').on('mouseenter', function(e){
      $("#sub-nav span").not('#nav-default').hide();
      $("#"+$(this).data('nav')).show();
    });
    // $('#mandala-sections a').on('mouseleave', function(e){
    //   $("#sub-nav span").hide();
    //   $("#nav-default").show();
    // });
    $('.transition-hidden').fadeIn(400, function(){
      $('#planets').show();
    });
    setInterval(rotator, 2000);
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