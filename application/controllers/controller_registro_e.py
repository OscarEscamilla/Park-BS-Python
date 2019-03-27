import web
import config as config
import hashlib #permite usar hash md5


class Registroe:
	def __init__(self):
		pass

	def GET(self):
		return config.render.registro_e()

	def POST(self):
		
		try:
			formulario = web.input()
			nombre = formulario['nombre']
			apellidos = formulario['apellidos']
			telefono = formulario['telefono']
			correo = formulario['correo']
			password = formulario['password'] #aplica md5 a la cadena de texto 
			passwordconf = formulario['passwordconf']
			rol = '2'
			mensaje = "las contrasenas no coinciden"
			usuarios = []
			usuarios = config.model_registro_e.select_usuarios()



		
			if password == passwordconf:
				password = hashlib.md5(formulario['password']).hexdigest() #aplica md5 a la cadena de texto 
				config.model_registro_e.insert_usuario(nombre, apellidos, telefono, correo, password, rol)
				raise web.seeother('/') 
		except Exception as e:
			return "error de regsiitro controller"
