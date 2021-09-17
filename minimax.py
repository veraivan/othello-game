import sys
import random

cantidad_movimientos = [(0,-1), (0,1), (-1,-1), (1,1), (-1,0), (1,0), (1,-1), (-1,1)]

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

# 1 ficha blanca, -1 ficha negra, 0 celda vacia


class Tablero:
    def __init__(self):
        self.tablero = [None] * 8
        for i in range(8):
            self.tablero[i] = [0]*8
        self.tablero[3][3] = 1
        self.tablero[3][4] = -1
        self.tablero[4][3] = -1
        self.tablero[4][4] = 1 
    
    def contar_fichas(self, pieza):
        posiciones = []
        for f in range(8):
            for c in range(8):
                if self.tablero[f][c] == pieza:
                    posiciones.append((f,c))
        return posiciones 
    
    def verificar_movimientos(self, x, y, destino, oponente):
        if self.tablero[x][y] == oponente:
            while x >= 0 and x < 8 and y >= 0 and y < 8:
                x += destino[0]
                y += destino[1]
                if self.tablero[x][y] == 0:
                    return (x,y) 
                elif self.tablero[x][y] == -oponente:
                    return False
        else:
            return False 
    
    def verificarTableroCompleto(self):
        for f in range(8):
            for c in range(8):
                if self.tablero[f][c] == 0:
                    return False 
        return True 
    
    def obtener_movimientos(self, origin, pieza):
        movimientos_legales = set()
        for destino in cantidad_movimientos:
            x, y = origin[0] + destino[0], origin[1] + destino[1]
            pos = self.verificar_movimientos(x,y, -pieza, destino)
            if pos:
                movimientos_legales.add(pos)
        return movimientos_legales 
    


"""
def funcion_evaluacion(table, color):
    oponente = -color 
    total = 0 

    coordenadas_jugador = countFicha(color) 
    for pos in coordenadas_jugador:
        total += tablero_pesos[pos[0]][pos[1]] 
    
    coordenadas_opp = countFicha(oponente) 
    for pos in coordenadas_opp:
        total -= tablero_pesos[pos[0]][pos[1]]

    return total



def verificacionCambiarColor(estado, x, y, destino, pieza):
    oponente = -pieza
    if estado[x][y] == oponente:
        while x >= 0 and x < 8 and y >= 0 and y < 8:
            x += destino[0]
            y += destino[1]
            if estado[x][y] == 0:
                return False
            elif estado[x][y] == pieza:
                return True
    else:
        return False



def colocarFicha(estado, punto, pieza):
    estado[punto[0]][punto[1]] = pieza 

    for destino in movimientos:
        if verificacionCambiarColor(estado, punto[0], punto[1], destino, pieza):
            mover(estado, punto[0], punto[1], destino, pieza)


def min_valor(estado):
    if tableroCompleto((estado)):
        return funcion_evaluacion(estado,-1)
    
    mejor_point = sys.maxsize 
    coor = countFicha(estado, -1)
    moves = verificar_movimientos(estado) 
    for move in moves:
        colocarFicha(estado, move, -1)
        mejor_point = min(mejor_point, max_valor(estado))
    return mejor_point

def max_valor(estado):
    if tableroCompleto((estado)):
        return funcion_evaluacion(estado,1)

    mejor_point = -sys.maxsize 
    coor = countFicha(estado, 1)
    moves = verificar_movimientos(estado) 
    for move in moves:
        colocarFicha(estado, move, 1)
        mejor_point = max(mejor_point,min_valor(estado))
    return mejor_point


def minimax(estado):
    mejor_movimiento = max_valor(estado)
    return mejor_movimiento

"""


class AgenteRL:

    def __init__(self, n):
        self.n = n
        self.tablero = None
        self.alfa = 0
        self.entrenar = True
        self.resultado_juego = 0
        self.n = 0
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

    def set_q(self, q):
        self.q_rate = q

    def actualizar_alfa(self, juego_actual):
        self.alfa = 0.5 - 0.49 * juego_actual / self.n

    def serializar_tablero(self, tablero):
        tablero_serializado = ''
        for i in range(len(tablero)):
            for j in range(len(tablero[0])):
                tablero_serializado += tablero[i][j]
        return tablero_serializado

    def obtener_probabilidad(self, tablero):
        tablero_serializado = self.serializar_tablero(tablero)
        if not self.lookupTablero[tablero_serializado]:
            self.lookupTablero[tablero_serializado] = 0.5
        return self.lookupTablero[tablero_serializado]

    def calcular_recompensa(self, tablero, jugador):
        contrario = (jugador % 2) + 1
        resultado = tablero.calcular_resultado()  # TODO: TOMAR DEL EVALUADOR DE RESULTADOS DE IVAN
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

    def actualizar_probabilidad(self, tablero, prob_prox_estado, jugador):
        prob = self.calcular_recompensa(tablero, jugador)
        prob = prob + self.alfa * (prob_prox_estado - prob)

        tablero_serializado = self.serializar_tablero(tablero)
        self.lookupTablero[tablero_serializado] = prob

    def copiar_tablero(self, tablero_origen, tablero_destino):
        tablero_destino = tablero_origen.copy()

    # ELITISTA
    def jugar(self, jugador):
        prob = 0
        fil = 0
        col = 0
        prob_max = -sys.maxsize
        # elegir casilla disponible con max reward
        for i in range(self.tablero.length):
            for j in range(self.tablero[0].length):
                if self.tablero[i][j] == 0:    # esta vacio
                    self.tablero[i][j] = jugador
                    prob = self.calcular_recompensa(self.tablero, jugador)
                    if prob > prob_max:
                        prob_max = prob
                        fil = i
                        col = j
                    self.tablero[i][j] = 0
        # entrenar
        if self.entrenar:
            self.actualizar_probabilidad(self.tablero_final, prob_max, jugador)
        # aplicar jugada
        self.tablero.colocarFicha(self.tablero.tablero, [fil, col], jugador)
        # actualizar ultimo tablero
        self.tablero_final = self.tablero.copy()

    def jugar_random(self, jugador):
        filas = []
        columnas = []
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[0])):
                if self.tablero[i][j] == 0:
                    filas.append(i)
                    columnas.append(i)
        rdm = int(random.random() * len(filas))
        self.tablero[filas[rdm]][columnas[rdm]] = jugador
        if jugador == self.jugador_agente:
            self.tablero_final = self.tablero.copy()

    def jugar_vs_random(self):
        jugador = self.jugador_agente
        contrario = (jugador % 2) + 1
        turno = 1
        jugadas = 64
        while jugadas > -1:
            if turno == jugador:
                q = random.random()
                if q <= self.q_rate or not self.entrenar:
                    self.jugar(jugador)
                else:
                    self.jugar_random(jugador)
            else:
                self.jugar_random(contrario)

            resultado_juego = self.tablero.calcular_resultado(self.tablero)
            if resultado_juego > 0:
                if resultado_juego != jugador and self.entrenar:
                    self.actualizar_probabilidad(self.tablero_final, self.calcular_recompensa(self.tablero, jugador), jugador)
                break
