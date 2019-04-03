import web 
import config as config



db = config.db

""" METODO PARA INSERTAR UN ESTACIONAIENTO"""
def insert_estacionamiento(nombre,titular, colonia, calle, numero, cp,  latitud, longitud, tarifa,telefono, correo, hora_apertura, hora_cierre, dia_inicio, dia_final ,password, rol):
	try:
		return db.insert('estacionamientos',
			nombre = nombre,
			titular = titular,
			colonia = colonia,
			calle = calle,
			numero = numero,
			cp = cp,
			latitud = latitud,
			longitud = longitud,
			tarifa = tarifa,
			telefono = telefono,
			correo = correo,
			hora_apertura = hora_cierre,
			hora_cierre = hora_cierre,
			dia_inicio = dia_inicio,
			dia_final = dia_final,
			password = password,
			rol = rol)
	except Exception as e:
		print "Model insert_estacionamientos Error ()".format(e.args)
		print "Model insert_estacionamientos {}".format(e.message)
		return None

""" METODO SELECCIONAR TODOS LOS REGISTROS DE ESTACIONAMIETOS"""
def select_estacionamientos():
	try:
		return db.select('estacionamientos')
	except Exception as e:
		print "Model select_usuaempresas Error {}".format(e.args)
        print "Model select_usuaempresas Message {}".format(e.message)
        return None 

"""
def ultimo_estacionamiento():
	try:
		return db.select('estacionamientos', where = )
"""
