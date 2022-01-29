from distutils.ccompiler import show_compilers
from enum import Flag
from re import S
from turtle import Screen
import pygame
from external_events import leak
from testbase import config, make_shops, event_checks
from pygame import K_DOWN, K_LCTRL, K_LEFT, K_RCTRL, K_RIGHT, K_UP, KEYDOWN, KEYUP, QUIT, K_a, K_d, K_s, K_w
from pygame.locals import (
    K_ESCAPE
)

FPS = 60
SPEED = 8
FramePerSec = pygame.time.Clock()

BLACK = (0, 0, 0)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

walk_count_left = 0
walk_count_right = 0
leak_count = 0

class Sink(pygame.sprite.Sprite):
    def __init__(self):
        super(Sink, self).__init__()
        self.surf = pygame.Surface((5, 100), pygame.SRCALPHA)
        self.rect_left = self.surf.get_rect()
        self.rect_left.move_ip(5, 500)
        self.rect_right = self.surf.get_rect()
        self.rect_right.move_ip(1275, 500)
        leak_transform = (200, 130)
        leaking_1 = pygame.transform.scale(pygame.image.load("Images\\leaking-1.png"), leak_transform)
        leaking_2 = pygame.transform.scale(pygame.image.load("Images\\leaking-2.png"), leak_transform)
        leaking_1_left = pygame.transform.scale(pygame.image.load("Images\\leaking-1-left.png"), leak_transform)
        leaking_2_left = pygame.transform.scale(pygame.image.load("Images\\leaking-2-left.png"), leak_transform)
        self.leaking = [leaking_1, leaking_2, leaking_1, leaking_2, leaking_1, leaking_2, leaking_1, leaking_2]
        self.leaking_left = [leaking_1_left, leaking_2_left, leaking_1_left, leaking_2_left, leaking_1_left, leaking_2_left, leaking_1_left, leaking_2_left]
        self.leaking_rect_left = leaking_1_left.get_rect()
        self.leaking_rect_right = leaking_1_left.get_rect()
        self.leaking_rect_left.move_ip(-70, 520)
        self.leaking_rect_right.move_ip(1155, 520)

    def draw(self, surface):
        surface.blit(self.surf, self.rect_left)
        surface.blit(self.surf, self.rect_right)

    def leak_right(self, surface):
        global leak_count
        if leak_count + 1 >= FPS:
            leak_count = 0
        surface.blit(self.leaking[int(leak_count//7.5)], self.leaking_rect_right)
        leak_count += 1

    
    def leak_left(self, surface):
        global leak_count
        if leak_count + 1 >= FPS:
            leak_count = 0
        surface.blit(self.leaking_left[int(leak_count//7.5)], self.leaking_rect_left)
        leak_count += 1


class Phone(pygame.sprite.Sprite):
    def __init__(self):
        super(Phone, self).__init__()
        self.surf = pygame.Surface((2, 100), pygame.SRCALPHA)
        self.rect_left = self.surf.get_rect()
        self.rect_left.move_ip(249, 474)
        self.rect_right = self.surf.get_rect()
        self.rect_right.move_ip(1028, 474)

    def draw(self, surface):
        surface.blit(self.surf, self.rect_left)
        surface.blit(self.surf, self.rect_right)


class CashRegister():
    def __init__(self):
        super(CashRegister, self).__init__()
        self.surf = pygame.Surface((2, 100), pygame.SRCALPHA)
        self.rect_left = self.surf.get_rect()
        self.rect_left.move_ip(483, 474)
        self.rect_right = self.surf.get_rect()
        self.rect_right.move_ip(793, 474)

    def draw(self, surface):
        surface.blit(self.surf, self.rect_left)
        surface.blit(self.surf, self.rect_right)


class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super(Floor, self).__init__()
        self.surf_left = pygame.Surface((1280, 10), pygame.SRCALPHA)
        self.rect_left = self.surf_left.get_rect()
        self.rect_left.move_ip(0, 635)
        self.surf_right = pygame.Surface((1280, 10), pygame.SRCALPHA)
        self.rect_right = self.surf_right.get_rect()
        self.rect_right.move_ip(0, 638)

    def draw(self, surface):
        surface.blit(self.surf_left, self.rect_left)
        surface.blit(self.surf_right, self.rect_right)


class FrontWall(pygame.sprite.Sprite):
    def __init__(self):
        super(FrontWall, self).__init__()
        self.surf_left = pygame.Surface((10, 720), pygame.SRCALPHA)
        self.rect_left = self.surf_left.get_rect()
        self.rect_left.move_ip(558, 0)
        self.surf_right = pygame.Surface((10, 720), pygame.SRCALPHA)
        self.rect_right = self.surf_right.get_rect()
        self.rect_right.move_ip(710, 0)

    def draw(self, surface):
        surface.blit(self.surf_left, self.rect_left)
        surface.blit(self.surf_right, self.rect_right)


class BackWall(pygame.sprite.Sprite):
    def __init__(self):
        super(BackWall, self).__init__()
        self.surf_left = pygame.Surface((1, 720), pygame.SRCALPHA)
        self.rect_left = self.surf_left.get_rect()
        self.rect_left.move_ip(0, 0)
        self.surf_right = pygame.Surface((10, 720), pygame.SRCALPHA)
        self.rect_right = self.surf_right.get_rect()
        self.rect_right.move_ip(1279, 0)

    def draw(self, surface):
        surface.blit(self.surf_left, self.rect_left)
        surface.blit(self.surf_right, self.rect_right)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.run_index = 0
        self.transform = (120, 120)
        running_1_left = pygame.transform.scale(pygame.image.load("Images\\running-1.png"), self.transform)
        running_1_right = pygame.transform.scale(pygame.image.load("Images\\running-1-right.png"), self.transform)
        running_2_left = pygame.transform.scale(pygame.image.load("Images\\running-2.png"), self.transform)
        running_2_right = pygame.transform.scale(pygame.image.load("Images\\running-2-right.png"), self.transform)
        standing_1_left = pygame.transform.scale(pygame.image.load("Images\\standing-1.png"), self.transform)
        standing_1_right = pygame.transform.scale(pygame.image.load("Images\\standing-1-right.png"), self.transform)
        standing_2_left = pygame.transform.scale(pygame.image.load("Images\\standing-2.png"), self.transform)
        standing_2_right = pygame.transform.scale(pygame.image.load("Images\\standing-2-right.png"), self.transform)
        self.running_left = [running_1_left, running_2_left, running_1_left, running_2_left, running_1_left, running_2_left, running_1_left, running_2_left]
        self.running_right = [running_1_right, running_2_right, running_1_right, running_2_right, running_1_right, running_2_right, running_1_right, running_2_right]
        self.standing_left = [standing_1_left, standing_2_left, standing_1_left, standing_2_left, standing_1_left, standing_2_left, standing_1_left, standing_2_left]
        self.standing_right = [standing_1_right, standing_2_right, standing_1_right, standing_2_right, standing_1_right, standing_2_right, standing_1_right, standing_2_right]
        self.rect = self.standing_left[0].get_rect()
        

    def place_right(self):
        self.rect.move_ip(1180, 500)
        self.last_look = 'left'

    def place_left(self):
        self.rect.move_ip(0, 500)
        self.last_look = 'right'

    def update_left(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_a]:
            self.rect.move_ip(-SPEED, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(SPEED, 0)

    def update_right(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-SPEED, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(SPEED, 0)

    def draw_left(self, surface):
        global walk_count_left
        pressed_keys = pygame.key.get_pressed()
        
        if walk_count_left + 1 >= FPS:
                walk_count_left = 0

        if pressed_keys[K_a]:
            surface.blit(self.running_left[int(walk_count_left//7.5)], self.rect)
            walk_count_left += 1
            self.last_look = 'left'
        elif pressed_keys[K_d]:
            surface.blit(self.running_right[int(walk_count_left//7.5)], self.rect)
            walk_count_left += 1
            self.last_look = 'right'
        else:
            if self.last_look == 'right':
                surface.blit(self.standing_right[int(walk_count_left//7.5)], self.rect)
                walk_count_left += 1
            elif self.last_look == 'left':
                surface.blit(self.standing_left[int(walk_count_left//7.5)], self.rect)
                walk_count_left += 1

    def draw_right(self, surface):
            global walk_count_right
            pressed_keys = pygame.key.get_pressed()
            
            if walk_count_right + 1 >= FPS:
                    walk_count_right = 0

            if pressed_keys[K_LEFT]:
                surface.blit(self.running_left[int(walk_count_right//7.5)], self.rect)
                walk_count_right += 1
                self.last_look = 'left'
            elif pressed_keys[K_RIGHT]:
                surface.blit(self.running_right[int(walk_count_right//7.5)], self.rect)
                walk_count_right += 1
                self.last_look = 'right'
            else:
                if self.last_look == 'right':
                    surface.blit(self.standing_right[int(walk_count_right//7.5)], self.rect)
                    walk_count_right += 1
                elif self.last_look == 'left':
                    surface.blit(self.standing_left[int(walk_count_right//7.5)], self.rect)
                    walk_count_right += 1


if __name__ == '__main__':           
    running = True

    pygame.init()
    pygame.font.init()

    myFont = pygame.font.SysFont("Comc Sans MS", 30)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    shops = make_shops(config["shops"], config["probabilities"])
    
    player_left = Player()
    player_left.place_left()
    player_right = Player()
    player_right.place_right()
    floor = Floor()
    sink = Sink()
    phone = Phone()
    cashregister = CashRegister()
    front_wall = FrontWall()
    back_wall = BackWall()
    frame_count = 0

    def check_time():
        global frame_count
        frame_count += 1
        if frame_count + 1 >= FPS:
            event_checks(shops[0])
            event_checks(shops[1])
            frame_count = 0

    pygame.display.update()

    while running:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_DOWN:
                    if sink.rect_right.colliderect(player_right.rect):
                        shops[1].start_cleaning()
                elif event.key == K_s:
                    if sink.rect_left.colliderect(player_left.rect):
                        shops[0].start_cleaning()
                elif event.key == K_w:
                    if phone.rect_left.colliderect(player_left.rect):
                        shops[0].call_pest_control()
                elif event.key == K_UP:
                    if phone.rect_right.colliderect(player_right.rect):
                        shops[1].call_pest_control()
                elif event.key == K_RCTRL:
                    if sink.rect_right.colliderect(player_right.rect):
                        shops[1].fix_leak()
                elif event.key == K_LCTRL:
                    if sink.rect_left.colliderect(player_left.rect):
                        shops[0].fix_leak()
                
            elif event.type == KEYUP:
                if event.key == K_DOWN:
                    shops[1].stop_cleaning()
                elif event.key == K_s:
                    shops[0].stop_cleaning()
            elif event.type == QUIT:
                running = False
        
        check_time()
        screen.fill(BLACK)
        screen.blit(pygame.transform.smoothscale(pygame.image.load("Images\\backgroundtest6.png").convert(), (1280, 720)), (0, 0))
        floor.draw(screen)
        front_wall.draw(screen)
        back_wall.draw(screen)
        sink.draw(screen)
        phone.draw(screen)
        cashregister.draw(screen)
        if shops[1].leaking:
            sink.leak_right(screen)
        if shops[0].leaking:
            sink.leak_left(screen)
        screen.blit(pygame.image.load(shops[1].img_file_names["cleanliness_overlay"]), (757, 284))
        screen.blit(pygame.image.load(shops[0].img_file_names["cleanliness_overlay"]), (-263, 284))
        hygiene_rating_1 = pygame.transform.smoothscale(pygame.image.load(shops[1].img_file_names["hygiene_score_image"]), (120, 80))
        screen.blit(hygiene_rating_1, (700, 240))
        hygiene_rating_0 = pygame.transform.smoothscale(pygame.image.load(shops[0].img_file_names["hygiene_score_image"]), (120, 80))
        screen.blit(hygiene_rating_0, (460, 240))
        shop_1_money = myFont.render(f"Moneys: {shops[0].moneys}", False, (0, 0, 0))
        screen.blit(shop_1_money, (10, 230))
        shop_2_money = myFont.render(f"Moneys: {shops[1].moneys}", False, (0, 0, 0))
        screen.blit(shop_2_money, (1133, 230))
        player_left.update_left()
        player_right.update_right()
        
        #Interactions
        if sink.rect_left.colliderect(player_left.rect):
            pass
        if sink.rect_right.colliderect(player_right.rect):
            pass

        # Exceptions
        if not floor.rect_left.colliderect(player_left.rect):
            player_left.rect.move_ip(0, 3)
        if not floor.rect_right.colliderect(player_right.rect):
            player_right.rect.move_ip(0, 3)
        if front_wall.rect_left.colliderect(player_left.rect):
            player_left.rect.move_ip(-SPEED, 0)
        if front_wall.rect_right.colliderect(player_right.rect):
            player_right.rect.move_ip(SPEED, 0)
        if back_wall.rect_left.colliderect(player_left.rect):
            player_left.rect.move_ip(SPEED, 0)
        if back_wall.rect_right.colliderect(player_right.rect):
            player_right.rect.move_ip(-SPEED, 0)
        player_left.draw_left(screen)
        player_right.draw_right(screen)

        pygame.display.update()
        FramePerSec.tick(FPS)