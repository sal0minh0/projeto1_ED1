import sys
import os

# Adicionando o diretório "Restaurante" para verificação no caminho de busca de módulos no Python
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
        """Calculate total expenses including employee salaries and bills"""
        salary_expenses = 0.0
        current = self.itens.cabeca
        
        # Sum all employee salaries
        while current:
            if isinstance(current.valor, dict) and 'salario' in current.valor:
                salary_expenses += float(current.valor['salario'])
            current = current.prox
            
        # Add other expenses from contas_a_pagar
        other_expenses = sum(conta['valor'] for conta in self.contas_a_pagar)
            
        # Update total expenses
        self.total_expenses = salary_expenses + other_expenses
        return self.total_expenses
        
    def set_faturamento_total_bruto(self):
        """Update gross revenue from Faturamento class"""
        self.faturamento_total_bruto = self.faturamento.somar_e_faturamento()
        return self.faturamento_total_bruto
     
    def calcular_lucro(self):
        """Calculate profit by subtracting total expenses from gross revenue"""
        # Get revenue directly from Faturamento class
        self.faturamento_total_bruto = self.faturamento.somar_e_faturamento()
        
        # Update expenses
        self.update_total_expenses()
        
        # Calculate profit using revenue from Faturamento
        lucro = self.faturamento_total_bruto - self.total_expenses
        return lucro
    
    def get_financial_summary(self):
        """Get a complete financial summary"""
        # Get revenue directly from Faturamento
        self.faturamento_total_bruto = self.faturamento.somar_e_faturamento()
        self.update_total_expenses()
        lucro = self.calcular_lucro()
        
        return {
            'faturamento_total_bruto': self.faturamento_total_bruto,
            'total_expenses': self.total_expenses,
            'lucro': lucro
        }
    
    def registrar_conta(self, descricao, valor):
        """Register a new bill to pay"""
        conta = {
            'descricao': descricao,
            'valor': float(valor),
            'pago': False
        }
        self.contas_a_pagar.append(conta)
        print(f"Conta registrada: {descricao} - R$ {valor:.2f}")
        
    def pagar_conta(self, descricao, valor):
        """Pay a bill and update revenue"""
        # First, update gross revenue
        self.set_faturamento_total_bruto()
        
        # Check if there's enough balance
        if valor > self.faturamento_total_bruto:
            print(f"Erro: Saldo insuficiente. Faturamento atual: R$ {self.faturamento_total_bruto:.2f}")
            return False
            
        # Look for the bill in the pending bills list
        for conta in self.contas_a_pagar:
            if conta['descricao'] == descricao and conta['valor'] == valor and not conta['pago']:
                # Mark bill as paid
                conta['pago'] = True
                # Subtract from revenue
                self.faturamento_total_bruto -= valor
                print(f"Conta paga com sucesso: {descricao} - R$ {valor:.2f}")
                print(f"Novo saldo: R$ {self.faturamento_total_bruto:.2f}")
                return True
                
        print("Conta não encontrada ou já foi paga")
        return False
        
    def listar_contas_pendentes(self):
        """List all pending bills"""
        contas_pendentes = [conta for conta in self.contas_a_pagar if not conta['pago']]
        if not contas_pendentes:
            print("Não há contas pendentes")
            return
            
        print("\nContas Pendentes:")
        for conta in contas_pendentes:
            print(f"Descrição: {conta['descricao']} - Valor: R$ {conta['valor']:.2f}")
           
    def adicionar_item(self, funcionario):
        """Add an employee to the linked list"""
        nome = funcionario.get('nome')
        cargo = funcionario.get('cargo')
        salario = funcionario.get('salario')

        if nome and cargo is not None and salario is not None:
            print(f"Adicionando funcionário: {nome}, Cargo: {cargo}, Salário: {salario}")
            self.itens.inserir_no_fim(funcionario)  # Store employee in linked list
        else:
            raise ValueError("Dados incompletos para adicionar o funcionário.")
    
    def remover_item(self, nome_funcionario):
        """Remove an employee by name"""
        def comparar_nome(item):
            return isinstance(item, dict) and item.get('nome', '').lower() == nome_funcionario.lower()
        
        if self.itens.remover(comparar_nome):
            print(f"Funcionário '{nome_funcionario}' removido com sucesso.")
            return True
        else:
            print(f"Funcionário '{nome_funcionario}' não encontrado.")
            return False

    def atualizar_item(self, nome_atual, novo_nome=None, novo_cargo=None, novo_salario=None):
        """Update an employee based on current name"""
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
        """Search for an employee by name and return data as dictionary or None"""
        atual = self.itens.cabeca
        while atual:
            if isinstance(atual.valor, dict) and atual.valor.get('nome', '').lower() == nome_funcionario.lower():
                return atual.valor
            atual = atual.prox
        return None
            
    def exibir_itens(self):
        """Display all restaurant workers"""
        print("Trabalhadores do restaurante:")
        self.itens.imprimir()
    
    def contar_itens(self):
        """Count number of registered workers"""
        quantidade_trabalhadores = self.itens.contar_elementos()
        print(f"O restaurante tem {quantidade_trabalhadores} trabalhadores cadastrados.")
            
    def verificar_lista_vazia(self):
        """Check if employee list is empty"""
        vazio = self.itens.verificar_lista_vazia()
        print(f"A lista de funcionários está vazia? {'Sim' if vazio else 'Não'}")
        