import web
import config as config


web.config.smtp_server = 'smtp.gmail.com'
web.config.smtp_port = 587
web.config.smtp_username = 'escamillaluqueno@gmail.com'
web.config.smtp_password = 'oscarescamilla26'
web.config.smtp_starttls = True

class Home:
	def __init__(self):
		pass

	def GET(self):
		return config.render.home() 

	def POST(self):

		formulario = web.input() #accedemos al formulario redenerizado en el metodo GET

		nombre = formulario['nombre']
		telefono = formulario['telefono']
		correo = formulario['correo']
		mensaje = formulario['mensaje']

		#web.sendmail(, '', 'subject', mensaje)


		