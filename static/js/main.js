$(".card").hover(function () {
	$(this).find(".card-image").addClass("card-hovered");
}, function() {
	$(this).find(".card-image").removeClass("card-hovered");
});