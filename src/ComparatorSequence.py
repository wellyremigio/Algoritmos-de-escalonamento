import matplotlib.pyplot as plt
import numpy as np

import CScan as cscan
import SSTF as sstf

requests1 = list(range(1000))
requests2 = list(range(2000))
requests3 = list(range(3000))
requests4 = list(range(4000))
requests5 = list(range(5000))
requests6 = list(range(6000))
requests7 = list(range(7000))

new_list = [
    requests1,
    requests2,
    requests3,
    requests4,
    requests5,
    requests6,
    requests7
]
# new_list = [
#     requests7
# ]


#HEAD no começo
# Calculando o tamanho das listas de requisições
tamanhos = list(map(len, new_list))

# Calculando a latência total para cada conjunto de requisições e bloco inicial usando C-SCAN e SSTF
# latencias_cscan = [cscan.cscan(0, new_list [i]) for i in range(len(new_list ))]
# latencias_sstf = [sstf.sstf_com_latency(0, new_list [i]) for i in range(len(new_list ))]

latencias_cscan = [cscan.cscan(0, new_list [i]) for i in range(len(new_list ))]
latencias_sstf = [sstf.sstf_com_latency(min(new_list [i]), new_list [i]) for i in range(len(new_list ))]
print("maior cscan" ,latencias_cscan )
print("maior sstf" ,latencias_sstf )  

# Plotando o gráfico de linha
plt.figure(figsize=(10, 6))

# Plotando os dados de latência para cada algoritmo
plt.plot(tamanhos, latencias_cscan, label='C-SCAN', marker='o')
plt.plot(tamanhos, latencias_sstf, label='SSTF', marker='o')

plt.title("Em ordem com head posionado no inicio")
plt.xlabel("Tamanho das Listas de Requisições")
plt.ylabel("Latência Total (ms)")
plt.xticks(tamanhos)
plt.legend()

plt.grid(True)
plt.show()


#HEAD no meio 

requests1 = list(range(1000))
requests2 = list(range(2000))
requests3 = list(range(3000))
requests4 = list(range(4000))
requests5 = list(range(5000))
requests6 = list(range(6000))
requests7 = list(range(7000))

new_list = [
    requests1,
    requests2,
    requests3,
    requests4,
    requests5,
    requests6,
    requests7
]

# Calculando o tamanho das listas de requisições
tamanhos = list(map(len, new_list))

# Calculando a latência total para cada conjunto de requisições e bloco inicial usando C-SCAN e SSTF
latencias_cscan = [cscan.cscan(max(new_list [i])//2, new_list [i]) for i in range(len(new_list ))]
latencias_sstf = [sstf.sstf_com_latency(max(new_list [i]) //2, new_list [i]) for i in range(len(new_list ))]
print("maior cscan" ,latencias_cscan )
print("maior sstf" ,latencias_sstf )  

# Plotando o gráfico de linha
plt.figure(figsize=(10, 6))

# Plotando os dados de latência para cada algoritmo
plt.plot(tamanhos, latencias_cscan, label='C-SCAN', marker='o')
plt.plot(tamanhos, latencias_sstf, label='SSTF', marker='o')

plt.title("Em ordem com head posionado no meio")
plt.xlabel("Tamanho das Listas de Requisições")
plt.ylabel("Latência Total (ms)")
plt.xticks(tamanhos)
plt.legend()

plt.grid(True)
plt.show()


#HEAD no final
requests1 = list(range(1000))
requests2 = list(range(2000))
requests3 = list(range(3000))
requests4 = list(range(4000))
requests5 = list(range(5000))
requests6 = list(range(6000))
requests7 = list(range(7000))

new_list = [
    requests1,
    requests2,
    requests3,
    requests4,
    requests5,
    requests6,
    requests7
]

# Calculando o tamanho das listas de requisições
tamanhos = list(map(len, new_list))

# Calculando a latência total para cada conjunto de requisições e bloco inicial usando C-SCAN e SSTF
# latencias_cscan = [cscan.cscan(max(new_list [i]), new_list [i]) for i in range(len(new_list ))]
latencias_cscan = [cscan.cscan(200, new_list [i]) for i in range(len(new_list ))]
latencias_sstf = [sstf.sstf_com_latency(max(new_list [i]), new_list [i]) for i in range(len(new_list ))]
print("maior cscan" ,latencias_cscan )
print("maior sstf" ,latencias_sstf )  
# latencias_cscan = [cscan.cscan(min(new_list [i]), new_list [i]) for i in range(len(new_list ))]
# latencias_sstf = [sstf.sstf_com_latency(min(new_list [i]), new_list [i]) for i in range(len(new_list ))]


# Plotando o gráfico de linha
plt.figure(figsize=(10, 6))

# Plotando os dados de latência para cada algoritmo
plt.plot(tamanhos, latencias_cscan, label='C-SCAN', marker='o')
plt.plot(tamanhos, latencias_sstf, label='SSTF', marker='o')

plt.title("Em ordem com head posionado no final")
plt.xlabel("Tamanho das Listas de Requisições")
plt.ylabel("Latência Total (ms)")
plt.xticks(tamanhos)
plt.legend()

plt.grid(True)
plt.show()