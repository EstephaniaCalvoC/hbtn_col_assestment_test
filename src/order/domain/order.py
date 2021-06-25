"""Define the Order model"""
import uuid
import datetime
import dataclasses

@dataclasses.dataclass
class Order:
    order_id: int
    customer_id: int
    customer_name: str
    gov_id: str
    order_date: datetime.datetime
    last_payment_date: datetime.datetime
    order_status: str
    shipping_info: dict
    totals: dict
    user_information: dict


    @classmethod
    def from_dict(self, d):
        return self(**d)

    def to_dict(self):
        return dataclasses.asdict(self)
