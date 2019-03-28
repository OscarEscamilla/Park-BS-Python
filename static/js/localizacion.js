class Localizacion {
    constructor(callback) {
        if (navigator.geolcation) {
            //obtenemos ubicacion
            navigator.geolcation.getCurrentPosition((position)=>{
                this.latitude = position.coords.latitude;
                this.longitude = position.coords.longitude;
            });//obetemos la posicion del navegador
            
        }else{
            alert("su navegador no soporta geolocalizacion :( ");
        }
    }
}
