import pygame, sys
from copy import deepcopy
from gui.figuras import Tablero, Ficha
from algoritmos import entrenar_nuevo_agente, minimax, minimax_alfa_beta

def iniciar_grafica():

    pygame.init()
    tablero = Tablero()

    WIDTH = HEIGHT = 560
    pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Juego Othello")
    time = pygame.time.Clock() 

    font1 = pygame.font.SysFont("notomono", 15, True)
    text_font = font1.render("Comenzar juego", True, "#FFFFFF") 

    font2 = pygame.font.SysFont("notomono", 22, True)
    text_agente = font2.render("Elegir oponente", True, "#FFFFFF")
    text_rl = font2.render("ENTRENANDO....", True, "#FFFFFF")

    background = pygame.image.load("gui/imagen.jpg").convert()
    rect = pygame.Rect((30,50), (160,50)) 

    btn1 = pygame.Rect((200,70), (160,50)) 
    text_btn1 = font1.render("VS Minimax", True, "#FFFFFF") 
    btn2 = pygame.Rect((155,150), (250,50))
    text_btn2 = font1.render("VS Minimax con Poda", True, "#FFFFFF")
    btn3 = pygame.Rect((200,230), (160,50))
    text_btn3 = font1.render("VS RL", True, "#FFFFFF")

    menu_main = True 
    menu_eleccion_agente = False
    juego = False
    agente = None
    entrenar_rl = False 

    algoritmo_minimax = False
    algoritmo_minimax_poda = False
    algoritmo_rl = False 
    final_juego = False

    while True:

        time.tick(90)

        decision = tablero.calcular_resultado()
        if decision != 0:
            menu_main = False
            juego = False 
            menu_eleccion_agente = False
            final_juego = True


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 

            if event.type == pygame.MOUSEBUTTONDOWN and not menu_main and not menu_eleccion_agente and not entrenar_rl and not final_juego:        
                x, y = pygame.mouse.get_pos()
                row = y // 70
                col = x // 70 
                if tablero.validarMovimientos(row, col, -1):
                    tablero.matriz[row][col] = Ficha(row, col, -1)
                    tablero.voltearFichas(row, col, -1) 
                    if algoritmo_minimax:
                        movimiento = minimax(tablero, 4, 1)
                        if movimiento:
                            x, y = movimiento
                            tablero.matriz[x][y] = Ficha(x, y, 1)
                            tablero.voltearFichas(x, y, 1)
                    elif algoritmo_minimax_poda:
                        movimiento = minimax_alfa_beta(tablero, 4, 1)
                        if movimiento:
                            x, y = movimiento
                            tablero.matriz[x][y] = Ficha(x, y, 1)
                            tablero.voltearFichas(x, y, 1)
                    elif algoritmo_rl:
                        tablero = agente.siguiente_jugada(tablero, 1) 
                else:
                    print("Invalido")
    
        pos = pygame.mouse.get_pos() 

        if menu_main: 
            pantalla.blit(background, (0,0))
            if rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]:
                    pygame.draw.rect(pantalla, "#191970", rect, border_radius=12)
                    menu_main = False
                    menu_eleccion_agente = True  
                else:
                    pygame.draw.rect(pantalla, "#191970", rect, border_radius=12)
            else:
                pygame.draw.rect(pantalla, "#008000", rect, border_radius=12)

            pantalla.blit(text_font, (30 + int((160 -text_font.get_width()) / 2),50+(int((50-text_font.get_height())) / 2)))
        elif menu_eleccion_agente:
            pantalla.fill("#008000")
            pantalla.blit(text_agente, (int((560 - text_agente.get_width()) / 2),30)) 

            if btn1.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]:
                    menu_eleccion_agente = False
                    juego = True
                    algoritmo_minimax = True
                else:
                    pygame.draw.rect(pantalla, "#000000", btn1, border_radius=12) 
            else:
                pygame.draw.rect(pantalla, "#191970", btn1, border_radius=12) 

            if btn2.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]:
                    menu_eleccion_agente = False
                    juego = True
                    algoritmo_minimax_poda = True 
                else:
                    pygame.draw.rect(pantalla, "#000000", btn2, border_radius=12)
            else:
                pygame.draw.rect(pantalla, "#191970", btn2, border_radius=12)

            if btn3.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]:
                    menu_eleccion_agente = False
                    entrenar_rl = True
                else:
                    pygame.draw.rect(pantalla, "#000000", btn3, border_radius=12)
            else:
                pygame.draw.rect(pantalla, "#191970", btn3, border_radius=12)

            pantalla.blit(text_btn1, (200 + int((160 -text_btn1.get_width()) / 2),70+(int((50-text_btn1.get_height())) / 2)))
            pantalla.blit(text_btn2, (200 + int((160 -text_btn2.get_width()) / 2),150+(int((50-text_btn2.get_height())) / 2)))
            pantalla.blit(text_btn3, (200 + int((160 -text_btn3.get_width()) / 2),230+(int((50-text_btn3.get_height())) / 2)))

        elif juego:
            pantalla.fill("#800000")
            tablero.pintarTablero(pantalla)
            tablero.colocarFichas(pantalla) 

        elif entrenar_rl:
            pantalla.fill("#808080")
            pantalla.blit(text_rl, (int((560 -text_rl.get_width()) / 2),int((560-text_rl.get_height()) / 2)))
            pygame.display.update()
            agente = entrenar_nuevo_agente()
            entrenar_rl = False 
            juego = True
            algoritmo_rl = True

        elif final_juego:
            pantalla.fill("#800000")
            text_blancas = "N° de fichas blancas: " + str(len(tablero.contarFichas(1)))
            text_negras = "N° de fichas negras: "  + str(len(tablero.contarFichas(-1))) 

            text_ficha_negra= font2.render(text_negras, True, "#FFFFFF")
            text_ficha_blanca = font2.render(text_blancas, True, "#FFFFFF")
            if decision == -1:
                text_ganador = font2.render("¡Ganaste!", True, "#FFFFFF")
            elif decision == 1:
                text_ganador = font2.render("¡Perdiste!", True, "#FFFFFF")
            else:
    
                text_ganador = font2.render("¡Empate!", True, "#FFFFFF")

            pantalla.blit(text_ganador, (int((560 -text_ganador.get_width()) / 2), 170)) 
            pantalla.blit(text_ficha_negra, (int((560 -text_ficha_negra.get_width()) / 2), 60))
            pantalla.blit(text_ficha_blanca, (int((560 -text_ficha_blanca.get_width()) / 2), 110)) 

        pygame.display.update()