#3. Informações de um produto

#Crie um programa para armazenar informações de um produto utilizando uma tupla. A tupla deverá armazenar:

#1. Nome do produto.
#2. Categoria.
#3. Preço.
#4. Código do produto.

#O programa deverá:

#1. Exibir cada informação individualmente.
info = ("Laptop", "Eletrônico", 3000, 64538970)
print(info[0])
print(info[1])
print(info[2])
print(info[3])
#2. Exibir todas as informações utilizando uma estrutura de repetição.
print("\n=== INFORMAÇÕES PRODUTOS ===")
for item in info:
    print(item)
#3. Informar a quantidade de informações armazenadas.
print("\n=== QUANTIDADE INFO ===")
print(len(info))
#4. Tentar alterar uma das informações da tupla.
temp = list(info)
temp[2] = 4000
info = tuple(temp)
print(info)
#5. Observar e explicar o que acontece ao tentar modificar um elemento.
#Não é possível alterar um elemento de uma tupla diretamente, porém, ao transformar
#a tupla em uma lista normal temporariamente usando o comando list, podemos mudar
#as informações, depois, apenas transformar-lá em tupla novamente usando o comando tuple.