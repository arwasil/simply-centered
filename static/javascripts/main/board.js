$(document).bind("spling:navigate", function(e, url){

  pattern = /user\/7GPortal\/splingboards\/(.*)/;
  match = url.match(pattern);

  patternBlog = /7gportal.com/;
  patternAmazon = /amazon.com/;
  
  if (match && match[1])
    window.location += '/'+match[1];
  else if(!url.match(patternBlog) && !url.match(patternAmazon))
    // Remove widget from start of url
    window.location = 'spling?url='+url.slice(7)

});
$(document).ready(function(){

  crumbs = window.location.pathname.split('/')
  $('#breadcrumbs').addClass(crumbs[1]);

});
