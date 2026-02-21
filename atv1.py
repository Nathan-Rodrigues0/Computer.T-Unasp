#atividade 1: fazer input que recebe o sálario + dependendo do cargo)junior/pleno/senior) + aumento percentual

salario = float(input("Qual é o seu sálario?"))
cargo = input("Qual é o seu cargo?")

if cargo == "junior":
    print("Você é Júnior")
    #aumento de 10%
elif cargo == "pleno":
    print("Você é Pleno")
    #aumento de 15%
elif cargo == "senior":
    print("Você é Senior")
    #aumento de 20%
else:
    print("Por favor, digite o seu cargo (junior/pleno/senior)")
