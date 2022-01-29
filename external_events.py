import random


def leak(shop):
    print("LEAKIN'")
    if shop.cleanliness - 2 < 0:
        shop.change_cleanliness(0)
    else:
        shop.change_cleanliness(shop.cleanliness - 2)


def pests(shop):
    # Decrease cleanliness by 4
    if shop.cleanliness - 4 < 0:
        shop.change_cleanliness(0)
    else:
        shop.change_cleanliness(shop.cleanliness - 4)
    print("THE RATS ARE COMING")


def inspector(shop):
    shop.update_hygiene_score()
    print("Uh oh, inspector coming")


def customer(shop):
    shop.moneys += 2
    rand = random.random()
    if rand < 0.2:
        # Decrease cleanliness by 1
        if shop.cleanliness - 1 < 0:
            shop.change_cleanliness(0)
        else:
            shop.change_cleanliness(shop.cleanliness - 1)
    print("Here comes a customer. Yay!")
