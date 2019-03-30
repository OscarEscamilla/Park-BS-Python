import web 

urls = (
	'/','application.controllers.home.Home',
	'/login','application.controllers.controller_login.Login',
	'/registro_usuarios','application.controllers.controller_registro_usuarios.Registro_usuarios',
	'/registro_estacionamientos','application.controllers.controller_registro_estacionamientos.Registro_estacionamientos',

	
	'/index_usuarios','application.controllers.users.controller_index_user.Index',
	'/index_estacionamientos','application.controllers.parks.controller_index_parks.Index'

	

	#'/productos', 'application.controllers.productos.index.Index',
	#'/insert', 'application.controllers.productos.insert.Insert',
	#'/update/(.*)', 'application.controllers.productos.update.Update',
	#'/delete/(.*)', 'application.controllers.productos.delete.Delete',
	#'/view/(.*)', 'application.controllers.productos.view.View', 
	

 

	)


if __name__ == "__main__":
	web.config.debug = False
	app = web.application(urls, globals())
	app.run()