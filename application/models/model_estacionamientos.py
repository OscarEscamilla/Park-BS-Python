import config as config



db = config.db

""" METODO PARA INSERTAR UN ESTACIONAIENTO"""
def insert_estacionamiento(nombre,titular, colonia, numero, telefono, latitud, longitud, correo, password, rol):
	try:
		return db.insert('estacionamientos',
			nombre = nombre,
			apellidos = apellidos,
			telefono = telefono,
			correo = correo,
			password = password,
			rol = rol)
	except Exception as e:
		print "Model insert_estacionamientos Error ()".format(e.args)
		print "Model insert_estacionamientos {}".format(e.message)
		return None

def select_estacionamientos():
	try:
		return db.select('estacionamientos')
	except Exception as e:
		print "Model select_usuaempresas Error {}".format(e.args)
        print "Model select_usuaempresas Message {}".format(e.message)
        return None 
