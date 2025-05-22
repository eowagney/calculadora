def menu():
    print("Bem-vindo à Calculadora!")
    print("Escolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potência")
    print("6. Raiz Quadrada")
    print("0. Sair")
    
def main():
    while True:
        menu()
        escolha = input("Digite o número da operação desejada: ")
        if escolha == '0':
            print("Saindo...")
            break
        if escolha in ['1', '2', '3', '4', '5']:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            print("Operação escolhida:", escolha)
            # Aqui você pode importar e chamar a função da operação
        elif escolha == '6':
            n = float(input("Digite o número: "))
            print("Operação escolhida: Raiz Quadrada")
            # Aqui você pode importar e chamar a função de raiz quadrada
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
