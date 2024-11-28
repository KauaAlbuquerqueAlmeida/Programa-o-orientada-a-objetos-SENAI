# from class import conta
conta = input ("Você ja posui uma conta? \n digite sim ou não")
if (conta == sim):
    print ("Função em desenvouvimento!")
else:
    print ("insira os dados para criar a sua conta-")
    titular = input ("insira o nome do usuario: ")
    numero = input ("insira seu numero de telefone: ")
    saldo = input ("insira o valor da conta: ")
    limite = input ("insira o limite da conta:")
    historico = {}
    comta = conta (titular, numero, saldo, limite, historico)



