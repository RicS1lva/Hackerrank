saldo_atual = float(input())
valor_deposito = float(input())
valor_saque = float(input())

def saldo_final(saldo, deposito, saque):
    saldo_final = saldo
    saldo_final += deposito
    saldo_final -= saque

    return saldo_final

print(f'Saldo atualizado na conta: {saldo_final(saldo_atual, valor_deposito, valor_saque):.1f}')