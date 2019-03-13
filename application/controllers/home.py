import web
import config as config

class Home:
	def __init__(self):
		pass

	def GET(self):
		return config.render.home() 

	def POST(self):

		formulario = web.input() #accedemos al formulario redenerizado en el metodo GET

		nombre = formulario['nombre']
		telefono = formulario['telefono']
		