import web
import config as config
import hashlib


class Login:
	
	def __init__(self):
		pass

	def GET(self):
		message = 0
		return config.render.login(message)

	def POST(self):
		try:
			log_user = [] #almacena el regsitro encontrado con el correo dado por el usuario y la contrasena
			log_park = []
			formulario = web.input()
			correo = formulario['correo'] #obtenemos por POST
			password = hashlib.md5(formulario['password']).hexdigest()#obtenemos por POST y hasheamos a md5

			#referenciamos al modelo y le pasamos los parametros recibidos por POST 
			log_user = config.model_login.login_usuario(correo, password) 	
			print log_user
			
			log_park = config.model_login.login_estacionamiento(correo, password)
			print log_park
			
			if log_user['correo'] == correo and log_user['password'] == password:
				print log_user['rol']
				print log_user['correo']
				print log_user['password']
				return config.render_usuario.index()
				  
			elif log_park['correo'] == correo and log_park['password'] == password:
				print log_park['rol']
				print log_park['correo']
				print log_park['password']
				return config.render_estacionamientos.index() 
			else:
				message = 1
				return config.render.login(message)

			"""
			#validamos si los datos dados por el usuarios coinciden con los datos devueltos por el modelo
			if log['correo'] == correo and log['password'] == password:
				rol = log['rol']
				print rol
				if rol == 1:
					print log['correo']
					print log['password']

					datosu = 'si renderizo con parametro usuario'
					#datos = config.model_usuarios.
					
					return config.render_usuario.index() 
					#siel rol sea igual a 1 renderizamos el index de usuario pasando como parametro sus datos del model_usuarios
					
				elif rol == 2: 
					print log['correo']
					print log['password']
					datose = "si renderizo estacionameitno"
					return config.render_estacionamientos.index() 
					#si el rol es = 2 renderizamos a el index de estacionamientos con datos del modelo model_estacionamientos
				else:
					message = 1
					return config.render.login(message)
				"""

		except Exception as e: 
			message = 2  #asignamos el valor 1 a la variable message si el incio de sesion falla y lo enviamos como parametro render.login
			return config.render.login(message)

		
	
			
		

	

		
		