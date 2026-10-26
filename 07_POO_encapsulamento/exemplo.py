#1. ENCAPSULAMENTO
#Proteger o salário para que só mude seguindo regras

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario #privado: dois underline


    def apresentar(self):
        print(f"Sou {self.nome} e ganho {self.__salario:.2f}")


    @property
    def salario(self):
        return self.__salario


    def dar_aumento(self, porcentagem):
        if porcentagem <= 0:
            print (f"Aumento inválido para {self.nome}")
        self.__salario = self.salario * (1 + porcentagem / 100)
        print(f"{self.nome} recebeu {porcentagem}% de aumento")



#####################################################################################


shanna = Funcionario("shanna", 1367)
shanna.salario = 4000
print(shanna.salario)
shanna.apresentar()
shanna.dar_aumento(20)
shanna.apresentar()


#0 try/except é um bloco usado em programação para tra
try:
        shanna.salario = 10000
except AttributeError:
    print ("NÃO PODE MUDAR O SALARIO DIRETAMENTE")

try:
    print(ana.__salario)
except AttributeError:
    print("O atributo __salario nao pode ser acessado de fora.")