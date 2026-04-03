#vetores / array / listas = uma variavel compondo vários elementos ou outras listas
x = [1, 2, 4, "ai", True, 4.54, [7, 8 ,5]]
x[2] = 3 #substituindo o item na posição 2 que é o 4 pelo 3
y = [[1,4], [4, 6]]
print(x)
print(y)
#printar um determinado elemento dentro da lista
print(x[6][2])#[]posição do elemento dentro da lista() = index do elemento

for i in y:#metodo for = cria uma variavel para percorer uma lista elemento por elemento
    print(i)

a = range(1, 10, 2)#percorre todos os numeros
for ei in a:
    print(ei) 