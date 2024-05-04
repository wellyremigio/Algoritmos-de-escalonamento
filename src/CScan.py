from datetime import datetime
import gc
import time
num_request = 8
tamanho_disco = 200
 
def CSCan(head, lista_requests):
    cont_seek = 0
    distancia = 0
    trilha_atual = 0
    left = []
    right = []
    sequencia_seek = []
    right.append(0)
    left.append(tamanho_disco - 1)

    for i in range(num_request):
        if (lista_requests[i] <= head):
            right.append(lista_requests[i])
        if (lista_requests[i] > head):
            left.append(lista_requests[i])
 
    right.sort()
    left.sort()

    for i in range(len(right)):
        trilha_atual = right[i]
        sequencia_seek.append(trilha_atual)
        distancia = abs(trilha_atual - head)
        cont_seek += distancia
        head = trilha_atual
 
    head = 0
    cont_seek += (tamanho_disco - 1)

    for i in range(len(left)):
        trilha_atual = left[i]
        sequencia_seek.append(trilha_atual)
        distancia = abs(trilha_atual - head)
        cont_seek += distancia
        head = trilha_atual
 
    print("Total number of seek operations =",
          cont_seek)
    print("Seek Sequence is")
    print(*sequencia_seek, sep="\n")
 
#entrada_requisicoes = [112, 64, 21, 150, 77, 11, 6, 198]
#entrada_requisicoes = [1,2,3,4,5,6,7,8,9]
entrada_requisicoes = [481, 862, 379, 113, 572, 632, 82, 277, 185, 983, 890, 864, 589, 119, 476, 877, 456, 190, 607, 60, 746, 242, 903, 724, 908, 378, 666, 858, 382, 781, 199, 991, 347, 183, 912, 963, 662, 358, 842, 597, 489, 935, 937, 611, 820, 52, 543, 630, 795, 734, 690, 803, 878, 630, 292, 564, 640, 764, 930, 871, 576, 137, 801, 364, 447, 93, 777, 135, 998, 588, 848, 773, 64, 550, 57, 221, 738, 569, 595, 976, 233, 444, 47, 870, 96, 874, 855, 948, 831, 541, 490, 769, 312, 237, 203, 506, 584, 670]

head = 100
sequencia = sorted([i for i in range(100)])

before = time.time()
CSCan(head, sequencia)
after =  time.time() # Este é o tempo depois da execução da função
tempo_de_execucao = (after - before) * 1000
print("Before: ", before)
print("After: ", after)
print("Tempo de execucao: ",tempo_de_execucao, "ms")

gc.collect()

# 0.14591217041015625 ms
#0:00:00.998000 ms - random


