import web
import config
import json

 
class Api_estacionamientos:
    def get(self, id):
        try:
            # http://0.0.0.0:8080/api_estacionamientos?user_hash=12345&action=get
            if id is None:
                result = config.model.select_estacionamientos()
                estacionamientos_json = []
                for row in result:
                    tmp = dict(row)
                    estacionamientos_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(estacionamientos_json)
            else:
                # http://0.0.0.0:8080/api_estacionamientos?user_hash=12345&action=get&id=1
                result = config.model.select_estacionamiento(int(id))
                estacionamientos_json = []
                estacionamientos_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(estacionamientos_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            estacionamientos_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(estacionamientos_json)

# http://0.0.0.0:8080/api_estacionamientos?user_hash=12345&action=put&id=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre,titular,colonia,calle,numero,cp,latitud,longitud,tarifa,telefono,correo,hora_apertura,hora_cierre,dia_inicio,dia_final,password,rol,disponibilidad,estado,imagen,puntuacion):
        try:
            config.model.insert_estacionamientos(nombre,titular,colonia,calle,numero,cp,latitud,longitud,tarifa,telefono,correo,hora_apertura,hora_cierre,dia_inicio,dia_final,password,rol,disponibilidad,estado,imagen,puntuacion)
            estacionamientos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(estacionamientos_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_estacionamientos?user_hash=12345&action=delete&id=1
    def delete(self, id):
        try:
            config.model.delete_estacionamientos(id)
            estacionamientos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(estacionamientos_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_estacionamientos?user_hash=12345&action=update&id=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id, nombre,titular,colonia,calle,numero,cp,latitud,longitud,tarifa,telefono,correo,hora_apertura,hora_cierre,dia_inicio,dia_final,password,rol,disponibilidad,estado,imagen,puntuacion):
        try:
            config.model.edit_estacionamientos(id,nombre,titular,colonia,calle,numero,cp,latitud,longitud,tarifa,telefono,correo,hora_apertura,hora_cierre,dia_inicio,dia_final,password,rol,disponibilidad,estado,imagen,puntuacion)
            estacionamientos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(estacionamientos_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            estacionamientos_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(estacionamientos_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id=None,
            nombre=None,
            titular=None,
            colonia=None,
            calle=None,
            numero=None,
            cp=None,
            latitud=None,
            longitud=None,
            tarifa=None,
            telefono=None,
            correo=None,
            hora_apertura=None,
            hora_cierre=None,
            dia_inicio=None,
            dia_final=None,
            password=None,
            rol=None,
            disponibilidad=None,
            estado=None,
            imagen=None,
            puntuacion=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id=user_data.id

            nombre=user_data.nombre

            titular=user_data.titular

            colonia=user_data.colonia

            calle=user_data.calle

            numero=user_data.numero

            cp=user_data.cp

            latitud=user_data.latitud

            longitud=user_data.longitud

            tarifa=user_data.tarifa

            telefono=user_data.telefono

            correo=user_data.correo

            hora_apertura=user_data.hora_apertura

            hora_cierre=user_data.hora_cierre

            dia_inicio=user_data.dia_inicio

            dia_final=user_data.dia_final

            password=user_data.password

            rol=user_data.rol

            disponibilidad=user_data.disponibilidad

            estado=user_data.estado

            imagen=user_data.imagen

            puntuacion=user_data.puntuacion

            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id)
                elif action == 'put':
                    return self.put(nombre,titular,colonia,calle,numero,cp,latitud,longitud,tarifa,telefono,correo,hora_apertura,hora_cierre,dia_inicio,dia_final,password,rol,disponibilidad,estado,imagen,puntuacion)
                elif action == 'delete':
                    return self.delete(id)
                elif action == 'update':
                    return self.update(id, nombre,titular,colonia,calle,numero,cp,latitud,longitud,tarifa,telefono,correo,hora_apertura,hora_cierre,dia_inicio,dia_final,password,rol,disponibilidad,estado,imagen,puntuacion)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
