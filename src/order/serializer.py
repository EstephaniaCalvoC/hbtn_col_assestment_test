import json


class OrderJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            to_serialize = {
                "order_id": obj.order_id,
                "customer_id": obj.customer_id,
                "customer_name": obj.customer_name,
                "gov_id": obj.gov_id,
                "order_date": str(obj.order_date),
                "last_payment_date": str(obj.last_payment_date),
                "order_status": obj.order_status,
                "shipping_info": obj.shipping_info,
                "totals": obj.totals,
                "user_information": obj.user_information,
            }
            # print("Real","="*30, to_serialize)
            return to_serialize
        except AttributeError:
            return super().default(obj)
