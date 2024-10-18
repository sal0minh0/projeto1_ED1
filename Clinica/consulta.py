import sys
import os

# Adicionando o diretorio "Clínica" para verificação no caminho de busca de módulos no Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Listas import lista_encadeada_dupla

class Consulta:
    """Representa os horários das consultas da clínica usando lista encadeada dupla"""
    def __init__(self):
        self.itens = lista_encadeada_dupla.ListaEncadeadaDupla()
        
    def adicionar_item(self, consulta):
        """Adiciona uma consulta para visualizar seus horários em uma lista"""
        self.itens.inserir(consulta)
        print(f"'{consulta}' adicionado as consultas.")
    
    def remover_item(self, consulta):
        """Remove uma consulta"""
        self.itens.remover(consulta)
    
    def atualizar_item(self, consulta_atual, nova_consulta):
        """Atualiza uma consulta"""
        if self.itens.atualizar(consulta_atual, nova_consulta):
            pass
        else:
            print(f"'{consulta_atual}' não está marcada.")
            
    def buscar_um_item(self, consulta):
        """Busca uma consulta na clínica"""
        _, posicao = self.itens.buscar(consulta)
        if posicao != -1:
            
            result = f"'{consulta}' encontrado na consulta {posicao+1}."
            print(result)
            return result
        
        else:
            result = f"'{consulta}' não está marcada."
            print(result)
            return result
            
    def exibir_itens(self):
        """Exibe os horários das consultas dessa clínica"""
        print("Consultas da clínica:")
        self.itens.imprimir()
        
    def verificar_vazio(self):
        """Verifica se a clínica está sem consultas"""
        vazio = self.itens.verificar_lista_vazia()
        print(f"A clínica está sem consultas? {'Sim' if vazio else 'Não'}")    
        
    def contar_itens(self):
        """Conta quantas consultas tem na clínica"""
        quantidade_consultas = self.itens.contar_elementos()
        print(f"A clínica tem {quantidade_consultas} consultas marcadas.")  
    
"""
# Exemplo de uso da consulta

# Criar objeto consulta
c = Consulta()

# Adicionando consultas a clínica
c.adicionar_item("Dr. João - 11:40")
c.adicionar_item("Dra. Maria - 14:00")
c.adicionar_item("Dr. José - 16:30")
print("")

# Remover uma consulta
c.remover_item("Dra. Maria - 14:00")
print("")

# Exibir consultas
c.exibir_item()
print("")

# Atualizar uma consulta
c.atualizar_item("Dr. José - 16:30", "Dr. José - 17:00")
print("")

# Exibir consultas
c.exibir_itens()
print("")

# Verificar se a clínica está sem consultas
c.verificar_vazio()
print("")

# Buscar uma consulta
c.buscar_um_item("Dr. José - 17:00")
print("")

# Contar consultas
c.contar_itens()
"""