# Importa as classes Cadeado e Chave
from cadeado import Cadeado
from chave import Chave


chave = Chave(22156)
cadeado = Cadeado(22156)


senha_digitada = chave.get_segredo() 
resultado = cadeado.abrir(senha_digitada)  
print(resultado)  


print(cadeado.fechar()) 
