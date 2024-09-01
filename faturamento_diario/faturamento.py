import json

def processar_faturamento(arquivo_json):
    with open(arquivo_json, 'r') as f:
        dados = json.load(f)

    faturamentos = [item['valor'] for item in dados['faturamento_diario']]

    faturamentos_validos = [valor for valor in faturamentos if valor > 0]

    menor_valor = min(faturamentos_validos)
    maior_valor = max(faturamentos_validos)

    media_mensal = sum(faturamentos_validos) / len(faturamentos_validos)
    dias_acima_media = sum(1 for valor in faturamentos_validos if valor > media_mensal)

    return menor_valor, maior_valor, dias_acima_media


arquivo_json = "faturamento_diario/faturamento.json"
menor, maior, dias_acima_media = processar_faturamento(arquivo_json)

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Número de dias acima da média: {dias_acima_media}")