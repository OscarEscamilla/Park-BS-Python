function initMap() {
  var myLatLng = {lat: 20.082635, lng: -98.368669}; 

  // Crea el objeto map seteandolo en el elemento con el id map del DOM
  // for display.
  var map = new google.maps.Map(document.getElementById('map'), {
    center: myLatLng,
    zoom: 15
  });

  // Create un marcador 
  var marker = new google.maps.Marker({
    map: map,
    position: myLatLng,
    title: '¡Estas Aqui!' 
    });
}
