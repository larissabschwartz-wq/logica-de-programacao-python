# 2. Controle de notas

#Crie um programa para armazenar as notas de um estudante. O programa deverá:

#1. Criar uma lista contendo 5 notas.

notas = [10.0, 8.0, 6.5, 9.0]

#2. Exibir todas as notas.

print(notas)

#3. Calcular a soma das notas.

soma = 0

for nota in notas:
    soma += nota

print(soma)

#4. Calcular a média das notas.

media =  soma / len(notas)
print(media)
#5. Identificar a maior nota.

notaMaior = 0
for nota in notas:
    if nota > notaMaior:
        notaMaior = nota
print(notaMaior)

#6. Identificar a menor nota.
notaMenor = 100000
for nota in notas:
    if nota < notaMenor:
        notaMenor = nota
print(notaMenor)
#7. Verificar se existe uma nota igual a 10.

if 10 in notas:
    print("Existe uma nota 10 na lista.")
else:
    print("Não existe uma nota 10 na lista.")

#8. Informar se o estudante foi aprovado ou reprovado.

if media >= 7:
    print("O aluno está aprovado.")
else:
    print("O aluno está reprovado.")
#9. Considerar média igual ou superior a 7 como aprovação.