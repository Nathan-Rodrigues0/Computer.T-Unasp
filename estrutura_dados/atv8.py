from time import sleep # importando o metódo sleep() para para o tempo, da biblioteca time

number = int(input("Tabuada de: "))

for multiplicador in range(101):#a variavel (multiplicador) vai recebendo/assumindo cada elemteno da lista do range
    print(f"{number} {chr(215)} {multiplicador} = {number * multiplicador}")
    sleep(0.5)
    if multiplicador in range(10, 101, 10):#o primeiro e o terceiro elemeto vai executar o bloco abaixo quando que no elemento da 5 colocação na lista range(100) e repete de acordo com o que está escolhido
        cont = input("Quer continuar?")
        if cont == "sim":
            continue
        elif cont == "não":
            print("Fim da Tabuada!")
            break
        