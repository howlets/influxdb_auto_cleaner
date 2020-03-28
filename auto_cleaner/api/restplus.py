import logging
import traceback

from flask_restplus import Api
import auto_cleaner.settings as settings

log = logging.getLogger(__name__)

api = Api(version='1.0', title='Influx Auto Cleaner')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500
