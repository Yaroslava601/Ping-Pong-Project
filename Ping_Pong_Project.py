#Ping Pong Project

from pygame import *
mixer.init()
font.init()

#background
win_x = 900
win_y = 700
window = display.set_mode((win_x, win_y))
display.set_caption('PING PONG')
background = transform.scale(image.load('sky.jpg'), (win_x, win_y))

#music

#main classes

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__(player_image, player_x, player_y, player_speed, size_x, size_y)
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 15:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_y - 275:
            self.rect.y += self.speed
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 15:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_y - 275:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__(player_image, player_x, player_y, player_speed, size_x, size_y)
    def update(self):
        global speed_x
        global speed_y
        self.rect.x += speed_x
        self.rect.y += speed_y
        if self.rect.y > win_y - 100 or self.rect.y < 0:
            speed_y *= -1

#SPRITES

ball = Ball('ball.png', 300, 200, 0, 100, 100)

platform_1 = Player('platform1.png', 40, 100, 3, 100, 250)
platform_2 = Player('platform2.png', 750, 250, 3, 100, 250)

#END

speed_x = 2
speed_y = 2
FPS = 60
game = True
finish = False
keys_pressed = key.get_pressed()
clock = time.Clock()
font1 = font.SysFont('Calibri', 70)
lose1 = font1.render(
    'PLAYER 1 LOSE!', True, (180, 0, 0))
lose2 = font1.render(
    'PLAYER 2 LOSE!', True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0, 0))
        clock.tick(FPS)
        platform_1.reset()
        platform_2.reset()
        platform_1.update_r()
        platform_2.update_l()
        ball.reset()
        ball.update()
        if sprite.collide_rect(platform_1, ball) or sprite.collide_rect(platform_2, ball):
                speed_x *= -1
        if ball.rect.x < -110:
            finish = True
            window.blit(lose1, (270, 270))
        if ball.rect.x > win_x:
            finish = True
            window.blit(lose2, (270, 270))
    
    display.update()