import matplotlib.pyplot as plt
import numpy as np

import CScan as cscan
import SSTF as sstf

#HEAD no meio 

requests0 = list(range(1))
requests1 = list(range(1000))
requests2 = list(range(2000))
requests3 = list(range(3000))
requests4 = list(range(4000))
requests5 = list(range(5000))
requests6 = list(range(6000))
requests7 = list(range(7000))
requests8 = list(range(8000))
requests9 = list(range(9000))
requests10 = list(range(10000))

new_list = [
    requests0,
    requests1,
    requests2,
    requests3,
    requests4,
    requests5,
    requests6,
    requests7,
    requests8,
    requests9,
    requests10
]

# Calculando o tamanho das listas de requisições
tamanhos = list(map(len, new_list))

# Calculando a latência total para cada conjunto de requisições e bloco inicial usando C-SCAN e SSTF
latencias_cscan = [cscan.cscan(max(new_list[i])//2, new_list [i]) for i in range(len(new_list ))]
latencias_sstf = [sstf.sstf_com_latency(max(new_list[i]) //2, new_list [i]) for i in range(len(new_list ))]
print("maior cscan" ,latencias_cscan )
print("maior sstf" ,latencias_sstf )  

# Plotando o gráfico de linha
plt.figure(figsize=(10, 6))

# Plotando os dados de latência para cada algoritmo
plt.plot(tamanhos, latencias_cscan, label='C-SCAN', marker='o')
plt.plot(tamanhos, latencias_sstf, label='SSTF', marker='o')

plt.title("Sequencial com head na requisição do meio")
plt.xlabel("Tamanho das Listas de Requisições")
plt.ylabel("Distância Percorrida")
plt.xticks(tamanhos)
plt.legend()

plt.grid(True)
plt.show()


#HEAD no final
requests0 = list(range(1))
requests1 = list(range(1000))
requests2 = list(range(2000))
requests3 = list(range(3000))
requests4 = list(range(4000))
requests5 = list(range(5000))
requests6 = list(range(6000))
requests7 = list(range(7000))
requests8 = list(range(8000))
requests9 = list(range(9000))
requests10 = list(range(10000))

new_list = [
    requests0,
    requests1,
    requests2,
    requests3,
    requests4,
    requests5,
    requests6,
    requests7,
    requests8,
    requests9,
    requests10
]

# Calculando o tamanho das listas de requisições
tamanhos = list(map(len, new_list))

latencias_cscan = [cscan.cscan(max(new_list[i]), new_list[i]) for i in range(len(new_list ))]
latencias_sstf = [sstf.sstf_com_latency(max(new_list [i]), new_list [i]) for i in range(len(new_list ))]

# Plotando o gráfico de linha
plt.figure(figsize=(10, 6))

# Plotando os dados de latência para cada algoritmo
plt.plot(tamanhos, latencias_cscan, label='C-SCAN', marker='o')
plt.plot(tamanhos, latencias_sstf, label='SSTF', marker='o')

plt.title("Sequencial com head na requisição do meio")
plt.xlabel("Tamanho das Listas de Requisições")
plt.ylabel("Distância Percorrida")
plt.xticks(tamanhos)
plt.legend()

plt.grid(True)
plt.show()