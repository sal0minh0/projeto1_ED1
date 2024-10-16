import sys
import os

# Adicionando o diretorio "Clínica" para a pasta Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Listas import lista_encadeada_dupla

class PacienteInfo:
    def __init__(self, nome, idade, 
                 historico_medico, ultima_consulta):
        self.nome = nome
        self.idade = idade
        self.historico_medico = historico_medico
        self.ultima_consulta = ultima_consulta

    def __str__(self):
        return f"{self.nome} (Idade: {self.idade})"

class Paciente:
    """Representa o paciente usando lista encadeada dupla"""
    def __init__(self):
        self.itens = lista_encadeada_dupla.ListaEncadeadaDupla()
        
    def adicionar_paciente(self, nome, idade,
                           historico_medico, ultima_consulta):
        """Adiciona um paciente para visualizar em numa lista"""
        paciente = PacienteInfo(nome, idade, historico_medico, ultima_consulta)
        self.itens.inserir(paciente)
        print(f"'{paciente}' adicionado a lista.")
    
    def remover_paciente(self, nome):
        """Remove um paciente"""
        paciente = self.buscar_paciente_por_nome(nome)
        if paciente:
            self.itens.remover(paciente)
            print(f"'{nome}' removido da lista.")
        else:
            print(f"'{nome}' não encontrado na lista.")
    
    def atualizar_paciente(self, nome, novo_nome = None, idade_nova = None,
                           novo_historico = None, nova_consulta = None):
        """Atualiza um paciente"""
        paciente = self.buscar_paciente_por_nome(nome)
        if paciente:
            if novo_nome:
                paciente.nome = novo_nome
            if idade_nova:
                paciente.idade = idade_nova
            if novo_historico:
                paciente.historico_medico = novo_historico
            if nova_consulta:
                paciente.ultima_consulta = nova_consulta
            print(f"Paciente '{nome}' atualizado com sucesso.")
        else:
            print(f"'{nome}' não é um paciente.")
            
    def buscar_paciente_por_nome(self, nome):
        """Busca um paciente na clínica pelo nome"""
        atual = self.itens.cabeca
        while atual:
            if atual.valor.nome == nome:
                return atual.valor
            atual = atual.prox
        return None
            
    def exibir_pacientes(self):
        """Exibe os pacientes dessa clínica"""
        print("Pacientes da clínica:")
        atual = self.itens.cabeca
        while atual:
            paciente = atual.valor
            print(f"Nome: {paciente.nome}, Idade: {paciente.idade}, Última Consulta: {paciente.ultima_consulta}")
            print(f"Histórico Médico: {paciente.historico_medico}")
            print("")
            atual = atual.prox
    
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
p.adicionar_paciente("John Doe", 30, "Hipertensão", "2024-03-15")
p.adicionar_paciente("Mary Smith", 45, "Diabetes tipo 2", "2024-02-28")
p.adicionar_paciente("Vanessa Silva", 28, "Sem histórico relevante", "2024-03-01")
print("")

# Exibindo os pacientes
p.exibir_pacientes()
print("")

# Atualizando informações de um paciente
p.atualizar_paciente("John Doe", idade_nova = 31, nova_consulta = "2024-03-20")
print("")

# Exibindo pacientes novamente
p.exibir_pacientes()
print("")

# Verificando se a clínica tem pacientes
p.verificar_vazio()
print("")

# Buscar um paciente
paciente = p.buscar_paciente_por_nome("Mary Smith")
if paciente:
    print(f"Paciente encontrado: {paciente}")
else:
    print("Paciente não encontrado")
print("")

# Contar quantos pacientes tem na clínica
p.contar_pacientes()
print("")