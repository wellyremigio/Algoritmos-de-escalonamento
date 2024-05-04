def latencia_sstf(bloco_atual, bloco_destino):
    rotacao = 2  # 2ms de tempo de rotação
    transferencia = 4 / 125  # Tempo de transferência de 4KB a 125MB/s
    
    if bloco_atual // 8 != bloco_destino // 8: #Cada trilha possui 8 segmentos
        seek = 4 
    else:
        seek = 0
    
    latencia_total = seek + rotacao + transferencia
    return latencia_total

def sstf_com_latency(requisicoes, bloco_inicial):
    bloco_atual = bloco_inicial
    total_latencia = 0
    
    requisicoes.sort()

    while requisicoes:

        proxima_requisicao = min(requisicoes, key=lambda x: abs(x - bloco_atual))
        total_latencia += latencia_sstf(bloco_atual, proxima_requisicao)
        bloco_atual = proxima_requisicao
        requisicoes.remove(proxima_requisicao)  # Remove a requisição atendida

    return total_latencia

bloco_inicial = 5

lista_requisicoes1 = [90, 35, 71, 14, 56, 25, 83, 160, 46, 48]
total_latencia = sstf_com_latency(lista_requisicoes1, bloco_inicial)
print("Tempo total de latência:", total_latencia, "ms")


lista_requisicoes2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total_latencia = sstf_com_latency(lista_requisicoes2, bloco_inicial)
print("Tempo total de latência:", total_latencia, "ms")

lista_requisicoes3 = [2, 3, 92, 567, 421, 689, 134, 876, 349, 598, 5]
total_latencia = sstf_com_latency(lista_requisicoes3, bloco_inicial)
print("Tempo total de latência:", total_latencia, "ms")
