#repetindo o exercicio de tabuada

tabuada = int(input("Qual número vai ser a tabuada?"))
multiplicador = 0

while multiplicador <= 10:
    resultado = multiplicador * tabuada
    print(f"{tabuada} X {multiplicador} = {resultado}")
    multiplicador += 1
    