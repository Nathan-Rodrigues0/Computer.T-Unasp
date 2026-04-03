nome = input("Qual é o seu nome?")
salario = float(input("Qual é o seu salário?"))
cargo = input("Qual é o seu cargo? (junior/pleno/senior): ")

percentual = {
    "junior" : 0.1,
    "pleno" :  0.15,
    "senior" : 0.2
}

if cargo in percentual:
    aumento = salario * percentual[cargo]
    result = salario + aumento
    print(f"Seu salário é R${result:.2f} reais. Por ser {cargo}, tem um aumento de {percentual[cargo]}0%")

filhos = input("Você tem filhos?")

if filhos == "sim":
    quantidade = float(input("Qantos filhos você tem?"))
    if quantidade:
        aumento_filho = 500 * quantidade
        print(f"R${result + aumento_filho:.2f}")

