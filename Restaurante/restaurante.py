import sys
import os

# Adicionando o diretório "Restaurante" para a pasta Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Listas import lista_encadeada_simples

class Restaurante:
    def __init__(self):
        self.itens = lista_encadeada_simples.ListaEncadeadaSimples()
        
    def adicionar_item(self, funcionario):
        """Adiciona um funcionário à lista encadeada."""
        nome = funcionario.get('nome')
        cargo = funcionario.get('cargo')
        salario = funcionario.get('salario')

        if nome and cargo is not None and salario is not None:
            print(f"Adicionando funcionário: {nome}, Cargo: {cargo}, Salário: {salario}")
            self.itens.inserir_no_fim(funcionario)  # Armazena o funcionário na lista encadeada
        else:
            raise ValueError("Dados incompletos para adicionar o funcionário.")
    
    def remover_item(self, nome_funcionario):
        """Remove um funcionário pelo nome."""
        def comparar_nome(item):
            return isinstance(item, dict) and item.get('nome', '').lower() == nome_funcionario.lower()
        
        if self.itens.remover(comparar_nome):
            print(f"Funcionário '{nome_funcionario}' removido com sucesso.")
            return True
        else:
            print(f"Funcionário '{nome_funcionario}' não encontrado.")
            return False

    def atualizar_item(self, nome_atual, novo_nome=None, novo_cargo=None, novo_salario=None):
        """Atualiza um funcionário com base no nome atual."""
        atual = self.itens.cabeca
        while atual:
            if isinstance(atual.valor, dict) and atual.valor.get('nome', '').lower() == nome_atual.lower():
                if novo_nome:
                    atual.valor['nome'] = novo_nome
                if novo_cargo:
                    atual.valor['cargo'] = novo_cargo
                if novo_salario:
                    atual.valor['salario'] = novo_salario
                print(f"Funcionário '{nome_atual}' atualizado com sucesso.")
                return True  # Funcionário atualizado com sucesso
            atual = atual.prox
        print(f"Funcionário '{nome_atual}' não encontrado.")
        return False  # Funcionário não encontrado
            
    def buscar_um_item(self, nome_funcionario):
        """Busca um funcionário pelo nome e retorna os dados encontrados como um dicionário ou None."""
        atual = self.itens.cabeca
        while atual:
            # Verifica se o valor atual é um dicionário e se o nome coincide
            if isinstance(atual.valor, dict) and atual.valor.get('nome', '').lower() == nome_funcionario.lower():
                return atual.valor  # Retorna o dicionário do funcionário
            atual = atual.prox
        return None  # Caso não encontre

            
    def exibir_itens(self):
        """Exibe todos os trabalhadores do restaurante."""
        print("Trabalhadores do restaurante:")
        self.itens.imprimir()
    
    def contar_itens(self):
        """Conta o número de trabalhadores cadastrados."""
        quantidade_trabalhadores = self.itens.contar_elementos()
        print(f"O restaurante tem {quantidade_trabalhadores} trabalhadores cadastrados.")
            
    def verificar_lista_vazia(self):
        """Verifica se a lista de funcionários está vazia."""
        vazio = self.itens.verificar_lista_vazia()
        print(f"A lista de funcionários está vazia? {'Sim' if vazio else 'Não'}")

# Exemplo de uso do sistema de gerenciamento do restaurante
"""
restaurante = Restaurante()

# Adicionando trabalhadores
restaurante.adicionar_item({'nome': "João", 'cargo': "Garçom", 'salario': 2000})
restaurante.adicionar_item({'nome': "Maria", 'cargo': "Cozinheira", 'salario': 2500})
restaurante.adicionar_item({'nome': "Pedro", 'cargo': "Gerente", 'salario': 3000})
print("")

# Exibindo trabalhadores
restaurante.exibir_itens()
print("")

# Contando trabalhadores
restaurante.contar_itens()
"""
