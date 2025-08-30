import pygame
import random


pygame.init()
width ,height = 400,400
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Лови блоки!")


white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)

platform_width = 80

platform_height = 10

platform_x = width // 2 - platform_width // 2
platform_y = height - 20 



platform_speed = 10




block_size = 20
block_x = random.randint(0,width - block_size)
block_y = 0
block_speed = 5

running = True 
clock = pygame.time.Clock()
score = 0


while running:
    screen.fill(black)
    pygame.draw.rect(screen,blue,(platform_x,platform_y,platform_width,platform_height))
    pygame.draw.rect(screen,red, (block_x,block_y,block_size,block_size))
    block_y += block_speed

    if block_y > height:
        blox_x = random.randint(0,width - block_size)
        block_y = 0
        score -= 1
    if (platform_x < block_size + block_x  and platform_x + platform_width > block_x and platform_y < block_y + block_size):
        blox_x = random.randint(0,width - block_size)
        block_y = 0    
        score += 1

    font = pygame.font.SysFont("Verdana",30)   
    score_text = font.render(f"Рахунок {score}",True,white)
    screen.blit(score_text,(10,10))





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and platform_x > 0:
        platform_x -= platform_speed

    if keys[pygame.K_d] and platform_x < width - platform_width:
        platform_x += platform_speed













    pygame.display.update()
    clock.tick(40)












