import web
import config
import json


class Api_desaparecidos:
    def get(self, id_desaparecido):
        try:
            # http://0.0.0.0:8080/api_desaparecidos?user_hash=12345&action=get
            if id_desaparecido is None:
                result = config.model.get_all_desaparecidos()
                desaparecidos_json = []
                for row in result:
                    tmp = dict(row)
                    desaparecidos_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(desaparecidos_json)
            else:
                # http://0.0.0.0:8080/api_desaparecidos?user_hash=12345&action=get&id_desaparecido=1
                result = config.model.get_desaparecidos(int(id_desaparecido))
                desaparecidos_json = []
                desaparecidos_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(desaparecidos_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            desaparecidos_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(desaparecidos_json)

# http://0.0.0.0:8080/api_desaparecidos?user_hash=12345&action=put&id_desaparecido=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre,apellido_paterno,edad,sexo,fecha_desaparicion,latitud,longitud):
        try:
            config.model.insert_desaparecidos(nombre,apellido_paterno,edad,sexo,fecha_desaparicion,latitud,longitud)
            desaparecidos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(desaparecidos_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_desaparecidos?user_hash=12345&action=delete&id_desaparecido=1
    def delete(self, id_desaparecido):
        try:
            config.model.delete_desaparecidos(id_desaparecido)
            desaparecidos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(desaparecidos_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_desaparecidos?user_hash=12345&action=update&id_desaparecido=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_desaparecido, nombre,apellido_paterno,edad,sexo,fecha_desaparicion,latitud,longitud):
        try:
            config.model.edit_desaparecidos(id_desaparecido,nombre,apellido_paterno,edad,sexo,fecha_desaparicion,latitud,longitud)
            desaparecidos_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(desaparecidos_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            desaparecidos_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(desaparecidos_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_desaparecido=None,
            nombre=None,
            apellido_paterno=None,
            edad=None,
            sexo=None,
            fecha_desaparicion=None,
            latitud=None,
            longitud=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_desaparecido=user_data.id_desaparecido
            nombre=user_data.nombre
            apellido_paterno=user_data.apellido_paterno
            edad=user_data.edad
            sexo=user_data.sexo
            fecha_desaparicion=user_data.fecha_desaparicion
            latitud=user_data.latitud
            longitud=user_data.longitud
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_desaparecido)
                elif action == 'put':
                    return self.put(nombre,apellido_paterno,edad,sexo,fecha_desaparicion,latitud,longitud)
                elif action == 'delete':
                    return self.delete(id_desaparecido)
                elif action == 'update':
                    return self.update(id_desaparecido, nombre,apellido_paterno,edad,sexo,fecha_desaparicion,latitud,longitud)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
