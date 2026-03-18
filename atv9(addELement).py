"""x = [1, 2, 3, 4, 5]
x.append(99)#adiciona o elemento (99) no final da lista de x
print(x)"""

#exercicio

"""lista = []
add_elemento = int(input("Adicione um número na lista: "))

lista.append(add_elemento)
print(lista)

for element in lista:
    adicionar = input("Deseja adicionar mais números na lista?")
    if adicionar == "sim":
        add_element2 = int(input("Qual número deseja adicionar?"))
        if add_element2 <= 0:
            break
        else:
            lista.append(add_element2)
            print(lista)
    elif adicionar == "não":
        break"""

    #resumido

vetor = []

while True:
    n = int(input("Adicione um número a lista:"))
    if n < 0:
        break
    else:
        vetor.append(n)
        print(vetor)