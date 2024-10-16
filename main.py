from Listas import lista_encadeada_simples
from Listas import lista_encadeada_dupla
from Listas import lista_encadeada_circular

ls = lista_encadeada_simples.ListaEncadeadaSimples()
ld = lista_encadeada_dupla.ListaEncadeadaDupla() 
lc = lista_encadeada_circular.ListaEncadeadaCircular()

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