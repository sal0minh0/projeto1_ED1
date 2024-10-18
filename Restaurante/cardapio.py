import sys
import os

# Adicionando o diretorio "Restaurante" para a pasta Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Listas import lista_encadeada_simples

class Mesa:
    def __init__(self, numero):
        self.numero = numero
        self.cliente = None
        self.ocupada = False

    def __str__(self):
        status = "Ocupada" if self.ocupada else "Livre"
        cliente_info = f", Cliente: {self.cliente}" if self.cliente else ""
        return f"Mesa {self.numero}: {status}{cliente_info}"

class Cardapio:
    def __init__(self):
        self.itens = lista_encadeada_simples.ListaEncadeadaSimples()
        self.mesas = lista_encadeada_simples.ListaEncadeadaSimples()

    def adicionar_item(self, item_string):
        print(f"Cardapio.adicionar_item chamado com: '{item_string}'")  # Debug print
        try:
            nome, preco = item_string.split('-')
            nome = nome.strip()
            preco = float(preco.strip())
            item = {'nome': nome, 'preco': preco}
            print(f"Item a ser inserido: {item}")  # Debug print
            self.itens.inserir_no_fim(item)
            resultado = f"'{nome}' adicionado ao cardápio por R${preco:.2f}."
            print(f"Resultado: {resultado}")  # Debug print
            return resultado
        except ValueError as e:
            print(f"Erro de valor: {str(e)}")  # Debug print
            return "Formato inválido. Use: Nome do Item - Preço"
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")  # Debug print
            return f"Erro ao adicionar item: {str(e)}"

    def remover_item(self, nome_alimento):
        print(f"Tentando remover item do cardápio: '{nome_alimento}'")
    
        def comparar_nome(item):
            return isinstance(item, dict) and item.get('nome', '').lower() == nome_alimento.lower()
    
        if self.itens.remover(comparar_nome):
            print(f"Item '{nome_alimento}' removido com sucesso")
            return f"'{nome_alimento}' removido do cardápio."
        else:
            print(f"Item '{nome_alimento}' não encontrado")
            return f"'{nome_alimento}' não encontrado no cardápio."


    def atualizar_item(self, item_atual, novo_item):
        # Quebra o valor do item atual no formato 'nome - preco'
        try:
            nome_atual, _ = item_atual.split(' - ')  # Ignora o preço do item atual
        except ValueError:
            return "Erro: Formato do item atual inválido. O formato deve ser 'nome - preço'."

        atual = self.itens.cabeca
        while atual is not None:
            print(f"Verificando nó com valor: {atual.valor}")  # Log de depuração
            # Verifica se o nome do item atual corresponde ao 'nome_atual'
            if atual.valor['nome'] == nome_atual:
                try:
                    nome_novo, preco_novo = novo_item.split(' - ')
                    preco_novo = float(preco_novo)  # Converte o preço para float
                except ValueError:
                    return "Erro: Formato inválido. O novo valor deve estar no formato 'nome - preço'."
                
                # Atualiza o nome e o preço do item
                atual.valor['nome'] = nome_novo
                atual.valor['preco'] = preco_novo
                return f"'{item_atual}' foi atualizado para '{novo_item}'."
            
            atual = atual.prox

        return f"'{item_atual}' não encontrado no cardápio."


    def buscar_um_item(self, alimento):
        _, posicao = self.itens.buscar(alimento)
        if posicao != -1:
            return f"'{alimento}' encontrado na posição {posicao+1} do cardápio."
        else:
            return f"'{alimento}' não encontrado no cardápio."

    def exibir_itens(self):
        itens = []
        atual = self.itens.cabeca
        while atual:
            if isinstance(atual.valor, dict):
                itens.append(f"{atual.valor['nome']} - {atual.valor['preco']}")
            else:
                itens.append(str(atual.valor))
            atual = atual.prox
        return "\n".join(itens) if itens else "O cardápio está vazio."


    def verificar_lista_vazia(self):
        return self.itens.verificar_lista_vazia()

    def adicionar_mesa(self, numero):
        nova_mesa = Mesa(numero)
        self.mesas.inserir_no_fim(nova_mesa)
        return f"Mesa {numero} adicionada ao restaurante."

    def ocupar_mesa(self, numero_mesa, nome_cliente):
        atual = self.mesas.cabeca
        while atual:
            if atual.valor.numero == numero_mesa:
                if not atual.valor.ocupada:
                    atual.valor.ocupada = True
                    atual.valor.cliente = nome_cliente
                    return f"Mesa {numero_mesa} ocupada por {nome_cliente}."
                else:
                    return f"Mesa {numero_mesa} já está ocupada."
            atual = atual.prox
        return f"Mesa {numero_mesa} não encontrada."

    def liberar_mesa(self, numero_mesa):
        atual = self.mesas.cabeca
        while atual:
            if atual.valor.numero == numero_mesa:
                if atual.valor.ocupada:
                    atual.valor.ocupada = False
                    atual.valor.cliente = None
                    return f"Mesa {numero_mesa} liberada."
                else:
                    return f"Mesa {numero_mesa} já está livre."
            atual = atual.prox
        return f"Mesa {numero_mesa} não encontrada."

    def exibir_status_mesas(self):
        status = "Status das mesas:\n"
        atual = self.mesas.cabeca
        while atual:
            status += str(atual.valor) + "\n"
            atual = atual.prox
        return status

"""
# Exemplo de uso do cardápio

# Criar objeto cardápio
c = Cardapio()

# Adicionar Alimentos
c.adicionar_alimento("Pizza")
c.adicionar_alimento("Hambúrguer")
c.adicionar_alimento("Suco de Laranja")
print("")

# Exibir cardápio
c.exibir_cardapio()
print("")

# Remover Alimento
c.remover_alimento("Hambúrguer")
print("")

# Exibir cardápio atualizado
c.exibir_cardapio()
print("")

# Atualizar Alimento
c.atualizar_alimento("Suco de Laranja", "Refrigerante")
print("")

# Exibir cardápio atualizado
c.exibir_cardapio()
print("")

# Verificar se o cardápio está vazio
c.verificar_vazio()
print("")

# Buscar Alimento
c.buscar_alimento("Pizza")
"""