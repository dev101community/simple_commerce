from server.models import BaseModel
from server.providers.errors import DataNotFoundException


class BaseDao:
    def __init__(self, entity_name, data = None) -> None:
        self.entity = entity_name
        self.data = data

    def get(self, id = None):
        if id is not None:
            return BaseModel(self.entity).get("id", id)
        return BaseModel(self.entity).get()

    def delete(self):
        pass

    def post(self, data):
        return BaseModel(self.entity).post(data)

    