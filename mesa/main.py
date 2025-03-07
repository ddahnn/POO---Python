# Importa as classes Mesa e Cadeira
from mesa import Mesa
from cadeira import Cadeira

# Criando um objeto do tipo Mesa
mesa = Mesa("marrom")
print(mesa.get_cor())  # Exibe a cor da mesa

# Criando um objeto do tipo Cadeira
cadeira = Cadeira("marrom")
print(cadeira.get_cor())  # Exibe a cor da cadeira
print(cadeira.get_lugares())  # Exibe a quantidade de lugares

# Testando sentar e levantar da cadeira
print(cadeira.sentar_pessoa())  # Ocupa a cadeira
print(cadeira.sentar_pessoa())  # Tentativa de sentar novamente
print(cadeira.levantar_pessoa())  # Desocupa a cadeira
print(cadeira.levantar_pessoa())  # Tentativa de desocupar novamente
