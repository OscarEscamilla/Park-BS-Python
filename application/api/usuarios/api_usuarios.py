import web
import config
import json


class Api_usuarios:


    def get(self, id):
        try:
            # http://0.0.0.0:8080/api_usuarios?user_hash=12345&action=get
            if id is None:
                result = config.model.select_usuarios()
                usuarios_json = []
                for row in result:
                    tmp = dict(row)
                    usuarios_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(usuarios_json)
            else:
              
                result = config.model.select_usuario(int(id))
                usuarios_json = []
                usuarios_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(usuarios_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            usuarios_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuarios_json)
    
    # http://localhost:8080/api_usuarios?user_hash=12345&action=put&nombre=nuevo&apellidos=nuevo&telefono=000000&correo=nuevo@gmail.com&password=nuevo&rol=1
    def put(self, nombre, apellidos, telefono,  correo, password, rol):
        try:
            config.model.insert_usuario(nombre, apellidos, telefono,  correo, password, rol)
            usuarios_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuarios_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

            
    # http://localhost:8080/api_usuarios?user_hash=12345&action=delete&id=2
    def delete(self, id):
        try:
            config.model.delete_usuario(id)
            usuarios_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuarios_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None
    
    # http://localhost:8080/api_usuarios?user_hash=12345&action=update&id=1&nombre=nuevo&apellidos=nuevo&telefono=000000&correo=nuevo@gmail.com&password=nuevo&rol=1
    def update(self, id, nombre, apellidos, telefono,  correo, password, rol):
        try:
            config.model.update_usuario(id, nombre, apellidos, telefono,  correo, password, rol)
            usuarios_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuarios_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None
    


    #metodo para recibir datos por la url
    def GET(self): 
         
        user_data = web.input( #arrglo que almacena los datos llegados por url
            user_hash = None,
            action = None,
            id = None,
            nombre = None,
            apellidos = None,
            telefono = None,
            correo = None,
            password = None,
            rol = None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id = user_data.id
            nombre = user_data.nombre
            apellidos = user_data.apellidos
            telefono = user_data.telefono
            correo = user_data.correo
            password = user_data.password
            rol = user_data.rol

            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id)
                elif action == 'put':
                    return self.put(nombre, apellidos, telefono,  correo, password, rol)
                elif action == 'delete':
                    return self.delete(id)
                elif action == 'update':
                    return self.update(id, nombre, apellidos, telefono,  correo, password, rol)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
