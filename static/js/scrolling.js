$(window).scroll(function(){
	var scroll = $(window).scrollTop();
	
	// document.getElementById("myBody").style.marginTop = (-100 - 0.5*scroll) + "px";

	if(scroll >= 600){
		$("#myNav").addClass("bg-primary");
	} else {
		$("#myNav").removeClass("bg-primary");
	}
});