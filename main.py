"""
# Main para teste de entradas
from Listas import lista_encadeada_dupla
l = lista_encadeada_dupla.ListaEncadeadaDupla() # Instanciar a classe com o objeto "l", se chamamos de outro arquivo
                                                # vai ser assim

#Exemplo de main
print("")
buscar_valor = input("Digite um valor para eu buscar: ") # Criar uma variavel de input
buscar_no = l.buscar(buscar_valor) # Buscar esse no
print("") 

if buscar_no:
    print(f"Encontramos o valor {buscar_no.valor}.")

else:
    print("O valor nao foi encontrado.")
"""