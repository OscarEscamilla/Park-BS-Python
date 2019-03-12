import web
import config as config


class Login:
	def __init__(self):
		pass

	def GET(self):
		return config.render.login()

		###def POST(self):
		###formulario = web.input()
		###correo = formulario['correo']
		###passw = formulario['passw']
		###config.model_login.login_user(correo, passw)
		###raise web.seeother('/')
		
		