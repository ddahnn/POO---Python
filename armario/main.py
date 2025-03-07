from armario import GuardaRoupa, Prateleira
from roupas import Camisa, Calça

# Criando um guarda-roupa com 2 prateleiras
guardaroupa = GuardaRoupa(2)
prateleira = Prateleira(2)

# Criando Roupas
roupa1 = Camisa("Azul")
roupa2 = Calça("Jeans")
roupa3 = Camisa("Vermelha")

# Adicionando roupas à prateleira
print(prateleira.adicionarItens(roupa1.get_cor()))  
print(prateleira.adicionarItens(roupa2.get_cor()))
print(prateleira.adicionarItens(roupa3.get_cor()))


print(prateleira.listar_itens())


print(prateleira.remover_item(roupa2.get_cor()))

print(prateleira.adicionarItens(roupa3.get_cor()))

print(prateleira.listar_itens())
