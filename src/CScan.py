

def cscan(bloco_inicial, lista_requisicoes):
    bloco_atual = bloco_inicial
    latencia_total = 0
    sequencia_atendimento = []  # Lista para armazenar a sequência de atendimentos
    tamanho_disco = 500
    left = []
    right = []
    tempo_seek = 0

    left.append(0)
    right.append(tamanho_disco-1)

    for i in range(len(lista_requisicoes)):
        if (lista_requisicoes[i] < bloco_inicial):
            left.append(lista_requisicoes[i])
        if (lista_requisicoes[i] > bloco_inicial):
            right.append(lista_requisicoes[i])

    # Dividindo a lista em left e right
    # left = [bloco for bloco in lista_requisicoes if bloco < bloco_atual]
    # right = [bloco for bloco in lista_requisicoes if bloco >= bloco_atual]

    # Ordena as solicitações em left e right
    left.sort()
    right.sort()

    # Servindo os blocos à direita
    for i in range(len(right)):
        proximo_bloco = right[i]
        sequencia_atendimento.append(proximo_bloco)  # Adicionando o bloco atendido à sequência
        tempo_seek += abs(proximo_bloco - bloco_atual)
        latencia_total = tempo_seek
        bloco_atual = proximo_bloco

    bloco_atual = 0
    tempo_seek += tamanho_disco -1

    # Servindo os blocos à esquerda
    for i in range(len(left)):
        proximo_bloco = left[i]
        sequencia_atendimento.append(proximo_bloco)  # Adicionando o bloco atendido à sequência
        tempo_seek += abs(proximo_bloco - bloco_atual)
        latencia_total = tempo_seek
        bloco_atual = proximo_bloco
        
    return latencia_total