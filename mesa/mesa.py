# Definição da classe Mesa
class Mesa:
    def __init__(self, cor):
        '''Construtor da classe Mesa, inicializa a cor da mesa'''
        self.cor = cor  # Atributo para armazenar a cor da mesa

    def set_cor(self, nova_cor):
        '''Método para alterar a cor da mesa'''
        self.cor = nova_cor  # Modifica o atributo de cor

    def get_cor(self):
        '''Método para obter a cor da mesa'''
        return f'A cor da mesa é {self.cor}'
