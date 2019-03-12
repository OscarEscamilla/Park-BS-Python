import config as config

db = config.db #accede al archivo config y al objeto db




""" METODO PARA LOCALIZAR EL USUARIO QUE INTENTA LOGEARSE"""
def insert_usuario(nombre, apellidos, telefono,  correo, password, rol):
	try:
		return db.insert('usuarios', 
			nombre = nombre,
			apellidos = apellidos,
			telefono = telefono,
			correo = correo,
			password = password,
			rol = rol)
	except Exception as e:
		print "Model insert_user Error ()".format(e.args)
		print "Model insert_user Message {}".format(e.message)
		return None