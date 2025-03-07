class Cadeado:
    '''Classe que simula um cadeado eletrônico com senha'''


    def __init__(self, segredo):
        self.segredo = segredo 
        self.fechado = True 


    def get_segredo(self):
        '''Retorna a senha do cadeado'''
        return self.segredo
    

    def get_fechado(self):
        '''Retorna o estado do cadeado (True = fechado, False = aberto)'''
        return self.fechado
    
   
    def abrir(self, senha):
        '''Tenta destravar o cadeado pedindo a senha correta (máx. 3 tentativas)'''
        contagem = 3 
        
        while contagem > 0:  
            if senha == self.segredo:  
                self.fechado = False 
                return "Cadeado destravado com sucesso!"
            #diminui a quantia a cada looping
            contagem -= 1 
            if contagem > 0:
                senha = int(input(f"Senha incorreta! Tente novamente ({contagem} tentativas restantes): "))  
        
        return "Cadeado bloqueado! Muitas tentativas erradas." 

    
    def fechar(self):
        '''Trava o cadeado novamente'''
        self.fechado = True 
        return "Cadeado travado!"
