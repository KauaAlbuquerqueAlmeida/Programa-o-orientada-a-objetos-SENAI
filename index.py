from metodos import conta
loga = input ("Você ja posui uma conta? \n digite sim ou não: ")
if (loga == "sim"):
    print ("Função em desenvouvimento!")
else:
    print ("insira os dados para criar a sua conta-")
    titular = input ("insira o nome do usuario: ")
    numero = input ("insira seu numero de telefone: ")
    saldo = int(input ("insira o valor da conta: "))
    limite = int(input("insira o limite da conta:"))
    historico = {}
    # cliente1 = 
    conta1 = conta ( numero,titular, saldo, limite, historico)
    valido = 1
    while( valido == 1 ):
        print (f"bem vindo ao Menu! usuario {conta1.titular}")
        fazer = int(input("O que você quer fazer? \n --------------------------------\n digite 1 para sacar; \n digite 2 para Depositar; \n digite 3 para emitir Extrato; \n digite 4 para emitir historico; \n digite 5 para sair "))
        if (fazer == 1):
            saque = int(input("insira o valor do saque:"))
            conta1.sacar(saque)
            print (f"saque de {saque} na conta do cliente {conta1.titular} realizado com susseso!")
        elif (fazer == 2):
            Depositar = int(input("insira o valor do deposito:"))
            conta1.depositar(Depositar)
            print (f"deposito de {Depositar} na conta do cliente {conta1.titular} realizado com susseso!")
        elif (fazer == 3):
            conta1.extrato()
        elif (fazer == 4):
            print (conta1.saidas)
        elif (fazer == 5):
            valido = 0 

print ("adeus")





