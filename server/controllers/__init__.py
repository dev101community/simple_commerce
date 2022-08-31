from http.client import HTTPException
from flask_restful import Resource, Api
from flask import Response, abort, request

from server.daos import BaseDao
from server.providers.errors import APIException


class EntitiesResource(Resource):
    def get(self, entity):
        try:
            return BaseDao(entity).get()
        except APIException as _e:
            abort(_e.code, str(_e.description))
        except Exception as e:
            abort(500, description=f"Unknown error: {str(e)}")

    def post(self, entity):
        try:
            return BaseDao(entity).post(request.json)
        except APIException as _e:
            abort(_e.code, str(_e.description))
        except Exception as e:
            abort(500, description=f"Unknown error: {str(e)}")

class EntityResource(Resource):
    def get(self, entity, id):
        return BaseDao(entity).get(id)

    def post(self, entity, id):
        print(id)