$(document).bind("spling:navigate", function(e, url){

  debugger;
  
  urls = {
    '17647' : 'healthy-diet',
    '19318' : 'mediterranean-diet',
    '19323' : 'paleo-diet'
  };

  pattern = /user\/portal\/splingboards\/(.*)/;
  match = url.match(pattern);

  if match && urls[match[1]]
    window.location = '/'+urls[match[1]];

});