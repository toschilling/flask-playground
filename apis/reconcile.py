from flask_restplus import Namespace, Resource, fields

api = Namespace('reconcile', description='OpenRefine\'s Reconciliation API endpoint')


@api.route('/')
class SomeList(Resource):
    def get(self):
        pass

@api.route('/properties')
@api.response(404, 'Not found')
class Reconcile(Resource):
    @api.doc('get_reconcile')
    def get(self, id):
        '''GET Method'''
        pass
