import pygame as pg
import time
import random

pg.init()
pg.mixer.init()

pg.mixer.music.load('sounds/background.wav')
pg.mixer.music.set_volume(0.1)
pg.mixer.music.play(-1)


W = 400
H = 600

screen = pg.display.set_mode((W, H))

clock = pg.time.Clock()
FPS = 60

pg.display.set_caption("Racer!")

bg_img = pg.image.load("graphs/AnimatedStreet.png")
player_img = pg.image.load("graphs/Player.png")
enemy_img = pg.image.load("graphs/Enemy.png")
coin_img = pg.transform.scale(pg.image.load("graphs/coin.png"), (30, 30))

bgy = 0

sound_crash = pg.mixer.Sound('sounds/crash.wav')

font = pg.font.SysFont("Verdana", 60)
game_over = font.render("Game Over", True, "black")
game_over_rect = game_over.get_rect(center = (W // 2, H // 2))

def drawtext(score):
    score_text = font.render(f"Score: {score}", True, "WHITE")
    screen.blit(score_text, (10, 10))

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = W // 2
        self.rect.bottom = H
        self.speed = 5

    def move(self):
        key = pg.key.get_pressed()
        
        if key[pg.K_d]:
            self.rect.move_ip(self.speed, 0)
        if key[pg.K_a]:
            self.rect.move_ip(-self.speed, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > W:
            self.rect.right = W

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.speed = 10
    
    def gen_rect(self):
        self.rect.left = random.randint(0, W - self.rect.w)
        self.rect.bottom = 0
    
    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > H:
            self.gen_rect()