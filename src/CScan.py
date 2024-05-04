def calculando_latencia_por_requisicao(tempo_seek): 
    tempo_transferencia = 4 / 125   #4KB / 125MB
    latencia_rotacao = 2 
    result = tempo_seek + latencia_rotacao + tempo_transferencia
    return result

def cscan(bloco_inicial, lista_requisicoes):
    bloco_atual = bloco_inicial
    num_total_seeks = 0
    latencia_total = 0
    # Dividindo a lista em left e right
    left = [bloco for bloco in lista_requisicoes if bloco < bloco_atual]
    right = [bloco for bloco in lista_requisicoes if bloco >= bloco_atual]

    # Ordena as solicitações em left e right
    left.sort(reverse=True)
    right.sort()

    # Servindo os blocos à direita
    while right:
        proximo_bloco = right.pop(0)
        tempo_seek = 4 if bloco_atual // 8 != proximo_bloco // 8 else 0
        latencia_total += calculando_latencia_por_requisicao(tempo_seek)
        bloco_atual = proximo_bloco

    # Servindo os blocos à esquerda
    while left:
        proximo_bloco = left.pop(0)
        tempo_seek = 4 if bloco_atual // 8 != proximo_bloco // 8 else 0
        latencia_total += calculando_latencia_por_requisicao(tempo_seek)
        bloco_atual = proximo_bloco
    return latencia_total


entrada_requisicoes1 = [90, 35, 71, 14, 56, 25, 83, 160, 46, 48]
entrada_requisicoes2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
entrada_requisicoes3 = [2, 3, 92, 567, 421, 689, 134, 876, 349, 598, 5]


head = 5
latencia_total1 = cscan(head, entrada_requisicoes1)
print("Tempo total de latencia 1:", latencia_total1, "ms")

latencia_total2 = cscan(head, entrada_requisicoes2)
print("Tempo total de latencia 2:", latencia_total2, "ms")

latencia_total3 = cscan(head, entrada_requisicoes3)
print("Tempo total de latencia 3:", latencia_total3, "ms")

