import sys
import os

# Adicionando o diretorio "Eventos" para a pasta Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Listas import lista_encadeada_circular

class Convidado:
    """Representa uma lista de convidados de um evento usando lista encadeada circular"""
    def __init__(self):
        self.itens = lista_encadeada_circular.ListaEncadeadaCircular()
        
    def adicionar_item(self, nome, numero_inscricao, evento):
        """Adiciona um convidado com nome, número de inscrição e evento"""
        convidado_info = {
            'nome': nome,
            'numero_inscricao': numero_inscricao,
            'evento': evento
        }
        self.itens.inserir(convidado_info)
        print(f"Convidado '{nome}' adicionado à lista de convidados.")
    
    def remover_item(self, nome):
        """Remove um convidado pelo nome"""
        atual = self.itens.cauda.proximo if self.itens.cauda else None
        while atual:
            if atual.valor['nome'] == nome:
                self.itens.remover(nome)
                print(f"Convidado '{nome}' removido da lista.")
                return
            atual = atual.proximo
            if atual == self.itens.cauda.proximo:
                break
        print(f"Convidado '{nome}' não encontrado.")
        
    def atualizar_item(self, nome_atual, novo_nome=None, novo_numero_inscricao=None, novo_evento=None):
        """Atualiza as informações de um convidado"""
        atual = self.itens.cauda.proximo if self.itens.cauda else None
        while atual:
            if atual.valor['nome'] == nome_atual:
                if novo_nome:
                    atual.valor['nome'] = novo_nome
                if novo_numero_inscricao:
                    atual.valor['numero_inscricao'] = novo_numero_inscricao
                if novo_evento:
                    atual.valor['evento'] = novo_evento
                print(f"Informações do convidado '{nome_atual}' atualizadas.")
                return
            atual = atual.proximo
            if atual == self.itens.cauda.proximo:
                break
        print(f"Convidado '{nome_atual}' não encontrado.")
    
    def buscar_um_item(self, nome):
        """Busca um convidado pelo nome e retorna suas informações"""
        atual = self.itens.cauda.proximo if self.itens.cauda else None
        while atual:
            if atual.valor['nome'] == nome:
                return (f"Convidado encontrado:\n"
                    f"Nome: {atual.valor['nome']}\n"
                    f"Número de Inscrição: {atual.valor['numero_inscricao']}\n"
                    f"Evento: {atual.valor['evento']}")
            atual = atual.proximo
            if atual == self.itens.cauda.proximo:
                break
        return f"Convidado '{nome}' não encontrado."
    
    def exibir_itens(self):
        """Exibe todos os convidados do evento"""
        print("Lista de Convidados:")
        atual = self.itens.cauda.proximo if self.itens.cauda else None
        while atual:
            print(f"Nome: {atual.valor['nome']}, Inscrição: {atual.valor['numero_inscricao']}, Evento: {atual.valor['evento']}")
            atual = atual.proximo
            if atual == self.itens.cauda.proximo:
                break
        if not self.itens.cauda:
            print("A lista de convidados está vazia.")
    
    def verificar_lista_vazia(self):
        """Verifica se o evento está sem convidados"""
        vazio = self.itens.verificar_lista_vazia()
        print(f"O evento está sem convidados? {'Sim' if vazio else 'Não'}")
    
    def contar_itens(self):
        """Conta quantos convidados tem no evento"""
        quantidade_convidados = self.itens.contar_elementos()
        print(f"O evento tem {quantidade_convidados} convidados.")
"""
# Exemplo de uso da classe Convidado estendida
if __name__ == "__main__":
    c = Convidado()

    # Adicionando convidados ao evento
    c.adicionar_item("Leandro", "001", "Conferência de Python")
    c.adicionar_item("Clara", "002", "Workshop de Django")
    c.adicionar_item("Vinícius", "003", "Palestra sobre Machine Learning")
    print("")

    # Exibir convidados
    c.exibir_itens()
    print("")

    # Buscar um convidado
    c.buscar_um_item("Clara")
    print("")

    # Atualizar informações de um convidado
    c.atualizar_item("Clara", novo_evento = "Workshop de Flask")
    print("")

    # Exibir convidados novamente para ver a atualização
    c.exibir_itens()
    print("")

    # Remover um convidado
    c.remover_item("Vinícius")
    print("")

    # Contar convidados
    c.contar_itens()
    """