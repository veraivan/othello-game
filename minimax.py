import sys
import random
from gui.figuras import Tablero, Ficha
from copy import deepcopy

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


#Limite de profundidad
N_LIMIT = None

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
            tupla = max_valor(nuevo_estado, N + 1, contrario, True, alfa, beta)
        else:
            tupla = max_valor(nuevo_estado, N + 1, contrario)
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
    global N_LIMIT
    N_LIMIT = N
    mejor_movimiento = max_valor(estado, 1, jugador, True, -sys.maxsize, sys.maxsize)[1]
    return mejor_movimiento


def minimax(estado, N, jugador):
    global N_LIMIT
    N_LIMIT = N
    mejor_movimiento = max_valor(estado, 1, jugador)[1]
    return mejor_movimiento


class AgenteRL:

    def __init__(self, n):
        self.n = n
        self.tablero = None
        self.alfa = 0
        self.entrenar = True
        self.resultado_juego = 0
        self.tablero_final = None
        self.jugador_agente = 1
        self.q_rate = 0.1
        self.lookupTablero = {}
        self.reset(True)

    def reset(self, entrenar):
        self.tablero = Tablero()
        self.tablero_final = Tablero()
        self.entrenar = entrenar
        self.resultado_juego = 0

    def set_n(self, n):
        self.n = n

    def set_alfa(self, alfa):
        self.alfa = alfa

    def set_q(self, q):
        self.q_rate = q

    def actualizar_alfa(self, juego_actual):
        self.alfa = 0.5 - 0.49 * juego_actual / self.n

    def serializar_tablero(self, tablero):
        tablero_serializado = ''
        for i in range(8):
            for j in range(8):
                if tablero.matriz[i][j]:
                    tablero_serializado += str(tablero.matriz[i][j].color)
                else:
                    tablero_serializado += '0'
        return tablero_serializado

    def obtener_probabilidad(self, tablero):
        tablero_serializado = self.serializar_tablero(tablero)
        if not tablero_serializado in self.lookupTablero:
            self.lookupTablero[tablero_serializado] = 0.5
        return self.lookupTablero[tablero_serializado]

    def actualizar_probabilidad(self, tablero, prob_prox_estado, jugador):
        prob = self.calcular_recompensa(tablero, jugador)
        prob = prob + self.alfa * (prob_prox_estado - prob)

        tablero_serializado = self.serializar_tablero(tablero)
        self.lookupTablero[tablero_serializado] = prob

    def calcular_recompensa(self, tablero, jugador):
        contrario = -jugador
        resultado = tablero.calcular_resultado()

        # GANO
        if resultado == jugador:
            return 1
        # PERDIO
        elif resultado == contrario:
            return 0
        # EMPATE
        elif resultado == 3:
            return 0
        else:
            return self.obtener_probabilidad(tablero)

    # ELITISTA
    def jugar(self, jugador):
        prob = 0
        fil = 0
        col = 0
        prob_max = -sys.maxsize
        matriz_anterior = deepcopy(self.tablero.matriz)
        # elegir casilla disponible con max reward
        movimientos = self.tablero.movimientosPosibles(jugador)
        for mov in movimientos:
            i = mov[0]
            j = mov[1]
            if not self.tablero.matriz[i][j]:    # esta vacio
                # INICIALMENTE
                # 1 es blanco, computador
                # -1 es negro, jugador

                # validar si es que deja poner en esa posicion
                if self.tablero.validarMovimientos(i, j, jugador):
                    self.tablero.colocar_ficha_nueva(i, j, jugador)
                    prob = self.calcular_recompensa(self.tablero, jugador)
                    if prob > prob_max:
                        prob_max = prob
                        fil = i
                        col = j
                    self.tablero.matriz = deepcopy(matriz_anterior)
        if len(movimientos) > 0:
            # entrenar
            if self.entrenar:
                self.actualizar_probabilidad(self.tablero_final, prob_max, jugador)
            # aplicar jugada
            self.tablero.colocar_ficha_nueva(fil, col, jugador)
            # actualizar ultimo tablero
            self.tablero_final = deepcopy(self.tablero)
        else:
            self.tablero_final = deepcopy(self.tablero)
            return fil, col

    def jugar_random(self, jugador):
        filas = []
        columnas = []
        movimientos = self.tablero.movimientosPosibles(jugador)
        cant_movs = len(movimientos)
        if cant_movs > 0:
            ficha_colocada = False
            while not ficha_colocada:
                rdm = int(random.random() * cant_movs)
                # validar la posicion y asignar
                if self.tablero.validarMovimientos(movimientos[rdm][0], movimientos[rdm][1], jugador):
                    self.tablero.colocar_ficha_nueva(movimientos[rdm][0], movimientos[rdm][1], jugador)
                    ficha_colocada = True
            if jugador == self.jugador_agente:
                self.tablero_final = deepcopy(self.tablero)

    def jugar_minimax(self, N):
        jugador = -1
        contrario = 1
        x, y = minimax(self.tablero, N, jugador)
        self.tablero.colocar_ficha_nueva(x, y, -1)

    def jugar_vs_random(self):
        jugador = self.jugador_agente
        contrario = -jugador
        turno = 1
        jugadas = 60
        contador_jugar = 1
        contador_jugar_random = 1
        while jugadas > -1 or self.tablero.finDeJuego():
            if turno == jugador:
                q = random.random()
                if q <= self.q_rate or not self.entrenar:
                    self.jugar(jugador)
                else:
                    self.jugar_random(jugador)
            else:
                self.jugar_random(contrario)

            self.resultado_juego = self.tablero.calcular_resultado()
            if self.resultado_juego != 0:
                if self.resultado_juego != jugador and self.entrenar:
                    self.actualizar_probabilidad(self.tablero_final, self.calcular_recompensa(self.tablero, jugador), jugador)
                break
            turno = 2 - turno + 1
            jugadas -= 1

    def jugar_vs_minimax(self):
        jugador = self.jugador_agente
        contrario = -jugador
        turno = 1
        jugadas = 60
        contador_jugar = 1
        contador_jugar_random = 1
        while jugadas > -1 or self.tablero.finDeJuego():
            if turno == jugador:
                q = random.random()
                if q <= self.q_rate or not self.entrenar:
                    self.jugar(jugador)
                else:
                    self.jugar_minimax(jugador)
            else:
                self.jugar_random(contrario)

            self.resultado_juego = self.tablero.calcular_resultado()
            if self.resultado_juego != 0:
                if self.resultado_juego != jugador and self.entrenar:
                    self.actualizar_probabilidad(self.tablero_final, self.calcular_recompensa(self.tablero, jugador), jugador)
                break
            turno = 2 - turno + 1
            jugadas -= 1

    def siguiente_jugada(self, tablero, jugador):
        self.tablero = tablero
        self.jugar(jugador)
        return self.tablero


def entrenar_nuevo_agente():
    q_rates = {0.5}

    ciclos_entrenamiento = 50
    ciclos_entrenamiento_humano = 0
    contador_total_juegos = 0

    for q in q_rates:
        tasa_victorias = 0
        tasa_derrotas = 0
        tasa_empates = 0

        agente = AgenteRL(ciclos_entrenamiento)
        agente.set_q(q)
        # SE ELIGE SI VA A SER ENTRENADO CON UN JUGADOR ALEATORIO O CON UN JUGADOR MINIMAX

        # JUGADOR ALEATORIO
        for i in range(agente.n):
            agente.reset(True)
            agente.actualizar_alfa(i)
            agente.jugar_vs_random()

        # JUGADOR MINIMAX
        for i in range(agente.n):
            agente.reset(True)
            agente.actualizar_alfa(i)
            agente.jugar_vs_minimax()

        victorias = 0
        derrotas = 0
        empates = 0
        contrario = -agente.jugador_agente
        for i in range(contador_total_juegos):
            agente.reset(False)
            agente.jugar_vs_random()

            if agente.resultado_juego == agente.jugador_agente:
                victorias += 1
            elif agente.resultado_juego == contrario:
                derrotas +=1
            else:
                empates += 1
        # tasa_victorias += victorias / contador_total_juegos
        # tasa_derrotas += derrotas / contador_total_juegos
        # tasa_empates += empates / contador_total_juegos
        #
        # print('>>>>>> TASA DE VICTORIAS: V/T=', tasa_victorias)
        # print('>>>>>> TASA DE DERROTAS: D/T=', tasa_derrotas)
        # print('>>>>>> TASA DE EMPATES: E/T=', tasa_empates)

    return agente