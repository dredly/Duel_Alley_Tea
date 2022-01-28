class Shop:
    def __init__(
        self, shop_name, customer_satisfaction, moneys, cleanliness, hygiene_score
    ):
        self.shop_name = shop_name
        self.customer_satisfaction = customer_satisfaction
        self.moneys = moneys
        self.cleanliness = cleanliness
        self.hygiene_score = hygiene_score

    def __repr__(self):
        return f"------\nShop: {self.shop_name}. Current moneys: ${self.moneys}\nCustomer satisfaction: {self.customer_satisfaction}\nCleanliness: {self.cleanliness}, hygiene score: {self.hygiene_score}\n-----"
