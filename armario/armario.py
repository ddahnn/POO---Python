class GuardaRoupa:
    '''Classe que representa um guarda-roupa com prateleiras'''
    def __init__(self, prateleiras):
        self.prateleiras = prateleiras  
        self.livre = True 

class Prateleira(GuardaRoupa):
    '''Classe que representa uma prateleira dentro do guarda-roupa'''
    def __init__(self, prateleiras):
        super().__init__(prateleiras)
        self.itens = [] 

    def adicionarItens(self, item):
        '''Adiciona um item à prateleira se houver espaço disponível'''
        if len(self.itens) < self.prateleiras:
            self.itens.append(item)
            return f"O item {item} foi adicionado à prateleira."
        else:
            return "Não há prateleiras disponíveis."
        
    def remover_item(self, item):
        '''Remove um item da prateleira'''
        if item in self.itens:
            self.itens.remove(item)
            return f"O item {item} foi removido com sucesso."
        else:
            return f"O item {item} não foi encontrado na prateleira."
        
    def listar_itens(self):
        '''Lista os itens armazenados na prateleira'''
        if self.itens:
            return "Os itens na prateleira são: " + ", ".join(self.itens)
        else:
            return "A prateleira está vazia."
