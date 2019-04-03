import web
import config as config

db = config.db #accede al archivo config y al objeto db




# METODO PARA REGISTRAR NUEVOS USUARIOS 
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

# METODO PARA OBTENER TODOS LOS USUARIOS 
def select_usuarios():
	try:

	    return db.select('usuarios')
	except Exception as e:
		print "Model select_usuarios Error {}".format(e.args)
        print "Model select_usuarios Message {}".format(e.message)
        return None 

#METODO PARA SELECCIONAR UN USUARIOS ESPECIFICO A PARTIR DE SU ID 

def select_usuario(id):
	try:
		return db.select('usuarios', where='id=$id', vars=locals())[0]
	
	except Exception as e:
		print "Model select_usuario Error {}".format(e.args)
        print "Model select_usuario Message {}".format(e.message)
        return None 



