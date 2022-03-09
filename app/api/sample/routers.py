from http import HTTPStatus

from flask import Blueprint, current_app, jsonify, request
from flask_pydantic_spec import Request, Response

import app.common.constants as C
from app.api.sample.logic import SampleLogicHandler
from app.common.models import SampleRequest, SampleResponse
from app.dependencies.apispec import apispec
from app.dependencies.security import sample_apikey_auth

sample = Blueprint('sample', __name__, url_prefix="/sample")


@sample.route('/', methods=[C.POST_METHOD])
@sample_apikey_auth.login_required()
@apispec.validate(body=Request(SampleRequest), resp=Response(HTTP_200=SampleResponse, HTTP_403=None), tags=['sample'])
def get_sample_response():
    try:
        request_body: SampleRequest = request.context.body
        handler = SampleLogicHandler()
        response: SampleResponse = handler.handle_request(request_body.account)
        return response.dict()
    except:
        current_app.logger.exception(C.THERE_WAS_PROBLEM_PROCESSING)
        return Response(status=HTTPStatus.BAD_REQUEST, response=C.THERE_WAS_PROBLEM_PROCESSING)