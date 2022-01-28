import random

from models import Shop
from external_events import *

config = {
    "shops": {
        "customer_satisfaction": 8,
        "moneys": 1000,
        "cleanliness": 10,
        "hygiene_score": 5,
    },
    "probablities": {
        "leak": (0.03, leak),
        "pests": (0.01, pests),
        "inspector": (0.01, inspector),
        "customer": (0.4, customer),
    },
}


def event_checks(probabilities):
    rand = random.random()
    for ev, prob in probabilities.items():
        if prob[0] > rand:
            prob[1]()


def make_shops(shop_config):
    left_shop = Shop(
        shop_name="Shop on left",
        customer_satisfaction=shop_config["customer_satisfaction"],
        moneys=shop_config["moneys"],
        cleanliness=shop_config["cleanliness"],
        hygiene_score=shop_config["hygiene_score"],
    )
    right_shop = Shop(
        shop_name="Shop on right",
        customer_satisfaction=shop_config["customer_satisfaction"],
        moneys=shop_config["moneys"],
        cleanliness=shop_config["cleanliness"],
        hygiene_score=shop_config["hygiene_score"],
    )
    return (left_shop, right_shop)


event_checks(config["probablities"])
