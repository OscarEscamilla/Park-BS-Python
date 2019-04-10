import web
import config as config

db = config.db #accede al archivo config y al objeto db

def nueva_sesion(id,rol):
    try:
		return db.insert('sessions',id = id,rol = rol) 

    except Exception as e:

        print "Model sesion_insert Error ()".format(e.args)
        print "Model insert_sesion Message {}".format(e.message)
        return None

def get_all_sessions():
	try:
		return db.select('sessions')
	except Exception as e:
		print "Model selectsesion Error {}".format(e.args)
        print "Model selectsesion Message {}".format(e.message)
        return None 