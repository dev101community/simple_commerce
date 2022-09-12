from providers.errors import DataNotFoundException
from providers.log_provider import logger
from providers.environment import AIRTABLE_API_KEY, AIRTABLE_BASE_KEY

from pyairtable import Table


class BaseModel:
    def __init__(self, entity_name) -> None:
        self.logger = logger
        self.entity = entity_name
        self.data = []
        self.airtable_client = Table(
            AIRTABLE_API_KEY, 
            AIRTABLE_BASE_KEY, 
            entity_name
        )
        self.logger.info(AIRTABLE_API_KEY)
        self.logger.info(AIRTABLE_BASE_KEY)
        self.logger.info(entity_name)
        

    def find(self, search_key, search_value):
        if search_key == "id":
            return self.select_by_id(search_value)
        elif self.data == []:
            self.data = self.select_all()
        for d in self.data:
            if d[search_key] == search_value:
                return d
        return None

    def select_all(self):
        self.data = self.airtable_client.all()
        return self.data

    def select_by_id(self, id: str):
        return self.airtable_client.get(id)


    def select(self, search_key = None, search_value = None):
        if search_key is not None:
            existing = self.find(search_key, search_value)
            if existing is not None:
                return existing
            else:
                raise DataNotFoundException(f"`{search_key}` - {search_value} Not found")
        return self.select_all()

    def insert(self, data):
        existing = self.find("id", data["id"])
        if existing is not None:
            raise DataNotFoundException(f"Can't update {self.entity.upper()}! Data exists.")
        self.data.append(data)
        return data