from minimax import AgenteRL


"""
ESTO DEBE ESTAR EN EL MAIN PRINCIPAL PARA EJECUTAR EL ALGORITMO
"""


q_rates = {0.5}

ciclos_entrenamiento = 100000
ciclos_entrenamiento_humano = 0

for q in q_rates:
    veces_ganadas = 0
    veces_perdidas = 0
    veces_empatadas = 0

    agente = AgenteRL(ciclos_entrenamiento)
    agente.set_q(q)
    for i in range(agente.n):
        agente.reset(True)
        agente.actualizar_alfa(i)
        # SE ELIGE SI VA A SER ENTRENADO CON UN JUGADOR ALEATORIO O CON UN JUGADOR MINIMAX

        # JUGADOR ALEATORIO
        agente.jugar_vs_random()

        # JUGADOR MINIMAX

        # JUGADOR HUMANO
        agente.set_n(ciclos_entrenamiento_humano)
        agente.set_alfa(0.7)
        for i in range(agente.n):
            agente.reset(True)
            agente.jugar_vs_humano()
