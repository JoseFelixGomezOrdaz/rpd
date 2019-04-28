import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_desaparecido, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(id_desaparecido) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_desaparecido, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_desaparecido) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_desaparecido, **k):

    @staticmethod
    def POST_EDIT(id_desaparecido, **k):
        
    '''

    def GET(self, id_desaparecido, **k):
        message = None # Error message
        id_desaparecido = config.check_secure_val(str(id_desaparecido)) # HMAC id_desaparecido validate
        result = config.model.get_desaparecidos(int(id_desaparecido)) # search for the id_desaparecido
        result.id_desaparecido = config.make_secure_val(str(result.id_desaparecido)) # apply HMAC for id_desaparecido
        return config.render.edit(result, message) # render desaparecidos edit.html

    def POST(self, id_desaparecido, **k):
        form = config.web.input()  # get form data
        form['id_desaparecido'] = config.check_secure_val(str(form['id_desaparecido'])) # HMAC id_desaparecido validate
        # edit user with new data
        result = config.model.edit_desaparecidos(
            form['id_desaparecido'],form['nombre'],form['apellido_paterno'],form['edad'],form['sexo'],form['fecha_desaparicion'],form['latitud'],form['longitud'],
        )
        if result == None: # Error on udpate data
            id_desaparecido = config.check_secure_val(str(id_desaparecido)) # validate HMAC id_desaparecido
            result = config.model.get_desaparecidos(int(id_desaparecido)) # search for id_desaparecido data
            result.id_desaparecido = config.make_secure_val(str(result.id_desaparecido)) # apply HMAC to id_desaparecido
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/desaparecidos') # render desaparecidos index.html
