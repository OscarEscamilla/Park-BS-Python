import web 


#importacion de cada modelo
import application.models.model_usuarios as model_usuarios



#renderiza todas las vistas con el master template
render = web.template.render('application/views/users', base ='master') 
  