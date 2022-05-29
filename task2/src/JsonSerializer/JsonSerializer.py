from src.packer import packer, unpacker
from src.JsonSerializer import JsonParser as json


class JsonSerializer:
    """JSON serializer main class"""
    def __init__(self, path: str):
        self.path = path
        self.packer = packer.Packer()
        self.unpacker = unpacker.Unpacker()

    def dump(self, obj: object):
        obj_dict = self.packer.pack(obj)
        with open(self.path, "w") as file:
            json.dump(obj_dict, fp=file)

    def dumps(self, obj: object):
        """Serializes object, class or function into JSON"""
        obj_dict = self.packer.pack(obj)
        return json.dumps(obj_dict)

    def load(self):
        with open(self.path, "r") as file:
            obj_dict = json.load(file)
        return self.unpacker.unpack(obj_dict)

    def loads(self, obj_str: str):
        """Deserializes object, class or function from JSON"""
        obj_dict = json.loads(obj_str)
        return self.unpacker.unpack(obj_dict)
