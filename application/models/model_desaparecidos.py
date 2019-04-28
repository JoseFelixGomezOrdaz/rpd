import web
import config

db = config.db


def get_all_desaparecidos():
    try:
        return db.select('desaparecidos')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_desaparecidos(id_desaparecido):
    try:
        return db.select('desaparecidos', where='id_desaparecido=$id_desaparecido', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_desaparecidos(id_desaparecido):
    try:
        return db.delete('desaparecidos', where='id_desaparecido=$id_desaparecido', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_desaparecidos(nombre,apellido_paterno,edad,sexo,fecha_desaparicion,latitud,longitud):
    try:
        return db.insert('desaparecidos',nombre=nombre,
apellido_paterno=apellido_paterno,
edad=edad,
sexo=sexo,
fecha_desaparicion=fecha_desaparicion,
latitud=latitud,
longitud=longitud)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_desaparecidos(id_desaparecido,nombre,apellido_paterno,edad,sexo,fecha_desaparicion,latitud,longitud):
    try:
        return db.update('desaparecidos',id_desaparecido=id_desaparecido,
nombre=nombre,
apellido_paterno=apellido_paterno,
edad=edad,
sexo=sexo,
fecha_desaparicion=fecha_desaparicion,
latitud=latitud,
longitud=longitud,
                  where='id_desaparecido=$id_desaparecido',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
