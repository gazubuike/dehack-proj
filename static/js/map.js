//<![CDATA[

var map;

// Ban Jelačić Square - Center of Zagreb, Croatia
var center = new google.maps.LatLng(42.3601, -71.0589);

function init() {
  var mapOptions = {
    zoom: 13,
    center: center,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
  };

  map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);

  var marker = new google.maps.Marker({
    map: map,
    position: center,
  });
}
//]]>
