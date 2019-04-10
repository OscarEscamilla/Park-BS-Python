import web
import config as config

class Index:
	def __init__(self):
		pass


	def GET(self, id):
		
		datos = config.model_usuarios.select_usuario(id)
		
		return config.render.index(datos) 