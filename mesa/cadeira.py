# Importa a classe Mesa do arquivo mesa.py
from mesa import Mesa

# Definição da classe Cadeira que herda de Mesa
class Cadeira(Mesa):
    def __init__(self, cor):
        '''Construtor da classe Cadeira, inicializa cor, lugares e status de ocupação'''
        super().__init__(cor)  # Chama o construtor da classe pai (Mesa)
        self.lugares = 1  # Define que cada cadeira tem 1 lugar
        self.livre = True  # Define que a cadeira começa livre

    def get_lugares(self):
        '''Método para retornar a quantidade de lugares da cadeira'''
        return f"A cadeira tem {self.lugares} lugar"

    def get_cor(self):
        '''Método para obter a cor da cadeira'''
        return f'A cor da cadeira é {self.cor}'
    
    def set_cor(self, nova_cor):
        '''Método para alterar a cor da cadeira'''
        self.cor = nova_cor  # Modifica a cor da cadeira

    def sentar_pessoa(self):
        '''Método para simular uma pessoa sentando na cadeira'''
        if self.livre:  # Se a cadeira estiver livre
            self.livre = False  # Agora está ocupada
            return "Uma pessoa sentou na cadeira."
        else:
            return "A cadeira já está ocupada."

    def levantar_pessoa(self):
        '''Método para liberar a cadeira'''
        if not self.livre:  # Se a cadeira estiver ocupada
            self.livre = True  # Agora está livre
            return "A cadeira foi desocupada."
        else:
            return "A cadeira já está livre."
