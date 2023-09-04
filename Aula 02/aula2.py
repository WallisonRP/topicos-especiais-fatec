
#Exercicio 1

def exercicio1():
    flag = "s"

    while flag == "s":
        try:
            peso = float(input("Digite o peso (kg): "))
            altura = float(input("Digite a altura (cm): "))

            if altura > 100:
                altura /= 100

            if peso > 0 and altura > 0:
                imc = peso / (altura * altura)  
            else:
                raise Exception("Insira apenas valores maiores que zero")
            
            print(f"Seu IMC é: {imc:.2f}")
        except ValueError:
            print("O valor informado não é um número válido")

        flag = input("Deseja continuar? S/N ")

#exercicio1()

#Exercício 2

def exercicio2():
    nome = input("Digite o nome do produto: ")
    valor = float(input(f"Digite o valor do produto {nome}: R$ "))
    desconto = 0

    if valor < 0:
        print("O valor do produto é invalido")
    
    if valor > 0:
        if valor >= 50 and valor < 200:
         desconto = valor * 0.05
        elif valor >= 200 and valor < 500:
            desconto =  valor * 0.06
        elif valor >= 500 and valor < 100:
            desconto =  valor * 0.07
        elif valor >= 1000:
            desconto =  valor * 0.08


        print(f"Produto: {nome} \nValor Original: R${valor} \nValor Com Desconto: R$ {valor - desconto}")

#exercicio2()

def exercicio3():
    resistencias = []
    resistenciasTexto = ""
    min = 0
    max = 0

    for i in range(4):
        resistencias.append(int(input(f"Insira o valor da {i+1}º resistência: ")))
        
    for i in range(len(resistencias)):
        resistenciasTexto += f"{resistencias[i]}, "

    resistencias.sort()
    print(f"Resistências fornecidas: \n{resistenciasTexto[:-2]}")
    print(f"A maior Resistência é: {resistencias[-1]}")
    print(f"A menor Resistência é: {resistencias[0]}")

    

#exercicio3()

def exercicio4():
    numero = int(input("Digite um número para gerar a tabuada: "))

    for i in range(1, 11):
        print(f"{i} x {numero} = {i * numero}")

#exercicio4()

def exercicio5():
    print("oi")
