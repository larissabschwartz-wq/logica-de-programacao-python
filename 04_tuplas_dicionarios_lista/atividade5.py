#5. Sistema de estoque

#Uma loja de informática deseja organizar seu estoque.

#Crie uma estrutura utilizando uma lista de dicionários para armazenar pelo menos 5 produtos. Cada produto deverá possuir:

#1. Nome.
#2. Categoria.
#3. Preço.
#4. Quantidade em estoque.

#O programa deverá:

#1. Exibir todos os produtos cadastrados.
produtos = [
    {"Nome": "Celular", "Categoria": "Eletrônico", "Preço": 3000, "Quantidade": 10},
    {"Nome": "Laptop", "Categoria": "Eletrônico", "Preço": 5000, "Quantidade": 5},
    {"Nome": "Teclado", "Categoria": "Periférico", "Preço": 300, "Quantidade": 15},
    {"Nome": "Mouse", "Categoria": "Periférico", "Preço": 200, "Quantidade": 20},
    {"Nome": "Mousepad", "Categoria": "Acessório", "Preço": 80, "Quantidade": 30}
]

print("=== PRODUTOS DISPONÍVEIS ===")
print("\nCelular")
print("Laptop")
print("Teclado")
print("Mouse")
print("Mousepad")

#2. Exibir o nome, preço e quantidade em estoque de cada produto.
print("\nProduto 1:", produtos[0])
print("Produto 2:", produtos[1])
print("Produto 3:", produtos[2])
print("Produto 4:", produtos[3])
print("Produto 5:", produtos[4])

#3. Calcular a quantidade total de itens armazenados no estoque.
soma = 0
for produto in produtos:
    soma += produto["Quantidade"]
print("\nQuantidade total do estoque:", soma)
#4. Calcular o valor total do estoque.
preco = 0
for produto in produtos:
    preco += produto["Preço"]
print("Preço do estoque:", preco)

#5. Identificar os produtos que possuem menos de 10 unidades disponíveis.
for produto in produtos:
    if produto["Quantidade"] < 10:
        print(f"\nO produto {produto['Nome']} está com baixo estoque.\n ")

#6. Verificar se determinado produto está cadastrado.
if "Celular" not in produtos:
     print("O produto Celular está cadastrado.")
#7. Alterar a quantidade em estoque de um produto.
produtos[1]["Quantidade"] = 7
print("\nProduto 1:", produtos[0])
print("Produto 2:", produtos[1])
print("Produto 3:", produtos[2])
print("Produto 4:", produtos[3])
print("Produto 5:", produtos[4])

#8. Adicionar um novo produto.

novo_cadastro = {"Nome": "Gabinete", "Categoria": "Componente", "Preço": 1500, "Quantidade": 20}
produtos.append(novo_cadastro)

print("\nProduto 1:", produtos[0])
print("Produto 2:", produtos[1])
print("Produto 3:", produtos[2])
print("Produto 4:", produtos[3])
print("Produto 5:", produtos[4])
print("Produto 6:", produtos[5])