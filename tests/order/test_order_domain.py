"""Test Order model"""
import uuid
import datetime
from src.order.domain.order import Order

def gen_dummy():
    user_id = uuid.uuid4()
    order_date = datetime.datetime()
    last_payment_date=datetime.datetime()

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
    },
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


def test_order_model_init():
    data = gen_dummy()

    order = Order(
        order_id=data["order_id"],
        customer_id=data["customer_id"],
        customer_name=data["customer_name"],
        gov_id=data["gov_id"],
        order_date=data["order_date"],
        last_payment_date=data["last_payment_date"],
        order_status=data["order_status"],
        shipping_info=data["shipping_info"],
        totals= data["totals"],
        user_information=data["user_information"]
    )

    assert order.order_id == 1
    assert order.customer_id == 34
    assert order.customer_name == "Hurrem"
    assert order.gov_id == "115476984"
    assert order.order_date == data["order_date"]
    assert order.last_payment_date == data["last_payment_date"]
    assert order.order_status == "pending"
    assert order.shipping_info == data["shipping_info"]
    assert order.totals == data["totals"]
    assert order.user_information == data["user_information"]


def test_order_model_from_dict():
    init_dict = gen_dummy()

    order = Order.from_dict(init_dict)

    assert order.order_id == 1
    assert order.customer_id == 34
    assert order.customer_name == "Hurrem"
    assert order.gov_id == "115476984"
    assert order.order_date == init_dict["order_date"]
    assert order.last_payment_date == init_dict["last_payment_date"]
    assert order.order_status == "pending"
    assert order.shipping_info == init_dict["shipping_info"]
    assert order.totals == init_dict["totals"]
    assert order.user_information == init_dict["user_information"]


def test_order_model_to_dict():
    init_dict = gen_dummy()

    order = Order.from_dict(init_dict)
    assert order.to_dict() == init_dict


def test_order_model_comparison():
    init_dict = gen_dummy()

    order_1 = Order.from_dict(init_dict)
    order_2 = Order.from_dict(init_dict)

    assert order_1 == order_2
