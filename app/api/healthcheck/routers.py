from http import HTTPStatus

from flask import Blueprint, Response, current_app

healthchecks = Blueprint('healthchecks', __name__, url_prefix="/health")


@healthchecks.route('/ready')
@healthchecks.route('/live')
def live():
    try:
        return Response(status=HTTPStatus.OK, response="Live")
    except:
        current_app.logger.exception("There was a problem in healthcheck")
        return Response(status=HTTPStatus.NOT_FOUND, response="Not Found")
