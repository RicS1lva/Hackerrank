ativos = []

qtde_ativos_usuario = int(input())

for _ in range(qtde_ativos_usuario):
    tipo_ativo = str(input())
    ativos.append(tipo_ativo)

ativos.sort()

for item in ativos:
    print(item)
