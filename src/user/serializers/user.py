import json


class UserJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            to_serialize = {
                "user_id": obj.user_id,
                "name": obj.name,
                "last_name": obj.last_name,
                "gov_id": obj.gov_id,
                "email": obj.email,
                "company": obj.company
            }
            return to_serialize
        except AttributeError:
            return super().default(obj)
