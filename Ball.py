# Warning! 
# This program requires the Pygame package installed
# 
import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
loop = False
x = 500
y = 500
xp = 200
yp = 200
points = 0
clock = pygame.time.Clock()
th = 0
loopt = 0


font = pygame.font.SysFont("comicsansms", 72)
text = font.render("Your points: " + str(points), True, (0, 255, 0))



while not loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 1
    if pressed[pygame.K_DOWN]: y += 1
    if pressed[pygame.K_LEFT]: x -= 1
    if pressed[pygame.K_RIGHT]: x += 1
    while loopt != 1000:
           pygame.draw.rect(screen, (20, th, 100), pygame.Rect(0, loopt, 1000, 100))
           th += 10
           loopt += 50
           if loopt == 1000:
               pygame.draw.circle(screen, (255, 255, 0), (500, 1000), 400)
               pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, 0, 1000, 50))
    text = font.render("Your points: " + str(points), True, (0, 255, 0))
    text2 = font.render("Score: " + str(points), True, (255, 0, 0))
    screen.blit(text2, (550 - text.get_width() // 2, 25- text.get_height() // 2))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 20)
    pygame.draw.circle(screen, (0, 0, 255), (xp, yp), 10)
    th = 0
    loopt = 0
    if x > xp - 15:
        if x < xp + 15:
            if y < yp + 15:
                if y > yp - 15:
                    points = points + 1
                    print(points)
                    xp = random.randint(100, 900)
                    yp = random.randint(100, 900)

    if x < xp + 15:
        if x > xp - 15:
            if y > yp - 15:
                if y < yp + 15:
                    points = points + 1
                    print(points)
                    xp = random.randint(100, 900)
                    yp = random.randint(100, 900)
    if x < xp + 15:
        if x > xp - 15:
            if y < yp + 15:
                if y > yp - 15:
                    points = points + 1
                    print(points)
                    xp = random.randint(100, 900)
                    yp = random.randint(100, 900)
    if x > xp - 15:
        if x < xp + 15:
            if y > yp - 15:
                if y < yp + 15:
                    points = points + 1
                    print(points)
                    xp = random.randint(100, 900)
                    yp = random.randint(100, 900)
    if y < 50:
        print("Your score " + str(points))
        screen.fill((0, 0, 255))
        screen.blit(text,(500 - text.get_width() // 2, 500 - text.get_height() // 2))
