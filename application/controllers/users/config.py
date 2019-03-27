import web 


#importacion de cada modelo
import application.models.users.model_user as model_user



#renderiza todas las vistas con el master template
render = web.template.render('application/views/users', base ='master') 
  