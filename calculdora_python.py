def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero"

def calculadora():
    print("Selecione a operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    while True:
        escolha = input("Digite o número da operação desejada (1/2/3/4): ")

        if escolha in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Por favor, digite números válidos.")
                continue

            if escolha == '1':
                print(f"{num1} + {num2} = {adicionar(num1, num2)}")

            elif escolha == '2':
                print(f"{num1} - {num2} = {subtrair(num1, num2)}")

            elif escolha == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")

            elif escolha == '4':
                print(f"{num1} / {num2} = {dividir(num1, num2)}")

            break
        else:
            print("Opção inválida. Por favor, selecione uma operação válida.")

if __name__ == "__main__":
    calculadora()
