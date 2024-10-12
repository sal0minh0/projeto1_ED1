import sys
import os

# Adicionando o diretorio "Restaurante" para a pasta Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Listas import lista_encadeada_simples

class Cardapio:
    """Representa o cardápio usando lista encadeada simples"""
    def __init__(self):
        self.itens = lista_encadeada_simples.ListaEncadeadaSimples()

    def adicionar_alimento(self, alimento):
        """Adiciona um alimento"""
        self.itens.inserir_no_fim(alimento)
        print(f"'{alimento}' adicionado ao cardápio.")

    def remover_alimento(self, alimento):
        """Remove um alimento"""
        self.itens.remover(alimento)

    def atualizar_alimento(self, alimento_atual, novo_alimento):
        """Atualiza um alimento do cardápio"""
        if self.itens.atualizar_lista(alimento_atual, novo_alimento):
            print(f"'{alimento_atual}' foi atualizado para '{novo_alimento}'.")
        else:
            print(f"'{alimento_atual}' não encontrado no cardápio.")

    def buscar_alimento(self, alimento):
        """Busca um alimento no cardápio"""
        _, posicao = self.itens.buscar(alimento)
        if posicao != -1:
            print(f"'{alimento}' encontrado na posição {posicao+1} do cardápio.")
        else:
            print(f"'{alimento}' não encontrado no cardápio.")

    def exibir_cardapio(self):
        """Exibe os itens do cardápio"""
        print("Itens do cardápio:")
        self.itens.imprimir()

    def verificar_vazio(self):
        """Verifica se o cardápio está vazio"""
        vazio = self.itens.verificar_lista_vazia()
        print(f"O cardápio está vazio? {'Sim' if vazio else 'Não'}")


# Exemplo de uso do cardápio

# Criar objeto cardápio
cardapio = Cardapio()

# Adicionar Alimentos
cardapio.adicionar_alimento("Pizza")
cardapio.adicionar_alimento("Hambúrguer")
cardapio.adicionar_alimento("Suco de Laranja")
print("")

# Exibir cardápio
cardapio.exibir_cardapio()
print("")

# Remover Alimento
cardapio.remover_alimento("Hambúrguer")
print("")

# Exibir cardápio atualizado
cardapio.exibir_cardapio()
print("")

# Atualizar Alimento
cardapio.atualizar_alimento("Suco de Laranja", "Refrigerante")
print("")

# Exibir cardápio atualizado
cardapio.exibir_cardapio()
print("")

# Verificar se o cardápio está vazio
cardapio.verificar_vazio()
print("")

# Buscar Alimento
cardapio.buscar_alimento("Pizza")