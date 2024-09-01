faturamento_mensal = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

faturamento_total = sum(faturamento_mensal.values())

faturamento_percentual = {}

for estado in faturamento_mensal.keys():
    faturamento_percentual[estado] = (faturamento_mensal[estado] / faturamento_total) * 100

    print(f"{estado} -> {faturamento_percentual[estado]:.2f}%")
