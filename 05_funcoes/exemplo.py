# <<< O QUE É UMA FUNÇÃO? >>>

# Função é um bloco de código criado para realizar
# uma determinada tarefa.



#1. CRIANDO UMA FUNÇÃO
# utilizar a palavra "def" para uma função


def saudacao():
    print("\nola bem vindo!!")


saudacao()



#2. Função com PARÂMETRO
# Parâmetros permitem enviar informações para a função.

def saudacao(nome):
    print(f"ola {nome}")

saudacao("Ana")
saudacao("Pindamoiangaba")


#3. Mais de um parâmetro
def apresentar(nome, idade):
    print(f"nome: {nome}")
    print(f"idade: {idade}")

apresentar("Maria", 17)




#4. Função com CÁLCULO

def somar(numero1, numero2):
    resultado = numero1 + numero2
    print (f"Resultado: {resultado}")

somar( 10, 20)




#5. Retornando um valor
# um Return devolve um valor pro local onde a função foi chamada

def somar (numero1, numero2):
    return numero1 + numero2

print (somar(10, 5))



#6. Função com condição

def verificarIdade(idade ):
    if idade>= 18:
        return "Maior de idade."
    else:
        return "Menor de idade."

print(verificarIdade(16))

#7. Parâmetro com valor padrão
def saudacao(nome = "Aluno"):
    print (f"Ola {nome}")

saudacao("Joao")
saudacao()




#8. Função utilizando LISTA

def calcularMedia(notas):
    soma = 0
    for nota in notas:
        soma += nota

    return soma/len(notas)
notas = [8, 7, 9, 10]
media = calcularMedia(notas)
print(f"Média: {media}")



#9. Funções para organizar um programa

def cadastrar_produto():

    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço:"))
    return nome, preco

def exibir_produto(nome, preco):

    print("\n ===== PRODUTO =====")
    print(f"Nome: {nome}")
    print(f"Preço: R$ {preco:.2f}")

nome, preco = cadastrar_produto()
exibir_produto(nome, preco)




