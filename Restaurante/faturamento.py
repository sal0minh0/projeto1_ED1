import sys
import os

# Adicionando o diretorio "Restaurante" para a pasta Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Listas import lista_encadeada_simples

class Faturamento:
    """Representa o faturamento usando lista encadeada simples"""
    def __init__(self):
        self.itens = lista_encadeada_simples.ListaEncadeadaSimples()
        
    def adicionar_vendas(self, vendas):
        """Adiciona um valor de vendas para calcular o faturamento"""
        self.itens.inserir_no_fim(vendas)
        print(f"'{vendas}' adicionado ao faturamento.")
        
    def remover_vendas(self, vendas):
        """Remove um valor de vendas"""
        self.itens.remover(vendas)
        
    def atualizar_vendas(self, vendas_atual, novo_vendas):
        """Atualiza um valor de vendas do faturamento"""
        if self.itens.atualizar_lista(vendas_atual, novo_vendas):
            print(f"'{vendas_atual}' foi atualizado para '{novo_vendas}'.")
        else:
            print(f"'{vendas_atual}' não encontrado no faturamento.")
    
    def buscar_uma_venda(self, vendas):
        """Busca um valor de vendas no faturamento"""
        _, posicao = self.itens.buscar(vendas)
        if posicao != -1:
            print(f"'{vendas}' encontrado na posição {posicao+1} do faturamento.")
        else:
            print(f"'{vendas}' não encontrado no faturamento.")
    
    def exibir_faturamento(self):
        """Exibe os valores do faturamento"""
        print("Valores do faturamento:")
        self.itens.imprimir()
        
    def verificar_vazio(self):
        """Verifica se o faturamento está vazio"""
        vazio = self.itens.verificar_lista_vazia()
        print(f"O faturamento está vazio? {'Sim' if vazio else 'Não'}")
        
    def somar_e_faturamento(self):
        """Soma os valores para calcular o faturamento bruto"""
        soma = self.itens.somar()
        quantidade_vendas = self.itens.contar_elementos()
        faturamento = soma * quantidade_vendas
        print(f"O faturamento total é de R${faturamento: .2f}")
        
# Exemplo de uso do faturamento
        
# Criar objeto faturamento
f = Faturamento()
        
# Adicionar vendas
f.adicionar_vendas(10.0)
f.adicionar_vendas(20.0)
f.adicionar_vendas(30.0)
print("")
        
# Remover vendas
f.remover_vendas(10.0)
print("")
        
# Exibir faturamento atualizado
f.exibir_faturamento()
print("")
        
# Atualizar vendas
f.atualizar_vendas(20.0, 25.0)
print("")
        
# Exibir faturamento
f.exibir_faturamento()
print("")
        
# Verificar se o faturamento está vazio
f.verificar_vazio()
print("")
        
# Buscar uma venda
f.buscar_uma_venda(25.0)
print("")

#Calcular o faturamento
f.somar_e_faturamento()
print("")
        
        
        
        
