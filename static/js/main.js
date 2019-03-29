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

/*
class Localizacion {
  constructor(callback) {
      if (navigator.geolocation) {
          //obtenemos ubicacion
          navigator.geolcation.getCurrentPosition((position)=>{
              this.latitude = position.coords.latitude;
              this.longitude = position.coords.longitude;
      callback();
          });//obetemos la posicion del navegador

      }else{
          alert("su navegador no soporta geolocalizacion :( ");
      }
  }
}

function initMap() {
  const ubicacion = new Localizacion(()=>{
  const options = {
    center: {
      lat: ubicacion.latitude,
      lng: ubicacion.longitude
    },
    zoom : 15
  }
  var map = document.getElementById('map');

  const mapa = new google.maps.Map(map, options);//dibujamos el mapa
  });
  console.log(map);
} 