def latencia_sstf(tempo_seek):
    rotacao = 2  # 2ms de tempo de rotação
    transferencia = 4 / 125  # Tempo de transferência de 4KB a 125MB/s
    latencia_total = tempo_seek + rotacao + transferencia
    return latencia_total

def sstf_com_latency(bloco_inicial, requisicoes):
    bloco_atual = bloco_inicial
    total_latencia = 0
    
    requisicoes.sort()

    while requisicoes:

        proxima_requisicao = min(requisicoes, key=lambda x: abs(x - bloco_atual))
        tempo_seek = 4 if bloco_atual // 8 != proxima_requisicao // 8 else 0
        total_latencia += latencia_sstf(tempo_seek)
        bloco_atual = proxima_requisicao
        requisicoes.remove(proxima_requisicao) 
    return total_latencia


# bloco_inicial = 5

# lista_requisicoes1 = [90, 35, 71, 14, 56, 25, 83, 160, 46, 48]
# total_latencia = sstf_com_latency( bloco_inicial, lista_requisicoes1)
# print("Tempo total de latência:", total_latencia, "ms")

# lista_requisicoes2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# total_latencia = sstf_com_latency(bloco_inicial, lista_requisicoes2)
# print("Tempo total de latência:", total_latencia, "ms")

# lista_requisicoes3 = [2, 3, 92, 567, 421, 689, 134, 876, 349, 598, 5]
# total_latencia = sstf_com_latency(bloco_inicial, lista_requisicoes3)
# print("Tempo total de latência:", total_latencia, "ms")