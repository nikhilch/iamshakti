var quote_height = 0;
$(document).ready(function(){
	$(window).on("resize",resize);
	resize();
	createFancyLinks();
});
function createFancyLinks() {
	$("a:not(.no-underline)").append("<span></span>")
		.mouseenter(function(){
		$(this).find("span").css("width","100%");
	})
		.mouseleave(function(){
		$(this).find("span").css("width","0%");
	});
}
function resize() {
	//quote_height = window.innerHeight-80;
	//assert(quote_height);

	//$("#quote-footer").css("top",quote_height-80+"px");
	//$(".quotes-container img").css("min-height",quote_height+"px");
}
function assert(item) {
	$("#testing").text(item);
}
function toTop() {
	window.scroll({
		top: 0, 
		left: 0, 
		behavior: 'smooth' 
	});
}
$(window).scroll(function() {
	var offset = $("#quotes").height() + $("#about").height() + 80 - window.innerHeight - $(window).scrollTop();
	var setoff = -100;
	var imgbase = 0-($("#why img").height() - 500);
	if (offset < 0) {
		$("#why img").css("bottom",Math.max(offset/2 + setoff,imgbase));
	}
});