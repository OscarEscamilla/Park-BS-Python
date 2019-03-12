import web 


#importacion de cada modelo
import application.models.model_registro as model_registro


#renderiza todas las vistas con el master template
render = web.template.render('application/views/', base ='master') 
