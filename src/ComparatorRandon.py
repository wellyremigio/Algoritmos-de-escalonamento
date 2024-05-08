import matplotlib.pyplot as plt
import numpy as np
import CScan as cscan
import SSTF as sstf


requests0 = list(np.random.randint(0, 10, size=1))
requests1 = list(np.random.randint(0, 10000, size=1000))
requests2 = list(np.random.randint(0, 20000, size=2000))
requests3 = list(np.random.randint(0, 30000, size=3000))
requests4 = list(np.random.randint(0, 40000, size=4000))
requests5 = list(np.random.randint(0, 50000, size=5000))
requests6 = list(np.random.randint(0, 60000, size=6000))
requests7 = list(np.random.randint(0, 70000, size=7000))
requests8 = list(np.random.randint(0, 80000, size=8000))
requests9 = list(np.random.randint(0, 90000, size=9000))
requests10 = list(np.random.randint(0, 100000, size=10000))

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

#HEAD NO ELEMENTO DO MEIO 

tamanhos = list(map(len, new_list))

# Calculando a latência total para cada conjunto de requisições e bloco inicial usando C-SCAN e SSTF
latencias_cscan = [cscan.cscan(max(new_list [i]) //2 , new_list [i]) for i in range(len(new_list ))]
latencias_sstf = [sstf.sstf_com_latency(max(new_list [i])// 2, new_list [i]) for i in range(len(new_list ))] 

# Plotando o gráfico de linha
plt.figure(figsize=(10, 6))

# Plotando os dados de latência para cada algoritmo
plt.plot(tamanhos, latencias_cscan, label='C-SCAN', marker='o')
plt.plot(tamanhos, latencias_sstf, label='SSTF', marker='o')

plt.title("Randon com head posionado no meio")
plt.xlabel("Tamanho das Listas de Requisições")
plt.ylabel("D")
plt.xticks(tamanhos)
plt.legend()

plt.grid(True)
plt.show()

requests0 = list(np.random.randint(0, 10, size=1))
requests1 = list(np.random.randint(0, 10000, size=1000))
requests2 = list(np.random.randint(0, 20000, size=2000))
requests3 = list(np.random.randint(0, 30000, size=3000))
requests4 = list(np.random.randint(0, 40000, size=4000))
requests5 = list(np.random.randint(0, 50000, size=5000))
requests6 = list(np.random.randint(0, 60000, size=6000))
requests7 = list(np.random.randint(0, 70000, size=7000))
requests8 = list(np.random.randint(0, 80000, size=8000))
requests9 = list(np.random.randint(0, 90000, size=9000))
requests10 = list(np.random.randint(0, 100000, size=10000))

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

#HEAD NO MAIOR ELEMENTO DA LISTA

# Calculando o tamanho das listas de requisições
tamanhos = list(map(len, new_list))

# Calculando a latência total para cada conjunto de requisições e bloco inicial usando C-SCAN e SSTF
latencias_cscan = [cscan.cscan(max(new_list [i]), new_list [i]) for i in range(len(new_list ))]
latencias_sstf = [sstf.sstf_com_latency(max(new_list [i]), new_list [i]) for i in range(len(new_list ))]

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

