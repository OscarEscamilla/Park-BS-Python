import web 


#importacion de cada modelo
import application.models.parks.model_park as model_park



#renderiza todas las vistas con el master template
render = web.template.render('application/views/parks', base ='master') 
  