import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('Игра Тир')
icon = pygame.image.load('img/images.jpg')
pygame.display.set_icon(icon)

target_img = pygame.image.load('img/target.png')
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

score = 0


def check_hit(mouse_x, mouse_y):
    global target_x, target_y, score
    if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_width:
        score += 10
        target_x = random.randint(0, SCREEN_WIDTH - target_width)
        target_y = random.randint(0, SCREEN_HEIGHT - target_height)


font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_hit(mouse_x, mouse_y)

    screen.blit(target_img, (target_x, target_y))
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.update()

pygame.quit()
