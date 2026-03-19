nome = input("Escreva o nome do produto:")

def produto(nome):
    return nome

produto = {"nome": "banana", "preco": [5]}

if nome == "banana":
   print(f"Preço do produto:{5}")
else:
   print("Produto não encontrado")