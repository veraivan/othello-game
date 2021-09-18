import pygame, sys, os 
from copy import deepcopy
from figuras import Tablero, Ficha

tablero_pesos = [
    [100, -10, 11, 6, 6, 11, -10, 100],
    [-10, -20, 1, 2, 2, 1, -20, -10],
    [10, 1, 5, 4, 4, 5, 1, 10],
    [6, 2, 4, 2, 2, 4, 2, 6],
    [6, 2, 4, 2, 2, 4, 2, 6],
    [10, 1, 5, 4, 4, 5, 1, 10],
    [-10, -20, 1, 2, 2, 1, -20, -10],
    [100, -10, 11, 6, 6, 11, -10, 100]
]


def funcion_evaluacion(tablero, color):
    oponente = -color 
    total = 0 

    coordenadas_jugador = tablero.contarFichas(color) 
    for pos in coordenadas_jugador:
        total += tablero_pesos[pos[0]][pos[1]] 
    
    coordenadas_op = tablero.contarFichas(oponente) 
    for pos in coordenadas_op:
        total -= tablero_pesos[pos[0]][pos[1]]

    return total


def min_valor(estado):

    if estado.finDeJuego():
        return (funcion_evaluacion(estado,1), None)
    
    mejor_utilidad = sys.maxsize 
    mejor_movimiento = None 
    
    for move in estado.movimientosPosibles(1):
        nuevo_estado = deepcopy(estado)
        nuevo_estado.voltearFichas(move[0],move[1],1)
        tupla = max_valor(nuevo_estado)
        if tupla[0] < mejor_utilidad:
            mejor_utilidad = tupla[0]
            mejor_movimiento = move
    return (mejor_utilidad, mejor_movimiento)


def max_valor(estado):
    if estado.finDeJuego():
        return (funcion_evaluacion(estado,-1),None)

    mejor_utilidad = -sys.maxsize
    mejor_movimiento = None 
    
    for move in estado.movimientosPosibles(-1):
        nuevo_estado = deepcopy(estado)
        nuevo_estado.voltearFichas(move[0],move[1],-1)
        tupla = min_valor(nuevo_estado)
        if tupla[0] > mejor_utilidad:
            mejor_utilidad = tupla[0]
            mejor_movimiento = move
    return (mejor_utilidad, mejor_movimiento)


def minimax(estado):
    mejor_movimiento = max_valor(estado)[1]
    return mejor_movimiento


tablero = Tablero()
print(minimax(tablero))

"""
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

    time.tick(90)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 

        if event.type == pygame.MOUSEBUTTONDOWN and not menu_main:
            x, y = pygame.mouse.get_pos()
            row = y // 70
            col = x // 70 
            if tablero.validarMovimientosJugador(row,col,1):
                tablero.matriz[row][col] = Ficha(row,col,1)
                tablero.voltearFichas(row,col,1)
            else:
                print("Invalido")
 
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
        tablero.pintarTablero(pantalla)
        tablero.colocarFichas(pantalla)
        
    
    pygame.display.update()

"""
