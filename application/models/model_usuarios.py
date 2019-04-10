import web
import config as config

db = config.db #accede al archivo config y al objeto db




# METODO PARA REGISTRAR NUEVOS USUARIOS 
def insert_usuario(nombre, apellidos, telefono,  correo, password, rol):
	try:
		return db.insert('users',
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

	    return db.select('users')
	except Exception as e:
		print "Model select_usuarios Error {}".format(e.args)
        print "Model select_usuarios Message {}".format(e.message)
        return None 

#METODO PARA SELECCIONAR UN USUARIOS ESPECIFICO A PARTIR DE SU ID 

def select_usuario(id):
	try:
		return db.select('users', where='id=$id', vars=locals())[0]
	
	except Exception as e:
		print "Model select_usuario Error {}".format(e.args)
        print "Model select_usuario Message {}".format(e.message)
        return None

def delete_usuario(id):
	try:
		return db.delete('users', where='id=$id', vars=locals())

	except Exception as e:
		print "Model delete_usuario Error {}".format(e.args)
        print "Model delete_usuario Message {}".format(e.message)
        return None


def update_usuario(id, nombre, apellidos, telefono,  correo, password, rol):
	try:
		return db.update('users',
			nombre = nombre,
			apellidos = apellidos,
			telefono = telefono,
			correo = correo,
			password = password,
			rol = rol,
			where='id=$id',
            vars=locals())
			
	except Exception as e:
		print "Model update_usuario Error {}".format(e.args)
        print "Model update_usuario Message {}".format(e.message)
        return None
