import config as config

db = config.db #accede al archivo config y al objeto db




""" METODO PARA LOCALIZAR EL USUARIO QUE INTENTA LOGEARSE"""
def login_usuario(correo, password):
    try:
        return db.select('usuarios', where = 'correo=$correo and password=$password' , vars=locals())[0] #selecciona el primer registro que coincida con el id dado en el parametro
    except Exception as e:
        print "Model log_user Error {}".format(e.args)
        print "Model log_user Message {}".format(e.message)
        return None 

def login_estacionamiento(correo, password):
    try:
        return db.select('estacionamientos', where = 'correo=$correo and password=$password' , vars=locals())[0] #selecciona el primer registro que coincida con el id dado en el parametro
    except Exception as e:
        print "Model log_park Error {}".format(e.args)
        print "Model log_park Message {}".format(e.message)
        return None

def get_all_login():
	try:
		return db.select('login')
	except Exception as e:
		print "Model select_usuaempresas Error {}".format(e.args)
        print "Model select_usuaempresas Message {}".format(e.message)
        return None 


def get_login(id):
	try:
		return db.select('login', where='id=$id', vars=locals())[0]
	
	except Exception as e:
		print "Model select_usuario Error {}".format(e.args)
        print "Model select_usuario Message {}".format(e.message)
        return None