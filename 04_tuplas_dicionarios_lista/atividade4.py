#4. Cadastro de funcionário

#Crie um programa para armazenar os dados de um funcionário utilizando um dicionário.

#O cadastro deverá possuir:

#1. Nome.
#2. Idade.
#3. Cargo.
#4. Salário.
#5. Setor.

#O programa deverá:

#1. Exibir cada informação do funcionário.
funcionario = {
    "Nome": "Jucelino",
    "Idade": 19,
    "Cargo": "Atendente de supermercado",
    "Salário": 7000,
    "Setor": "Caixa",
}

print(funcionario)
#2. Alterar o salário do funcionário.

funcionario["Salário"] = "9000"
print(funcionario)
#3. Adicionar uma nova informação ao cadastro.
funcionario["Anos de Experiência"] = 5
print(funcionario)
#4. Remover uma informação do cadastro.
del funcionario["Idade"]
print(funcionario)
#5. Verificar se determinada chave existe.
if "Setor" in funcionario:
    print("O dicionário possui a chave Setor.")
else:
    print("O dicionário não possui a chave Setor.")
#6. Percorrer o dicionário exibindo as chaves e seus respectivos valores.
for chave in funcionario:
    print(chave, funcionario[chave])