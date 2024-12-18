import sys
import os

# Adicionando o diretorio "Clínica" para verificação no caminho de busca de módulos no Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Listas import lista_encadeada_dupla

class Instrumento:
    def __init__(self):
        self.itens = lista_encadeada_dupla.ListaEncadeadaDupla()
    
    def adicionar_item(self, instrumento):
        self.itens.inserir(instrumento)
        return f"'{instrumento}' adicionado ao instrumento."
    
    def remover_item(self, instrumento):
        self.itens.remover(instrumento)
        return f"'{instrumento}' removido dos instrumentos."
        
    def atualizar_item(self, instrumento_atual, novo_instrumento):
        
        if self.itens.atualizar(instrumento_atual, novo_instrumento):
            return f"'{instrumento_atual}' atualizado para '{novo_instrumento}'."
        else:
            return f"'{instrumento_atual}' não está cadastrado."
            
    def buscar_um_item(self, instrumento):
        _, posicao = self.itens.buscar(instrumento)
        
        if posicao != -1:
            return f"'{instrumento}' encontrado na posição {posicao+1} da clínica."
        else:
            return f"'{instrumento}' não está cadastrado."
    
    def exibir_itens(self):
        return self.itens.imprimir()
        
    def verificar_vazio(self):
        vazio = self.itens.verificar_lista_vazia()
        return f"A clínica está sem instrumentos? {'Sim' if vazio else 'Não'}"
    
    def contar_itens(self):
        quantidade_instrumentos = self.itens.contar_elementos()
        return f"A clínica tem {quantidade_instrumentos} instrumentos cadastrados."
    def get_quantidade_from_string(self, instrumento_str):
        """Extrai a quantidade do formato 'Nome - Quantidade'"""
        try:
            return int(instrumento_str.split('-')[1].strip())
        except:
            return 0

    def get_instrumento_menor_quantidade(self):
        """Retorna o instrumento com menor quantidade"""
        if self.itens.verificar_lista_vazia():
            return None

        current = self.itens.cabeca
        menor_quantidade = float('inf')
        instrumento_menor = None

        while current:
            quantidade = self.get_quantidade_from_string(current.valor)
            if quantidade < menor_quantidade:
                menor_quantidade = quantidade
                instrumento_menor = current.valor
            current = current.prox

        return instrumento_menor
"""
# Exemplo de uso do instrumento

# Criar objeto instrumento
i = Instrumento()

# Adicionando instrumentos a clínica
i.adicionar_itens("Máscara")
i.adicionar_itens("Bisturi")
i.adicionar_itens("Pinça")
print("")

# Remover um instrumento
i.remover_itens("Bisturi")
print("")

# Exibir instrumentos
i.exibir_itens()
print("")

# Atualizar um instrumento
i.atualizar_itens("Pinça", "Tesoura")
print("")

# Exibir instrumentos
i.exibir_itens()
print("")

# Verificar se a clínica está sem instrumentos
i.verificar_vazio()
print("")

# Buscar um instrumento
i.buscar_um_item("Máscara")
print("")

# Contar quantos instrumentos tem na clínica
i.contar_itens()
print("")
"""