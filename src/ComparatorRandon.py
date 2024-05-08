import matplotlib.pyplot as plt
import numpy as np
import CScan as cscan
import SSTF as sstf
import copy



requests0 = list(np.random.randint(0, 10, size=1))
requests1 = list(np.random.randint(0, 100000, size=1000))
requests2 = list(np.random.randint(0, 200000, size=2000))
requests3 = list(np.random.randint(0, 300000, size=3000))
requests4 = list(np.random.randint(0, 400000, size=4000))
requests5 = list(np.random.randint(0, 500000, size=5000))
requests6 = list(np.random.randint(0, 600000, size=6000))
requests7 = list(np.random.randint(0, 700000, size=7000))
requests8 = list(np.random.randint(0, 800000, size=8000))
requests9 = list(np.random.randint(0, 900000, size=9000))
requests10 = list(np.random.randint(0, 1000000, size=10000))

# Ordenando as listas
requests1.sort()
requests2.sort()
requests3.sort()
requests4.sort()
requests5.sort()
requests6.sort()
requests7.sort()
requests8.sort()
requests9.sort()
requests10.sort()

# Copiando as listas usando deepcopy para que não sejam modificadas
new_list1 = [copy.deepcopy(requests0),
             copy.deepcopy(requests1),
             copy.deepcopy(requests2),
             copy.deepcopy(requests3),
             copy.deepcopy(requests4),
             copy.deepcopy(requests5),
             copy.deepcopy(requests6),
             copy.deepcopy(requests7),
             copy.deepcopy(requests8),
             copy.deepcopy(requests9),
             copy.deepcopy(requests10)]

new_list2 = copy.deepcopy(new_list1)

# Criando new_list sem deepcopy, as listas nessa lista podem ser modificadas
new_list = [requests0,
            requests1,
            requests2,
            requests3,
            requests4,
            requests5,
            requests6,
            requests7,
            requests8,
            requests9,
            requests10]

# Criando head_menor_meio com o elemento do meio de cada lista
head_menor_meio = [0] + [np.random.randint(0, requests[len(requests)// 2])
    for requests in [requests1, 
                     requests2, 
                     requests3, 
                     requests4, 
                     requests5, 
                     requests6, 
                     requests7, 
                     requests8, 
                     requests9, 
                     requests10]]

head_maior_meio = [np.random.choice(requests[len(requests) // 2:]) 
    for requests in [requests0, 
                     requests1, 
                     requests2, 
                     requests3, 
                     requests4, 
                     requests5, 
                     requests6, 
                     requests7,  
                     requests8, 
                     requests9,   
                     requests10]]

#HEAD NO ELEMENTO DO MEIO 

tamanhos = list(map(len, new_list))

# Calculando a latência total para cada conjunto de requisições e bloco inicial usando C-SCAN e SSTF
latencias_cscan = [cscan.cscan(new_list[i][len(new_list[i]) //2], new_list [i]) for i in range(len(new_list))]
latencias_sstf = [sstf.sstf_com_latency(new_list[i][len(new_list[i]) //2], new_list [i]) for i in range(len(new_list ))] 

# Plotando o gráfico de linha
plt.figure(figsize=(10, 6))

# Plotando os dados de latência para cada algoritmo
plt.plot(tamanhos, latencias_cscan, label='C-SCAN', marker='o')
plt.plot(tamanhos, latencias_sstf, label='SSTF', marker='o')

plt.title("Sequência aleatória com head na requisição do meio")
plt.xlabel("Tamanho das Listas de Requisições")
plt.ylabel("Distância Percorrida")
plt.xticks(tamanhos)
plt.legend()

plt.grid(True)
plt.show()



#HEAD NO MAIOR ELEMENTO DA LISTA

# Calculando o tamanho das listas de requisições
tamanhos = list(map(len, new_list1))

# Calculando a latência total para cada conjunto de requisições e bloco inicial usando C-SCAN e SSTF
latencias_cscan = [cscan.cscan( new_list1[i][len(new_list1[i]) // 4], new_list1 [i]) for i in range(len(new_list1 ))]
latencias_sstf = [sstf.sstf_com_latency(new_list1[i][len(new_list1[i]) // 4], new_list1 [i]) for i in range(len(new_list1 ))]

# Plotando o gráfico de linha
plt.figure(figsize=(10, 6))

# Plotando os dados de latência para cada algoritmo
plt.plot(tamanhos, latencias_cscan, label='C-SCAN', marker='o')
plt.plot(tamanhos, latencias_sstf, label='SSTF', marker='o')

plt.title("Sequência aleatória com head aleatório do início ao meio")
plt.xlabel("Tamanho das Listas de Requisições")
plt.ylabel("Distância percorrida")
plt.xticks(tamanhos)
plt.legend()

plt.grid(True)
plt.show()




#HEAD NO MAIOR ELEMENTO DA LISTA

# Calculando o tamanho das listas de requisições
tamanhos = list(map(len, new_list2))

# Calculando a latência total para cada conjunto de requisições e bloco inicial usando C-SCAN e SSTF
latencias_cscan = [cscan.cscan( new_list2[i][len(new_list2[i]) *2 // 3], new_list2 [i]) for i in range(len(new_list2 ))]
latencias_sstf = [sstf.sstf_com_latency(new_list2[i][len(new_list2[i]) *2 // 3], new_list2 [i]) for i in range(len(new_list2 ))]

# Plotando o gráfico de linha
plt.figure(figsize=(10, 6))

# Plotando os dados de latência para cada algoritmo
plt.plot(tamanhos, latencias_cscan, label='C-SCAN', marker='o')
plt.plot(tamanhos, latencias_sstf, label='SSTF', marker='o')

plt.title("Sequência aleatória com head aleatório do meio para o fim")
plt.xlabel("Tamanho das Listas de Requisições")
plt.ylabel("Distância percorrida")
plt.xticks(tamanhos)
plt.legend()

plt.grid(True)
plt.show()