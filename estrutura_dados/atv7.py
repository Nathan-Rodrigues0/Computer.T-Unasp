"""number = int(input("Tabuade de: "))
multiplicador = range(11)

for n in multiplicador:
    print(f"{number} {chr(215)} {n} = {number * n}")
    n +=1"""

from time import sleep # importando o metódo sleep() para para o tempo, da biblioteca time

number = int(input("Tabuada de: "))

for multiplicador in range(11):#a variavel (multiplicador) vai recebendo/assumindo cada elemteno da lista do range
    print(f"{number} {chr(215)} {multiplicador} = {number * multiplicador}")
    sleep(1)
print("Fim da Tabuada!")

#aula 07 (11/03/26)
#como fazer a tabuada ultizando o método FOR