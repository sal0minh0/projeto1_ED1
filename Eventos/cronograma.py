import sys
import os

# Adicionando o diretorio "Eventos" para verificação no caminho de busca de módulos no Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Listas import lista_encadeada_circular

class Cronograma:
    """Representa um cronograma de um evento usando lista encadeada circular"""
    def __init__(self):
        self.itens = lista_encadeada_circular.ListaEncadeadaCircular()
        
    def adicionar_item(self, atividade):
        """Adiciona uma atividade no cronograma"""
        self.itens.inserir(atividade)
        print(f"'{atividade}' adicionado ao cronograma.")
    
    def remover_item(self, atividade):
        """Remove uma atividade do cronograma"""
        self.itens.remover(atividade)
    
    def atualizar_item(self, atividade_atual, nova_atividade):
        """Atualiza uma atividade no cronograma"""
        if self.itens.atualizar(atividade_atual, nova_atividade):
            print(f"'{atividade_atual}' foi atualizado para '{nova_atividade}'.")
        else:
            print(f"'{atividade_atual}' não está no cronograma.")
    
    def buscar_um_item(self, atividade):
        """Busca um item e retorna uma string com as informações"""
        atual = self.itens.cauda.proximo if self.itens.cauda else None
        posicao = 0
        while atual:
            if atual.valor == atividade: 
                return f"'{atividade}' encontrado na posicao {posicao+1} da lista."
            atual = atual.proximo
            if atual == self.itens.cauda.proximo:
                break
            
        return f"'{atividade}' não encontrado na lista."
    
    def exibir_itens(self):
        """Exibe o cronograma do evento"""
        print("Cronograma do evento:")
        self.itens.imprimir()
    
    def verificar_lista_vazia(self):
        """Verifica se o cronograma está vazio"""
        vazio = self.itens.verificar_lista_vazia()
        print(f"O cronograma está vazio? {'Sim' if vazio else 'Não'}")
    
    def contar_itens(self):
        """Conta quantas atividades tem no cronograma"""
        quantidade_atividades = self.itens.contar_elementos()
        print(f"O cronograma tem {quantidade_atividades} atividades.")
    
"""
# Exemplo de uso do cronograma

# Criar objeto cronograma
c = Cronograma()

# Adicionando atividades ao cronograma
c.adicionar_atividade("Palestra de abertura - 9:00")
c.adicionar_atividade("Pausa para o café - 10:00")
c.adicionar_atividade("Palestra sobre Python - 10:30")
c.adicionar_atividade("Almoço - 12:00")
c.adicionar_atividade("Palestra sobre Django - 13:00")
c.adicionar_atividade("Sorteio de brindes - 18:00")
print("")

# Remover uma atividade
c.remover_atividade("Sorteio de brindes - 18:00")
print("")

# Exibir atividades
c.exibir_cronograma()
print("")

# Atualizar uma atividade
c.atualizar_atividade("Palestra sobre Python - 10:30", "Palestra sobre Java - 10:30")
print("")

# Atualizar uma atividade de novo
c.atualizar_atividade("Palestra sobre Django - 13:00", "Palestra sobre Spring - 10:30")
print("")

# Exibir atividades
c.exibir_cronograma()
print("")

# Verificar se o cronograma está vazio
c.verificar_vazio()
print("")

# Buscar uma atividade
c.buscar_uma_atividade("Almoço - 12:00")
print("")

# Contar quantas atividades tem no cronograma
c.contar_atividades()
"""
