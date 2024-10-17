import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Listas import lista_encadeada_dupla

class PacienteInfo:
    def __init__(self, nome, idade, historico_medico, ultima_consulta):
        self.nome = nome
        self.idade = idade
        self.historico_medico = historico_medico
        self.ultima_consulta = ultima_consulta

    def __str__(self):
        return f"{self.nome} (Idade: {self.idade})"

class Paciente:
    def __init__(self):
        self.itens = lista_encadeada_dupla.ListaEncadeadaDupla()
        
    def adicionar_item(self, paciente_info):
        nome, idade, historico_medico, ultima_consulta = paciente_info.split(',')
        paciente = PacienteInfo(nome.strip(), int(idade.strip()), historico_medico.strip(), ultima_consulta.strip())
        self.itens.inserir(paciente)
        return f"'{paciente}' adicionado a lista."
    
    def remover_item(self, nome):
        paciente = self.buscar_paciente_por_nome(nome)
        if paciente:
            self.itens.remover(paciente)
            return f"'{nome}' removido da lista."
        else:
            return f"'{nome}' não encontrado na lista."
    
    def atualizar_item(self, nome_atual, novo_paciente_info):
        novo_nome, idade_nova, novo_historico, nova_consulta = novo_paciente_info.split(',')
        paciente = self.buscar_paciente_por_nome(nome_atual)
        if paciente:
            paciente.nome = novo_nome.strip()
            paciente.idade = int(idade_nova.strip())
            paciente.historico_medico = novo_historico.strip()
            paciente.ultima_consulta = nova_consulta.strip()
            return f"Paciente '{nome_atual}' atualizado com sucesso."
        else:
            return f"'{nome_atual}' não é um paciente."
            
    def buscar_um_item(self, nome):
        paciente = self.buscar_paciente_por_nome(nome)
        if paciente:
            return f"Paciente encontrado: {paciente}"
        else:
            return f"Paciente '{nome}' não encontrado"
    
    def buscar_paciente_por_nome(self, nome):
        atual = self.itens.cabeca
        while atual:
            if atual.valor.nome == nome:
                return atual.valor
            atual = atual.prox
        return None
            
    def exibir_itens(self):
        resultado = "Pacientes da clínica:\n"
        atual = self.itens.cabeca
        while atual:
            paciente = atual.valor
            resultado += f"Nome: {paciente.nome}, Idade: {paciente.idade}, Última Consulta: {paciente.ultima_consulta}\n"
            resultado += f"Histórico Médico: {paciente.historico_medico}\n\n"
            atual = atual.prox
        return resultado
    
    def verificar_vazio(self):
        vazio = self.itens.verificar_lista_vazia()
        return f"A clínica está sem pacientes? {'Sim' if vazio else 'Não'}"
        
    def contar_itens(self):
        quantidade_pacientes = self.itens.contar_elementos()
        return f"A clínica tem {quantidade_pacientes} pacientes cadastrados."