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
            "cleanliness_overlay": f"cleanliness_level_{self.cleanliness}.png",
            "leak_overlay": None,
            "hygiene_score_image": f"hygiene_score_{self.hygiene_score}.png",
        }

    def change_cleanliness(self, new_val):
        self.cleanliness = new_val
        self.img_file_names["cleanliness_overlay"] = f"cleanliness_level_{new_val}.png"

    def update_hygiene_score(self):
        # TODO add bribery
        self.hygiene_score = self.cleanliness // 2
        self.img_file_names[
            "hygien_score_images"
        ] = f"hygiene_score_{self.hygiene_score}.png"
        print("UPDATING HYGIENE SCORE")

    def leak(self):
        self.img_file_names["leak_overlay"] = "leak.png"

    def fix_leak(self):
        self.img_file_names["leak_overlay"] = None

    def __repr__(self):
        return f"------\nShop: {self.shop_name}. Current moneys: ${self.moneys}\nCustomer satisfaction: {self.customer_satisfaction}\nCleanliness: {self.cleanliness}, hygiene score: {self.hygiene_score}\n-----"
