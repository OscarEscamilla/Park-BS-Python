import config as config

db = config.db #accede al archivo config y al objeto db




""" METODO PARA LOCALIZAR EL USUARIO QUE INTENTA LOGEARSE"""
def login_user(correo, password):
    try:
        return db.select('usuarios', where = 'correo=$correo and password=$password' , vars=locals())[0] #selecciona el primer registro que coincida con el id dado en el parametro
    except Exception as e:
        print "Model log_user Error {}".format(e.args)
        print "Model log_user Message {}".format(e.message)
        return None 