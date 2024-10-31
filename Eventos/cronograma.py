import sys
import os
import datetime

# Adicionando o diretorio "Eventos" para verificação no caminho de busca de módulos no Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Listas import lista_encadeada_circular

class Cronograma:
    """Representa um cronograma de um evento usando lista encadeada circular"""
    def __init__(self):
        self.itens = lista_encadeada_circular.ListaEncadeadaCircular()
        
    def adicionar_item(self, atividade, horario):
        """Adiciona uma atividade no cronograma com seu horário"""
        self.itens.inserir((atividade, horario))
        print(f"'{atividade}' ({horario}) adicionado ao cronograma.")
    
    def remover_item(self, atividade):
        """Remove uma atividade do cronograma"""
        atual = self.itens.cauda.proximo if self.itens.cauda else None
        while atual:
            if atual.valor[0] == atividade:
                self.itens.remover((atividade, atual.valor[1]))
                print(f"'{atividade}' removido do cronograma.")
                return True
            atual = atual.proximo
            if atual == self.itens.cauda.proximo:
                break
        return False
    
    def atualizar_item(self, atividade_atual, nova_atividade, novo_horario):
        """Atualiza uma atividade no cronograma"""
        atual = self.itens.cauda.proximo if self.itens.cauda else None
        while atual:
            if atual.valor[0] == atividade_atual:
                valor_antigo = atual.valor
                self.itens.atualizar(valor_antigo, (nova_atividade, novo_horario))
                print(f"'{atividade_atual}' foi atualizado para '{nova_atividade}' ({novo_horario}).")
                return True
            atual = atual.proximo
            if atual == self.itens.cauda.proximo:
                break
        print(f"'{atividade_atual}' não está no cronograma.")
        return False
    
    def buscar_um_item(self, atividade):
        """Busca um item e retorna uma string com as informações"""
        atual = self.itens.cauda.proximo if self.itens.cauda else None
        posicao = 0
        while atual:
            if atual.valor[0] == atividade:
                return f"'{atividade}' encontrado na posição {posicao+1} da lista com o horário {atual.valor[1]}."
            atual = atual.proximo
            if atual == self.itens.cauda.proximo:
                break
            posicao += 1
        return f"'{atividade}' não encontrado na lista."
    
    def exibir_itens(self):
        """Exibe o cronograma do evento"""
        print("Cronograma do evento:")
        self.itens.imprimir(lambda x: f"{x[0]} ({x[1]})")
    
    def verificar_lista_vazia(self):
        """Verifica se o cronograma está vazio"""
        return self.itens.verificar_lista_vazia()
    
    def contar_itens(self):
        """Conta quantas atividades tem no cronograma"""
        quantidade_atividades = self.itens.contar_elementos()
        print(f"O cronograma tem {quantidade_atividades} atividades.")
        
    def calcular_intervalo(self, index1, index2):
        """Calcula o intervalo de tempo entre duas atividades"""
        atividade1 = self.itens.obter_elemento(index1)
        atividade2 = self.itens.obter_elemento(index2)
        
        if not atividade1 or not atividade2:
            return "Não foi possível calcular o intervalo, uma das atividades não existe."
        
        horario1 = datetime.datetime.strptime(atividade1[1], "%H:%M")
        horario2 = datetime.datetime.strptime(atividade2[1], "%H:%M")
        
        intervalo = horario2 - horario1
        return f"O intervalo entre '{atividade1[0]}' e '{atividade2[0]}' é de {intervalo}"  