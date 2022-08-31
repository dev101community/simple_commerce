from server.providers.errors import DataNotFoundException

data = [
    {
        "id": 1,
        "name": "Muthu"
    }
]

class BaseModel:
    def __init__(self, entity_name) -> None:
        self.entity = entity_name
        self.data = data

    def find(self, search_key, search_value):
        for d in self.data:
            if d[search_key] == int(search_value):
                return d
        return None

    def select(self, search_key = None, search_value = None):
        if search_key is not None:
            existing = self.find(search_key, search_value)
            if existing is not None:
                return existing
            else:
                raise DataNotFoundException(f"`{search_key}` - {search_value} Not found")
        return self.data

    def insert(self, data):
        existing = self.find("id", data["id"])
        if existing is not None:
            raise DataNotFoundException(f"Can't update {self.entity.upper()}! Data exists.")
        self.data.append(data)
        return data