import web
import config as config
import hashlib #permite usar hash md5

#mensaje = 1 error de contrasenas no coinciden
#mensaje = 2
class Registro_usuarios:
	def __init__(self):
		pass 

	def GET(self):
		alert = 0
		return config.render.registro_usuarios(alert)

	def POST(self):

		try:
			formulario = web.input() #almamacenamos todos los datos del formulario en variales
			nombre = formulario['nombre']
			apellidos = formulario['apellidos']
			telefono = formulario['telefono']
			correo = formulario['correo']
			password = formulario['password'] #aplica md5 a la cadena de texto
			passwordconf = formulario['passwordconf']
			rol = '1'
			 #alacena todos los datos de la tabla usuarios para comprobar si el correo ingresado ya esta asiciado a una cuenta 
		

			if password == passwordconf:
				password = hashlib.md5(formulario['password']).hexdigest() #aplica md5 a la cadena de texto
				config.model_usuarios.insert_usuario(nombre, apellidos, telefono, correo, password, rol)
				raise web.seeother('/login')
			else:
				alert = 1
				return config.render.registro_usuarios(alert)

		except Exception as e:
			alert = 2
			return config.render.registro_usuarios(alert)
