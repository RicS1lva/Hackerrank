valor_inicial = float(input())
taxa_juros_anual = float(input())
periodo_anos = int(input())

valor_final = valor_inicial

for ano in range(periodo_anos):
    juros_anual = taxa_juros_anual * valor_final
    valor_final += juros_anual

print(f'Valor final do investimento: R$ {valor_final:.2f}')
