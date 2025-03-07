
class Chave:
    '''Classe que simula uma chave que contém um segredo'''

   
    def __init__(self, segredo):
        self.segredo = segredo  
    
    def get_segredo(self):
        '''Retorna o segredo da chave'''
        return self.segredo
    
    
    def set_segredo(self, novo_segredo):
        '''Define um novo segredo para a chave'''
        self.segredo = novo_segredo
