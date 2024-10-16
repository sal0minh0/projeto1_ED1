import sys
import os

# Adicionando o diretorio "Eventos" para a pasta Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Listas import lista_encadeada_circular

class Convidado:
    """Representa uma lista de convidados de um evento usando lista encadeada circular"""
    def __init__(self):
        self.itens = lista_encadeada_circular.ListaEncadeadaCircular()
        
    def adicionar_convidado(self, convidado):
        """Adiciona um convidado para visualizar a lista de convidados"""
        self.itens.inserir(convidado)
        print(f"'{convidado}' adicionado a lista de convidados.")
    
    def remover_convidado(self, convidado):
        """Remove um convidado"""
        self.itens.remover(convidado)
        
    def atualizar_convidado(self, convidado_atual, novo_convidado):
        """Atualiza um convidado"""
        if self.itens.atualizar(convidado_atual, novo_convidado):
            pass
        else:
            print(f"'{convidado_atual}' não está na lista de convidados.")
    
    def buscar_um_convidado(self, convidado):
        """Busca um convidado na lista de convidados"""
        _, posicao = self.itens.buscar(convidado)
        if posicao != -1:
            print(f"'{convidado}' encontrado na posição {posicao+1}.")
        else:
            print(f"'{convidado}' não está na lista de convidados.")
    
    def exibir_convidados(self):
        """Exibe os convidados do evento"""
        print("Convidados do evento:")
        self.itens.imprimir()
    
    def verificar_vazio(self):
        """Verifica se o evento está sem convidados"""
        vazio = self.itens.verificar_lista_vazia()
        print(f"O evento está sem convidados? {'Sim' if vazio else 'Não'}")
    
    def contar_convidados(self):
        """Conta quantos convidados tem no evento"""
        quantidade_convidados = self.itens.contar_elementos()
        print(f"O evento tem {quantidade_convidados} convidados.")
    
# Exemplo de uso do convidado

# Criar objeto convidado
c = Convidado()

# Adicionando convidados ao evento
c.adicionar_convidado("Leandro")
c.adicionar_convidado("Clara")
c.adicionar_convidado("Vinícius")
print("")

# Remover um convidado
c.remover_convidado("Clara")
print("")

# Exibir convidados
c.exibir_convidados()
print("")

# Atualizar um convidado
c.atualizar_convidado("Leandro", "Isabela")
print("")

# Exibir convidados
c.exibir_convidados()
print("")

# Verificar se o evento está sem convidados
c.verificar_vazio()
print("")

# Buscar um convidado
c.buscar_um_convidado("Isabela")
print("")

# Contar quantos convidados tem no evento
c.contar_convidados()