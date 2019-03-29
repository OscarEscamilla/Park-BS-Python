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
			log = [] #almacena el regsitro encontrado con el correo dado por el usuario y la contrasena
			formulario = web.input()
			correo = formulario['correo'] #obtenemos por POST
			password = hashlib.md5(formulario['password']).hexdigest()#obtenemos por POST y hasheamos a md5

			#referenciamos al modelo y le pasamos los parametros recibidos por POST 
			log = config.model_login.login_user(correo, password) 


			#validamos si los datos dados por el usuarios coinciden con los datos devueltos por el modelo
			if log['correo'] == correo and log['password'] == password:
				rol = log['rol']
				print rol
				if rol == 1:
					print log['correo']
					print log['password']
					raise web.seeother('/index_u')
				elif rol = 2:
					#raise web.seeother('/index_empresa')  #aqui vamos aredireciconar al perfil de empresa


		except Exception as e:
			message = 1  #asignamos el valor 1 a la variable message si el incio de sesion falla y lo enviamos como parametro render.login
			return config.render.login(message)

		
	
			
		

	

		
		