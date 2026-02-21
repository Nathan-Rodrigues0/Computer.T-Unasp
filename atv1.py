#atividade 1: fazer input que recebe o sálario + dependendo do cargo)junior/pleno/senior) + aumento percentual
"""
nome = input("Qual é o seu nome?")
salario = float(input("Qual é o seu sálario?"))
cargo = input("Qual é o seu cargo? (junior/pleno/senior)").lower()

if cargo == "junior":
    #aumento de 10%
    aumento = salario * 0.1
    print(f"Olá {nome}. Seu sálario é R${aumento + salario:.2f} por ser {cargo.capitalize()}")
elif cargo == "pleno":
    #aumento de 15%
    aumento = salario * 0.15
    print(f"Olá {nome}. Seu sálario é R${aumento + salario:.2f} por ser {cargo.capitalize()}")
elif cargo == "senior":
    #aumento de 20%
    aumento = salario * 0.2
    print(f"Olá {nome}. Seu sálario é R${aumento + salario:.2f} por ser {cargo.capitalize()}")
else:
    print(f"{nome}. Por favor, digite o seu cargo (junior/pleno/senior)")


#atribuindo a quantidade de filhos o usuários tiver, vai ter um bônus  de R$500,00 por filho.
filhos = input("Você tem filhos?")
if filhos == "sim":
    quantidade = input("tem quantos filhos?")
    salario_filho = aumento + salario
    if quantidade == "1":
        print(f"{nome}. Seu sálario com bônus ao ter filho é de R${salario_filho + 500}")
    elif quantidade == "2":
        print(f"{nome}. Seu sálario com bônus ao ter filhos é de R${salario_filho + 500 * 2}")
    elif quantidade == "3":
        print(f"{nome}. Seu sálario com bônus ao ter filhos é de R${salario_filho + 500 * 3}")
    elif quantidade == "4":
        print(f"{nome}. Seu sálario com bônus ao ter filhos é de R${salario_filho + 500 * 4}")
    else:
        print(f"{nome}. Seu sálario com bônus ao ter filhos é de R${salario_filho + 2000}")

print("Obrigado por participar dessas perguntas!")
"""
#código limpo e resumido

nome = input("Qual é o seu nome?")
salario = float(input("Qual é o seu sálario?"))
cargo = input("Qual é o seu cargo? (junior/pleno/senior)").lower()

percentuais = {
    "junior": 0.10,
    "pleno": 0.15,
    "senior": 0.20
}

print(percentuais)