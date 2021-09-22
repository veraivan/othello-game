from minimax import AgenteRL
import time
from minimax import entrenar_nuevo_agente, minimax, minimax_alfa_beta, validacion_agente
from gui.figuras import Tablero


def tests():
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    print("Minimax(2) vs Alfabeta(2)")
    duracion_media_turno_minimax, duracion_media_turno_alfabeta, duracion_media_partida, victorias_minimax, victorias_alfabeta, empates = minimax_vs_alfabeta(2, 2)
    print("Duracion media turno Minimax(2): ", duracion_media_turno_minimax)
    print("Duracion media turno Alfabeta(2): ", duracion_media_turno_alfabeta)
    print("Duracion media partida: ", duracion_media_partida)
    print("Victorias de Minimax(2): ", victorias_minimax)
    print("Victorias de Alfabeta(2)", victorias_alfabeta)
    print("Empates", empates)
    print()
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    print("Minimax(2) vs Alfabeta(3)")
    duracion_media_turno_minimax, duracion_media_turno_alfabeta, duracion_media_partida, victorias_minimax, victorias_alfabeta, empates = minimax_vs_alfabeta(2, 3)
    print("Duracion media turno Minimax(2): ", duracion_media_turno_minimax)
    print("Duracion media turno Alfabeta(3): ", duracion_media_turno_alfabeta)
    print("Duracion media partida: ", duracion_media_partida)
    print("Victorias de Minimax(2): ", victorias_minimax)
    print("Victorias de Alfabeta(3)", victorias_alfabeta)
    print("Empates", empates)
    print()
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    print("Minimax(2) vs Alfabeta(4)")
    duracion_media_turno_minimax, duracion_media_turno_alfabeta, duracion_media_partida, victorias_minimax, victorias_alfabeta, empates = minimax_vs_alfabeta(2, 4)
    print("Duracion media turno Minimax(2): ", duracion_media_turno_minimax)
    print("Duracion media turno Alfabeta(4): ", duracion_media_turno_alfabeta)
    print("Duracion media partida: ", duracion_media_partida)
    print("Victorias de Minimax(2): ", victorias_minimax)
    print("Victorias de Alfabeta(6)", victorias_alfabeta)
    print("Empates: ", empates)
    print()
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    print("Minimax(3) vs Alfabeta(2)")
    duracion_media_turno_minimax, duracion_media_turno_alfabeta, duracion_media_partida, victorias_minimax, victorias_alfabeta, empates = minimax_vs_alfabeta(3, 2)
    print("Duracion media turno Minimax(3): ", duracion_media_turno_minimax)
    print("Duracion media turno Alfabeta(2): ", duracion_media_turno_alfabeta)
    print("Duracion media partida: ", duracion_media_partida)
    print("Victorias de Minimax(3): ", victorias_minimax)
    print("Victorias de Alfabeta(2)", victorias_alfabeta)
    print("Empates", empates)
    print()
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    print("Minimax(3) vs Alfabeta(3)")
    duracion_media_turno_minimax, duracion_media_turno_alfabeta, duracion_media_partida, victorias_minimax, victorias_alfabeta, empates = minimax_vs_alfabeta(3, 3)
    print("Duracion media turno Minimax(3): ", duracion_media_turno_minimax)
    print("Duracion media turno Alfabeta(3): ", duracion_media_turno_alfabeta)
    print("Duracion media partida: ", duracion_media_partida)
    print("Victorias de Minimax(3): ", victorias_minimax)
    print("Victorias de Alfabeta(3)", victorias_alfabeta)
    print("Empates: ", empates)
    print()
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    print("Minimax(3) vs Alfabeta(4)")
    duracion_media_turno_minimax, duracion_media_turno_alfabeta, duracion_media_partida, victorias_minimax, victorias_alfabeta, empates = minimax_vs_alfabeta(3, 4)
    print("Duracion media turno Minimax(3): ", duracion_media_turno_minimax)
    print("Duracion media turno Alfabeta(4): ", duracion_media_turno_alfabeta)
    print("Duracion media partida: ", duracion_media_partida)
    print("Victorias de Minimax(3): ", victorias_minimax)
    print("Victorias de Alfabeta(4)", victorias_alfabeta)
    print("Empates: ", empates)
    print()
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    print("Minimax(4) vs Alfabeta(3)")
    duracion_media_turno_minimax, duracion_media_turno_alfabeta, duracion_media_partida, victorias_minimax, victorias_alfabeta, empates = minimax_vs_alfabeta(4, 3)
    print("Duracion media turno Minimax(4): ", duracion_media_turno_minimax)
    print("Duracion media turno Alfabeta(3): ", duracion_media_turno_alfabeta)
    print("Duracion media partida: ", duracion_media_partida)
    print("Victorias de Minimax(4): ", victorias_minimax)
    print("Victorias de Alfabeta(3)", victorias_alfabeta)
    print("Empates: ", empates)
    print()
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    print("Minimax(4) vs Alfabeta(4)")
    duracion_media_turno_minimax, duracion_media_turno_alfabeta, duracion_media_partida, victorias_minimax, victorias_alfabeta, empates = minimax_vs_alfabeta(4, 4)
    print("Duracion media turno Minimax(4): ", duracion_media_turno_minimax)
    print("Duracion media turno Alfabeta(4): ", duracion_media_turno_alfabeta)
    print("Duracion media partida: ", duracion_media_partida)
    print("Victorias de Minimax(4): ", victorias_minimax)
    print("Victorias de Alfabeta(4)", victorias_alfabeta)
    print("Empates: ", empates)
    print()
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    print("Minimax(4) vs Alfabeta(5)")
    duracion_media_turno_minimax, duracion_media_turno_alfabeta, duracion_media_partida, victorias_minimax, victorias_alfabeta, empates = minimax_vs_alfabeta(4, 5)
    print("Duracion media turno Minimax(4): ", duracion_media_turno_minimax)
    print("Duracion media turno Alfabeta(5): ", duracion_media_turno_alfabeta)
    print("Duracion media partida: ", duracion_media_partida)
    print("Victorias de Minimax(4): ", victorias_minimax)
    print("Victorias de Alfabeta(5)", victorias_alfabeta)
    print("Empates: ", empates)
    print()
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    print("Minimax(5) vs Alfabeta(3)")
    duracion_media_turno_minimax, duracion_media_turno_alfabeta, duracion_media_partida, victorias_minimax, victorias_alfabeta, empates = minimax_vs_alfabeta(5, 3)
    print("Duracion media turno Minimax(5): ", duracion_media_turno_minimax)
    print("Duracion media turno Alfabeta(3): ", duracion_media_turno_alfabeta)
    print("Duracion media partida: ", duracion_media_partida)
    print("Victorias de Minimax(5): ", victorias_minimax)
    print("Victorias de Alfabeta(3)", victorias_alfabeta)
    print("Empates: ", empates)
    print()
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    print("Minimax(5) vs Alfabeta(4)")
    duracion_media_turno_minimax, duracion_media_turno_alfabeta, duracion_media_partida, victorias_minimax, victorias_alfabeta, empates = minimax_vs_alfabeta(5, 4)
    print("Duracion media turno Minimax(5): ", duracion_media_turno_minimax)
    print("Duracion media turno Alfabeta(4): ", duracion_media_turno_alfabeta)
    print("Duracion media partida: ", duracion_media_partida)
    print("Victorias de Minimax(5): ", victorias_minimax)
    print("Victorias de Alfabeta(4)", victorias_alfabeta)
    print("Empates: ", empates)
    print()
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    print("Minimax(5) vs Alfabeta(5)")
    duracion_media_turno_minimax, duracion_media_turno_alfabeta, duracion_media_partida, victorias_minimax, victorias_alfabeta, empates = minimax_vs_alfabeta(5, 5)
    print("Duracion media turno Minimax(5): ", duracion_media_turno_minimax)
    print("Duracion media turno Alfabeta(5): ", duracion_media_turno_alfabeta)
    print("Duracion media partida: ", duracion_media_partida)
    print("Victorias de Minimax(5): ", victorias_minimax)
    print("Victorias de Alfabeta(5)", victorias_alfabeta)
    print("Empates: ", empates)
    print()
    print("--------------------------------------------------------------------------------------------------------------------------------------------")

    agente = entrenar_nuevo_agente()
    duracion_media_turno_minimax, duracion_media_turno_agenterl, duracion_media_partida, victorias_minimax, victorias_agenterl, empates = minimax_vs_agenteRL(False, 2, agente)
    print("Duracion media turno Minimax(2): ", duracion_media_turno_minimax)
    print("Duracion media turno Agente RL: ", duracion_media_turno_agenterl)
    print("Duracion media partida: ", duracion_media_partida)
    print("Victorias de Minimax(2): ", victorias_minimax)
    print("Victorias de Agente RL", victorias_agenterl)
    print("Empates: ", empates)
    print()
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    duracion_media_turno_minimax, duracion_media_turno_agenterl, duracion_media_partida, victorias_minimax, victorias_agenterl, empates = minimax_vs_agenteRL(False, 3, agente)
    print("Duracion media turno Minimax(3): ", duracion_media_turno_minimax)
    print("Duracion media turno Agente RL: ", duracion_media_turno_agenterl)
    print("Duracion media partida: ", duracion_media_partida)
    print("Victorias de Minimax(3): ", victorias_minimax)
    print("Victorias de Agente RL", victorias_agenterl)
    print("Empates: ", empates)
    print()
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    duracion_media_turno_minimax, duracion_media_turno_agenterl, duracion_media_partida, victorias_minimax, victorias_agenterl, empates = minimax_vs_agenteRL(False, 4, agente)
    print("Duracion media turno Minimax(4): ", duracion_media_turno_minimax)
    print("Duracion media turno Agente RL: ", duracion_media_turno_agenterl)
    print("Duracion media partida: ", duracion_media_partida)
    print("Victorias de Minimax(4): ", victorias_minimax)
    print("Victorias de Agente RL", victorias_agenterl)
    print("Empates: ", empates)
    print()
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    duracion_media_turno_minimax, duracion_media_turno_agenterl, duracion_media_partida, victorias_minimax, victorias_agenterl, empates = minimax_vs_agenteRL(True, 2, agente)
    print("Duracion media turno Alfabeta(2): ", duracion_media_turno_minimax)
    print("Duracion media turno Agente RL: ", duracion_media_turno_agenterl)
    print("Duracion media partida: ", duracion_media_partida)
    print("Victorias de Alfabeta(2): ", victorias_minimax)
    print("Victorias de Agente RL", victorias_agenterl)
    print("Empates: ", empates)
    print()
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    duracion_media_turno_minimax, duracion_media_turno_agenterl, duracion_media_partida, victorias_minimax, victorias_agenterl, empates = minimax_vs_agenteRL(True, 3, agente)
    print("Duracion media turno Alfabeta(3): ", duracion_media_turno_minimax)
    print("Duracion media turno Agente RL: ", duracion_media_turno_agenterl)
    print("Duracion media partida: ", duracion_media_partida)
    print("Victorias de Alfabeta(3): ", victorias_minimax)
    print("Victorias de Agente RL", victorias_agenterl)
    print("Empates: ", empates)
    print()
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    duracion_media_turno_minimax, duracion_media_turno_agenterl, duracion_media_partida, victorias_minimax, victorias_agenterl, empates = minimax_vs_agenteRL(True, 4, agente)
    print("Duracion media turno Alfabeta(4): ", duracion_media_turno_minimax)
    print("Duracion media turno Agente RL: ", duracion_media_turno_agenterl)
    print("Duracion media partida: ", duracion_media_partida)
    print("Victorias de Alfabeta(4): ", victorias_minimax)
    print("Victorias de Agente RL", victorias_agenterl)
    print("Empates: ", empates)
    print()

    print()
    print(
        "--------------------------------------------------------------------------------------------------------------------------------------------")
    print(
        "--------------------------------------------------------------------------------------------------------------------------------------------")
    print('Entrenamiento Agente RL')
    print(
        "--------------------------------------------------------------------------------------------------------------------------------------------")
    print('Con 50 ciclos y contrincante aleatorio:')
    tiempo_entrenamiento, tasa_victorias, tasa_derrotas, tasa_empates = evaluacion_agente(50, 1)
    print('Tiempo de entrenamiento: ', tiempo_entrenamiento)
    print('Tasa de victorias:', tasa_victorias)
    print('Tasa de derrotas:', tasa_derrotas)
    print('Tasa de empates:', tasa_empates)
    print()
    print('Con 100 ciclos y contrincante aleatorio:')
    tiempo_entrenamiento, tasa_victorias, tasa_derrotas, tasa_empates = evaluacion_agente(100, 1)
    print('Tiempo de entrenamiento: ', tiempo_entrenamiento)
    print('Tasa de victorias:', tasa_victorias)
    print('Tasa de derrotas:', tasa_derrotas)
    print('Tasa de empates:', tasa_empates)
    print()
    print('Con 150 ciclos y contrincante aleatorio:')
    tiempo_entrenamiento, tasa_victorias, tasa_derrotas, tasa_empates = evaluacion_agente(150, 1)
    print('Tiempo de entrenamiento: ', tiempo_entrenamiento)
    print('Tasa de victorias:', tasa_victorias)
    print('Tasa de derrotas:', tasa_derrotas)
    print('Tasa de empates:', tasa_empates)
    print()
    print('Con 200 ciclos y contrincante aleatorio:')
    tiempo_entrenamiento, tasa_victorias, tasa_derrotas, tasa_empates = evaluacion_agente(200, 1)
    print('Tiempo de entrenamiento: ', tiempo_entrenamiento)
    print('Tasa de victorias:', tasa_victorias)
    print('Tasa de derrotas:', tasa_derrotas)
    print('Tasa de empates:', tasa_empates)
    print()
    print('Con 250 ciclos y contrincante aleatorio:')
    tiempo_entrenamiento, tasa_victorias, tasa_derrotas, tasa_empates = evaluacion_agente(250, 1)
    print('Tiempo de entrenamiento: ', tiempo_entrenamiento)
    print('Tasa de victorias:', tasa_victorias)
    print('Tasa de derrotas:', tasa_derrotas)
    print('Tasa de empates:', tasa_empates)
    print()
    print('Con 300 ciclos y contrincante aleatorio:')
    tiempo_entrenamiento, tasa_victorias, tasa_derrotas, tasa_empates = evaluacion_agente(300, 1)
    print('Tiempo de entrenamiento: ', tiempo_entrenamiento)
    print('Tasa de victorias:', tasa_victorias)
    print('Tasa de derrotas:', tasa_derrotas)
    print('Tasa de empates:', tasa_empates)
    print()
    # print('Con 350 ciclos y contrincante aleatorio:')
    # tiempo_entrenamiento, tasa_victorias, tasa_derrotas, tasa_empates = evaluacion_agente(350, 1)
    # print('Tiempo de entrenamiento: ', tiempo_entrenamiento)
    # print('Tasa de victorias:', tasa_victorias)
    # print('Tasa de derrotas:', tasa_derrotas)
    # print('Tasa de empates:', tasa_empates)
    # print()
    # print('Con 400 ciclos y contrincante aleatorio:')
    # tiempo_entrenamiento, tasa_victorias, tasa_derrotas, tasa_empates = evaluacion_agente(400, 1)
    # print('Tiempo de entrenamiento: ', tiempo_entrenamiento)
    # print('Tasa de victorias:', tasa_victorias)
    # print('Tasa de derrotas:', tasa_derrotas)
    # print('Tasa de empates:', tasa_empates)
    # print()
    # print('Con 450 ciclos y contrincante aleatorio:')
    # tiempo_entrenamiento, tasa_victorias, tasa_derrotas, tasa_empates = evaluacion_agente(450, 1)
    # print('Tiempo de entrenamiento: ', tiempo_entrenamiento)
    # print('Tasa de victorias:', tasa_victorias)
    # print('Tasa de derrotas:', tasa_derrotas)
    # print('Tasa de empates:', tasa_empates)
    # print()
    # print('Con 500 ciclos y contrincante aleatorio:')
    # tiempo_entrenamiento, tasa_victorias, tasa_derrotas, tasa_empates = evaluacion_agente(500, 1)
    # print('Tiempo de entrenamiento: ', tiempo_entrenamiento)
    # print('Tasa de victorias:', tasa_victorias)
    # print('Tasa de derrotas:', tasa_derrotas)
    # print('Tasa de empates:', tasa_empates)
    # print()
    # print('Con 550 ciclos y contrincante aleatorio:')
    # tiempo_entrenamiento, tasa_victorias, tasa_derrotas, tasa_empates = evaluacion_agente(550, 1)
    # print('Tiempo de entrenamiento: ', tiempo_entrenamiento)
    # print('Tasa de victorias:', tasa_victorias)
    # print('Tasa de derrotas:', tasa_derrotas)
    # print('Tasa de empates:', tasa_empates)
    # print()
    # print('Con 600 ciclos y contrincante aleatorio:')
    # tiempo_entrenamiento, tasa_victorias, tasa_derrotas, tasa_empates = evaluacion_agente(600, 1)
    # print('Tiempo de entrenamiento: ', tiempo_entrenamiento)
    # print('Tasa de victorias:', tasa_victorias)
    # print('Tasa de derrotas:', tasa_derrotas)
    # print('Tasa de empates:', tasa_empates)
    # print()
    # print('Con 650 ciclos y contrincante aleatorio:')
    # tiempo_entrenamiento, tasa_victorias, tasa_derrotas, tasa_empates = evaluacion_agente(650, 1)
    # print('Tiempo de entrenamiento: ', tiempo_entrenamiento)
    # print('Tasa de victorias:', tasa_victorias)
    # print('Tasa de derrotas:', tasa_derrotas)
    # print('Tasa de empates:', tasa_empates)
    # print()
    # print('Con 700 ciclos y contrincante aleatorio:')
    # tiempo_entrenamiento, tasa_victorias, tasa_derrotas, tasa_empates = evaluacion_agente(700, 1)
    # print('Tiempo de entrenamiento: ', tiempo_entrenamiento)
    # print('Tasa de victorias:', tasa_victorias)
    # print('Tasa de derrotas:', tasa_derrotas)
    # print('Tasa de empates:', tasa_empates)
    print()
    print(
        "--------------------------------------------------------------------------------------------------------------------------------------------")
    print('Con 50 ciclos y contrincante Minimax:')
    tiempo_entrenamiento, tasa_victorias, tasa_derrotas, tasa_empates = evaluacion_agente(50, 2)
    print('Tiempo de entrenamiento: ', tiempo_entrenamiento)
    print('Tasa de victorias:', tasa_victorias)
    print('Tasa de derrotas:', tasa_derrotas)
    print('Tasa de empates:', tasa_empates)
    print()
    print('Con 100 ciclos y contrincante Minimax:')
    tiempo_entrenamiento, tasa_victorias, tasa_derrotas, tasa_empates = evaluacion_agente(100, 2)
    print('Tiempo de entrenamiento: ', tiempo_entrenamiento)
    print('Tasa de victorias:', tasa_victorias)
    print('Tasa de derrotas:', tasa_derrotas)
    print('Tasa de empates:', tasa_empates)
    print()
    print('Con 150 ciclos y contrincante Minimax:')
    tiempo_entrenamiento, tasa_victorias, tasa_derrotas, tasa_empates = evaluacion_agente(150, 2)
    print('Tiempo de entrenamiento: ', tiempo_entrenamiento)
    print('Tasa de victorias:', tasa_victorias)
    print('Tasa de derrotas:', tasa_derrotas)
    print('Tasa de empates:', tasa_empates)
    print()
    print('Con 200 ciclos y contrincante Minimax:')
    tiempo_entrenamiento, tasa_victorias, tasa_derrotas, tasa_empates = evaluacion_agente(200, 2)
    print('Tiempo de entrenamiento: ', tiempo_entrenamiento)
    print('Tasa de victorias:', tasa_victorias)
    print('Tasa de derrotas:', tasa_derrotas)
    print('Tasa de empates:', tasa_empates)
    print()
    print('Con 250 ciclos y contrincante Minimax:')
    tiempo_entrenamiento, tasa_victorias, tasa_derrotas, tasa_empates = evaluacion_agente(250, 2)
    print('Tiempo de entrenamiento: ', tiempo_entrenamiento)
    print('Tasa de victorias:', tasa_victorias)
    print('Tasa de derrotas:', tasa_derrotas)
    print('Tasa de empates:', tasa_empates)
    print()
    print('Con 300 ciclos y contrincante Minimax:')
    tiempo_entrenamiento, tasa_victorias, tasa_derrotas, tasa_empates = evaluacion_agente(300, 2)
    print('Tiempo de entrenamiento: ', tiempo_entrenamiento)
    print('Tasa de victorias:', tasa_victorias)
    print('Tasa de derrotas:', tasa_derrotas)
    print('Tasa de empates:', tasa_empates)
    print()


def minimax_vs_alfabeta(n_minimax, n_alfabeta):
    tiempo_individual_minimax = 0
    tiempo_individual_alfabeta = 0
    duracion_partida = 0
    victorias_minimax = 0
    victorias_alfabeta = 0
    empates = 0
    for i in range(100):
        tablero = Tablero()
        turno = -1
        jugador_minimax = 1
        jugador_alfabeta = -1
        inicio_juego = time.time()
        print(i)
        while not tablero.finDeJuego():
            if turno == 1:
                inicio_turno = time.time()
                minimax.N_LIMIT = n_minimax
                movimiento = minimax(tablero, n_minimax, jugador_minimax)
                if movimiento:
                    x, y = movimiento
                    tablero.colocar_ficha_nueva(x, y, jugador_minimax)
                fin_turno = time.time()
                tiempo_individual_minimax += (fin_turno - inicio_turno)
                turno = -1
            elif turno == -1:
                inicio_turno = time.time()
                minimax.N_LIMIT = n_alfabeta
                movimiento = minimax_alfa_beta(tablero, n_alfabeta, jugador_alfabeta)
                if movimiento:
                    x, y = movimiento
                    tablero.colocar_ficha_nueva(x, y, jugador_alfabeta)
                fin_turno = time.time()
                tiempo_individual_alfabeta += (fin_turno - inicio_turno)
                turno = 1
        fin_juego = time.time()
        duracion_partida += (fin_juego - inicio_juego)
        result = tablero.calcular_resultado()
        if result == jugador_minimax:
            victorias_minimax += 1
        elif result == jugador_alfabeta:
            victorias_alfabeta += 1
        else:
            empates += 1

    duracion_media_turno_minimax = tiempo_individual_minimax/100
    duracion_media_turno_alfabeta = tiempo_individual_alfabeta/100
    duracion_media_partida = duracion_partida/100

    return duracion_media_turno_minimax, duracion_media_turno_alfabeta, duracion_media_partida, victorias_minimax, victorias_alfabeta, empates


def minimax_vs_agenteRL(poda, n, agente):
    tiempo_individual_minimax = 0
    tiempo_individual_agenterl = 0
    duracion_partida = 0
    victorias_minimax = 0
    victorias_agenterl = 0
    empates = 0
    for i in range(10):
        tablero = Tablero()
        jugador_minimax = 1
        jugador_agenterl = -1
        inicio_juego = time.time()
        while tablero.finDeJuego():
            if turno == 1:
                inicio_turno = time.time()
                if poda == False:
                    movimiento = minimax(tablero, n, jugador_minimax)
                    if movimiento:
                        x, y = movimiento
                        tablero.colocar_ficha_nueva(x, y, jugador_minimax)
                else:
                    movimiento = minimax_alfa_beta(tablero, n, jugador_minimax)
                    if movimiento:
                        x, y = movimiento
                        tablero.colocar_ficha_nueva(x, y, jugador_minimax)
                fin_turno = time.time()
                tiempo_individual_minimax += (fin_turno - inicio_turno)
                turno = -1
            elif turno == -1:
                inicio_turno = time.time()
                agente.tablero = tablero
                agente.jugar(tablero, jugador_agenterl)
                fin_turno = time.time()
                tiempo_individual_agenterl += (fin_turno - inicio_turno)
                turno = 1
        fin_juego = time.time()
        duracion_partida += (fin_juego - inicio_juego)
        result = tablero.calcular_resultado()
        if result == jugador_minimax:
            victorias_minimax += 1
        elif result == jugador_agenterl:
            victorias_agenterl += 1
        else:
            empates += 1

    duracion_media_turno_minimax = tiempo_individual_minimax/100
    duracion_media_turno_agenterl = tiempo_individual_minimax/100
    duracion_media_partida = duracion_partida/100

    return duracion_media_turno_minimax, duracion_media_turno_agenterl, duracion_media_partida, victorias_minimax, victorias_agenterl, empates


def evaluacion_agente(ciclos_entrenamiento, jugador):
    n = 5
    total_tasa_victorias = 0
    total_tasa_derrotas = 0
    total_tasa_empates = 0
    total_tiempo_entrenamiento = 0
    for i in range(n):
        print(i)
        inicio_entrenamiento = time.time()
        agente = entrenar_nuevo_agente(ciclos_entrenamiento, jugador)
        fin_entrenamiento = time.time()
        tiempo_entrenamiento = fin_entrenamiento - inicio_entrenamiento
        tasa_victorias, tasa_derrotas, tasa_empates = validacion_agente(agente, 50)
        total_tasa_victorias += tasa_victorias
        total_tasa_derrotas += tasa_derrotas
        total_tasa_empates += tasa_empates
        total_tiempo_entrenamiento += tiempo_entrenamiento
    return total_tiempo_entrenamiento/n, total_tasa_victorias/n, total_tasa_derrotas/n, total_tasa_empates/n


if __name__ == "__main__":
    tests()
