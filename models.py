import pygame
from pygame import mixer


mixer.init()

class Shop:
    def __init__(self, shop_name, moneys, cleanliness, hygiene_score, probabilities):
        self.shop_name = shop_name
        self.customer_satisfaction = []
        self.moneys = moneys
        self.cleanliness = cleanliness
        self.hygiene_score = hygiene_score
        self.is_infested = False
        self.is_cleaning = False
        self.leaking = False
        self.probabilities = probabilities
        self.has_customer = False
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
        if self.hygiene_score == 0:
            self.hygiene_score = 1
        self.img_file_names[
            "hygiene_score_image"
        ] = f"so_called_art\\pngs\\hygiene_rating_{self.hygiene_score}.png"
        # print("UPDATING HYGIENE SCORE")

    def leak(self):
        pygame.mixer.Sound.play(self.leak_noise, -1)
        self.leaking = True

    def fix_leak(self):
        self.leaking = False
        self.moneys -= 200
        pygame.mixer.Sound.stop(self.leak_noise)

    def start_cleaning(self):
        # print('Starting to Clean')
        self.is_cleaning = True

    def stop_cleaning(self):
        self.is_cleaning = False

    def make_rat_noise(self):
        self.rat_noise = mixer.Sound(self.pest_soundfile)

    def make_leak_noise(self):
        self.leak_noise = mixer.Sound(self.leak_soundfile)
    
    def infest(self):
        self.is_infested = True
        pygame.mixer.Sound.play(self.rat_noise, -1)


    def call_pest_control(self):
        self.moneys -= 200
        self.is_infested = False
        pygame.mixer.Sound.stop(self.rat_noise)

    def avg_rating(self):
        if len(self.customer_satisfaction) == 0:
            return "No ratings"
        else:
            avg = sum(self.customer_satisfaction) / len(self.customer_satisfaction)
            return round(avg)

    def __repr__(self):
        return f"------\nShop: {self.shop_name}. Current moneys: ${self.moneys}\nCustomer satisfaction: {self.customer_satisfaction}, average rating: {self.avg_rating()}\nCleanliness: {self.cleanliness}, hygiene score: {self.hygiene_score}\n-----"
