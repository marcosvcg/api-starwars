from api.utils import query
import json

class BaseModel:
    def __init__(self, raw_data: str):
        data = json.loads(raw_data)
        for key, value in data.items():
            setattr(self, key, value)

    def to_dict(self):
        return self.__dict__

class BaseQuerySet:
    model = None

    def __init__(self, urls):
        self.items = []

        for url in urls:
            response = query(url)
            self.items.append(self.model(response.content))
            
    def to_list(self):
        return [item.to_dict() for item in self.items]