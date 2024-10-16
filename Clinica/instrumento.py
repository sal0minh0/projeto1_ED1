import sys
import os

# Adicionando o diretorio "Clínica" para a pasta Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Listas import lista_encadeada_dupla

class Instrumento:
    """Representa os instrumentos de trabalho da clínica usando lista encadeada dupla"""
    def __init__(self):
        self.itens = lista_encadeada_dupla.ListaEncadeadaDupla()
    
    def adicionar_instrumento(self, instrumento):
        """Adiciona os instrumentos para assim visualizar em numa lista"""
        self.itens.inserir(instrumento)
        print(f"'{instrumento}' adicionado ao instrumento.")
    
    def remover_instrumento(self, instrumento):
        """Remove um instrumento"""
        self.itens.remover(instrumento)
        
    def atualizar_instrumento(self, instrumento_atual, novo_instrumento):
        """Atualiza um instrumento"""
        if self.itens.atualizar(instrumento_atual, novo_instrumento):
            pass
        else:
            print(f"'{instrumento_atual}' não está cadastrado.")
            
    def buscar_um_instrumento(self, instrumento):
        """Busca um instrumento na clínica"""
        _, posicao = self.itens.buscar(instrumento)
        if posicao != -1:
            print(f"'{instrumento}' encontrado na posição {posicao+1} da clínica.")
        else:
            print(f"'{instrumento}' não está cadastrado.")
    
    def exibir_instrumentos(self):
        """Exibe os instrumentos dessa clínica"""
        print("Instrumentos da clínica:")
        self.itens.imprimir()
        
    def verificar_vazio(self):
        """Verifica se a clínica está sem instrumentos"""
        vazio = self.itens.verificar_lista_vazia()
        print(f"A clínica está sem instrumentos? {'Sim' if vazio else 'Não'}")
    
    def contar_instrumentos(self):
        """Conta quantos instrumentos tem na clínica"""
        quantidade_instrumentos = self.itens.contar_elementos()
        print(f"A clínica tem {quantidade_instrumentos} instrumentos cadastrados.")
    
# Exemplo de uso do instrumento

# Criar objeto instrumento
i = Instrumento()

# Adicionando instrumentos a clínica
i.adicionar_instrumento("Máscara")
i.adicionar_instrumento("Bisturi")
i.adicionar_instrumento("Pinça")
print("")

# Remover um instrumento
i.remover_instrumento("Bisturi")
print("")

# Exibir instrumentos
i.exibir_instrumentos()
print("")

# Atualizar um instrumento
i.atualizar_instrumento("Pinça", "Tesoura")
print("")

# Exibir instrumentos
i.exibir_instrumentos()
print("")

# Verificar se a clínica está sem instrumentos
i.verificar_vazio()
print("")

# Buscar um instrumento
i.buscar_um_instrumento("Máscara")
print("")

i.contar_instrumentos()
print("")