"""Define the Order serializer"""
import json


class OrderJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return obj.to_dict()
        except AttributeError:
            return super().default(obj)
