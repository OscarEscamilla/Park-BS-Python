import web
import config as config
import hashlib


class Login:
	def __init__(self):
		pass

	def GET(self):
		return config.render.login()

	def POST(self):
		log = [] #almacena el regsitro encontrado con el correo dado por el usuario y la contraseña
		formulario = web.input()
		correo = formulario['correo'] #obtenemos por POST
		password = hashlib.md5(formulario['password']).hexdigest()#obtenemos por POST y hasheamos a md5

		#referenciamos al modelo y le pasamos los parametros recibidos por POST 
		log = config.model_login.login_user(correo, password) 


		try:
			#validamos si los datos dados por el usuarios coinciden con los datos devueltos por el modelo
			if log['correo'] == correo and log['password'] == password:
				print log['correo']
				print log['password']
				raise web.seeother('/registro')
		except Exception as e:
			return "la pass no es valida"

		
	
			
		

	

		
		