class Cachorro:
    def __init__(self, nome, raca  , idade = 20):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
         print(f"{self.nome} diz: abrobra")

    def info(self):
        print(f"{self.nome}, {self.raca}, {self.idade}")



cachorro1 = Cachorro("skeike", "picnes", 7)
cachorro1.info()
cachorro1.latir()


cachorro2 = Cachorro("yasmin", "yorkwhire", 9)
cachorro2.info()
cachorro2.latir()

cachorro1.idade = 10
cachorro1.info()