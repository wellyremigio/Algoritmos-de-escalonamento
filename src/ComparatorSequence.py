import matplotlib.pyplot as plt
import random
import copy
import CScan as cscan
import SSTF as sstf

def criar_lista_sequencial(start):
    return list(range(start, start + 100))

def criar_sequencia():
    return [criar_lista_sequencial(i * 100) for i in range(50)]

def gerar_head():
    return random.randint(0, 5000)

def chamar_alogoritmos():
    listas_sequenciais = criar_sequencia()
    head = gerar_head()
    latencias_cscan = [cscan.cscan(head, lista) for lista in listas_sequenciais]
    latencias_sstf = [sstf.sstf(head, lista) for lista in listas_sequenciais]
    tamanhos = [len(lista) for lista in listas_sequenciais]
    indices = list(range(1, len(listas_sequenciais) + 1))
    return indices, latencias_cscan , latencias_sstf

def gerar_grafico():
    indices, latencias_cscan, latencias_sstf = chamar_alogoritmos()
    plt.figure(figsize=(10, 6))
    plt.plot(indices, latencias_cscan, label='C-SCAN')
    plt.plot(indices, latencias_sstf, label='SSTF')
    plt.title("Sequência ordenanda com cabeça posicionada gerada aleatoriamente")
    plt.xlabel("Lista de Requisições")
    plt.ylabel("Distância Percorrida")
    plt.legend()
    plt.grid(True)
    plt.show()

