import sys
import os

# Adicionando o diretorio "Restaurante" para a pasta Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Listas import lista_encadeada_simples

class Trabalhador:
    """Representa o trabalhador usando lista encadeada simples"""
    def __init__(self):
        self.itens = lista_encadeada_simples.ListaEncadeadaSimples()
        
    def adicionar_trabalhador(self, trabalhador):
        """Adiciona um trabalhador para visualizar em numa lista"""
        self.itens.inserir_no_fim(trabalhador)
        print(f"'{trabalhador}' adicionado ao trabalhador.")
    
    def remover_trabalhador(self, trabalhador):
        """Remove um trabalhador"""
        self.itens.remover(trabalhador)
    
    def atualizar_trabalhador(self, trabalhador_atual, novo_trabalhador):
        """Atualiza um trabalhador"""
        if self.itens.atualizar_lista(trabalhador_atual, novo_trabalhador):
            print(f"'{trabalhador_atual}' foi atualizado para '{novo_trabalhador}'.")
        else:
            print(f"'{trabalhador_atual}' não trabalha na empresa.")
            
    def buscar_um_trabalhador(self, trabalhador):
        """Busca um trabalhador na empresa"""
        _, posicao = self.itens.buscar(trabalhador)
        if posicao != -1:
            print(f"'{trabalhador}' encontrado na posição {posicao+1} da empresa.")
        else:
            print(f"'{trabalhador}' não trabalha na empresa ou não está cadastrado.")
            
    def exibir_trabalhadores(self):
        """Exibe os trabalhadores dessa empresa"""
        print("Trabalhadores da empresa:")
        self.itens.imprimir()
    
    def verificar_vazio(self):
        """Verifica se a empresa está vazia"""
        vazio = self.itens.verificar_lista_vazia()
        print(f"A empresa está sem trabalhadores? {'Sim' if vazio else 'Não'}")
        
    def contar_trabalhadores(self):
        """Conta quantos trabalhadores tem na empresa"""
        quantidade_trabalhadores = self.itens.contar_elementos()
        print(f"A empresa tem {quantidade_trabalhadores} trabalhadores cadastrados.")
        
# Exemplo de uso da lista_de_trabalhadores

# Criar objeto trabalhador
t = Trabalhador()

# Adicionando trabalhadores a empresa
t.adicionar_trabalhador("Amor")
t.adicionar_trabalhador("Sal")
t.adicionar_trabalhador("Ana")
t.adicionar_trabalhador("Sem Amor")
print("")

# Demitindo trabalhadores
t.remover_trabalhador("Sem Amor")
print("")

# Exibindo trabalhadores
t.exibir_trabalhadores()
print("")

# Atualizando trabalhadores
t.atualizar_trabalhador("Amor", "Amor Eterno")
print("")

# Exibindo trabalhadores de novo
t.exibir_trabalhadores()
print("")

# Verficando se a empresa sem ninguém
t.verificar_vazio()
print("")

# Buscar uma venda
t.buscar_um_trabalhador("Ana")
print("")

# Retornar a quantidade de trabalhadores da empresa
t.contar_trabalhadores()
print("")

