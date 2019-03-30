import web 


#importacion de cada modelo
import application.models.model_usuarios as model_usuarios
import application.models.model_estacionamientos as model_estacionamientos 
import application.models.model_login as model_login


#renderiza todas las vistas con el master template
render = web.template.render('application/views/', base ='master') 
render_usuario = web.template.render('application/views/users', base ='master') 
render_estacionamientos = web.template.render('application/views/parks', base ='master') 
