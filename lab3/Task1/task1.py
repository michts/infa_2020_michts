# C:\Users\Michael\infa_2020_michts\lab3\Task1
import pygame
from  pygame.draw import *
pygame.init()
Light_BLUE = (88, 239, 220)   
FPS = 30
path='/Python/My_puple_programs/'
import os
#game_folder = os.path.dirname(path)
#img_folder = os.path.join(game_folder, 'Task1')
screen = pygame.display.set_mode((600, 400))
print(os.getcwd())
#print(game_folder)
#print(img_folder)
beach=((251,247,77),(0,280,600,120))
sea=((0,0,255),(0,190,600,90))
sky=(Light_BLUE,(0,0,600,190))
#screen.fill(Light_BLUE)  
rect(screen, beach[0],beach[1])
rect(screen, sea[0],sea[1])
rect(screen, sky[0],sky[1])

F_Name=('grib.gif','ship.gif','cloud.gif','Sun1.gif')
def All_operations(File_name,x,y):
    """
    Загружает спрайт, настраивает прозрачность пикселей
    выделяет под него rect,выгружает rect,
    перемещает в нужное место, заполняет изображением
    """
    I_Name = pygame.image.load(File_name)
    I_Name.set_colorkey((255,255,255))
    I_rect = I_Name.get_rect()
    I_rect.move(0,0)
    I_rect.center=(x,y)
    screen.blit(I_Name,I_rect)


All_operations(F_Name[0],90,300)
All_operations(F_Name[1],400,180)
All_operations(F_Name[2],100,50)
All_operations(F_Name[3],500,50)
    


clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    
    pygame.display.update()# повторять после изменений
     
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
