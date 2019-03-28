import web
import config as config
import hashlib #permite usar hash md5

#mensaje = 1 error de contrasenas no coinciden
#mensaje = 2
class Registro:
	def __init__(self):
		pass

	def GET(self):
		alert = 0
		return config.render.registro(alert)

	def POST(self):

		try:
			formulario = web.input() #alamacenamos todos los datos del formulario en variales
			nombre = formulario['nombre']
			apellidos = formulario['apellidos']
			telefono = formulario['telefono']
			correo = formulario['correo']
			password = formulario['password'] #aplica md5 a la cadena de texto
			passwordconf = formulario['passwordconf']
			rol = '1'
			usuarios = [] #alacena todos los datos de la tabla usuarios para comprobar si el correo ingresado ya esta asiciado a una cuenta 
			usuarios = config.model_registro.select_usuarios()

			if password == passwordconf:
				password = hashlib.md5(formulario['password']).hexdigest() #aplica md5 a la cadena de texto
				config.model_registro.insert_usuario(nombre, apellidos, telefono, correo, password, rol)
				raise web.seeother('/login')
			else:
				alert = 1
				return config.render.registro(alert)

		except Exception as e:
			alert = 1
			return config.render.registro(alert)
