import datetime
import json
import uuid

from src.order.serializer import OrderJsonEncoder
from src.order.domain import Order


def gen_dummy():
    user_id = str(uuid.uuid4())
    order_date = str(datetime.datetime.now())
    last_payment_date= str(datetime.datetime.now())

    shipping_info={
        "address": "Carrera 8 No. 34 - 12",
        "city": "Meta",
        "state": "Cesar",
        "country": "Colombia",
        "cost": 6000
    }
    totals= {
        "subtotal": 120000,
        "taxes": 22800,
        "shipping_cost": 6000,
        "total": 148800,
        "total_paid": 100000,
        "total_pending": 48800
    }
    user_information = {
        "user_id": user_id,
        "name": "Alexander",
        "last_name": "Mikelson",
        "gov_id": "115476984",
        "email": "alexander.hamilton@gmail.com",
        "company": "Toyota"
    }

    init_dict = {
        "order_id": 1,
        "customer_id": 34,
        "customer_name": "Hurrem",
        "gov_id": "115476984",
        "order_date": order_date,
        "last_payment_date": last_payment_date,
        "order_status": "pending",
        "shipping_info": shipping_info,
        "totals": totals,
        "user_information": user_information
    }

    return init_dict


def test_serialize_domain_order():
    init_dict = gen_dummy()
    order = Order.from_dict(init_dict)

    expected_json = f"""
        {{
            "order_id": 1,
            "customer_id": 34,
            "customer_name": "Hurrem",
            "gov_id": "115476984",
            "order_date": {str(init_dict["order_date"])},
            "last_payment_date": {str(init_dict["last_payment_date"])},
            "order_status": "pending",
            "shipping_info": {{
                "address": "Carrera 8 No. 34 - 12",
                "city": "Meta",
                "state": "Cesar",
                "country": "Colombia",
                "cost": 6000}},
            "totals": {{
                "subtotal": 120000,
                "taxes": 22800,
                "shipping_cost": 6000,
                "total": 148800,
                "total_paid": 100000,
                "total_pending": 48800}},
            "user_information": {{
                "user_id": {init_dict["user_information"]["user_id"]},
                "name": "Alexander",
                "last_name": "Mikelson",
                "gov_id": "115476984",
                "email": "alexander.hamilton@gmail.com",
                "company": "Toyota"}},
        }}
    """

    json_order = json.dumps(order, cls=OrderJsonEncoder)

    assert json.loads(json_order) == order.to_dict()
