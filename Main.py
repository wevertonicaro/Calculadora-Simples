from operacoes.soma import soma
from operacoes.subtracao import subtracao
from operacoes.multiplicacao import multiplicacao
from operacoes.divisao import divisao
from utils.entrada import capturar_numero

def menu():
    print("\n*** Calculadora Simples ***")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. Sair")

    while True:
        try:
            escolha = int(input("Escolha uma opção: "))
            if escolha in [0, 1, 2, 3, 4,]:
                return escolha
            else:
                print("Opção inválida. Escolha entre 0 e 4.")
        except ValueError:
            print("Por favor, insira um número válido.")

def main():
    while True:
        escolha = menu()

        if escolha == 0:
            print("Saindo da calculadora. Até logo!")
            break

        num1 = capturar_numero("Digite o primeiro número: ")
        num2 = capturar_numero("Digite o segundo número: ")

        if escolha == 1:
            print(f"Resultado: {soma(num1, num2)}")
        elif escolha == 2:
            print(f"Resultado: {subtracao(num1, num2)}")
        elif escolha == 3:
            print(f"Resultado: {multiplicacao(num1, num2)}")
        elif escolha == 4:
            try:
                print(f"Resultado: {divisao(num1, num2)}")
            except ValueError as e:
                print(e)

if __name__ == "__main__":
    main()
