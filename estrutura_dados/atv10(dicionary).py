#lista [] = lista/array 
#tuple () = lista inalteravel usada registro de segurança
#dicionary {} = lista com 'chave': valor

#exemple:

dicionary = {'number one': 1, 'fruts': "apple", 'List': [1, 2, 3, 4, 5]}
print(dicionary)

#desafio de estoque de frutas

estoque = {}
while True:

    produto = input("Qual produto deseja adicionar ao estoque?")
    valor_produto = int(input("Qual é o valor desse produto?"))
    estoque[produto] = f"R$ {valor_produto:.2f}"
    print(estoque)

    saída = input("Quer adicionar mais produto?")
    if saída == "sim":
        continue
    elif saída == "não":
        print("Estoque finalizado")
        print(estoque)
        break
    else:
        print("Dados não reconhecido, digite novamente...")
        continue 