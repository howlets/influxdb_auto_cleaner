from auto_cleaner.api.restplus import api
from flask_restplus import Resource
from logger.logging import service_logger
from flask import request

log = service_logger()
ns = api.namespace('', description='InfluxDB Auto Cleaner')


@ns.route('/health')
class Health(Resource):

    @staticmethod
    def get():
        """
        Service health check
        """

        return {'status': 'UP'}, 200



