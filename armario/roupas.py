class Roupa:
    '''Classe base para representar roupas'''
    def __init__(self):
        pass

class Camisa(Roupa):
    '''Classe que representa uma camisa'''
    def __init__(self, cor, manga="Longa"):
        super().__init__()
        self.cor = cor
        self.manga = manga

    def get_cor(self):
        '''Retorna a cor da camisa'''
        return f'Camisa {self.cor}'

    def transformar_manga_curta(self):
        self.manga = "Curta"
        return self.manga

    def virar_regata(self):
        self.manga = "Regata"
        return self.manga

class CamisaCurta(Camisa):
    def __init__(self, cor):
        super().__init__(cor, "Curta")

    def virar_regata(self):
        self.manga = "Regata"
        return self.manga

class Regata(Camisa):
    def __init__(self, cor):
        super().__init__(cor, "Regata")

class Calca(Roupa):
    '''Classe que representa uma calça'''
    def __init__(self, cor):
        super().__init__()
        self.cor = cor

    def get_cor(self):
        '''Retorna a cor da calça'''
        return f'Calça {self.cor}'
