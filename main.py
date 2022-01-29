import pygame
from pygame import RLEACCEL, KEYDOWN, QUIT, K_a, K_d, K_s, K_w
from pygame.locals import (
    K_ESCAPE
)

FPS = 60
FramePerSec = pygame.time.Clock()

BLACK = (0, 0, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

walk_count = 0

class TeaShop(pygame.sprite.Sprite):
    def __init__(self):
        super(TeaShop, self).__init__()
        self.surf = pygame.transform.scale(pygame.image.load("Images\\paint-background.png").convert(), (800, 400))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(0, 100)

    def draw(self, surface):
        surface.blit(self.surf, self.rect)


class Floor(pygame.sprite.Sprite):
    def __init__(self):
        super(Floor, self).__init__()
        self.surf = pygame.Surface((800, 10))
        self.surf.fill((200, 0, 0))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(0, 416)

    def draw(self, surface):
        surface.blit(self.surf, self.rect)


class FrontWall(pygame.sprite.Sprite):
    def __init__(self):
        super(FrontWall, self).__init__()
        self.surf = pygame.Surface((10, 600))
        self.surf.fill((200, 0, 0))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(340, 0)

    def draw(self, surface):
        surface.blit(self.surf, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.run_index = 0
        self.transform = (55, 55)
        running_1_left = pygame.transform.scale(pygame.image.load("Images\\running-1.png"), self.transform)
        running_1_right = pygame.transform.scale(pygame.image.load("Images\\running-1-right.png"), self.transform)
        running_2_left = pygame.transform.scale(pygame.image.load("Images\\running-2.png"), self.transform)
        running_2_right = pygame.transform.scale(pygame.image.load("Images\\running-2-right.png"), self.transform)
        standing_left = pygame.transform.scale(pygame.image.load("Images\\standing.png"), self.transform)
        standing_right = pygame.transform.scale(pygame.image.load("Images\\standing-right.png"), self.transform)
        self.running_left = [running_1_left, running_2_left, running_1_left, running_2_left, running_1_left, running_2_left, running_1_left, running_2_left]
        self.running_right = [running_1_right, running_2_right, running_1_right, running_2_right, running_1_right, running_2_right, running_1_right, running_2_right]
        self.standing_left = standing_left
        self.standing_right = standing_right
        self.rect = self.standing_left.get_rect()
        self.last_look = 'right'

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_a]:
            self.rect.move_ip(-2, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(2, 0)

    def draw(self, surface):
        global walk_count
        pressed_keys = pygame.key.get_pressed()
        
        if walk_count + 1 >= 60:
                walk_count = 0

        if pressed_keys[K_a]:
            surface.blit(self.running_left[int(walk_count//7.5)], self.rect)
            walk_count += 1
            self.last_look = 'left'
        elif pressed_keys[K_d]:
            surface.blit(self.running_right[int(walk_count//7.5)], self.rect)
            walk_count += 1
            self.last_look = 'right'
        else:
            if self.last_look == 'right':
                surface.blit(self.standing_right, self.rect)
            elif self.last_look == 'left':
                surface.blit(self.standing_left, self.rect)
            walk_count = 0

               
running = True

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

shop_left = TeaShop()
player_left = Player()
floor = Floor()
front_wall = FrontWall()

small = pygame.transform.scale(shop_left.surf, (200, 100))

screen.blit(small, (0, 200))
screen.blit(player_left.standing_left, player_left.rect)

pygame.display.update()

while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    
    screen.fill(BLACK)
    shop_left.draw(screen)
    floor.draw(screen)
    front_wall.draw(screen)
    player_left.update()
    if not floor.rect.colliderect(player_left.rect):
        player_left.rect.move_ip(0, 5)    
    if front_wall.rect.colliderect(player_left.rect):
        player_left.rect.move_ip(-2, 0)
    player_left.draw(screen)

    pygame.display.update()
    FramePerSec.tick(FPS)