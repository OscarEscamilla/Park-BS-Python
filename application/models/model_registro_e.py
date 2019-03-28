import config as config



db = config.db

""" METODO PARA LOCALIZAR EL USUARIO QUE INTENTA LOGEARSE"""
def insert_empresa(nombre,titular, colonia, numero, telefono,  correo, password, rol):
	try:
		return db.insert('usuarios',
			nombre = nombre,
			apellidos = apellidos,
			telefono = telefono,
			correo = correo,
			password = password,
			rol = rol)
	except Exception as e:
		print "Model insert_empresas Error ()".format(e.args)
		print "Model insert_empresas Message {}".format(e.message)
		return None

def select_estacionamientos():
	try:
		return db.select('estacionamientos')
	except Exception as e:
		print "Model select_usuaempresas Error {}".format(e.args)
        print "Model select_usuaempresas Message {}".format(e.message)
        return None
