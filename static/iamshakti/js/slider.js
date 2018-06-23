/*
 *
 *	Slider created by Charlie Collar, 2018
 *
 */
$(window).on("load",function() {
	var max = $(".quote-container").length;
	$(window).on("resize",function() {
		$("#rarrow,#larrow,.quote-container,#quotes").css("height",(window.innerHeight-80)+"px");
		$("#rarrow,#larrow").css("padding-top",(window.innerHeight-80)*.4+"px");
		$("#quote-footer").css({"top":(window.innerHeight-120)+"px","left":(window.innerWidth/2-100)+"px"});
		for (var i = 0; i < max; i++) {
			var h = $(".quote").eq(i).height();
			$(".quote").eq(i).css("top",(window.innerHeight-100-h)/2 + "px");
		}
	});
	$("#rarrow,#larrow,.quote-container,#quotes").css("height",(window.innerHeight-80)+"px");
	$("#rarrow,#larrow").css("padding-top",(window.innerHeight-80)*.4+"px");
	$("#quote-footer").css({"top":(window.innerHeight-120)+"px","left":(window.innerWidth/2-100)+"px"});
	var index = 0;
	$(".quote-container").css("opacity","0"); // Set all opacities to 0.
	$(".quote-container").eq(index).css("opacity","1"); // Set original to 1.
	for (var i = 0; i < max; i++) {
		$("#quote-footer ul").append("<li id='"+i+"'>&bull;</li>");
		var h = $(".quote").eq(i).height();
		$(".quote").eq(i).css("top",(window.innerHeight-100-h)/2 + "px");
		if ($(".quote").eq(i).children("p").length == 1) {
			$(".quote").eq(i).children("p").css("width","80%");
		}
	}
	var v = setInterval(function(){
		changeQuote(index,index = (index + 1)%max);
	},4000);
	$("#quote-footer li").eq(index).css("opacity","1");
	$("#rarrow").click(function(){
		clearInterval(v);
		changeQuote(index,index = (index + 1)%max);
	});
	$("#larrow").click(function(){
		clearInterval(v);
		changeQuote(index,index = (index - 1)%max);
	});
	$("#quote-footer li").click(function() {
		clearInterval(v);
		changeQuote(index,index = $(this).attr("id"));
	});
});
function changeQuote(o,n) {
	$("#quote-footer li").css("opacity",".8");
	$("#"+n).css("opacity","1");
	$(".quote-container").eq(o).css("opacity","0");
	$(".quote-container").eq(n).css("opacity","1");
}