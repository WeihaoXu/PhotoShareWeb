// when hovered on my-hover-control elements, the descending elements in my-hover-display will be shown/hidden.
$(document).ready(function(){
	$(".my-hover-display").css('visibility', 'hidden');
	$(".my-hover-control").hover(function(){
			$(this).find(".my-hover-display").css('visibility', 'visible');
			console.log($(this).css());
		},
		function(){
			$(this).find(".my-hover-display").css('visibility', 'hidden');
			console.log($(this).css());
		}
	);

});
