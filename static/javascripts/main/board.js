$(document).bind("spling:navigate", function(e, url){

  pattern = /user\/7GPortal\/splingboards\/(.*)/;
  match = url.match(pattern);

  if (match && match[1])
    window.location = match[1];

});