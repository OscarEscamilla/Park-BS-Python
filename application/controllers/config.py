import web 


#importacion de cada modelo
import application.models.model_registro as model_registro
import application.models.model_registro_e as model_registro_e
import application.models.model_login as model_login


#renderiza todas las vistas con el master template
render = web.template.render('application/views/', base ='master') 
