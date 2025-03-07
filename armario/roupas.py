class Roupas:
    '''Classe base para representar roupas'''
    def __init__(self):
        pass  

class Camisa(Roupas):
    '''Classe que representa uma camisa'''
    def __init__(self, cor):
        super().__init__()
        self.cor = cor

    def get_cor(self):
        '''Retorna a cor da camisa'''
        return f'Camisa {self.cor}'

class Calça(Roupas):
    '''Classe que representa uma calça'''
    def __init__(self, cor):
        super().__init__()
        self.cor = cor

    def get_cor(self):
        '''Retorna a cor da calça'''
        return f'Calça {self.cor}'
