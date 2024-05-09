import matplotlib.pyplot as plt
import numpy as np
import CScan as cscan
import SSTF as sstf
import copy
import random

def criar_lista():
    return list(np.random.randint(0, 5000, size=100))

def criar_sequencia():
    return [criar_lista() for _ in range(100)]

def gerar_head():
    return random.randint(0, 5000)

def chamar_alogoritmos():
    listas_sequenciais = criar_sequencia()
    head = gerar_head()
    latencias_cscan = [cscan.cscan(head, lista) for lista in listas_sequenciais]
    latencias_sstf = [sstf.sstf(head, lista) for lista in listas_sequenciais]
    indices = list(range(1, len(listas_sequenciais) + 1))
    return indices, latencias_cscan , latencias_sstf

def gerar_grafico():
    indices, latencias_cscan, latencias_sstf = chamar_alogoritmos()
    plt.figure(figsize=(10, 6))
    plt.plot(indices, latencias_cscan, label='C-SCAN')
    plt.plot(indices, latencias_sstf, label='SSTF')
    plt.title("Sequência aleatória com cabeça gerada aleatoriamente")
    plt.xlabel("Lista de Requisições")
    plt.ylabel("Distância Percorrida")
    plt.legend()
    plt.grid(True)
    plt.show()