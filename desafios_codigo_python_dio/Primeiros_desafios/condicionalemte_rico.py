saldo_total = int(input())
valor_saque = int(input())

def saque(saldo, valor_saque):
    if saldo >= valor_saque:
        saldo -= valor_saque
        print(f'Saque realizado com sucesso. Novo saldo: {saldo}')
    
    else:
        print(f'Saldo insuficiente. Saque nao realizado!')


saque(saldo_total, valor_saque)