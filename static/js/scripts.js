var LI_SITE_NAV;
var A_SUBMENU_PARENT;
var UL_CHILD;
var UL_CHILD_LI_A;

var A_RIGHT_MENU;
var UL_RIGHT_SUBMENU;

var CAROUSEL_SHOWN;
var CAROUSEL_COUNT;

var SUBMENU_ONHOVER;
var SUBMENU_PARENT_ONHOVER;
var CHILD_ONHOVER;

$(document).ready(function() {

	$("#popup-bg-overlay").hide();
	$(".main-popup").hide();

	$(".submenu").hide();
	$(".parent-triangle").hide();
	$(".child").hide();

	$("#menu-blogs-submenu").hide();

	init();

	animate();

	SUBMENU_PARENT_ONHOVER = false;
	CHILD_ONHOVER = false;

	$(".submenu").mouseenter(function() {
		SUBMENU_ONHOVER = true;
		console.log("Dropdown on Hover");
	}).mouseleave(function() {
		SUBMENU_ONHOVER = false;
		SUBMENU_PARENT_ONHOVER = false;
		CHILD_ONHOVER = false;
		$(this).hide();

		var top_menu = $(this).parent().children("a");
		top_menu.removeClass("active");

		console.log("Dropdown leave");
	});

	LI_SITE_NAV.mouseenter(siteNavHover).mouseleave(siteNavLeave);
	A_SUBMENU_PARENT.mouseenter(submenuParentHover).mouseleave(submenuParentLeave);
	UL_CHILD.mouseenter(childHover).mouseleave(childLeave);

	$("#site-nav ul").mouseenter(function() {
		if (SUBMENU_PARENT_ONHOVER || CHILD_ONHOVER) return;

		$(this).css("paddingBottom", "50px");
		$("#site-header").css("box-shadow", "0px 100px 700px #888");

		console.log("UL Hover");

	}).mouseleave(function() {
		if (SUBMENU_ONHOVER || CHILD_ONHOVER) return;

		$(this).css("paddingBottom", "0px");
		$("#site-header").css("box-shadow", "none");

		$(".submenu").animate({
			opacity: 0,
			top: 120
		}, 180, function() {
			$(this).hide();
		});

		console.log("UL Leave");
	});

	///////////////////////////////////////////////////////////////////////////////////////////////

	$("#facet-health,#facet-food,#facet-lifestyle,#facet-fitness").click(function() {
		window.location = $(this).find('a').attr('href');
	});

	///////////////////////////////////////////////////////////////////////////////////////////////

	//$(".menu-blogs-wrapper").mouseenter(rightMenuHover).mouseleave(rightMenuLeave);
	//UL_RIGHT_SUBMENU.mouseenter(rightSubmenuHover).mouseleave(rightSubmenuLeave);

	$("#menu-blogs-wrapper").mouseenter(function() {
		$(this).css("paddingBottom", "50px");
		$("#site-header").css("box-shadow", "0px 100px 700px #888");

		var parent = $(this).children("a");
		var submenu_wrapper = $(this).children("#menu-blogs-submenu");
		var submenu = submenu_wrapper.children(".right-submenu");
		var triangle = submenu_wrapper.children(".right-submenu-triangle");

		parent.addClass("active");

		submenu_wrapper.show();
		submenu.show();
		triangle.show();

		submenu.css({top: 35, opacity: 0}).animate({
			top: 23,
			opacity: 1
		}, 220);

		triangle.css({top: 27, opacity: 0}).animate({
			top: 15,
			opacity: 1
		}, 220);

	}).mouseleave(function() {
		$(this).css("paddingBottom", "50px");
		$("#site-header").css("box-shadow", "none");

		var parent = $(this).children("a");
		var submenu_wrapper = $(this).children("#menu-blogs-submenu");
		var submenu = submenu_wrapper.children(".right-submenu");
		var triangle = submenu_wrapper.children(".right-submenu-triangle");

		parent.removeClass("active");

		//submenu_wrapper.show();
		//submenu.show();
		//triangle.show();

		submenu.animate({
			top: 35,
			opacity: 0
		}, 150, function() {
			$(submenu_wrapper).hide();
		});

		triangle.animate({
			top: 27,
			opacity: 0
		}, 150);

	});


	///////////////////////////////////////////////////////////////////////////////////////////////

	$("#login-menu").click(function() {
		$(".main-popup").hide();
		$("#popup-bg-overlay").fadeIn(100, function() {
			$("#popup-login").show("scale", 350);
		});
	});

	$("#popup-bg-overlay").click(function() {
		$(".main-popup").hide("scale", 200, function() {
			$("#popup-bg-overlay").fadeOut(80);
		});
	});

	$("#link-register").click(function(event) {
		event.preventDefault();
		$("#popup-login").hide("scale", 100, function() {
			$("#popup-register").show("scale", 350);
		})
	});

	$("#link-login").click(function(event) {
		event.preventDefault();
		$("#popup-register").hide("scale", 100, function() {
			$("#popup-login").show("scale", 350);
		})
	});

	$("#menu-join").click(function(event) {
		event.preventDefault();
		$(".main-popup").hide();
		$("#popup-bg-overlay").fadeIn(100, function() {
			$("#popup-register").show("scale", 350);
		});
	});

	///////////////////////////////////////////////////////////////////////////////////////////////

	CAROUSEL_SHOWN = 1;
	CAROUSEL_COUNT = 4;
	$("#carousel-2").fadeOut(0);
	$("#carousel-3").fadeOut(0);
	$("#carousel-4").fadeOut(0);
	//carousel();

	$(".facet-btn").mouseenter(function() {
		var pie_class = $(this).attr("data-pie");
		$(pie_class).addClass("active");
		$(this).next().css("display", "block");
		$(this).next().addClass('animated bounceIn');

		$(this).children(".icon-big").animate({
			top: 63,
			left: 19,
			width: 96,
			height: 96,
			opacity: 0.6
		}, 150);

	}).mouseleave(function() {
		var pie_class = $(this).attr("data-pie");
		$(pie_class).removeClass("active");
		$(this).next().css("display", "none");

		$(this).children(".icon-big").animate({
			top: 68,
			left: 54,
			width: 26,
			height: 26,
			opacity: 1
		}, 150);
	});

	/*$("#mandala ul li").mouseenter(function() {
		var facet_id = $(this).attr("data-facet");
		$(facet_id).addClass("active");
		$(facet_id).next().css("display", "block");
		$(facet_id).next().addClass('animated bounceIn');

	}).mouseleave(function() {
		var facet_id = $(this).attr("data-facet");
		$(facet_id).removeClass("active");
		$(facet_id).next().css("display", "none");
	});*/

	$("#carousel-nav a").click(function() {
		var next = parseInt($(this).attr('data-carousel'));

		var cur_data = "#carousel-" + CAROUSEL_SHOWN;
		var next_data = "#carousel-" + next;
		var next_nav = "#carousel-nav-" + next;

		$(cur_data).stop(true, false);

		$(cur_data).delay(100).fadeOut(80, function() {
			$(next_data).delay(300).fadeIn('slow', function() {
				CAROUSEL_SHOWN = next;
				$("#carousel-nav a").removeClass("active");
				$(next_nav).addClass("active");
				console.log(CAROUSEL_SHOWN);
				carousel();
			});
		});

	});

	$("#social-btn ul li a").mouseenter(function() {
		var btn_id = $(this).attr('data-social');

		$("#social-btn-hover").stop(true, true);
		
		$("#social-btn-hover ul li input").css("display", "none");
		$("#social-btn-hover ul li a").css("display", "none");

		$(btn_id).css("display", "block");
		$("#social-btn-hover").animate({width: "200px"}, 300);
	}).mouseleave(function() {

	});

	$("#social-btn-hover ul li").mouseenter(function() {
		
	}).mouseleave(function() {
		$("#social-btn-hover").animate({width: "0"}, 200);
	});
});

function init()
{
	LI_SITE_NAV = $("#site-nav ul li");
	A_SUBMENU_PARENT = $("#site-nav .submenu .parent li a");
	UL_CHILD = $("#site-nav .submenu .child");
	UL_CHILD_LI_A = $("#site-nav .submenu .child li a");

	A_RIGHT_MENU = $("#header-right ul a");
	UL_RIGHT_SUBMENU = $("#header-right .right-submenu");
}

function animate() {
	//$("#mandala").hide();
	$("#mandala-border").hide();
	$(".facet-btn").hide();
	//$("#mandala ul li a").hide();

	// $("#SpiralCanvas").fadeOut(0);

	$("#carousel-bg").addClass('animated bounceIn');

	$("#mandala-bg").addClass('animated bounceIn');

	//$("#mandala-border").show().addClass('animated fadeIn');

	//$(".facet-btn").show().addClass('animated fadeIn');

	$("#mandala").addClass('animated scaleIn');
	//$("#mandala").css("opacity", 0).delay(2000).animate({opacity: 1},1000);

	$("#site-header").addClass('animated bounceInDown');
	$("#social-btn ul li").addClass('animated fadeInRight');

	$("#mandala-border").delay(1200).fadeTo(300, 0.7);
	$(".facet-btn").delay(1500).fadeTo(300, 0.9);
	//$("#carousel-bg").delay(3000).fadeOut(1000);

	/*$("#mandala ul li:nth-child(3)").delay(3400).animate({ backgroundColor: "#f2796b" }, 200, function() {
		$("#mandala ul li:nth-child(4)").animate({ backgroundColor: "#f2796b" }, 200, function() {
			$("#mandala ul li:nth-child(5)").animate({ backgroundColor: "#69ae37" }, 200, function() {
				$("#mandala ul li:nth-child(6)").animate({ backgroundColor: "#69ae37" }, 200, function() {
					$("#mandala ul li:nth-child(7)").animate({ backgroundColor: "#3467c0" }, 200, function() {
						$("#mandala ul li:nth-child(8)").animate({ backgroundColor: "#3467c0" }, 200, function() {
							$("#mandala ul li:first-child").animate({ backgroundColor: "#f3c12a" }, 200, function() {
								$("#mandala ul li:nth-child(2)").animate({ backgroundColor: "#f3c12a" }, 200, function() {
									$("#mandala ul li").delay(500).animate({ backgroundColor: "#f3f3f3" }, 600);
								});
							});
						});
					});
				});
			});
		});
	});*/

	/*$("#mandala ul li:nth-child(3) a").delay(2200).fadeIn(300, function() {
		$("#mandala ul li:nth-child(4) a").fadeIn(300, function() {
			$("#mandala ul li:nth-child(5) a").fadeIn(300, function() {
				$("#mandala ul li:nth-child(6) a").fadeIn(300, function() {
					$("#mandala ul li:nth-child(7) a").fadeIn(300, function() {
						$("#mandala ul li:nth-child(8) a").fadeIn(300, function() {
							$("#mandala ul li:first-child a").fadeIn(300, function() {
								$("#mandala ul li:nth-child(2) a").fadeIn(300);
							});
						});
					});
				});
			});
		});
	});*/

	/*$("#mandala ul li:nth-child(3) a").delay(1700).show( "bounce", { distance: 5, times: 2 }, 10, function() {
		$("#mandala ul li:nth-child(4) a").show( "bounce", { distance: 5, times: 2 }, 10, function() {
			$("#mandala ul li:nth-child(5) a").show( "bounce", { distance: 5, times: 2 }, 10, function() {
				$("#mandala ul li:nth-child(6) a").show( "bounce", { distance: 5, times: 2 }, 10, function() {
					$("#mandala ul li:nth-child(7) a").show( "bounce", { distance: 5, times: 2 }, 10, function() {
						$("#mandala ul li:nth-child(8) a").show( "bounce", { distance: 5, times: 2 }, 10, function() {
							$("#mandala ul li:first-child a").show( "bounce", { distance: 5, times: 2 }, 10, function() {
								$("#mandala ul li:nth-child(2) a").show( "bounce", { distance: 5, times: 2 }, 10, function() {});
							});
						});
					});
				});
			});
		});
	});*/

	/*$("#mandala ul li:nth-child(3) a").delay(2500).show( "bounce", { distance: 3, times: 2 }, 150);
	$("#mandala ul li:nth-child(4) a").delay(2600).show( "bounce", { distance: 3, times: 2 }, 150);
	$("#mandala ul li:nth-child(5) a").delay(2700).show( "bounce", { distance: 3, times: 2 }, 150);
	$("#mandala ul li:nth-child(6) a").delay(2800).show( "bounce", { distance: 3, times: 2 }, 150);
	$("#mandala ul li:nth-child(7) a").delay(2900).show( "bounce", { distance: 3, times: 2 }, 150);
	$("#mandala ul li:nth-child(8) a").delay(3000).show( "bounce", { distance: 3, times: 2 }, 150);
	$("#mandala ul li:first-child a").delay(3100).show( "bounce", { distance: 3, times: 2 }, 150);
	$("#mandala ul li:nth-child(2) a").delay(3200).show( "bounce", { distance: 3, times: 2 }, 150);*/

	//$("#mandala ul li:nth-child(3) a").show( "bounce", { distance: 0, times: 1 }, 1000);

	//$("#mandala ul li a").css({opacity:0, fontSize:19});
	//$("#mandala ul li a").delay(3200).animate({opacity:1, fontSize: 15},400,"easeOutCubic");
	/*$("#mandala ul li:nth-child(4) a").delay(3300).animate({opacity:1, fontSize: 15},400,"easeOutCubic");
	$("#mandala ul li:nth-child(5) a").delay(3400).animate({opacity:1, fontSize: 15},400,"easeOutCubic");
	$("#mandala ul li:nth-child(6) a").delay(3500).animate({opacity:1, fontSize: 15},400,"easeOutCubic");
	$("#mandala ul li:nth-child(7) a").delay(3600).animate({opacity:1, fontSize: 15},400,"easeOutCubic");
	$("#mandala ul li:nth-child(8) a").delay(3700).animate({opacity:1, fontSize: 15},400,"easeOutCubic");
	$("#mandala ul li:first-child a").delay(3800).animate({opacity:1, fontSize: 15},400,"easeOutCubic");
	$("#mandala ul li:nth-child(2) a").delay(3900).animate({opacity:1, fontSize: 15},400,"easeOutCubic");*/
	
/*
	$("#SpiralCanvas").delay(8200).fadeIn(1000);
	$("#SpiralCanvas").delay(18200).fadeOut(1000, function() {
		$("#SpiralCanvas").hide();
		$("#SpiralCanvas").remove();
	});
*/

}

function carousel() {
	var next = CAROUSEL_SHOWN + 1;
	if (next > CAROUSEL_COUNT) next = 1;

	var cur_data = "#carousel-" + CAROUSEL_SHOWN;
	var next_data = "#carousel-" + next;
	var next_nav = "#carousel-nav-" + next;

	$(cur_data).delay(3000).fadeOut(100, function() {
		$(next_data).delay(50).fadeIn(400, function() {
			CAROUSEL_SHOWN = next;
			$("#carousel-nav a").removeClass("active");
			$(next_nav).addClass("active");
			carousel();
		});
	});
}

function siteNavHover()
{
	/*$(".submenu").css("display", "none");
	$(".child").css("display", "none");
	$(".parent-triangle").css("display", "none");

	var div_submenu = $(this).children(".submenu");
	//var submenu_triangle = $(this).children(".submenu").children(".submenu_triangle");
	//$(".submenu-triangle").css("display", "block");

	//div_submenu.stop(true, false);
	div_submenu.css("display", "block");
	div_submenu.css("top", "120px");
	div_submenu.animate({
		opacity: 1,
		top: 108
	}, 150);*/

	//$("#site-header").css("box-shadow", "0px 100px 700px #888");

	if (SUBMENU_ONHOVER || SUBMENU_PARENT_ONHOVER || CHILD_ONHOVER) return;

	var div_submenu = $(this).children(".submenu");
	$(".submenu").hide();
	$(".child").hide();
	$(".parent-triangle").hide();

	div_submenu.css({top: 120, opacity: 0}).show().animate({
		height: "auto",
		top: 108,
		opacity: 1
	}, 150);

	console.log("Site Nav Hover");
}

function siteNavLeave()
{
	//var div_submenu = $(this).children(".submenu");
	//$(".parent-triangle").css("display", "none");

	/*div_submenu.animate({
		opacity: 0,
		top: 120
	}, 100, function() {
		div_submenu.css("display", "none");
	});*/

	//$("#site-header").css("box-shadow", "none");

	console.log("Site Nav Leave");
}

function submenuParentHover() {
	/*var submenu = $(this).parent().parent().parent();
	submenu.css("display", "block").css("opacity", 1);
	var child_id = $(this).attr("data-dropdown");
	var child = $(child_id);

	UL_CHILD.stop(true, false);
	UL_CHILD.css("display", "none");

	var triangle = $(this).parent().children(".parent-triangle");
	triangle.css("display", "none");
	triangle.addClass("active");

	var parent_menu = $(this).parent().parent().parent().parent().children("a");
	parent_menu.addClass("active");

	child.css("display", "block");
	child.animate({
		opacity: 1,
	}, 500, function() {
		triangle.css("display", "block");
	});*/

	SUBMENU_PARENT_ONHOVER = true;

	$(".child").hide();
	$(".parent-triangle").hide();
	$(".parent li a").removeClass("active");

	var top_menu = $(this).parent().parent().parent().parent().children("a");
	top_menu.addClass("active");

	console.log(top_menu);

	var child_id = $(this).attr('data-dropdown');
	var child = $(child_id);

	if (child.length >= 1) {
		var triangle = $(this).parent().children(".parent-triangle");

		child.show();
		triangle.show();
	}

	console.log("Submenu Parent Hover");
}

function submenuParentLeave() {
	/*var child_id = $(this).attr("data-dropdown");
	var child = $(child_id);

	var triangle = $(this).parent().children(".parent-triangle");
	//triangle.css("display", "none");

	var parent_menu = $(this).parent().parent().parent().parent().children("a");
	parent_menu.removeClass("active");

	$(this).removeClass('active');

	child.animate({
		opacity: 0,
	}, 500, function() {
		child.css("display", "none");
	});*/
	SUBMENU_PARENT_ONHOVER = false;

	console.log("Submenu Parent Leave");
}

function childHover() {
	/*var id_parent_menu = $(this).attr("data-parent");
	var parent_menu = $(this).parent().children(".parent").children("li").children(id_parent_menu);
	var triangle = parent_menu.parent().children(".parent-triangle");

	var site_nav = $(this).parent().parent().children("a");
	site_nav.addClass('active');

	triangle.css("display", "block");
	triangle.addClass('active');

	parent_menu.addClass('active');

	$(this).stop(true, false);*/

	CHILD_ONHOVER = true;
	var submenu = $(this).parent();
	submenu.show();

	var parent_id = $(this).attr("data-parent");
	var parent = $(parent_id);
	parent.addClass("active");

	console.log("Child Hover");
}

function childLeave() {
	/*var id_parent_menu = $(this).attr("data-parent");
	var parent_menu = $(this).parent().children(".parent").children("li").children(id_parent_menu);
	var triangle = parent_menu.parent().children(".parent-triangle");

	var site_nav = $(this).parent().parent().children("a");
	site_nav.removeClass('active');
	
	triangle.css("display", "block");
	triangle.addClass('active');

	parent_menu.removeClass('active');*/
	console.log("Child Leave");
}

function rightMenuHover() {
	/*var ul_submenu = $(this).parent().children(".right-submenu");
	var triangle = $(this).parent().children(".right-submenu-triangle");
	
	ul_submenu.stop(true, false);
	ul_submenu.css("display", "block");

	triangle.stop(true, true);
	triangle.css("display", "block");

	ul_submenu.animate({
		opacity: 1
	}, 500);

	triangle.animate({
		opacity: 1
	}, 500);*/

	var submenu_wrapper = $(this).next("#menu-blogs-submenu");
	var submenu = submenu_wrapper.children(".right-submenu");
	var triangle = submenu_wrapper.children(".right-submenu-triangle");

	submenu_wrapper.show();
	submenu.show();
	triangle.show();

	submenu.css({top: 35, opacity: 0}).animate({
		top: 23,
		opacity: 1
	}, 300);

	triangle.css({top: 27, opacity: 0}).animate({
		top: 15,
		opacity: 1
	}, 300);

	console.log("Right Menu Hover");
}

function rightMenuLeave() {
	/*var ul_submenu = $(this).parent().children(".right-submenu");
	var triangle = $(this).parent().children(".right-submenu-triangle");

	ul_submenu.animate({
		opacity: 0
	}, 800, function() {
		ul_submenu.css("display", "none");
	});

	triangle.animate({
		opacity: 0
	}, 800, function() {
		triangle.css("display", "none");
	});*/
	console.log("Right Menu Leave");
}

function rightSubmenuHover() {
	$(this).stop(true, false);
	var triangle = $(this).parent().children(".right-submenu-triangle");

	$(this).css("opacity", 1);

	triangle.stop(true, false);
	triangle.css("opacity", 1);
	triangle.css("display", "block");

	$("#site-header").css("box-shadow", "0px 100px 700px #888");

	var parent_menu = $(this).parent().children("a");
	parent_menu.addClass("active");
}

function rightSubmenuLeave() {
	var ul_submenu = $(this);
	var triangle = $(this).parent().children(".right-submenu-triangle");

	ul_submenu.animate({
		opacity: 0
	}, 800, function() {
		ul_submenu.css("display", "none");
	});

	triangle.animate({
		opacity: 0
	}, 800, function() {
		triangle.css("display", "none");
	});

	$("#site-header").css("box-shadow", "none");

	var parent_menu = $(this).parent().children("a");
	parent_menu.removeClass("active");
}

$(document).bind("spling:navigate", function(e, url){

  pattern = /user\/NewSimplyCentered\/splingboards\/(.*)/;
  match = url.match(pattern);

  patternBlog = /7gportal.com/;
  patternAmazon = /amazon.com/;
  
  if (match && match[1])
    window.location += '/'+match[1];
  // else if(!url.match(patternBlog) && !url.match(patternAmazon))
  //   // Remove widget from start of url
  //   window.location = 'spling?url='+url.slice(7)

});