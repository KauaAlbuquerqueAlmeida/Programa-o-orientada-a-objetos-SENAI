class conta:
    def __init__(self, numero, titular, saldo, limite, saidas):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.saidas = saidas
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.saidas.append = {"entrada": valor, "valor_atual": self.saldo}
            return True
        else:
            return False
        
    def sacar(self, valor):
        if self.saldo >= valor and valor <= self.limite:

            self.saldo -= valor
            self.saidas.append = {"saida": valor, "valor_atual": self.saldo}
            return True
        else:
            return False
    
    
    def extrato(self):
        return f"Número da Conta: {self.numero}\nTitular: {self.titular}\nSaldo: R$ {self.saldo:.2f}\nLimite: R$ {self.limite:.2f} \n saidas: R$ {self.saidas:.2f}\n"

class Cliente:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)
        return True
    
    def remover_conta(self, numero):
        for i, conta in enumerate(self.contas):
            if conta.numero == numero:
                self.contas.pop(i)
                return True
        return False
    
    def buscar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None
    
    def extrato_total(self):
        total_entradas = 0
        total_saidas = 0
        total_saldo = 0
        
        for conta in self.contas:
            total_entradas += sum(saida["entrada"] for saida in conta.saidas)
            total_saidas += sum(saida["saida"] for saida in conta.saidas)
            total_saldo += conta.saldo
        
        return f"Total Entradas: R$ {total_entradas:.2f}\nTotal Saidas: R$ {total_saidas:.2f}\nTotal Saldo: R$ {total_saldo:.2f}"