import web
import config as config
import app
class Perfil:
	def __init__(self):
		pass


	def GET(self):
		
		datos = config.model_usuarios.select_usuarios().list()
		return config.render.perfil(datos) 