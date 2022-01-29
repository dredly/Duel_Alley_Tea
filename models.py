class Shop:
    def __init__(self, shop_name, moneys, cleanliness, hygiene_score, probabilities):
        self.shop_name = shop_name
        self.customer_satisfaction = []
        self.moneys = moneys
        self.cleanliness = cleanliness
        self.hygiene_score = hygiene_score
        self.is_infested = False
        self.is_cleaning = False
        self.probabilities = probabilities
        self.img_file_names = {
            "cleanliness_overlay": f"so_called_art\\pngs\\cleanliness_level_{self.cleanliness}.png",
            "leak_overlay": None,
            "hygiene_score_image": f"so_called_art\\pngs\\hygiene_rating_{self.hygiene_score}.png",
        }

    def change_cleanliness(self, new_val):
        self.cleanliness = new_val
        self.img_file_names["cleanliness_overlay"] = f"so_called_art\\pngs\\cleanliness_level_{new_val}.png"

    def update_hygiene_score(self):
        # TODO add bribery
        self.hygiene_score = self.cleanliness // 2
        self.img_file_names[
            "hygiene_score_image"
        ] = f"so_called_art\\pngs\\hygiene_rating_{self.hygiene_score}.png"
        print("UPDATING HYGIENE SCORE")

    def leak(self):
        self.img_file_names["leak_overlay"] = "leak.png"

    def fix_leak(self):
        self.img_file_names["leak_overlay"] = None

    def start_cleaning(self):
        is_cleaning = True

    def stop_cleaning(self):
        is_cleaning = False

    def call_pest_control(self):
        self.moneys -= 500
        self.is_infested = False

    def avg_rating(self):
        if len(self.customer_satisfaction) == 0:
            return "No ratings"
        else:
            avg = sum(self.customer_satisfaction) / len(self.customer_satisfaction)
            return round(avg)

    def __repr__(self):
        return f"------\nShop: {self.shop_name}. Current moneys: ${self.moneys}\nCustomer satisfaction: {self.customer_satisfaction}, average rating: {self.avg_rating()}\nCleanliness: {self.cleanliness}, hygiene score: {self.hygiene_score}\n-----"
