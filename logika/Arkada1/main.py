import pygame  
import time  
from random import randint
pygame.init()  


width = 500
height = 500


screen = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("arcanoid") 

clock = pygame.time.Clock()  


background_color = (200, 255, 255)  
screen.fill(background_color)  
pygame.display.update()  


class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)  
        self.fill_color = color  

    def fill(self):
        pygame.draw.rect(screen, self.fill_color, self.rect) 

    def color(self,new_color):
        self.fill_color = new_color
    def outline(self,frame_color,thickness):
        pygame.draw.rect(screen,frame_color,self.rect,thickness)
    
    def collidepoint(self,rect):
        return self.rect.colliderect(rect)
    
class Picture(Area):
    def __init__(self,filename,x,y,width,height):
        Area.__init__(self,x = x ,y = y,width=width,height=height,color = None)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image,(width,height))






    def draw(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))






class Label(Area):
    def set_text(self,text,fsize,text_color):
        self.mytext = pygame.font.SysFont("verdana",fsize).render(text,True,text_color)

    def draw(self,shift_x,shift_y):
        self.fill()
        screen.blit(self.mytext,(self.rect.x + shift_x ,self.rect.y + shift_y))








ball = Picture("ball_1.png",210,400,50,50)
platform = Picture("platformT1.png",180,450,100,30)
platform_x = 200
platform_y = 310

move_right = False
move_left = False





game_over = False

start_x = 5
start_y = 5
count = 9
monsters = []

for j in  range(3):
    y = start_y + (55 * j)
    x = start_x + (28 * j)
    for i in range(count):
        d = Picture("enemy.png",x,y,50,50)
        monsters.append(d)
        x = x + 55
    count -= 1



dx = 5
dy = 5









while not game_over:
    screen.fill(background_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_right = True
            if event.key == pygame.K_LEFT:
                move_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                move_right = False
            if event.key == pygame.K_LEFT:
                move_left = False
    if move_right:
        platform.rect.x += 5

    if move_left:
        platform.rect.x -= 5

    ball.rect.x += dx
    ball.rect.y += dy

    if ball.rect.y < 0:
        dy *= -1
    if ball.rect.y > 420 or ball.rect.y < 0:
        dx *= -1
    if ball.rect.colliderect(platform.rect):
        dy *= -1
    if ball.rect.y > 500:
        win_text = Label(150,150,50,50,background_color)
        win_text.set_text("YOU LOSE",60,(255,0,0))
        win_text.draw(10,10)
    if len(monsters) == 0:
        win_text = Label(150,150,50,50,background_color)
        win_text.set_text("YOU WINNNNNNN",60,(255,0,0))
        win_text.draw(10,10)


    ball.draw()
    platform.draw()
    for m in monsters:
        m.draw()
        if m.rect.colliderect(ball.rect):
            monsters.remove(m)
            
            dy *= -1


    pygame.display.update()
    clock.tick(40)













