import pygame
from pygame.locals import *
from pygame import mixer
import random
import math

# from pygame.event import Event

# Initialize The Pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((1024, 768))  # ((width, height))

# Background 1
background = pygame.image.load('bg_final.gif')
score: int = 0

# Background Sound

mixer.music.load('bg_audio.mp3')
mixer.music.play(-1)
# Title and Icon
pygame.display.set_caption("Liminal City")
icon = pygame.image.load('girl.png')
pygame.display.set_icon(icon)

# Player
Mc_Img = pygame.image.load('MC.png')
playerX = 512
playerY = 650
playerX_change = 0
playerY_change = 0


def rect():
    playerX_change_n = playerX_change + 10
    playerX_change_p = playerX_change - 10
    playerY_change_p = playerY_change + 3
    playerY_change_n = playerY_change + 2


def player(x, y):
    screen.blit(Mc_Img, (x, y))


# Enemy
enemy1_png = []
enemy1_X = []
enemy1_Y = []
enemy1_X_change = []
enemy1_Y_change = []
o = input("Select difficulty level: \n EASY \n MEDIUM \n HARD \n")
num_of_enemies = o
if o == "EASY":
    num_of_enemies = 3
elif o == "MEDIUM":
    num_of_enemies = 6
elif o == "HARD":
    num_of_enemies = 9

for i in range(num_of_enemies):
    # Game Over
    # if enemy1_X[i] <= playerY_change+11:
    #   for j in range(num_of_enemies):

    enemy1_png.append(pygame.image.load('enemy1.png'))
    enemy1_X.append(random.randint(1, 1020))
    enemy1_Y.append(random.randint(20, 750))
    enemy1_X_change.append(4)
    enemy1_Y_change.append(40)


def enemy1(x, y, i):
    screen.blit(enemy1_png[i], (x, y))


# Bullet level 1
# Ready means you cant see the bullet
# Fire means the bullet is currently moving
level1bullet = pygame.image.load('level1bullet.png')
level1bullet_X = 0
level1bullet_Y = 390
level1bullet_X_change = 0
level1bullet_Y_change = 2
level1bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('gtavc_regular.ttf', 36)

textX = 10
textY = 10


def show_score(x, y):
    score = font.render("Score -> " + str(score_value), True, (197, 70, 156))
    screen.blit(score, (x, y))
    return score


def fire_level1bullet(x, y):
    global level1bullet_state
    level1bullet_state = "fire"
    screen.blit(level1bullet, (x + 16, y + 10))


op = 0


# Collision
def isCollision(enemy1_X, enemy1_Y, level1bullet_X, level1bullet_Y):
    distance = math.sqrt((math.pow(enemy1_X - level1bullet_X, 2)) + (math.pow(enemy1_Y - level1bullet_Y, 2)))
    if distance < 27:
        global op
        op += 1
        print(op)
        return True


    else:
        return False


# Level changer
running = True
runner = False

# Game Loop
while running:

    # RGB
    screen.fill((0, 255, 255))
    # Background Image
    screen.blit(background, (0, 0))
    # event: Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystore is pressed check weather is right or left

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1

            if event.key == pygame.K_UP:
                playerY_change = -1
            if event.key == pygame.K_DOWN:
                playerY_change = 1

            if event.key == pygame.K_SPACE:
                if level1bullet_state == "ready":
                    bullet_sound = mixer.Sound('gun1_shoot.wav')
                    bullet_sound.play()
                    level1bullet_X = playerX
                    fire_level1bullet(playerX, level1bullet_Y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or pygame.KSCAN_LEFT:
                print("Keystroke has been released")
                playerX_change = 0
                playerY_change = 0

    # Checking for boundaries of spaceship, so it doesn't go out of bounds
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 959:
        playerX = 959

    # Player movement
    playerY += playerY_change
    if playerY <= 0:
        playerY = 0
    elif playerY >= 600:
        playerY = 690

    # Enemy movement
    for i in range(num_of_enemies):
        enemy1_X[i] += enemy1_X_change[i]
        if enemy1_X[i] <= 0:
            enemy1_X_change[i] = 2
        elif enemy1_X[i] >= 958:
            enemy1_X_change[i] = -1.5

        enemy1_Y[i] += enemy1_Y_change[i]
        if enemy1_Y[i] <= 0:
            enemy1_Y_change[i] = 2
        elif enemy1_Y[i] >= 600:
            enemy1_Y_change[i] = -1.6

        # Collision
        collision = isCollision(enemy1_X[i], enemy1_Y[i], level1bullet_X, level1bullet_Y)
        if collision:
            explosion_sound = mixer.Sound('enemy1_b_collision.wav')
            explosion_sound.play()
            level1bullet_Y = 700
            level1bullet_state = "ready"

            score_value += 1
            enemy1_X[i] = random.randint(1, 479)
            enemy1_Y[i] = random.randint(50, 479)

        enemy1(enemy1_X[i], enemy1_Y[i], i)

    # Bullet level 1 movement
    if level1bullet_Y <= -13:
        level1bullet_Y = playerY
        level1bullet_state = "ready"
    if level1bullet_state == "fire":
        fire_level1bullet(level1bullet_X, level1bullet_Y)
        level1bullet_Y -= level1bullet_Y_change

    if op == 5:
        running = False
        runner = True

    player(playerX, playerY)
    show_score(textX, textY)
    enemy1_X += enemy1_X_change
    pygame.display.update()

############################LEVEL 2##############################

while runner:
    # from pygame.event import Event

    # Initialize The Pygame
    # pygame.init()

    # create the screen
    screen = pygame.display.set_mode((1024, 768))  # ((width, height))

    #####################################################################################################################################

    # Background 1
    background = pygame.image.load('bg2.png')
    score: int = 0

    # Background Sound

    mixer.music.load('bg_audio.mp3')
    mixer.music.play(-1)
    # Title and Icon
    pygame.display.set_caption("Liminal City")
    icon = pygame.image.load('girl.png')
    pygame.display.set_icon(icon)

    # Player
    Mc_Img = pygame.image.load('MC.png')
    playerX = 512
    playerY = 650
    playerX_change = 0
    playerY_change = 0


    def player(x, y):
        screen.blit(Mc_Img, (x, y))


    # Boss
    boss_png = pygame.image.load('boss.png')
    boss_X = random.randint(1, 1020)
    boss_Y = random.randint(20, 750)
    boss_X_change = 4
    boss_Y_change = 40
    # o = input("Select difficulty level: \n EASY \n MEDIUM \n HARD \n")
    num_of_enemies = 9
    # if o == "EASY":
    #    num_of_enemies = 3
    # elif o == "MEDIUM":
    #    num_of_enemies = 6
    # elif o == "HARD":
    #    num_of_enemies = 9
    for i in range(num_of_enemies):
        # Game Over
        # if enemy1_X[i] <= playerY_change+11:
        #   for j in range(num_of_enemies):

        def bossf(x, y, i):
            screen.blit(boss_png, (x, y))

    # Bullet level 1
    # Ready means you cant see the bullet
    # Fire means the bullet is currently moving
    bomb1 = pygame.image.load('bomb.png')
    bomb1_X = 0
    bomb1_Y = 390
    bomb1_X_change = 0
    bomb_Y_change = 7
    bomb1_state = "ready"

    # Score
    score_value = 0
    font = pygame.font.Font('gtavc_regular.ttf', 36)

    textX = 10
    textY = 10


    def show_score(x, y):
        score = font.render("Score -> " + str(score_value), True, (197, 70, 156))
        screen.blit(score, (x, y))


    def fire_bomb(x, y):
        global bomb1_state
        bomb1_state = "fire"
        screen.blit(bomb1, (x + 16, y + 10))


    # Collision
    def isCollision(boss_X, boss_Y, bomb1_X, bomb1_Y):
        distance = math.sqrt((math.pow(boss_X - bomb1_X, 2)) + (math.pow(boss_Y - bomb1_Y, 2)))
        if distance < 150:
            return True


        else:
            return False


    # Game Loop
    # runner = True
    while runner:

        # RGB
        screen.fill((0, 255, 255))
        # Background Image
        screen.blit(background, (0, 0))
        # event: Event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runner = False

            # If keystore is pressed check weather is right or left

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    playerX_change = -4
                if event.key == pygame.K_RIGHT:
                    playerX_change = 4

                if event.key == pygame.K_UP:
                    playerY_change = -1
                if event.key == pygame.K_DOWN:
                    playerY_change = 1

                if event.key == pygame.K_SPACE:
                    if bomb1_state == "ready":
                        bullet_sound = mixer.Sound('gun1_shoot.wav')
                        bullet_sound.play()
                        bomb1_X = playerX
                        fire_bomb(playerX, bomb1_Y)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or pygame.KSCAN_LEFT:
                    print("Keystroke has been released")
                    playerX_change = 0
                    playerY_change = 0

        # Checking for boundaries of spaceship, so it doesn't go out of bounds
        playerX += playerX_change
        if playerX <= 0:
            playerX = 0
        elif playerX >= 959:
            playerX = 959

        # Player movement
        playerY += playerY_change
        if playerY <= 0:
            playerY = 0
        elif playerY >= 600:
            playerY = 690

        # Enemy movement

        boss_X += boss_X_change
        if boss_X <= -20:
            boss_X_change = 2
        elif boss_X >= 800:
            boss_X_change = -1.5

        boss_Y += boss_Y_change
        if boss_Y <= 0:
            boss_Y_change = 2
        elif boss_Y >= 400:
            boss_Y_change = -1.6

        # Collision
        collision = isCollision(boss_X, boss_Y, bomb1_X, bomb1_Y)
        if collision:
            explosion_sound = mixer.Sound('enemy1_b_collision.wav')
            explosion_sound.play()
            bomb1_Y = 700
            bomb1_state = "ready"

            score_value += 1
            boss_X = random.randint(1, 479)
            boss_Y = random.randint(50, 479)

        bossf(boss_X, boss_Y, i)

        # Bomb movement
        if bomb1_Y <= 0:
            bomb1_Y = playerY
            bomb1_state = "ready"
        if bomb1_state == "fire":
            fire_bomb(bomb1_X, bomb1_Y)
            bomb1_Y -= bomb_Y_change
        player(playerX, playerY)
        show_score(textX, textY)
        boss_X += boss_X_change
        pygame.display.update()
pygame.quit()

quit()
