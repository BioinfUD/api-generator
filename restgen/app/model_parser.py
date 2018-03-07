import argparse
import colorama
import yaml
from jinja2 import Template
from colorama import Fore, Back, Style
import sys
import os
from os import mkdir
from os.path import exists, dirname, join

colorama.init()


from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['nv'])
)
script_location = this_folder = dirname(__file__)

class IncompleteModel(Exception):
   pass


types_mapping = {'entero':'Integer',
                 'si': 'True',
                 'fecha': 'Date',
                 'flotante':'Float',
                 'texto': 'Unicode',
                 'fecha-hora':'DateTime',
                 'llave_primaria': 'Integer',
                 'llave_foranea': 'Integer'
                 }

parser = argparse.ArgumentParser(prog="restgen",description='Generar una nueva aplicacion Restful')
parser.add_argument('--model', metavar='M', nargs='?',help='El modelo a interpretar para generar la aplicacion')
args = parser.parse_args()

def attribute_definition(field):
    #  nulo llave_foranea llave_primaria unico
    #  db.Column(db.Integer, db.ForeignKey('person.id'))
    #  db.Column(db.Integer, primary_key=True)
    #  db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    field_config = []
    column_type = types_mapping[field['tipo']]
    for attribute in field:
        if attribute == 'llave_primaria':
            field_config.append("primary_key=True")
        if attribute == 'unico':
            field_config.append("unique=True")
        if attribute == 'nulo':
            field_config.append("nullable=False")
        if attribute == 'llave_foranea':
            field_config.append("db.ForeignKey('{}')".format(field['llave_foranea']))
    return ",".join(["db.{}".format(column_type.capitalize())]+field_config)


def parse_model(model_name):
    with open(model_name,'r') as f:
        try:
            model = yaml.load(f)
            validate_model(model)
        except yaml.parser.ParserError as e:
            print Fore.RED+'Revise su archivo YAML tiene un formato incorrecto'
            print 'El error del interprete es:'
            print(Style.RESET_ALL)
            print e
        except yaml.scanner.ScannerError as e:
            print Fore.RED+'Revise su archivo YAML tiene un formato incorrecto'
            print 'El error del interprete es:'
            print(Style.RESET_ALL)
            print e
        except IncompleteModel as e:
            print "\n"
            print Fore.RED+e.message
            sys.exit(1)
        return model

def generate_backend_service(model):
    template = env.get_template('backend/restful.nv')
    template = template.stream(model=model,mapping=types_mapping)
    template.dump("../backend/code/api.py")
    print "\n"
    print Fore.WHITE+"Su servicio API Restful se ha creado satisfactoriamente "+ Fore.YELLOW+":)"
    print Fore.GREEN + "Creado servicio API [OK]"

def validate_model(model):
    invalido = False
    for entity in model:
        print Fore.WHITE+"\n Verificando Entidad: '{}'".format(entity)
        llave_primaria = False
        print " |"
        for field in model[entity]:
            print Fore.WHITE+" |--->  Campo: {}".format(field)
            if model[entity][field] == None:
                print Fore.RED+"     |----> El campo {} no tiene ninguna descripcion de tipo de dato".format(field)
                continue
            if "llave_primaria" in model[entity][field]:
                llave_primaria = True
            if "tipo" not in model[entity][field]:
                invalido = True
                print Fore.RED+"El campo {} no tiene un tipo de dato asociado".format(field)
            else:
                if model[entity][field]['tipo'] not in types_mapping:
                    invalido = True
                    print Fore.RED+"     |----> El campo {} no tiene un tipo de dato valido (entero, flotante, texto, fecha-hora) Valor actual: {}".format(field,model[entity][field]['tipo'])
        if not llave_primaria:
            invalido = True
            print Fore.RED+" |--> La entidad {} no tiene una llave primaria asociada".format(entity)

    if invalido:
         raise IncompleteModel("*Existe un error en la definicion de su modelo por favor verifique su archivo*")

def generate_frontend_service(model):

    routing_template = env.get_template('frontend/routing/routing.module.ts.nv').stream(model=model)
    routing_template.dump("../frontend/code/routing/routing.module.ts")

    app_module_template = env.get_template('frontend/app.module.ts.nv').stream(model=model)
    app_module_template.dump("../frontend/code/app.module.ts")

    navegacion_entity_folder = join(this_folder, "../frontend/code/entities/navegacion")
    if not os.path.exists(navegacion_entity_folder):
        print "Creando carpeta: {}".format(navegacion_entity_folder)
        os.makedirs(navegacion_entity_folder)

    nav_template = env.get_template('frontend/navegacion/navegacion.component.html.nv').stream(model=model)
    nav_template.dump("../frontend/code/entities/navegacion/navegacion.component.html")

    for entity in model:
        service_template = env.get_template('frontend/services/entity.service.ts.nv').stream(entity=entity)
        service_template.dump("../frontend/code/services/{}.service.ts".format(entity))

        model_template = env.get_template('frontend/models/entity.nv').stream(properties=model[entity],entity=entity)
        model_template.dump("../frontend/code/models/{}.ts".format(entity))

        frontend_entity_folder = join(this_folder, "../frontend/code/entities/{}/view".format(entity))
        if not os.path.exists(frontend_entity_folder):
            print "Creando carpeta: {}".format(frontend_entity_folder)
            os.makedirs(frontend_entity_folder)

        frontend_entity_folder = join(this_folder, "../frontend/code/entities/{}/new".format(entity))
        if not os.path.exists(frontend_entity_folder):
            print "Creando carpeta: {}".format(frontend_entity_folder)
            os.makedirs(frontend_entity_folder)

        frontend_entity_folder = join(this_folder, "../frontend/code/entities/{}/edit".format(entity))
        if not os.path.exists(frontend_entity_folder):
            print "Creando carpeta: {}".format(frontend_entity_folder)
            os.makedirs(frontend_entity_folder)




        view_template_html = env.get_template('frontend/entity/view/entity-view.component.html.nv').stream(properties=model[entity],entity=entity)
        view_template_html.dump("../frontend/code/entities/{}/view/{}-view.component.html".format(entity,entity))

        view_template_ts = env.get_template('frontend/entity/view/entity-view.component.ts.nv').stream(entity=entity)
        view_template_ts.dump("../frontend/code/entities/{}/view/{}-view.component.ts".format(entity,entity))

        new_template_html = env.get_template('frontend/entity/new/entity-new.component.html.nv').stream(properties=model[entity],entity=entity)
        new_template_html.dump("../frontend/code/entities/{}/new/{}-new.component.html".format(entity,entity))

        new_template_ts = env.get_template('frontend/entity/new/entity-new.component.ts.nv').stream(entity=entity)
        new_template_ts.dump("../frontend/code/entities/{}/new/{}-new.component.ts".format(entity,entity))

        edit_template_ts = env.get_template('frontend/entity/edit/entity-edit.component.ts.nv').stream(entity=entity)
        edit_template_ts.dump("../frontend/code/entities/{}/edit/{}-edit.component.ts".format(entity,entity))

        edit_template_html = env.get_template('frontend/entity/edit/entity-edit.component.html.nv').stream(properties=model[entity],entity=entity)
        edit_template_html.dump("../frontend/code/entities/{}/edit/{}-edit.component.html".format(entity,entity))






env.globals['attribute_definition'] = attribute_definition

if(args.model == None):
    parser.print_help()
else:
    model = parse_model(args.model)
    generate_backend_service(model)
    generate_frontend_service(model)
