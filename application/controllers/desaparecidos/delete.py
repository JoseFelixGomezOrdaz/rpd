import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, id_desaparecido, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id_desaparecido) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_desaparecido, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id_desaparecido) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_desaparecido, **k):

    @staticmethod
    def POST_DELETE(id_desaparecido, **k):
    '''

    def GET(self, id_desaparecido, **k):
        message = None # Error message
        id_desaparecido = config.check_secure_val(str(id_desaparecido)) # HMAC id_desaparecido validate
        result = config.model.get_desaparecidos(int(id_desaparecido)) # search  id_desaparecido
        result.id_desaparecido = config.make_secure_val(str(result.id_desaparecido)) # apply HMAC for id_desaparecido
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, id_desaparecido, **k):
        form = config.web.input() # get form data
        form['id_desaparecido'] = config.check_secure_val(str(form['id_desaparecido'])) # HMAC id_desaparecido validate
        result = config.model.delete_desaparecidos(form['id_desaparecido']) # get desaparecidos data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_desaparecido = config.check_secure_val(str(id_desaparecido))  # HMAC user validate
            id_desaparecido = config.check_secure_val(str(id_desaparecido))  # HMAC user validate
            result = config.model.get_desaparecidos(int(id_desaparecido)) # get id_desaparecido data
            result.id_desaparecido = config.make_secure_val(str(result.id_desaparecido)) # apply HMAC to id_desaparecido
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/desaparecidos') # render desaparecidos delete.html 
