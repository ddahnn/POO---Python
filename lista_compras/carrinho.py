import os  # biblioteca para manipulação de diretórios

class CarrinhoCompras:
    def __init__(self):
        '''Construtor da classe, inicializa a lista de itens'''
        self.lista = {}  # Dicionário para armazenar itens e quantidades
        self.caminho_arquivo = "lista_compras/carrinho.txt"

        # Garante que o diretório existe
        os.makedirs(os.path.dirname(self.caminho_arquivo), exist_ok=True)

    def adicionar_item(self, item, quantidade=1):
        '''Adiciona um item ao carrinho'''
        try:
            if item in self.lista:
                self.lista[item] += quantidade  # Soma a quantidade se o item já existir
            else:
                self.lista[item] = quantidade  # Adiciona novo item

            # Salva os itens no arquivo
            with open(self.caminho_arquivo, 'w') as arquivo:
                for produto, qtd in self.lista.items():
                    arquivo.write(f"{produto}: {qtd}\n")

            return f"O item '{item}' foi adicionado com sucesso."
    
        except Exception as e:
            return f"Erro ao adicionar o item: {str(e)}"

    def remover_item(self, item):
        '''Remove um item do carrinho'''
        if item in self.lista:
            del self.lista[item]
            return f"O item '{item}' foi removido."
        else:
            return f"O item '{item}' não está na lista."

    def visualizar_carrinho(self):
        '''Exibe os itens do carrinho'''
        if not self.lista:
            return "O carrinho está vazio."
        return "\n".join([f"{item}: {qtd}" for item, qtd in self.lista.items()])
