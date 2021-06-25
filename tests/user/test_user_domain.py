"""Test user model"""
import uuid
from src.user.domain.user import User


def test_user_model_init():
    user_id = uuid.uuid4()
    user = User(
        user_id,
        name="Alexander",
        last_name="Mikelson",
        gov_id="115476984",
        email="alexander.hamilton@gmail.com",
        company="Toyota"
    )

    assert user.user_id == user_id
    assert user.name == "Alexander"
    assert user.last_name == "Mikelson"
    assert user.gov_id == "115476984"
    assert user.email == "alexander.hamilton@gmail.com"
    assert user.company== "Toyota"


def test_user_model_from_dict():
    user_id = uuid.uuid4()
    init_dict = {
        "user_id": user_id,
        "name": "Alexander",
        "last_name": "Mikelson",
        "gov_id": "115476984",
        "email": "alexander.hamilton@gmail.com",
        "company": "Toyota"
    }

    user = User.from_dict(init_dict)

    assert user.user_id == user_id
    assert user.name == "Alexander"
    assert user.last_name == "Mikelson"
    assert user.gov_id == "115476984"
    assert user.email == "alexander.hamilton@gmail.com"
    assert user.company== "Toyota"


def test_user_model_to_dict():
    init_dict = {
        "user_id": uuid.uuid4(),
        "name": "Alexander",
        "last_name": "Mikelson",
        "gov_id": "115476984",
        "email": "alexander.hamilton@gmail.com",
        "company": "Toyota"
    }

    user = User.from_dict(init_dict)
    assert user.to_dict() == init_dict


def test_user_model_comparison():
    init_dict = {
        "user_id": uuid.uuid4(),
        "name": "Alexander",
        "last_name": "Mikelson",
        "gov_id": "115476984",
        "email": "alexander.hamilton@gmail.com",
        "company": "Toyota"
    }

    user1 = User.from_dict(init_dict)
    user2 = User.from_dict(init_dict)

    assert user1 == user2
