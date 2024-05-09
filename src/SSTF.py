def calcular_tempo_seek(bloco_atual, proximo_bloco):
    tempo_seek = 0
    
    if bloco_atual // 8 != proximo_bloco // 8:
        tempo_seek = abs(proximo_bloco // 8 - bloco_atual // 8)
    return tempo_seek

def sstf_com_latency(bloco_inicial, requisicoes):
    print(requisicoes)
    print(bloco_inicial)
    bloco_atual = bloco_inicial
    total_latencia = 0
    
    requisicoes.sort()

    while requisicoes:

        proxima_requisicao = min(requisicoes, key=lambda x: abs(x - bloco_atual))
        total_latencia += calcular_tempo_seek(bloco_atual, proxima_requisicao)
        bloco_atual = proxima_requisicao
        requisicoes.remove(proxima_requisicao) 
    return total_latencia
