import pygame
import random
import time
pygame.init()

velx=0
vely=0
snakelist=[]
snakelen=1
display_width=720
display_height=720
display=pygame.display.set_mode((display_width,display_height))

x=10;y=10

width=25
height=25
apple_width=25
apple_height=25
gamedelay=30

applex=round(random.randrange(0,display_width-apple_width)/10)*10
appley=round(random.randrange(0,display_height-apple_height)/10)*10
gameover=False
font=pygame.font.SysFont(None,25)
clock=pygame.time.Clock()

def snake(width,snakelist):
    for xny in snakelist:
        pygame.draw.rect(display,(0,255,0) ,(xny[0],xny[1],width,width))


# def message(msg,color):
#     screen_text=font.render(msg,True,color)
#     display.blit(screen_text,[15,15])

while not gameover:
    pygame.time.delay(gamedelay)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameover=True
    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        velx=-10 
        vely=0

    if keys[pygame.K_RIGHT]:
        velx=10
        vely=0

    if keys[pygame.K_UP]:
        vely=-10
        velx=0

    if keys[pygame.K_DOWN]:
        vely=10
        velx=0
    if x>=display_width or x<0  or y>=display_height or y<0:
        gameover=True
    if x == applex and y ==appley or x == applex+10 and y ==appley+10 or x == applex-10 and y ==appley-10:
        
        applex=round(random.randrange(0,display_width-apple_width)/10)*10
        appley=round(random.randrange(0,display_height-apple_height)/10)*10
        snakelen=snakelen+10
    # if snakelen>=10:
    #     gamedelay=20
    # if snakelen>=20:
    #     gamedelay=10
    display.fill((0,0,0))
    pygame.draw.rect(display,(255,255,255),(applex+5,appley+5,10,10))

    snakehead=[]
    snakehead.append(x)
    snakehead.append(y)
    snakelist.append(snakehead)
    if len(snakelist) > snakelen:
        del  snakelist[0]
    if snakehead in snakelist[:-1]:
        gameover=True
    snake(width,snakelist)
    x=x+velx
    y=y+vely
    screen_text=font.render(f"Score {snakelen}",True,(255,255,255))
    display.blit(screen_text,[15,15])

    pygame.display.update()
    # clock.tick(100)
pygame.display.update()
pygame.quit()
quit()

