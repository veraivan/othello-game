from minimax import AgenteRL


"""
ESTO DEBE ESTAR EN EL MAIN PRINCIPAL PARA EJECUTAR EL ALGORITMO
"""


q_rates = {0.5}

ciclos_entrenamiento = 100000

for q in q_rates:
    veces_ganadas = 0
    veces_perdidas = 0
    veces_empatadas = 0

    agente = AgenteRL(ciclos_entrenamiento)
    agente.set_q(q)
    for i in range(agente.n):
        agente.reset(True)
        agente.actualizar_alfa(i)
        agente.jugar_vs_random()
