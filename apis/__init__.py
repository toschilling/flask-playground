from flask_restplus import Api

from .cats import api      as ns1
from .reconcile import api as ns2

api = Api(
    title='flask-RESTPlus example',
    version='1.0',
    description='A very detailed description',
    # All API metadatas
)

api.add_namespace(ns1)
api.add_namespace(ns2)
