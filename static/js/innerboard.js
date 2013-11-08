var RATE_POPUP_SHOWN;
var RATE;

$(document).ready(function() {

	$(".item-rate").hide();
	$("#rate-form-popup").hide();
	$("#rate-success-popup").hide();
	$(".board-popup").hide();

	$(".item-overlay").hide();
	$(".item-featured-link").hide();

	RATE_POPUP_SHOWN = false;

	$(".board-item").mouseenter(boardItemHover).mouseleave(boardItemLeave);

	$(".board-item-link").mouseenter(boardItemLinkHover).mouseleave(boardItemLinkLeave);

	$("#popup-review-close").click(closePopup);
	$("#popup-bg-overlay").click(closePopup);

	$(".item-rate ul li").mouseenter(itemRateHover).mouseleave(itemRateLeave);

	$(".item-rate ul li").click(itemRateClick);

	$("#rate-form-submit").click(function(event) { reviewSubmit(event) });

	$(".popup-item-rate ul li").mouseenter(popupItemRateHover).mouseleave(popupItemRateLeave);
	$(".popup-item-rate ul li").click(popupItemRateClick);

});

/*************************************************************************************************\

\*************************************************************************************************/
function boardItemHover() {
	if (RATE_POPUP_SHOWN == true) return;
	item_rate = $(this).children(".item-rate").fadeIn("fast");
}

function boardItemLeave() {
	if (!RATE_POPUP_SHOWN) $(this).children(".item-rate").fadeOut("fast");
	else return;
}

/*************************************************************************************************\

\*************************************************************************************************/
function boardItemLinkHover() {
	$(this).children(".item-overlay").fadeIn("fast");
	$(this).children(".item-featured-link").fadeIn("fast");
}

function boardItemLinkLeave() {
	$(this).children(".item-overlay").fadeOut("fast");
	$(this).children(".item-featured-link").fadeOut("fast");
}


/*************************************************************************************************\

\*************************************************************************************************/
function itemRateHover() {
	var rate = parseInt( $(this).children("a").attr("data-rate") );
	
	var targets = $(this).parent().children("li").children("a");
	$(targets).removeClass("active");
	
	for (var i = 1; i < rate; i++) {
		var target = $(this).parent().children("li").children(".rate" + i);
		target.addClass("active");
	}
}

function itemRateLeave() {
	var targets = $(this).parent().children("li").children("a");
	$(targets).removeClass("active");
}

/*************************************************************************************************\

\*************************************************************************************************/

function itemRateClick() {
	$("#popup-bg-overlay").fadeIn(100, function() {
		$("#popup-review").show().css({opacity:0,top:200}).animate({
			opacity: 1,
			top: 100
		}, 400);
	});

	RATE = parseInt( $(this).children("a").attr("data-rate") );
	$(".popup-item-rate .rate").removeClass("active");
	for (var i = 1; i <= RATE; i++) {
		$(".popup-item-rate .rate" + i).addClass("active");
	}
}

function closePopup() {
	$("#popup-bg-overlay").stop(true, false);
	$("#popup-review").stop(true, false);

	$("#popup-review").fadeOut(200).hide();
	$("#popup-bg-overlay").fadeOut(200).hide();
}

function reviewSubmit(evt) {
	
}

/*************************************************************************************************\

\*************************************************************************************************/
function popupItemRateHover() {
	var cur_rate = parseInt( $(this).children("a").attr("data-rate") );
	
	var targets = $(this).parent().children("li").children("a");
	$(targets).removeClass("active");
	
	for (var i = 1; i < cur_rate; i++) {
		var target = $(this).parent().children("li").children(".rate" + i);
		target.addClass("active");
	}
}

function popupItemRateLeave() {
	$(".popup-item-rate .rate").removeClass("active");
	for (var i = 1; i <= RATE; i++) {
		$(".popup-item-rate .rate" + i).addClass("active");
	}
}

function popupItemRateClick() {
	RATE = parseInt( $(this).children("a").attr("data-rate") );
}