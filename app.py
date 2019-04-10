import web
import application.models.model_sesiones as model_sesiones
web.config.debug = False

urls = (
	'/','application.controllers.home.Home',
	'/login','application.controllers.controller_login.Login',
	'/registro_usuarios','application.controllers.controller_registro_usuarios.Registro_usuarios',
	'/registro_estacionamientos','application.controllers.controller_registro_estacionamientos.Registro_estacionamientos',

	#rutas de usuarios
	'/index_usuarios/(.*)','application.controllers.users.controller_index_user.Index',
	'/perfil_usuarios','application.controllers.users.controller_perfil.Perfil',
	#rutas de estacionamientos
	'/index_estacionamientos','application.controllers.parks.controller_index_parks.Index',

	'/api_usuarios/?', 'application.api.usuarios.api_usuarios.Api_usuarios',
	'/api_estacionamientos/?', 'application.api.estacionamientos.api_estacionamientos.Api_estacionamientos',
	'/api_login/?', 'application.api.login.api_login.Api_login',

	"/count", "count",
    "/reset", "reset"


	)


app = web.application(urls, globals())

session = web.session.Session(app, web.session.DiskStore('sessions'), initializer={'count': 0})

class count:
    def GET(self):
		user = []
		user = model_sesiones.get_all_sessions().list()
		print user 
		if user['rol'] == 2:
			session.count += 1
			str(session.count)
			raise web.seeother('/index_usuarios')
		

class reset:
    def GET(self):
        session.kill()
        return ""

        



if __name__ == "__main__":
	app.run()