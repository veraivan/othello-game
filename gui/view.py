import pygame, sys, os 
from copy import deepcopy
from gui.figuras import Tablero, Ficha
from minimax import entrenar_nuevo_agente



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


N_LIMIT = 6

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


def min_valor(estado, N, jugador, poda=False, alfa=0, beta=0):
    contrario = -jugador

    if N == N_LIMIT:
        return funcion_evaluacion(estado, contrario), None
    
    lista_movimientos = estado.movimientosPosibles(jugador)

    if not lista_movimientos:
        return funcion_evaluacion(estado, jugador), None

    mejor_utilidad = sys.maxsize
    mejor_movimiento = None

    for move in lista_movimientos:
        nuevo_estado = deepcopy(estado)
        nuevo_estado.matriz[move[0]][move[1]] = Ficha(move[0], move[0], jugador)
        nuevo_estado.voltearFichas(move[0], move[1], jugador)
        if poda:
            tupla = max_valor(nuevo_estado, N+1, contrario, True, alfa, beta)
        else:
            tupla = max_valor(nuevo_estado, N+1, contrario)
        if tupla[0] < mejor_utilidad:
            mejor_utilidad = tupla[0]
            mejor_movimiento = move
            if poda:
                if mejor_utilidad <= alfa:
                    return mejor_utilidad, move
                beta = min(beta, mejor_utilidad)
    return mejor_utilidad, mejor_movimiento


def max_valor(estado, N, jugador, poda=False, alfa=0, beta=0):

    contrario = -jugador

    if N == N_LIMIT:
        return funcion_evaluacion(estado, contrario), None

    lista_movimientos = estado.movimientosPosibles(jugador)

    if not lista_movimientos:
        return funcion_evaluacion(estado, jugador), None

    mejor_utilidad = -sys.maxsize
    mejor_movimiento = None
    
    for move in lista_movimientos:
        nuevo_estado = deepcopy(estado)
        nuevo_estado.matriz[move[0]][move[1]] = Ficha(move[0], move[0], jugador)
        nuevo_estado.voltearFichas(move[0], move[1], jugador)
        if poda:
            tupla = min_valor(nuevo_estado, N + 1, contrario, True, alfa, beta)
        else:
            tupla = min_valor(nuevo_estado, contrario, N + 1)
        if tupla[0] > mejor_utilidad:
            mejor_utilidad = tupla[0]
            mejor_movimiento = move
            if poda:
                if mejor_utilidad >= beta:
                    return mejor_utilidad, move
                alfa = max(alfa, mejor_utilidad)
    return mejor_utilidad, mejor_movimiento


def minimax_alfa_beta(estado, N, jugador):
    mejor_movimiento = max_valor(estado, 1, jugador, True, -sys.maxsize, sys.maxsize)[1]
    return mejor_movimiento


def minimax(estado, N, jugador):
    mejor_movimiento = max_valor(estado, 1, jugador, True, -sys.maxsize, sys.maxsize)[1]
    return mejor_movimiento

tablero = Tablero()


pygame.init()


WIDTH = HEIGHT = 560
pantalla = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Juego Othello")
time = pygame.time.Clock() 


font = pygame.font.SysFont("notomono", 15, True)
text_font = font.render("Comenzar juego", True, "#FFFFFF")

background = pygame.image.load("gui/principal.jpg").convert()
rect = pygame.Rect((30,50), (160,50)) 

menu_main = True 
juego = False
turno = 1
agente = None
rl = False
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
            if tablero.validarMovimientos(row, col, -1):
                tablero.matriz[row][col] = Ficha(row, col, -1)
                tablero.voltearFichas(row, col, -1)
                x, y = minimax(tablero, 1, 1)
                tablero.matriz[x][y] = Ficha(x, y, 1)
                tablero.voltearFichas(x, y, 1)
                turno = -1
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
                if rl:
                    agente = entrenar_nuevo_agente()
                #MENSAJE ENTRENANDO
                #
            else:
                pygame.draw.rect(pantalla, "#191970", rect, border_radius=12)
        else:
            pygame.draw.rect(pantalla, "#008000", rect, border_radius=12)

        pantalla.blit(text_font, (30 + int((160 -text_font.get_width()) / 2),50+(int((50-text_font.get_height())) / 2)))
    elif juego:
        if turno == -1 and rl:
            tablero = agente.siguiente_jugada(tablero, -1)
            turno = 1
        pantalla.fill("#008000")
        tablero.pintarTablero(pantalla)
        tablero.colocarFichas(pantalla)
        
    
    pygame.display.update()
