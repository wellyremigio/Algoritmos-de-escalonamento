
def sstf_com_latency(bloco_inicial, requisicoes):
    bloco_atual = bloco_inicial
    total_latencia = 0
    
    requisicoes.sort()

    while requisicoes:

        proxima_requisicao = min(requisicoes, key=lambda x: abs(x - bloco_atual))
        total_latencia += abs(proxima_requisicao - bloco_atual)
        bloco_atual = proxima_requisicao
        requisicoes.remove(proxima_requisicao) 
    return total_latencia
