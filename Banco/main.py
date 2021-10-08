cliente_1 = Cliente("joao", "sousa", '333.333.333-02')
cliente_2 = Cliente("marcos", "oliveira jose", '111.111.111-03')

conta_1 = Conta('111', cliente_1, 1200, 1000)
conta_2 = Conta('222', cliente_2, 1000, 5000)

transferiu = conta_1.transfere(conta_2, 200)
if transferiu:
    print("transferencia realizada")
else:
    print("transferencia não realizada")
        
transferiu = conta_2.transfere(conta_1, 1300)
if transferiu:
    print("transferencia realizada")
else:
    print("transferencia não realizada")

print(f"saldo da conta 1: {conta_1.saldo}. Saldo da conta 2: {conta_2.saldo}")

conta_1.sacar(300)
conta_1.depositar(2000)

conta_1.exibir_historico()
conta_2.exibir_historico()
