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
    