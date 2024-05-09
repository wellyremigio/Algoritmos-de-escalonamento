def calcular_distancia(bloco_atual, proximo_bloco):
    tempo_seek = 0
    
    if bloco_atual // 50 != proximo_bloco // 50:
        tempo_seek = abs(proximo_bloco // 50 - bloco_atual // 50)
    return tempo_seek

def sstf(bloco_inicial, requisicoes):
    bloco_atual = bloco_inicial
    total_latencia = 0
    sequencia =[]
    
    requisicoes.sort()

    while requisicoes:

        proxima_requisicao = min(requisicoes, key=lambda x: abs(x - bloco_atual))
        total_latencia += calcular_distancia(bloco_atual, proxima_requisicao)
        bloco_atual = proxima_requisicao
        sequencia.append(bloco_atual)
        requisicoes.remove(proxima_requisicao)

    return total_latencia
