import web
import config as config
import hashlib #permite usar hash md5


class Registro:
	def __init__(self):
		pass

	def GET(self):
		return config.render.registro()

	def POST(self):
		

		formulario = web.input()
		nombre = formulario['nombre']
		apellidos = formulario['apellidos']
		telefono = formulario['telefono']
		correo = formulario['correo']
		password = hashlib.md5(formulario['password']).hexdigest() #aplica md5 a la cadena de texto 
		passwordconf = formulario['passwordconf']
		rol = '1'
		config.model_registro.insert_usuario(nombre, apellidos, telefono, correo, password, rol)
		raise web.seeother('/') 
		
		