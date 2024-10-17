import sys
import os

# Adicionando o diretorio "Restaurante" para a pasta Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Listas import lista_encadeada_simples

class Restaurante:
    def __init__(self):
        self.itens = lista_encadeada_simples.ListaEncadeadaSimples()
        
    def adicionar_item(self, nome, cargo, salario):
        trabalhador = {
            'nome': nome,
            'cargo': cargo,
            'salario': salario
        }
        self.itens.inserir_no_fim(trabalhador)
        print(f"Trabalhador {nome} adicionado com sucesso!")
    
    def remover_item(self, trabalhador):
        self.itens.remover(trabalhador)
    
    def atualizar_item(self, nome_atual, novo_nome=None, novo_cargo=None, novo_salario=None):
        """Atualiza um funcionário com base no nome atual"""
        atual = self.itens.cabeca
        while atual:
            if atual.valor['nome'].lower() == nome_atual.lower():
                if novo_nome:
                    atual.valor['nome'] = novo_nome
                if novo_cargo:
                    atual.valor['cargo'] = novo_cargo
                if novo_salario:
                    atual.valor['salario'] = novo_salario
                return True  # Funcionário atualizado com sucesso
            atual = atual.prox
        return False  # Funcionário não encontrado
            
    def buscar_um_item(self, nome_funcionario):
        """Busca um funcionário pelo nome e retorna os dados encontrados"""
        atual = self.itens.cabeca
        while atual:
            if atual.valor['nome'].lower() == nome_funcionario.lower():
                return f"Nome do Funcionário buscado: {atual.valor['nome']}, Cargo: {atual.valor['cargo']}, Salário: {atual.valor['salario']}"
            atual = atual.prox
        return None  # Caso não encontre
            
    def exibir_itens(self):
        print("Trabalhadores do restaurante:")
        self.itens.imprimir()
    
    def contar_itens(self):
        quantidade_trabalhadores = self.itens.contar_elementos()
        print(f"O restaurante tem {quantidade_trabalhadores} trabalhadores cadastrados.")
            
    def verificar_lista_vazia(self):
        """Verifica se o faturamento está vazio"""
        vazio = self.itens.verificar_lista_vazia()
        print(f"O faturamento está vazio? {'Sim' if vazio else 'Não'}")
        
"""
# Exemplo de uso do sistema de gerenciamento do restaurante

restaurante = Restaurante()

# Adicionando trabalhadores
restaurante.adicionar_trabalhador("João")
restaurante.adicionar_trabalhador("Maria")
restaurante.adicionar_trabalhador("Pedro")
print("")

# Exibindo trabalhadores
restaurante.exibir_trabalhadores()
print("")

# Adicionando mesas
restaurante.adicionar_mesa(1)
restaurante.adicionar_mesa(2)
restaurante.adicionar_mesa(3)
print("")

# Ocupando mesas
restaurante.ocupar_mesa(1, "Carlos")
restaurante.ocupar_mesa(2, "Ana")
print("")

# Exibindo status das mesas
restaurante.exibir_status_mesas()
print("")

# Liberando uma mesa
restaurante.liberar_mesa(1)
print("")

# Exibindo status atualizado das mesas
restaurante.exibir_status_mesas()
print("")

# Contando trabalhadores
restaurante.contar_trabalhadores()
"""