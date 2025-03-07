from carrinho import CarrinhoCompras

# Criando um objeto do carrinho
carrinho = CarrinhoCompras()

# Menu de opções
menu = '''
    1 - Adicionar item
    2 - Adicionar quantidade
    3 - Remover item
    4 - Visualizar carrinho
    5 - Sair
'''

while True:
    print(menu)
    try:
        opcao = int(input("Digite a opção desejada: "))

        if opcao == 1:
            item = input("Digite o nome do item: ")
            print(carrinho.adicionar_item(item))

        elif opcao == 2:
            item = input("Digite o nome do item: ")
            quantidade = int(input("Digite a quantidade a adicionar: "))
            print(carrinho.adicionar_item(item, quantidade))

        elif opcao == 3:
            item = input("Digite o nome do item a remover: ")
            print(carrinho.remover_item(item))

        elif opcao == 4:
            print("\nItens no carrinho:")
            print(carrinho.visualizar_carrinho())

        elif opcao == 5:
            print("Encerrando o programa.")
            break 

        else:
            print("Opção inválida, tente novamente com uma opção válida.")

    except ValueError:
        print("Erro! Digite um número válido.")
