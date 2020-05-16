import pygame

screen_width = 800
screen_height = 600

back_color = (200,200,200)
light_gray = pygame.Color('grey12')



pygame.init()

clock = pygame.timeClock() #Reloj de FPS

screen = pygame.display.set_mode((screen_width,screen_height))

def mover_rectangulo():
    global speed

    if rectangulo.top + 50 < screen_height:
        rectangulo.top += speed

rectangulo = pygame.Rect (10,10,50,50)


while True:
    screen.fill(back_color)

    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            speed = -3
            if event.key == pygame.K_UP:
                speed = 3
            elif event.key == pygame.K_DOWN:
                speed = 3



    pygame.draw.rect(screen, white_color, rectangulo)
    pygame.draw.ellipse(screen,white_color,)
    pygame.display.flip()
    clock.tick(60) #ejecutar máximo a 60FPS

