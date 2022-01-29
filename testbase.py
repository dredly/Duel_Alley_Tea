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


def event_checks(shop, probabilities):
    print(shop.shop_name)
    for ev, prob in probabilities.items():
        rand = random.random()
        if prob[0] > rand:
            prob[1](shop)


def make_shops(shop_config):
    left_shop = Shop(
        shop_name="Shop on left",
        moneys=shop_config["moneys"],
        cleanliness=shop_config["cleanliness"],
        hygiene_score=shop_config["hygiene_score"],
    )
    right_shop = Shop(
        shop_name="Shop on right",
        moneys=shop_config["moneys"],
        cleanliness=shop_config["cleanliness"],
        hygiene_score=shop_config["hygiene_score"],
    )
    return (left_shop, right_shop)


# left_shop = make_shops(config["shops"])[0]
# print(left_shop)
# print("PESTS ARE COMING")
# pests(left_shop)
# print(left_shop)
# print("SUMMONING THE INSPECTOR")
# inspector(left_shop)
# print(left_shop)
# print("Customer coming!")
# customer(left_shop)
# print(left_shop)

# Testing the event triggering
shops = make_shops(config["shops"])
print(shops[0])
for i in range(50):
    print(f"Round {i}")
    event_checks(shops[0], config["probablities"])
    event_checks(shops[1], config["probablities"])
print(shops[0])
