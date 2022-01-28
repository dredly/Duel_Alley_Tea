class Shop:
    def __init__(
        self, shop_name, customer_satisfaction, moneys, cleanliness, hygiene_score
    ):
        self.shop_name = shop_name
        self.customer_satisfaction = customer_satisfaction
        self.moneys = moneys
        self.cleanliness = cleanliness
        self.hygiene_score = hygiene_score
        self.img_file_names = {
            "cleanliness_overlay": f"cleanliness_level{cleanliness}.png"
        }

    def change_cleanliness(self, new_val):
        self.cleanliness = new_val
        self.img_file_names["cleanliness_overlay"] = f"cleanliness_level{new_val}.png"

    def update_hygiene_score(self):
        # TODO add bribery
        print("UPDATING HYGIEN SCORE")
        self.hygiene_score = self.cleanliness // 2

    def __repr__(self):
        return f"------\nShop: {self.shop_name}. Current moneys: ${self.moneys}\nCustomer satisfaction: {self.customer_satisfaction}\nCleanliness: {self.cleanliness}, hygiene score: {self.hygiene_score}\n-----"
