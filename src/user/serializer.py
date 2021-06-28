"""Define the User serializer"""
import json


class UserJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return obj.to_dict()
        except AttributeError:
            return super().default(obj)
