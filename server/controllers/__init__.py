from http.client import HTTPException
from flask_restful import Resource, Api
from flask import Response, abort, request

from daos import BaseDao
from providers.errors import APIException


class EntitiesResource(Resource):
    def get(self, entity):
        try:
            return BaseDao(entity).read()
        except APIException as _e:
            abort(_e.code, str(_e.description))
        except Exception as e:
            abort(500, description=f"Unknown error: {str(e)}")

    def post(self, entity):
        try:
            return BaseDao(entity).save(request.json)
        except APIException as _e:
            abort(_e.code, str(_e.description))
        except Exception as e:
            abort(500, description=f"Unknown error: {str(e)}")

class EntityResource(Resource):
    def get(self, entity, id):
        try:
            return BaseDao(entity).read(id)
        except APIException as _e:
            abort(_e.code, str(_e.description))
        except Exception as e:
            abort(500, description=f"Unknown error: {str(e)}")

    def post(self, entity, id):
        print(id)