def calcular_distancia(bloco_atual, proximo_bloco):
    distancia_seek = 0

    if bloco_atual // 50 != proximo_bloco // 50:
        distancia_seek = abs(proximo_bloco // 50 - bloco_atual // 50)
    return distancia_seek

def cscan(bloco_inicial, lista_requisicoes):
    bloco_atual = bloco_inicial
    latencia_total = 0
    tamanho_lista_requisicoes = 5000
    left = []
    right = []
    distancia_seek = 0

    left.append(0)
    right.append(tamanho_lista_requisicoes-1)

    for i in range(len(lista_requisicoes)):
        if (lista_requisicoes[i] < bloco_inicial):
            left.append(lista_requisicoes[i])
        if (lista_requisicoes[i] > bloco_inicial):
            right.append(lista_requisicoes[i])

    left.sort()
    right.sort()

    # Servindo os blocos à direita
    for i in range(len(right)):
        proximo_bloco = right[i]
        distancia_seek = calcular_distancia(bloco_atual, proximo_bloco)
        latencia_total += distancia_seek
        bloco_atual = proximo_bloco

    bloco_atual = 0
    distancia_seek = (tamanho_lista_requisicoes-1) // 50
    latencia_total += distancia_seek

    # Servindo os blocos à esquerda
    for i in range(len(left)):
        proximo_bloco = left[i]
        distancia_seek = calcular_distancia(bloco_atual, proximo_bloco)
        latencia_total += distancia_seek
        bloco_atual = proximo_bloco

    return latencia_total