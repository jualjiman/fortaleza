$(function(){
	initialize();
});

//contact map
function initialize() {
	var ubicacion = new google.maps.LatLng(16.844216, -99.878995);
	var mapOptions = {
	  	center: ubicacion,
	  	zoom: 12,
	  	mapTypeId: google.maps.MapTypeId.ROADMAP
	};
	var map = new google.maps.Map($("#map-content")[0], mapOptions);
}