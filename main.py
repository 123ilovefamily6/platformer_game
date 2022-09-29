import pygame
import random
pygame.init()
windowwidth = 750
windowheight = 750
win = pygame.display.set_mode((windowwidth, windowheight))
blue = (0, 0, 255)
cyan = (0, 255, 255)
yellow = (255, 255, 0)
green = (0, 228, 0)
bg_color = cyan
white = (255, 255, 255)
black = (0, 0, 0)
r = 0
class Player:
    def __init__(self):
        global r
        self.y = 700
        self.x = 0
        self.height = 50
        self.width = 50
        self.velx = 0
        self.vely = 0
        self.gravity = 1
        self.jumping = False
        if r == 0:
            self.image = pygame.transform.scale(pygame.image.load("art/guy.png"), (self.height, self.width))
        if r >= 1:
            self.image = pygame.transform.scale(pygame.image.load("art/pixil-frame-1.png"), (self.height, self.width))
        self.jumppower = 25
        self.rect = pygame.Rect(self.x,self.y, self.width, self.height)
        self.xp = 0
        self.coins = 0
    def tick(self):
        global r
        if keys[pygame.K_LEFT]:
            if self.velx >= 0:
                self.velx = -1
            self.velx -= 0.1
        if keys[pygame.K_RIGHT]:
            if self.velx <= 0:
                self.velx = 1
            self.velx += 0.1
            r += 1
            print(r)
        self.x += self.velx
        if keys[pygame.K_UP] and self.jumping == False and self.y >= windowheight - self.height:
            self.vely = -self.jumppower
            self.jumping = True

        for platform in platformlist:
            if self.rect.colliderect(platform.rect) == True:
                if keys[pygame.K_UP] and self.jumping == False:
                    self.vely = -self.jumppower
                    self.jumping = True
                #print (self.y, platform.y + platform.height, self.vely)
                if self.y > platform.y - self.height and self.vely > 0:
                    self.y = platform.y - self.height
                    self.vely = 0
                    self.jumping = False

                if self.y < platform.y + platform.height and self.vely < 0 and self.y > platform.y+10:
                    self.y = platform.y + platform.height

        self.vely += self.gravity
        self.y += self.vely
        if self.x > windowwidth - self.width:
            self.x = windowwidth - self.width
        if self.x < 0:
            self.x = 0
        if self.y > windowheight - self.height:
            self.y = windowheight - self.height
            self.vely = 0
            self.jumping = False
        if self.y < 0:
            self.y = 0

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        win.blit(self.image,(self.x,self.y))
class pickup:
    def __init__(self):
        self.y = 700
        self.x = 0
        self.height = 70
        self.width = 70
        self.image = pygame.transform.scale(pygame.image.load("Art/Pumkin.png"),(self.height,self.width))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def tick(self):
        if self.rect.colliderect(player.rect) == True:
            player.coins += 1
            print("Pumkin "+str(player.coins-1))
            overlaping = True
            while overlaping == True:
                self.x = random.randint(0, windowwidth - coin.width)
                self.y = random.randint(windowheight // 2 - self.height // 2, windowheight - coin.height)
                self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
                if self.rect.colliderect(player.rect) == False:
                    overlaping = False
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        win.blit(self.image,(self.x, self.y))
class platform:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    def tick(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(win, green, self.rect)

win.fill(bg_color)
player = Player()
coin = pickup()
platform1 = platform(300, 475, 350, 50)
platform2 = platform(50, 475, 89, 30)
platform3 = platform(215, 300, 30, 450)
platformlist = [platform1, platform2, platform3]
pygame.display.set_caption("Python Platformer")
run = True
while run:
    pygame.time.delay(25)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    win.fill(cyan)
    player.tick()
    coin.tick()
    for platform in platformlist:
        platform.tick()
    pygame.display.update()