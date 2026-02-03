import json

class BaseModel:
    def __init__(self, raw_data: str):
        data = json.loads(raw_data)
        for key, value in data.items():
            setattr(self, key, value)

    def to_dict(self):
        return self.__dict__