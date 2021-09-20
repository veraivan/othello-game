# othello-game

Agentes que juegan de forma inteligente contra un humano el juego Othello/Reversi, usando técnicas de IA.

### Devs
-----
- José Benitez
- Ivan Vera 

## Algoritmos 
-----

**Basados en busqueda con Adversario**
- Minimax
- Minimax con poda Alfa-Beta 

**Basado en aprendizaje**
- Reinforcement Learning 


## Instalación y juego: 
-----
>Tener instalado python3 en la maquina

**Instalar la siguiente libreria:** 
```sh 
pip3 install pygame
```

**Para comenzar a jugar ejecute:** 
```sh
python3 main.py
```

## Test
-----
Los test realizados se basan en hacerle jugar a los agentes entre ellos y analizar la cantidad de victorias, derrotas o empates. El aprendizaje por refuerzo es entrenado a partir de un Minimax y Minimax con poda.

**Ejecutar test:**
```sh
python3 test.py
```
