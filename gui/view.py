import pygame, sys

pygame.init()

WIDTH = HEIGHT = 560
pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Juego Othello")
time = pygame.time.Clock() 


font = pygame.font.SysFont("notomono", 15, True)
text_font = font.render("Comenzar juego", True, "#FFFFFF")

background = pygame.image.load("principal.jpg").convert() 
rect = pygame.Rect((30,50), (160,50)) 

menu_main = True 
juego = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    pos = pygame.mouse.get_pos() 

    if menu_main: 
        pantalla.blit(background, (0,0))
        if rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(pantalla, "#191970", rect, border_radius=12)
                menu_main = False 
                juego = True
            else:
                pygame.draw.rect(pantalla, "#191970", rect, border_radius=12)
        else:
            pygame.draw.rect(pantalla, "#008000", rect, border_radius=12)

        pantalla.blit(text_font, (30 + int((160 -text_font.get_width()) / 2),50+(int((50-text_font.get_height())) / 2)))
    elif juego:
        pantalla.fill("#008000")
        pygame.draw.circle(pantalla, "#FFFFFF", (175,35), 30)
        x_pos = 0
        y_pos = 0
        while y_pos < 560:          
            pygame.draw.rect(pantalla, "#000000", [x_pos,y_pos,70,70], 1)
            x_pos += 70
            if x_pos == 560:
                x_pos = 0
                y_pos += 70
    time.tick(40)
    pygame.display.update()

