import matplotlib.pyplot as plt
import numpy as np
import random


import CScan as cscan
import SSTF as sstf

requests1 = list(np.random.randint(0, 100001, size=1000))
requests2 = list(np.random.randint(0, 100001, size=2000))
requests3 = list(np.random.randint(0, 100001, size=3000))
requests4 = list(np.random.randint(0, 100001, size=4000))
requests5 = list(np.random.randint(0, 100001, size=5000))
requests6 = list(np.random.randint(0, 100001, size=6000))
requests7 = list(np.random.randint(0, 100001, size=7000))

new_list = [
    requests1,
    requests2,
    requests3,
    requests4,
    requests5,
    requests6,
    requests7
]

#HEAD NO MENOR ELEMENTO DA LISTA

# Calculando o tamanho das listas de requisições
tamanhos = list(map(len, new_list))

# Calculando a latência total para cada conjunto de requisições e bloco inicial usando C-SCAN e SSTF
latencias_cscan = [cscan.cscan(0, new_list [i]) for i in range(len(new_list ))]
latencias_sstf = [sstf.sstf_com_latency(min (new_list [i]), new_list [i]) for i in range(len(new_list ))]

print("menor cscan" ,latencias_cscan )
print("menor sstf" ,latencias_sstf )



# Plotando o gráfico de linha
plt.figure(figsize=(10, 6))

# Plotando os dados de latência para cada algoritmo
plt.plot(tamanhos, latencias_cscan, label='C-SCAN', marker='o')
plt.plot(tamanhos, latencias_sstf, label='SSTF', marker='o')

plt.title("Randon com head posionado no inicio")
plt.xlabel("Tamanho das Listas de Requisições")
plt.ylabel("Latência Total (ms)")
plt.xticks(tamanhos)
plt.legend()

plt.grid(True)
plt.show()


requests1 = list(np.random.randint(0, 100001, size=1000))
requests2 = list(np.random.randint(0, 100001, size=2000))
requests3 = list(np.random.randint(0, 100001, size=3000))
requests4 = list(np.random.randint(0, 100001, size=4000))
requests5 = list(np.random.randint(0, 100001, size=5000))
requests6 = list(np.random.randint(0, 100001, size=6000))
requests7 = list(np.random.randint(0, 100001, size=7000))

new_list = [
    requests1,
    requests2,
    requests3,
    requests4,
    requests5,
    requests6,
    requests7
]

#HEAD NO MAIOR ELEMENTO DA LISTA

# Calculando o tamanho das listas de requisições
tamanhos = list(map(len, new_list))

# Calculando a latência total para cada conjunto de requisições e bloco inicial usando C-SCAN e SSTF
latencias_cscan = [cscan.cscan(200, new_list [i]) for i in range(len(new_list ))]
latencias_sstf = [sstf.sstf_com_latency(max(new_list [i]), new_list [i]) for i in range(len(new_list ))]
print("maior cscan" ,latencias_cscan )
print("maior sstf" ,latencias_sstf )

# Plotando o gráfico de linha
plt.figure(figsize=(10, 6))

# Plotando os dados de latência para cada algoritmo
plt.plot(tamanhos, latencias_cscan, label='C-SCAN', marker='o')
plt.plot(tamanhos, latencias_sstf, label='SSTF', marker='o')

plt.title("Randon com head posionado no final")
plt.xlabel("Tamanho das Listas de Requisições")
plt.ylabel("Latência Total (ms)")
plt.xticks(tamanhos)
plt.legend()

plt.grid(True)
plt.show()

requests1 = list(np.random.randint(0, 100001, size=1000))
requests2 = list(np.random.randint(0, 100001, size=2000))
requests3 = list(np.random.randint(0, 100001, size=3000))
requests4 = list(np.random.randint(0, 100001, size=4000))
requests5 = list(np.random.randint(0, 100001, size=5000))
requests6 = list(np.random.randint(0, 100001, size=6000))
requests7 = list(np.random.randint(0, 100001, size=7000))

new_list = [
    requests1,
    requests2,
    requests3,
    requests4,
    requests5,
    requests6,
    requests7
]

#HEAD NO ELEMENTO DO MEIO 

tamanhos = list(map(len, new_list))

# Calculando a latência total para cada conjunto de requisições e bloco inicial usando C-SCAN e SSTF
latencias_cscan = [cscan.cscan(max(new_list [i]) //2 , new_list [i]) for i in range(len(new_list ))]
latencias_sstf = [sstf.sstf_com_latency(max(new_list [i])// 2, new_list [i]) for i in range(len(new_list ))]
print("maior cscan" ,latencias_cscan )
print("maior sstf" ,latencias_sstf )    

# Plotando o gráfico de linha
plt.figure(figsize=(10, 6))

# Plotando os dados de latência para cada algoritmo
plt.plot(tamanhos, latencias_cscan, label='C-SCAN', marker='o')
plt.plot(tamanhos, latencias_sstf, label='SSTF', marker='o')

plt.title("Randon com head posionado no meio")
plt.xlabel("Tamanho das Listas de Requisições")
plt.ylabel("Latência Total (ms)")
plt.xticks(tamanhos)
plt.legend()

plt.grid(True)
plt.show()

