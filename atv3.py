tabuada = int(input("Tabuada de qual número?"))
multiplicavel = 0

print(f"Tabuada do {tabuada}:")
while multiplicavel <= 10:
    resultado = tabuada * multiplicavel
    print(f"{tabuada} X {multiplicavel} = {resultado}")
    multiplicavel+=1