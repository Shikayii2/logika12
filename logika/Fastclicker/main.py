import pygame  
import time  
from random import randint
pygame.init()  


width = 500
height = 500


screen = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("Fast Clicker") 

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
    
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)



class Label(Area):  
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
      
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):

        self.fill()  
        self.outline((0,0,0),5)
        screen.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))  
    def drawtext(self, shift_x=0, shift_y=0):

        self.fill()  
       
        screen.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

yellow = (255, 255, 0) 
black = (0,0,0)


cards = []
num_cards = 4  
x = 70 

for i in range(num_cards):
    new_card = Label(x, 170, 70, 100, yellow)  
    
    new_card.set_text('click', 26) 
    cards.append(new_card) 
    x = x + 100  


wait = 0
points = 0

time_text = Label(0, 0, 50, 50, background_color) #створення прямокутника
#в якому буде розміщуватись текст
time_text.set_text("Час:", 30, (0,0,100)) #створення тексту з певним розміром 
#та кольором
time_text.drawtext(20, 0) #намалювати текст в межах прямокутника 
#(з певними відступами всередині)


timer = Label(10, 40, 50, 50, background_color) #створення прямокутника
#в якому буде розміщуватись текст
timer.set_text("0", 30, (0,0,100)) #створення тексту з певним розміром 
#та кольором
timer.drawtext(20, 20) #намалювати текст в межах прямокутника 
#(з певними відступами всередині)

score = Label(400, 0, 50, 50, background_color) #створення прямокутника
#в якому буде розміщуватись текст
score.set_text("Бали:", 30, (0,0,100)) #створення тексту з певним розміром 
#та кольором
score.drawtext(20, 0) #намалювати текст в межах прямокутника 
#(з певними відступами всередині)


score1 = Label(420, 40, 50, 50, background_color) #створення прямокутника
#в якому буде розміщуватись текст
score1.set_text("0", 30, (0,0,100)) #створення тексту з певним розміром 
#та кольором
score1.drawtext(20, 20) #намалювати текст в межах прямокутника 
#(з певними відступами всередині)


startgame = time.time()
cur_time = startgame







while True:
    if wait == 0:
        wait = 24
        click = randint(1,num_cards)
    for i in range(num_cards):
        cards[i].color(yellow)
        if (i + 1) == click:
            cards[i].draw(10, 30)
        else:
            cards[i].fill()
    else:
        wait = wait - 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x,y = event.pos
            for i in range(num_cards):
                if cards[i].collidepoint(x,y):
                    if i + 1 == click:
                        cards[i].color((0,100,0))
                        points = points + 1
                    else:
                        cards[i].color((139,0,0))
                        points = points  - 1
                    cards[i].draw(10, 40)
                    score1.set_text(str(points),30,(0,0,100))
                    
                    score1.drawtext(0,0)
    newtime = time.time()
    if newtime - startgame >= 11:
        win = Label (0,0,500,500,(255,0,0))
        win.set_text("Час вичерпано",60,(76,0,238))
        win.draw(110,180)
        
    if int(newtime) - int(cur_time) == 1:
        timer.set_text(str(int(newtime - startgame)),40,(254, 0, 238))
        timer.draw(0,0)
        cur_time = newtime
        pygame.display.update()

    if points >= 5:
        win =Label(0,0,500,500,(2,78,11))
        win.set_text("Ти переміг",60,(76,0,238))
        win.drawtext(140,180)
        result_time = Label(90,230,250,250,(2,78,11))
        result_time.set_text("Час проходження: " + str(int(newtime-startgame))+" секунд", 40, (76, 0, 238))
        result_time.drawtext(0,0)
        
    pygame.display.update()  
    clock.tick(40)  
