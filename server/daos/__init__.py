from server.models import BaseModel
from server.providers.errors import DataNotFoundException


class BaseDao:
    def __init__(self, entity_name, data = None) -> None:
        self.entity = entity_name
        self.data = data

    def read(self, id = None):
        if id is not None:
            return BaseModel(self.entity).select("id", id)
        return BaseModel(self.entity).select()

    def delete(self):
        pass

    def save(self, data):
        return BaseModel(self.entity).insert(data)

    