import web
import config as config
import hashlib #permite usar hash md5


class Registro_estacionamientos:
	def __init__(self):
		pass

	def GET(self):
		alert = 0
		return config.render.registro_estacionamientos(alert)

	def POST(self):
		
		try: 
			
			formulario = web.input() #objeto para acceder a los valores recibidos por el metodo POST
			nombre = formulario['nombre']
			titular = formulario['titular']
			calle = formulario['calle']
			cp = formulario['cp']
			colonia = formulario['colonia']
			numero = formulario['numero']
			latitud = formulario['latitud']
			longitud = formulario['longitud']
			tarifa = formulario['tarifa']
			telefono = formulario['telefono']
			correo = formulario['correo']
			"""
			hora_apertura = formulario['hora_apertura']
			hora_cierre = formulario['hora_cierre']
			print hora_apertura, hora_cierre
			"""

			dia_inicio = formulario['dia_inicio']
			dia_final = formulario['dia_final']
			password = formulario['password']
			passwordconf = formulario['passwordconf']
			rol = 2

			mensaje = "las contrasenas no coinciden"
			
			if password == passwordconf:
				
				password = hashlib.md5(formulario['password']).hexdigest() #aplica md5 a la cadena de texto 
				#config.model_estacionamientos.insert_estacionamiento(nombre, apellidos, telefono, correo, password, rol)
				print password
				raise web.seeother('/login')
			
			else:
				alert = 1
				return config.render.registro_e(alert)
		except Exception as e:
				return "error de registro estacionamiento controller"
