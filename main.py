# Exercício RLC - Autor: Maria Braga - Disciplina: Eletrônica de Potência - P2

# Objetivo:
# Obter a resposta temporal da corrente no indutor e da 
# tensão no capacitor durante o funcionamento do circuito.

# Etapa 1: circuito série (Capacitor + Indutor)
# Etapa 2: circuito paralelo (Capacitor + Resistor + Indutor)

import numpy
import matplotlib.pyplot
from scipy.integrate import solve_ivp

# Parâmetros do circuito
V0 = 900          # [V] tensão inicial do capacitor (Vc)
L = 11e-6            # [H] indutância da bobina
R = 85e-3           # [Ohm] resistência
C = 180e-6         # [F] capacitância

# Equações diferenciais do circuito

def circuito(t, y):
    i, vC = y

    # Etapa 1: diodo desligado (C e L em série)
    if vC > 0:
        di_dt = vC / L               # tensão do capacitor acelera a corrente
        dv_dt = -i / C               # corrente descarrega o capacitor

    # Etapa 2: diodo conduz (C, R e L em paralelo)
    else:
        di_dt = (vC - R * i) / L
        dv_dt = -(i + vC / R) / C

    return [di_dt, dv_dt]

# Condições iniciais e tempo de simulação

i0 = 0.0
v0 = V0
condicoes_iniciais = [i0, v0]

t0 = 0.0
tf = 600e-6
t_eval = numpy.linspace(t0, tf, 5000)

# Resolução numérica

solucao = solve_ivp(circuito, [t0, tf], condicoes_iniciais, t_eval = t_eval)

tempo = solucao.t
corrente = solucao.y[0]
tensao = solucao.y[1]

# Gráficos

matplotlib.pyplot.figure(figsize=(9, 6))

# Corrente no indutor
matplotlib.pyplot.subplot(2, 1, 1) #Gráfico 1
matplotlib.pyplot.plot(tempo * 1e6, corrente, color='blue')
matplotlib.pyplot.title("Resposta Temporal do Circuito RLC com Diodo - INDUTOR e CAPACITOR")
matplotlib.pyplot.ylabel("Corrente no Indutor [A]")
matplotlib.pyplot.grid(True)

# Tensão no capacitor
matplotlib.pyplot.subplot(2, 1, 2) #Gráfico 2
matplotlib.pyplot.plot(tempo * 1e6, tensao, color='green')
matplotlib.pyplot.xlabel("Tempo [µs]")
matplotlib.pyplot.ylabel("Tensão no Capacitor [V]")
matplotlib.pyplot.grid(True)

matplotlib.pyplot.tight_layout()
matplotlib.pyplot.show()

# Resultados principais
print("===== Resultados da Simulação =====")
print(f"Corrente máxima no indutor: {numpy.max(corrente):.4f} A")
print(f"Tensão mínima no capacitor: {numpy.min(tensao):.4f} V")
print("===================================")