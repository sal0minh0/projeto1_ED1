from Listas import lista_encadeada_simples

class Cardapio:
    """Classe que representa o cardápio usando uma lista encadeada"""
    def __init__(self):
        self.itens = lista_encadeada_simples.ListaEncadeadaSimples()

    def adicionar_item(self, item):
        """Adiciona um item no final do cardápio"""
        self.itens.inserir_no_fim(item)
        print(f"Item '{item}' adicionado ao cardápio.")

    def remover_item(self, item):
        """Remove um item do cardápio"""
        self.itens.remover(item)

    def atualizar_item(self, item_atual, novo_item):
        """Atualiza um item do cardápio"""
        if self.itens.atualizar_lista(item_atual, novo_item):
            print(f"Item '{item_atual}' foi atualizado para '{novo_item}'.")
        else:
            print(f"Item '{item_atual}' não encontrado no cardápio.")

    def buscar_item(self, item):
        """Busca um item no cardápio"""
        _, posicao = self.itens.buscar(item)
        if posicao != -1:
            print(f"Item '{item}' encontrado na posição {posicao+1} do cardápio.")
        else:
            print(f"Item '{item}' não encontrado no cardápio.")

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

# Adicionar itens
cardapio.adicionar_item("Pizza")
cardapio.adicionar_item("Hambúrguer")
cardapio.adicionar_item("Suco de Laranja")
print("")

# Exibir cardápio
cardapio.exibir_cardapio()
print("")

# Remover item
cardapio.remover_item("Hambúrguer")
print("")

# Exibir cardápio atualizado
cardapio.exibir_cardapio()
print("")

# Atualizar item
cardapio.atualizar_item("Suco de Laranja", "Refrigerante")
print("")

# Exibir cardápio atualizado
cardapio.exibir_cardapio()
print("")

# Verificar se o cardápio está vazio
cardapio.verificar_vazio()
print("")

# Buscar item
cardapio.buscar_item("Pizza")

