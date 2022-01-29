import random


def leak(shop):
    # print("LEAKIN'")
    shop.leak()
    if shop.cleanliness - 2 < 0:
        shop.change_cleanliness(0)
    else:
        shop.change_cleanliness(shop.cleanliness - 2)


def pests(shop):
    # Decrease cleanliness by 4
    shop.is_infested = True
    # print("THE RATS ARE COMING")


def inspector(shop):
    shop.update_hygiene_score()
    # print("Uh oh, inspector coming")


def customer(shop):
    # random comment
    if not shop.is_cleaning:
        # print("Here comes a customer. Yay!")
        shop.moneys += 2
        rand = random.random()
        # Chance of customer making the shop dirtier
        if rand < 0.2:
            # Decrease cleanliness by 1
            if shop.cleanliness - 1 < 0:
                shop.change_cleanliness(0)
            else:
                shop.change_cleanliness(shop.cleanliness - 1)

        rand2 = random.random()
        # Chance of customer leaving a review
        if rand2 < 0.2:
            if shop.cleanliness - 2 < 0:
                min_review = 0
            else:
                min_review = shop.cleanliness - 2
            if shop.cleanliness + 2 > 10:
                max_review = 10
            else:
                max_review = shop.cleanliness + 2
            new_review = random.randint(min_review, max_review)
            shop.customer_satisfaction.append(new_review)
            customer_likelihood_modifier = (shop.avg_rating() - 5) * 0.08
            shop.probabilities["customer"][0] = 0.4 + customer_likelihood_modifier
            # print(f"\nReview score: {new_review}\n")
            # print(f"\nNew avg score: {shop.avg_rating()}\n")
            # print(f"\nprobability of new customers: {shop.probabilities['customer'][0]}")
