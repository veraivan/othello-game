import pygame

movimientos = [(0,-1), (0,1), (-1,-1), (1,1), (-1,0), (1,0), (1,-1), (-1,1)] 


# 1 Blanca, -1 Negro, None vacio
class Ficha:
    def __init__(self, row, col, color):
        self.x = 70 * col + 35
        self.y = 70 * row + 35 
        self.color = color 

        if self.color == 1:
            self.cod_color = "#FFFFFF"
        else:
            self.cod_color = "#000000"

    def pintarFicha(self, pantalla):
        pygame.draw.circle(pantalla, self.cod_color, (self.x,self.y), 30) 
    

class Tablero: 
    def __init__(self):
        self.matriz = [None]*8
        for i in range(8):
            self.matriz[i] = [None]*8

        self.matriz[3][3] = Ficha(3,3,1)
        self.matriz[3][4] = Ficha(3,4,-1)
        self.matriz[4][3] = Ficha(4,3,-1)
        self.matriz[4][4] = Ficha(4,4,1)
    
    def pintarTablero(self, pantalla):
        for row in range(0,630,70):
            for col in range(0,630,70):
                pygame.draw.rect(pantalla, "#000000", [row,col,70,70], 1) 

    def colocarFichas(self, pantalla):
        for f in range(8):
            for c in range(8):
                if self.matriz[f][c] != None:
                    ficha = self.matriz[f][c] 
                    ficha.pintarFicha(pantalla) 
    
    def validarMovimientos(self, row, col, pieza):
        if self.matriz[row][col] != None:
            return False
        else:
            oponente = -pieza 
            for pos in movimientos:
                if self.validarDireccion(row+pos[0] ,col+pos[1]) and self.checkearVolteo(row+pos[0] ,col+pos[1], pos, pieza, oponente):
                    return True

    def checkearVolteo(self, x, y, pos, pieza, oponente):
        if self.matriz[x][y] and self.matriz[x][y].color == oponente:
            while self.validarDireccion(x,y):
                x += pos[0]
                y += pos[1]
                if self.matriz[x][y] == None:
                    return False 
                elif self.matriz[x][y].color == pieza:
                    return True 
        else:
            return False    
    
    def validarDireccion(self, x, y):
        if x >= 0 and x < 8 and y >= 0 and y < 8:
            return True
        else:
            return False 

    def voltearFichas(self, row, col, pieza):
        oponente = -pieza 
        for pos in movimientos:
            if self.checkearVolteo(row+pos[0] ,col+pos[1], pos, pieza, oponente):
                self.cambioColor(row+pos[0] ,col+pos[1], pos, pieza, oponente)
    
    def cambioColor(self, x, y, pos, pieza, oponente):
        while self.validarDireccion(x,y) and self.matriz[x][y].color == oponente:
            self.matriz[x][y] = Ficha(x,y,pieza)
            x += pos[0]
            y += pos[1] 
    
    def contarFichas(self, pieza):
        posiciones = []
        for f in range(8):
            for c in range(8):
                if self.matriz[f][c] and self.matriz[f][c].color  == pieza:
                    posiciones.append((f,c))
        return posiciones 

    def getMovimientos(self, x, y, destino, oponente):
        if self.matriz[x][y] and self.matriz[x][y].color  == oponente:
            while x >= 0 and x < 8 and y >= 0 and y < 8:
                x += destino[0]
                y += destino[1]
                if self.matriz[x][y] == None:
                    return (x,y) 
                elif self.matriz[x][y].color == -oponente:
                    return False
        else:
            return False 


    def movimientosPosibles(self, pieza):
        movimientos_legales = []
        for origin in self.contarFichas(pieza):
            for destino in movimientos:
                x, y = origin[0] + destino[0], origin[1] + destino[1]
                pos = self.getMovimientos(x, y, destino, -pieza)
                if pos:
                    movimientos_legales.append(pos)
        return movimientos_legales 

    def listaMovimientos(self, pieza):
        numMovimientos = 0
        for f in range(8):
            for c in range(8):
                if self.validarMovimientos(f, c, pieza):
                    numMovimientos += 1 
        return numMovimientos

    def finDeJuego(self):
        numBlanco = self.listaMovimientos(1)
        numNegro = self.listaMovimientos(-1)
        if numBlanco == 0 and numNegro == 0:
            return True 
        else:
            return False

    
