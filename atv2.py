#código limpo e resumido
""""
saída = False
while not saída:

    nome = input("Qual é o seu nome?")
    salario = float(input("Qual é o seu sálario?"))
    cargo = input("Qual é o seu cargo? (junior/pleno/senior):").lower()

    percentuais = {
        "junior": 0.10,
        "pleno": 0.15,
        "senior": 0.20
    }
    #condição para o cargo usando o array percentuais
    if cargo in percentuais:
        aumento = salario * percentuais[cargo]#percentais e [cargos: dentro dos cargos escritos]
        salario_final = salario + aumento
        print(f"Olá {nome}. Seu sálario é R${salario_final:.2f} por ser {cargo.capitalize()}")
    else:
        print("Cargo inválido! Digite novamente")

    #criando bônus para quem tem filhos
    filhos = input("Você tem filhos? (sim/não):").lower()

    if filhos == "sim":
        quantidade = int(input("Quantos filhos você tem?"))
        bonus = 500 * quantidade
        salario_atualizado = salario_final + bonus
        print(f"{nome}, esse é o teu salário atualizado por ter filhos: R${salario_atualizado:.2f}")
    
    saída = input("Você quer sair?")
    if saída == "sim":
        saída = True
        print(f"{nome}. Obrigado por participar desse questionário!")
        break
    else:
        saída = False 
"""

#código limpo e resumido
while True:

    nome = input("Qual é o seu nome?")
    salario = float(input("Qual é o seu sálario?"))
    cargo = input("Qual é o seu cargo? (junior/pleno/senior):").lower()

    percentuais = {
        "junior": 0.10,
        "pleno": 0.15,
        "senior": 0.20
    }
    #condição para o cargo usando o array percentuais
    if cargo in percentuais:
        aumento = salario * percentuais[cargo]#percentais e [cargos: dentro dos cargos escritos]
        salario_final = salario + aumento
        print(f"Olá {nome}. Seu sálario é R${salario_final:.2f} por ser {cargo.capitalize()}")
    else:
        print("Cargo inválido! Digite novamente")

    #criando bônus para quem tem filhos
    filhos = input("Você tem filhos? (sim/não):").lower()

    if filhos == "sim":
        quantidade = int(input("Quantos filhos você tem?"))
        bonus = 500 * quantidade
        salario_atualizado = salario_final + bonus
        print(f"{nome}, esse é o teu salário atualizado por ter filhos: R${salario_atualizado:.2f}")
    
    saída = input("Você quer sair?")
    if saída == "sim":
        saída = False
        print(f"{nome}. Obrigado por participar desse questionário!")
        break
    else:
        continue 