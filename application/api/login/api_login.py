import web
import config
import json


class Api_login:
    def get(self, id):
        try:
            # http://0.0.0.0:8080/api_login?user_hash=12345&action=get
            if  id is None:
                result = config.model.get_all_login()
                login_json = []
                for row in result:
                    tmp = dict(row)
                    login_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(login_json)
            else:
                # http://0.0.0.0:8080/api_login?user_hash=12345&action=get&=1
                result = config.model.get_login(int(id))
                login_json = []
                login_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(login_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            login_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(login_json)

# http://0.0.0.0:8080/api_login?user_hash=12345&action=put&=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, correo,password,rol):
        try:
            config.model.insert_login(correo,password,rol)
            login_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(login_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None


    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id=None,
            correo=None,
            password=None,
            rol=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id=user_data.id

            correo=user_data.correo

            password=user_data.password

            rol=user_data.rol

            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id)
                elif action == 'put':
                    return self.put(correo,password,rol)
                
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
