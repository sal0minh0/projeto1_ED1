import sys
import os

# Adicionando o diretório "Restaurante" ao caminho de busca de módulos do Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Listas import lista_encadeada_simples

class Restaurante:
    def __init__(self):
        from Restaurante.faturamento import Faturamento
        self.itens = lista_encadeada_simples.ListaEncadeadaSimples()
        self.total_expenses = 0.0
        self.faturamento = Faturamento()
        self.faturamento_total_bruto = 0.0
        self.contas_a_pagar = []  # Lista para armazenar as contas pendentes
        self.funcionarios = []
        
    def update_total_expenses(self):
        """Calcular despesas totais, incluindo salários dos funcionários e contas"""
        salary_expenses = 0.0
        current = self.itens.cabeca
        
        # Somar todos os salários dos funcionários
        while current:
            if isinstance(current.valor, dict) and 'salario' in current.valor:
                salary_expenses += float(current.valor['salario'])
            current = current.prox
            
        # Adicionar outras despesas das contas pendentes
        other_expenses = sum(conta['valor'] for conta in self.contas_a_pagar)
            
        # Atualizar despesas totais
        self.total_expenses = salary_expenses + other_expenses
        return self.total_expenses
        
    def set_faturamento_total_bruto(self):
        """Atualizar faturamento bruto a partir da classe Faturamento"""
        self.faturamento_total_bruto = self.faturamento.somar_e_faturamento()
        return self.faturamento_total_bruto
     
    def calcular_lucro(self):
        """Calcular lucro subtraindo despesas totais do faturamento bruto"""
        # Obter o faturamento diretamente da classe Faturamento
        self.faturamento_total_bruto = self.faturamento.somar_e_faturamento()
        
        # Atualizar despesas
        self.update_total_expenses()
        
        # Calcular lucro usando o faturamento da classe Faturamento
        lucro = self.faturamento_total_bruto - self.total_expenses
        return lucro
    
    def get_financial_summary(self):
        """Obter um resumo financeiro completo"""
        # Obter faturamento diretamente da classe Faturamento
        self.faturamento_total_bruto = self.faturamento.somar_e_faturamento()
        self.update_total_expenses()
        lucro = self.calcular_lucro()
        
        return {
            'faturamento_total_bruto': self.faturamento_total_bruto,
            'total_expenses': self.total_expenses,
            'lucro': lucro
        }
    
    def registrar_conta(self, descricao, valor):
        """Registrar uma nova conta a pagar"""
        conta = {
            'descricao': descricao,
            'valor': float(valor),
            'pago': False
        }
        self.contas_a_pagar.append(conta)
        print(f"Conta registrada: {descricao} - R$ {valor:.2f}")
        
    def pagar_conta(self, descricao, valor):
        """Pagar uma conta e atualizar o faturamento"""
        # Primeiro, atualizar o faturamento bruto
        self.set_faturamento_total_bruto()
        
        # Verificar se há saldo suficiente
        if valor > self.faturamento_total_bruto:
            print(f"Erro: Saldo insuficiente. Faturamento atual: R$ {self.faturamento_total_bruto:.2f}")
            return False
            
        # Procurar a conta na lista de contas pendentes
        for conta in self.contas_a_pagar:
            if conta['descricao'] == descricao and conta['valor'] == valor and not conta['pago']:
                # Marcar a conta como paga
                conta['pago'] = True
                # Subtrair do faturamento
                self.faturamento_total_bruto -= valor
                print(f"Conta paga com sucesso: {descricao} - R$ {valor:.2f}")
                print(f"Novo saldo: R$ {self.faturamento_total_bruto:.2f}")
                return True
                
        print("Conta não encontrada ou já foi paga")
        return False
        
    def listar_contas_pendentes(self):
        """Listar todas as contas pendentes"""
        contas_pendentes = [conta for conta in self.contas_a_pagar if not conta['pago']]
        if not contas_pendentes:
            print("Não há contas pendentes")
            return
            
        print("\nContas Pendentes:")
        for conta in contas_pendentes:
            print(f"Descrição: {conta['descricao']} - Valor: R$ {conta['valor']:.2f}")
           
    def adicionar_item(self, funcionario):
        """Adicionar um funcionário à lista encadeada"""
        nome = funcionario.get('nome')
        cargo = funcionario.get('cargo')
        salario = funcionario.get('salario')

        if nome and cargo is not None and salario is not None:
            print(f"Adicionando funcionário: {nome}, Cargo: {cargo}, Salário: {salario}")
            self.itens.inserir_no_fim(funcionario)  # Armazenar funcionário na lista encadeada
        else:
            raise ValueError("Dados incompletos para adicionar o funcionário.")
    
    def remover_item(self, nome_funcionario):
        """Remover um funcionário pelo nome"""
        def comparar_nome(item):
            return isinstance(item, dict) and item.get('nome', '').lower() == nome_funcionario.lower()
        
        if self.itens.remover(comparar_nome):
            print(f"Funcionário '{nome_funcionario}' removido com sucesso.")
            return True
        else:
            print(f"Funcionário '{nome_funcionario}' não encontrado.")
            return False

    def atualizar_item(self, nome_atual, novo_nome=None, novo_cargo=None, novo_salario=None):
        """Atualizar um funcionário com base no nome atual"""
        atual = self.itens.cabeca
        
        while atual:
            if isinstance(atual.valor, dict) and atual.valor.get('nome', '').lower() == nome_atual.lower():
                if novo_nome:
                    atual.valor['nome'] = novo_nome
                if novo_cargo:
                    atual.valor['cargo'] = novo_cargo
                if novo_salario is not None:
                    atual.valor['salario'] = novo_salario
                print(f"Funcionário '{nome_atual}' atualizado com sucesso.")
                return True
            atual = atual.prox
        print(f"Funcionário '{nome_atual}' não encontrado.")
        return False
            
    def buscar_um_item(self, nome_funcionario):
        """Buscar um funcionário pelo nome e retornar os dados como dicionário ou None"""
        atual = self.itens.cabeca
        while atual:
            if isinstance(atual.valor, dict) and atual.valor.get('nome', '').lower() == nome_funcionario.lower():
                return atual.valor
            atual = atual.prox
        return None
            
    def exibir_itens(self):
        """Exibir todos os trabalhadores do restaurante"""
        print("Trabalhadores do restaurante:")
        self.itens.imprimir()
    
    def contar_itens(self):
        """Contar o número de trabalhadores cadastrados"""
        quantidade_trabalhadores = self.itens.contar_elementos()
        print(f"O restaurante tem {quantidade_trabalhadores} trabalhadores cadastrados.")
            
    def verificar_lista_vazia(self):
        """Verificar se a lista de funcionários está vazia"""
        vazio = self.itens.verificar_lista_vazia()
        print(f"A lista de funcionários está vazia? {'Sim' if vazio else 'Não'}")
