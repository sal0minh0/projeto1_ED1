import sys
import os

# Adicionando o diretorio "Restaurante" para verificação no caminho de busca de módulos no Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Listas import lista_encadeada_simples

class Faturamento:
    """Representa o faturamento usando lista encadeada simples"""
    def __init__(self):
        self.itens = lista_encadeada_simples.ListaEncadeadaSimples()
        self.observadores = []  # Lista para armazenar observadores
        
    def adicionar_observador(self, callback):
        """Adiciona um observador que será notificado quando o faturamento mudar"""
        self.observadores.append(callback)

    def notificar_observadores(self):
        """Notifica todos os observadores registrados sobre mudanças no faturamento"""
        for observador in self.observadores:
            observador()
        
    def adicionar_item(self, item_str):
        """Adiciona um valor de vendas para calcular o faturamento
        Espera uma string no formato 'data - valor'"""
        
        try:
            # Dividir a string de entrada em data e valor
            partes = item_str.split('-')
            if len(partes) != 2:
                raise ValueError("Formato inválido. Use: 'data - valor'")
            
            data = partes[0].strip()
            valor = float(partes[1].strip().replace('R$', '').replace(',', '.'))
            
            # Criar um dicionário com os valores analisados
            item = {
                'data': data,
                'valor': valor
            }
            
            self.itens.inserir_no_fim(item)
            print(f"Faturamento adicionado: Data {data}, Valor R$ {valor:.2f}")
            
            # Notifica observadores após adicionar item
            self.notificar_observadores()
            return True
        except ValueError as e:
            print(f"Erro ao adicionar faturamento: {str(e)}")
            raise
        
    def remover_item(self, data):
        """Remove um valor de vendas do faturamento baseado apenas na data"""
        try:
            data = data.strip()
            
            # Define uma função de comparação personalizada para correspondência de itens
            def compare_items(node_item, search_data):
                return node_item.get('data') == search_data
            
            # Tentar remover o item
            if self.itens.remover(data, compare_func=compare_items):
                # Notifica observadores após remover item
                self.notificar_observadores()
                return f"Faturamento removido: Data {data}"
            else:
                return f"Faturamento não encontrado: Data {data}"
                    
        except Exception as e:
            return f"Erro ao remover faturamento: {str(e)}"
        
    def atualizar_item(self, item_atual, novo_item):
        """Atualiza um valor de vendas do faturamento"""
        print(f"Tentando atualizar item no Faturamento")
        print(f"Novos dados do item: {novo_item}")
        print(f"Item atual para atualizar: {item_atual}")
        print(f"Valor do novo item: {novo_item}")
        
        atual = self.itens.cabeca
        while atual:
            print(f"Checking item: {atual.valor}")
            if atual.valor.get('data') == item_atual['data'] and atual.valor.get('valor') == item_atual['valor']:
                atual.valor = novo_item
                print(f"Item atualizado com sucesso")
                print(f"Faturamento atualizado: Data {novo_item['data']}, Valor R$ {novo_item['valor']:.2f}")
                # Notifica observadores após atualizar item
                self.notificar_observadores()
                return True
            atual = atual.prox
        print("Faturamento não encontrado para atualização.")
        return False
    
    def buscar_um_item(self, vendas_str):
        """Busca um valor de vendas no faturamento"""
        print(f"Procurando pelo item: {vendas_str}")
        try:
            data, valor_str = vendas_str.split('-')
            data = data.strip()
            valor = float(valor_str.strip().replace('R$', '').replace(',', '.'))
            
            item_busca = {'data': data, 'valor': valor}
            print(f"Item de busca analisado: {item_busca}")
            
            atual = self.itens.cabeca
            posicao = 0
            while atual:
                print(f"Verificando item na posição {posicao+1}: {atual.valor}")
                if atual.valor['data'] == item_busca['data'] and atual.valor['valor'] == item_busca['valor']:
                    print(f"Item encontrado na posição {posicao+1}")
                    return atual.valor, posicao
                atual = atual.prox
                posicao += 1
            
            print("Item não encontrado")
            return None, -1
        except Exception as e:
            print(f"Erro ao analisar a string de busca: {str(e)}")
            return None, -1
    
    def exibir_itens(self):
        """Retorna uma string formatada com os valores do faturamento"""
        print("=== Debug exibir_itens ===")
        print(f"Verificando lista vazia: {self.itens.verificar_lista_vazia()}")
        
        atual = self.itens.cabeca
        items_count = 0
        
        while atual:
            print(f"Item encontrado: {atual.valor}")
            items_count += 1
            atual = atual.prox
        
        print(f"Total de itens encontrados: {items_count}")
        print("========================")
        
        if self.itens.verificar_lista_vazia():
            return "Não há itens de faturamento registrados."
        
        resultado = "Valores do faturamento:\n"
        atual = self.itens.cabeca
        while atual:
            item = atual.valor
            resultado += f"Data: {item['data']}, Valor: R$ {item['valor']:.2f}\n"
            atual = atual.prox
        return resultado
        
    def verificar_lista_vazia(self):
        """Verifica se o faturamento está vazio"""
        vazio = self.itens.verificar_lista_vazia()
        print(f"O faturamento está vazio? {'Sim' if vazio else 'Não'}")
        
    def somar_e_faturamento(self):
        """Calcula o faturamento bruto somando todos os valores dos nós."""
        total = 0.0
        atual = self.itens.cabeca
        print("Calculando faturamento total...")  # Debug print
        while atual:
            print(f"Processando item: {atual.valor}")
            if isinstance(atual.valor, dict) and 'valor' in atual.valor:
                total += atual.valor['valor']
            atual = atual.prox
        return total