import sys
import os

# Adicionando o diretorio "Restaurante" para a pasta Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Listas import lista_encadeada_simples

class Mesa:
    def __init__(self, numero):
        self.numero = numero
        self.cliente = None
        self.ocupada = False

    def __str__(self):
        status = "Ocupada" if self.ocupada else "Livre"
        cliente_info = f", Cliente: {self.cliente}" if self.cliente else ""
        return f"Mesa {self.numero}: {status}{cliente_info}"

class Cardapio:
    """Representa o cardápio usando lista encadeada simples"""
    def __init__(self):
        self.itens = lista_encadeada_simples.ListaEncadeadaSimples()

    def adicionar_item(self, alimento):
        """Adiciona um alimento"""
        self.itens.inserir_no_fim(alimento)
        print(f"'{alimento}' adicionado ao cardápio.")

    def remover_item(self, alimento):
        """Remove um alimento"""
        self.itens.remover(alimento)

    def atualizar_item(self, alimento_atual, novo_alimento):
        """Atualiza um alimento do cardápio"""
        if self.itens.atualizar_lista(alimento_atual, novo_alimento):
            print(f"'{alimento_atual}' foi atualizado para '{novo_alimento}'.")
        else:
            print(f"'{alimento_atual}' não encontrado no cardápio.")

    def buscar_um_item(self, alimento):
        """Busca um alimento no cardápio"""
        _, posicao = self.itens.buscar(alimento)
        if posicao != -1:
            print(f"'{alimento}' encontrado na posição {posicao+1} do cardápio.")
        else:
            print(f"'{alimento}' não encontrado no cardápio.")

    def exibir_itens(self):
        """Exibe os itens do cardápio"""
        print("Itens do cardápio:")
        self.itens.imprimir()

    def verificar_lista_vazia(self):
        """Verifica se o cardápio está vazio"""
        vazio = self.itens.verificar_lista_vazia()
        print(f"O cardápio está vazio? {'Sim' if vazio else 'Não'}")
        
    def adicionar_mesa(self, numero):
        nova_mesa = Mesa(numero)
        self.itens.inserir_no_fim(nova_mesa)
        print(f"Mesa {numero} adicionada ao restaurante.")

    def ocupar_mesa(self, numero_mesa, nome_cliente):
        atual = self.itens.cabeca
        while atual:
            if atual.valor.numero == numero_mesa:
                if not atual.valor.ocupada:
                    atual.valor.ocupada = True
                    atual.valor.cliente = nome_cliente
                    print(f"Mesa {numero_mesa} ocupada por {nome_cliente}.")
                else:
                    print(f"Mesa {numero_mesa} já está ocupada.")
                return
            atual = atual.prox
        print(f"Mesa {numero_mesa} não encontrada.")

    def liberar_mesa(self, numero_mesa):
        atual = self.itens.cabeca
        while atual:
            if atual.valor.numero == numero_mesa:
                if atual.valor.ocupada:
                    atual.valor.ocupada = False
                    atual.valor.cliente = None
                    print(f"Mesa {numero_mesa} liberada.")
                else:
                    print(f"Mesa {numero_mesa} já está livre.")
                return
            atual = atual.prox
        print(f"Mesa {numero_mesa} não encontrada.")

    def exibir_status_mesas(self):
        print("Status das mesas:")
        atual = self.itens.cabeca
        while atual:
            print(atual.valor)
            atual = atual.prox

"""
# Exemplo de uso do cardápio

# Criar objeto cardápio
c = Cardapio()

# Adicionar Alimentos
c.adicionar_alimento("Pizza")
c.adicionar_alimento("Hambúrguer")
c.adicionar_alimento("Suco de Laranja")
print("")

# Exibir cardápio
c.exibir_cardapio()
print("")

# Remover Alimento
c.remover_alimento("Hambúrguer")
print("")

# Exibir cardápio atualizado
c.exibir_cardapio()
print("")

# Atualizar Alimento
c.atualizar_alimento("Suco de Laranja", "Refrigerante")
print("")

# Exibir cardápio atualizado
c.exibir_cardapio()
print("")

# Verificar se o cardápio está vazio
c.verificar_vazio()
print("")

# Buscar Alimento
c.buscar_alimento("Pizza")
"""