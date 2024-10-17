import sys
import os

# Adicionando o diretorio "Restaurante" para a pasta Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Listas import lista_encadeada_simples

class Faturamento:
    """Representa o faturamento usando lista encadeada simples"""
    def __init__(self):
        self.itens = lista_encadeada_simples.ListaEncadeadaSimples()
        
    def adicionar_item(self, item_str):
        """Adiciona um valor de vendas para calcular o faturamento
        Espera uma string no formato 'data - valor'"""
        try:
            # Split the input string into data and valor
            partes = item_str.split('-')
            if len(partes) != 2:
                raise ValueError("Formato inválido. Use: 'data - valor'")
            
            data = partes[0].strip()
            valor = float(partes[1].strip().replace('R$', '').replace(',', '.'))
            
            # Create a dictionary with the parsed values
            item = {
                'data': data,
                'valor': valor
            }
            
            self.itens.inserir_no_fim(item)
            print(f"Faturamento adicionado: Data {data}, Valor R$ {valor:.2f}")
            return True
        except ValueError as e:
            print(f"Erro ao adicionar faturamento: {str(e)}")
            raise
        
    def remover_item(self, vendas):
        """Remove um valor de vendas"""
        self.itens.remover(vendas)
        
    def atualizar_item(self, item_atual, novo_item):
        """Atualiza um valor de vendas do faturamento"""
        print(f"Debug: Attempting to update item in Faturamento")
        print(f"Debug: Current item to update: {item_atual}")
        print(f"Debug: New item data: {novo_item}")
        
        atual = self.itens.cabeca
        while atual:
            print(f"Debug: Checking item: {atual.valor}")
            if atual.valor.get('data') == item_atual['data'] and atual.valor.get('valor') == item_atual['valor']:
                atual.valor = novo_item
                print(f"Debug: Item updated successfully")
                print(f"Faturamento atualizado: Data {novo_item['data']}, Valor R$ {novo_item['valor']:.2f}")
                return True
            atual = atual.prox
        print("Debug: Faturamento não encontrado para atualização.")
        return False
    
    def buscar_um_item(self, vendas_str):
        """Busca um valor de vendas no faturamento"""
        print(f"Debug: Searching for item: {vendas_str}")
        try:
            data, valor_str = vendas_str.split('-')
            data = data.strip()
            valor = float(valor_str.strip().replace('R$', '').replace(',', '.'))
            
            item_busca = {'data': data, 'valor': valor}
            print(f"Debug: Parsed search item: {item_busca}")
            
            atual = self.itens.cabeca
            posicao = 0
            while atual:
                print(f"Debug: Checking item at position {posicao}: {atual.valor}")
                if atual.valor['data'] == item_busca['data'] and atual.valor['valor'] == item_busca['valor']:
                    print(f"Debug: Item found at position {posicao}")
                    return atual.valor, posicao
                atual = atual.prox
                posicao += 1
            
            print("Debug: Item not found")
            return None, -1
        except Exception as e:
            print(f"Debug: Error parsing search string: {str(e)}")
            return None, -1
    
    def exibir_faturamento(self):
        """Exibe os valores do faturamento"""
        print("Valores do faturamento:")
        self.itens.imprimir()
        
    def verificar_lista_vazia(self):
        """Verifica se o faturamento está vazio"""
        vazio = self.itens.verificar_lista_vazia()
        print(f"O faturamento está vazio? {'Sim' if vazio else 'Não'}")
        
    def somar_e_faturamento(self):
        """Calcula o faturamento bruto somando todos os valores dos nós."""
        total = 0.0
        atual = self.itens.cabeca
        while atual:
            if isinstance(atual.valor, dict) and 'valor' in atual.valor:
                total += atual.valor['valor']
            atual = atual.prox
        return total
"""     
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
"""       
        
        
        
