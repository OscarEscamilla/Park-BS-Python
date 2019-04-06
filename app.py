import web 

urls = (
	'/','application.controllers.home.Home',
	'/login','application.controllers.controller_login.Login',
	'/registro_usuarios','application.controllers.controller_registro_usuarios.Registro_usuarios',
	'/registro_estacionamientos','application.controllers.controller_registro_estacionamientos.Registro_estacionamientos',

	#rutas de usuarios
	'/index_usuarios','application.controllers.users.controller_index_user.Index',
	'/perfil_usuarios','application.controllers.users.controller_perfil.Perfil',
	#rutas de estacionamientos
	'/index_estacionamientos','application.controllers.parks.controller_index_parks.Index',

	'/api_usuarios/?', 'application.api.usuarios.api_usuarios.Api_usuarios',
	'/api_estacionamientos/?', 'application.api.estacionamientos.api_estacionamientos.Api_estacionamientos',
	'/api_login/?', 'application.api.login.api_login.Api_login'




	)


if __name__ == "__main__":
	web.config.debug = False
	app = web.application(urls, globals())
	app.run()