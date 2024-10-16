import sys
import os

# Adicionando o diretorio "Clínica" para a pasta Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Listas import lista_encadeada_dupla

class Consulta:
    """Representa os horários das consultas da clínica usando lista encadeada dupla"""
    def __init__(self):
        self.itens = lista_encadeada_dupla.ListaEncadeadaDupla()
        
    def adicionar_consulta(self, consulta):
        """Adiciona uma consulta para visualizar seus horraios em uma lista"""
        self.itens.inserir(consulta)
        print(f"'{consulta}' adicionado aos horários.")
    
    def remover_consulta(self, consulta):
        """Remove uma consulta"""
        self.itens.remover(consulta)
    
    def atualizar_consulta(self, consulta_atual, nova_consulta):
        """Atualiza uma consulta"""
        if self.itens.atualizar(consulta_atual, nova_consulta):
            pass
        else:
            print(f"'{consulta_atual}' não está marcada.")
            
    def buscar_uma_consulta(self, consulta):
        """Busca uma consulta na clínica"""
        _, posicao = self.itens.buscar(consulta)
        if posicao != -1:
            print(f"'{consulta}' encontrado no horário {posicao+1}.")
        else:
            print(f"'{consulta}' não está marcada.")
            
    def exibir_consultas(self):
        """Exibe os horários das consultas dessa clínica"""
        print("Consultas da clínica:")
        self.itens.imprimir()
        
    def verificar_vazio(self):
        """Verifica se a clínica está sem consultas"""
        vazio = self.itens.verificar_lista_vazia()
        print(f"A clínica está sem consultas? {'Sim' if vazio else 'Não'}")    
        
    def contar_consultas(self):
        """Conta quantas consultas tem na clínica"""
        quantidade_consultas = self.itens.contar_elementos()
        print(f"A clínica tem {quantidade_consultas} consultas marcadas.")  
    
# Exemplo de uso da consulta

# Criar objeto consulta
c = Consulta()

# Adicionando consultas a clínica
c.adicionar_consulta("Dr. João - 11:40")
c.adicionar_consulta("Dra. Maria - 14:00")
c.adicionar_consulta("Dr. José - 16:30")
print("")

# Remover uma consulta
c.remover_consulta("Dra. Maria - 14:00")
print("")

# Exibir consultas
c.exibir_consultas()
print("")

# Atualizar uma consulta
c.atualizar_consulta("Dr. José - 16:30", "Dr. José - 17:00")

# Exibir consultas
c.exibir_consultas()
print("")

# Verificar se a clínica está sem consultas
c.verificar_vazio()
print("")

# Buscar uma consulta
c.buscar_uma_consulta("Dr. José - 17:00")
print("")

# Contar consultas
c.contar_consultas()