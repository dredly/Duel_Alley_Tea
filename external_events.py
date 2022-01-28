def leak(shop):
    print("LEAKIN'")


def pests(shop):
    if shop.cleanliness - 4 < 0:
        shop.change_cleanliness(0)
    shop.change_cleanliness(shop.cleanliness - 4)
    print("THE RATS ARE COMING")


def inspector(shop):
    shop.update_hygiene_score()
    print("Uh oh, inspector coming")


def customer(shop):
    print("Here comes a customer. Yay!")
