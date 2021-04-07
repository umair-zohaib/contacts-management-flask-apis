from flask import Blueprint
from flask_restx import Api

from app.main.controller.contact_controller import api as contact_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTX API for Contacts Management',
          version='1.0',
          description='a contacts management flask based rest apis'
          )

api.add_namespace(contact_ns, path='/contact')
