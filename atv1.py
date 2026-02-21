#atividade 1: fazer input que recebe o sálario + dependendo do cargo)junior/pleno/senior) + aumento percentual

salario = float(input("Qual é o seu sálario?"))
cargo = input("Qual é o seu cargo?")

if cargo == "junior":
    #aumento de 10%
    aumento = salario * 0.1
    print(f"Seu sálario é R${aumento + salario:.2f} por ser {cargo.capitalize()}")
elif cargo == "pleno":
    #aumento de 15%
    aumento = salario * 0.15
    print(f"Seu sálario é R${aumento + salario:.2f} por ser {cargo.capitalize()}")
elif cargo == "senior":
    #aumento de 20%
    aumento = salario * 0.2
    print(f"Seu sálario é R${aumento + salario:.2f} por ser {cargo.capitalize()}")
else:
    print("Por favor, digite o seu cargo (junior/pleno/senior)")

#atribuindo a quantidade de filhos o usuários tiver, vai ter um bônus  de R$500,00 por filho.
filhos = input("Você tem filhos?")
if filhos == "sim":
    quantidade = input("tem quantos filhos?")
    salario_filho = aumento + salario
    if quantidade == "1":
        print(salario_filho + 500)
    elif quantidade == "2":
        print(salario_filho + 500 * 2)
    elif quantidade == "3":
        print(salario_filho + 500 * 3)
    elif quantidade == "4":
        print(salario_filho + 500 * 4)
    else:
        print(salario_filho + 2000)

    