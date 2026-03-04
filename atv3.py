tabuada = int(input("Tabuada de qual número?"))#recebe um numero estavel(estagnado) ao multiplicador
multiplicavel = 0 #numero que ira multiplicar

print(f"Tabuada do número {tabuada}:")
while multiplicavel <= 10:
    resultado = tabuada * multiplicavel
    print(f"{tabuada} X {multiplicavel} = {resultado}")
    multiplicavel+=1#somando 1 sempre quen aparecer está variavel