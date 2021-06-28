import json
import uuid

from src.user.serializers.user import UserJsonEncoder
from src.user.domain.user import User


def test_serialize_domain_user():
    user_id = uuid.uuid4()
    user = User(
        user_id,
        name="Alexander",
        last_name="Mikelson",
        gov_id="115476984",
        email="alexander.hamilton@gmail.com",
        company="Toyota"
    )

    expected_json = f"""
        {{
            "user_id": "{user_id}",
            "name": "Alexander",
            "last_name": "Mikelson",
            "gov_id": "115476984",
            "email": "alexander.hamilton@gmail.com",
            "company": "Toyota"
        }}
    """

    json_room = json.dumps(room, cls=UserJsonEncoder)

    assert json.loads(json_room) == json.loads(expected_json)
