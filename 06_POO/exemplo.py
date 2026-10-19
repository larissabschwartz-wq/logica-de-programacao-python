#A CLASSE: o modelo(a planta)
from types import coroutine


class Celular:
    def __init__(self, marca, modelo , cor , bateria = 100):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.bateria = bateria
        self.ligado = False

    def ligar(self):
        if self.bateria == 0:     # ==> Sempre que mencionar um atributo, escrever "self."
            print("Sem bateria! Coloque para carregar.")
        else:
            self.ligado = True
            print(f" {self.modelo} Ligado!")



#OS OBJETOS: Criados a partir da classe (as "casas")
celular1 = Celular ("Samsung", "Galaxy s23" , "Preto")
celular2 = Celular ("Motorola", "Tijolão" , "Vermelho")



#Acessando e alterando atributos
print(celular2.marca)


#Também podemos alterar diretamente
celular1.cor = "Vermelho"
print (celular1.cor)


