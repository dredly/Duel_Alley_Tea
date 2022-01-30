import random
import copy
from models import Shop
from external_events import *

config = {
    "shops": {
        "customer_satisfaction": 8,
        "moneys": 1000,
        "cleanliness": 10,
        "hygiene_score": 5,
    },
    "probabilities": {
        "leak": [0.05, leak],
        "pests": [0.05, pests],
        "inspector": [0.7, inspector],
        "customer": [0.4, customer],
    },
    #1137, 427 - right

}


def event_checks(shop):
    # print(shop.shop_name)
    if shop.is_cleaning:
        if shop.cleanliness + 1 > 10:
            shop.change_cleanliness(10)
        else:
            shop.change_cleanliness(shop.cleanliness + 1)
    if shop.is_infested:
        rand = random.random()
        if rand < 0.2:
            # Decrease cleanliness by 1
            if shop.cleanliness - 1 < 0:
                shop.change_cleanliness(0)
            else:
                shop.change_cleanliness(shop.cleanliness - 1)
    for ev, prob in shop.probabilities.items():
        rand = random.random()
        if prob[0] > rand:
            prob[1](shop)


def make_shops(shop_config, probabilities):
    left_shop = Shop(
        shop_name="Shop on left",
        moneys=shop_config["moneys"],
        cleanliness=shop_config["cleanliness"],
        hygiene_score=shop_config["hygiene_score"],
        probabilities=copy.deepcopy(probabilities),
    )
    left_shop.pest_soundfile = "Sounds\\pests_1.wav"
    left_shop.make_rat_noise()
    right_shop = Shop(
        shop_name="Shop on right",
        moneys=shop_config["moneys"],
        cleanliness=shop_config["cleanliness"],
        hygiene_score=shop_config["hygiene_score"],
        probabilities=copy.deepcopy(probabilities),
    )
    right_shop.pest_soundfile = "Sounds\\pests_2.wav"
    right_shop.make_rat_noise()
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
if  __name__ == "__main__":
    shops = make_shops(config["shops"], config["probabilities"])
    # print(shops[0])
    for i in range(100):
        # print(f"Round {i}")
        event_checks(shops[0])
        event_checks(shops[1])
    # print(shops)
    # print([shop.probabilities["customer"][0] for shop in shops])
