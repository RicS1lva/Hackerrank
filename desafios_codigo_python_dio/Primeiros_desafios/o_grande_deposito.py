valor = float(input())

if valor == 0:
    print(f'Encerrando o programa...')

elif valor < 0:
    print(f'Valor invalido! Digite um valor maior que zero.')

else:
    print(f'Deposito realizado com sucesso!\nSaldo atual: R$ {valor}')