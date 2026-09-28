# 1. Cadastro de filmes

#Crie um programa para organizar uma lista de filmes. O programa deverá:

#1. Criar uma lista contendo inicialmente 5 filmes.

lista = ["Luca", "Soul", "Up Altas Aventuras", "Coco", "Wall-e"]
#2. Exibir todos os filmes cadastrados.

print(lista)

#3. Exibir o primeiro filme da lista.

print(lista[0])

#4. Exibir o último filme da lista.

print(lista[-1])

#5. Adicionar um novo filme ao final da lista.

lista.append("Bambi")
print(lista)

#6. Inserir um novo filme em uma posição específica.

lista.insert(3, "Meet The Robinsons")
print(lista)
#7. Remover um filme da lista.

lista.remove("Os Incríveis II")
print(lista)
#8. Alterar o nome de um dos filmes.

lista[1] = "Toy Story 5"
print(lista)
#9. Exibir a quantidade de filmes cadastrados.

print(len(lista))
#10. Verificar se um determinado filme está presente na lista.
if "Luca" in lista:
    print("O filme Luca está na lista.")
else:
    print("O filme Luca não está na lista.")