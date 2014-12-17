$(document).ready(function() {
	$(".project").fancybox({
		maxWidth	: '100%',
		maxHeight	: '100%',
		fitToView	: false,
		width		: 940,
		height		: 800,
		autoSize	: false,
		closeClick	: false,
		openEffect	: 'elastic',
		closeEffect	: 'elastic',
		autoLoad	: true,
		helpers : {
			thumbs : {
				width		: 175,
				height		: 100,
			},
			title : {
				type	: 'inside'
			}
		}
	});
});
