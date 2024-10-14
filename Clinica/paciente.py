import sys
import os

# Adicionando o diretorio "Clínica" para a pasta Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Listas import lista_encadeada_dupla

class Paciente:
    """Representa o paciente usando lista encadeada dupla"""
    def __init__(self):
        self.itens = lista_encadeada_dupla.ListaEncadeadaDupla()
        
    def adicionar_paciente(self, paciente):
        """Adiciona um paciente para visualizar em numa lista"""
        self.itens.inserir(paciente)
        print(f"'{paciente}' adicionado ao paciente.")
    
    def remover_paciente(self, paciente):
        """Remove um paciente"""
        self.itens.remover(paciente)
    
    def atualizar_paciente(self, paciente_atual, novo_paciente):
        """Atualiza um paciente"""
        if self.itens.atualizar(paciente_atual, novo_paciente):
            print(f"'{paciente_atual}' foi atualizado para '{novo_paciente}'.")
        else:
            print(f"'{paciente_atual}' não é um paciente.")
            
    def buscar_um_paciente(self, paciente):
        """Busca um paciente na clínica"""
        _, posicao = self.itens.buscar(paciente)
        if posicao != -1:
            print(f"'{paciente}' encontrado na posição {posicao+1} da clínica.")
        else:
            print(f"'{paciente}' não é um paciente ou não está cadastrado.")
            
    def exibir_pacientes(self):
        """Exibe os pacientes dessa clínica"""
        print("Pacientes da clínica:")
        self.itens.imprimir()
    
    def verificar_vazio(self):
        """Verifica se a clínica está vazia"""
        vazio = self.itens.verificar_lista_vazia()
        print(f"A clínica está sem pacientes? {'Sim' if vazio else 'Não'}")
        
    def contar_pacientes(self):
        """Conta quantos pacientes tem na clínica"""
        quantidade_pacientes = self.itens.contar_elementos()
        print(f"A clínica tem {quantidade_pacientes} pacientes cadastrados.")
        
# Exemplo de uso da lista_de_pacientes

# Criar objeto paciente
p = Paciente()

# Adicionando pacientes a clínica
p.adicionar_paciente("John")
p.adicionar_paciente("Mary")
p.adicionar_paciente("Vanessa")
print("")

# Removendo um paciente
p.remover_paciente("Mary")
print("")

# Exibindo os pacientes
p.exibir_pacientes()
print("")

# Atualizando pacientes para colocar o nome completo
p.atualizar_paciente("Vanessa", "Vanessa Silva")
print("")

# Exibindo pacientes de novo
p.exibir_pacientes()
print("")

# Verificando se a empresa tem ninguém
p.verificar_vazio()
print("")

# Buscar um paciente
p.buscar_um_paciente("John")

# Contar quantos pacientes tem na clínica
p.contar_pacientes()
print("")