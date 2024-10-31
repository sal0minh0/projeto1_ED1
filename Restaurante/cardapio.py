import sys
import os

# Adicionando o diretorio "Restaurante" para verificação no caminho de busca de módulos no Python
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
        self.contador_pedidos = {} 

    def adicionar_item(self, item_string):
        try:
            nome, preco = item_string.split('-')
            nome = nome.strip()
            preco = float(preco.strip())
            item = {'nome': nome, 'preco': preco}
            self.itens.inserir_no_fim(item)
            self.contador_pedidos[nome] = 0  
            resultado = f"'{nome}' adicionado ao cardápio por R${preco:.2f}."
            return resultado
        except ValueError as e:
            return "Formato inválido. Use: Nome do Item - Preço"
        except Exception as e:
            return f"Erro ao adicionar item: {str(e)}"
    def registrar_pedido(self, nome_item):
        """Registra um pedido para um item específico."""
        nome_item = nome_item.strip()
        if nome_item in self.contador_pedidos:
            self.contador_pedidos[nome_item] += 1
            return f"Pedido registrado para {nome_item}"
        return f"Item {nome_item} não encontrado no cardápio"
    
    def obter_item_menos_pedido(self):
        """Retorna o item menos pedido do cardápio com seu preço promocional (20% de desconto)."""
        if not self.contador_pedidos:
            return None

        # Encontra o item com menor número de pedidos
        item_menos_pedido = min(self.contador_pedidos.items(), key=lambda x: x[1])
        nome_item = item_menos_pedido[0]

        # Busca o preço original do item
        atual = self.itens.cabeca
        while atual:
            if isinstance(atual.valor, dict) and atual.valor['nome'] == nome_item:
                preco_original = atual.valor['preco']
                preco_promocional = preco_original * 0.8  # 20% de desconto
                return {
                    'nome': nome_item,
                    'preco_original': preco_original,
                    'preco_promocional': preco_promocional,
                    'quantidade_pedidos': item_menos_pedido[1]
                }
            atual = atual.prox
        return None

    def remover_item(self, nome_alimento):
        if not nome_alimento:
            return "Nome do item não pode estar vazio"
            
        atual = self.itens.cabeca
        anterior = None
        
        # Normaliza a entrada removendo espaços e convertendo para minúsculas
        nome_alimento = nome_alimento.strip().lower()
        
        if nome_alimento in self.contador_pedidos:
            del self.contador_pedidos[nome_alimento]
        
        while atual is not None:
            # Verifica se o nó atual possui um dicionário válido com a chave 'nome'
            if isinstance(atual.valor, dict) and 'nome' in atual.valor:
                # Normaliza o nome armazenado da mesma forma que a entrada
                nome_atual = atual.valor['nome'].strip().lower()
                
                if nome_atual == nome_alimento:
                    # Se for o primeiro nó
                    if anterior is None:
                        self.itens.cabeca = atual.prox
                    else:
                        anterior.prox = atual.prox
                    return f"'{nome_alimento}' removido do cardápio."
                    
            anterior = atual
            atual = atual.prox
            
        return f"'{nome_alimento}' não encontrado no cardápio."


    def atualizar_item(self, item_atual, novo_item):
        try:
            # Analisar o nome do item atual e os detalhes do novo item
            nome_atual = item_atual.split(' - ')[0].strip().lower()
            nome_novo, preco_novo = novo_item.split(' - ')
            preco_novo = float(preco_novo.strip())
            
            atual = self.itens.cabeca
            while atual:
                if isinstance(atual.valor, dict) and 'nome' in atual.valor:
                    if atual.valor['nome'].lower() == nome_atual:
                        # Atualizar o item
                        atual.valor['nome'] = nome_novo.strip()
                        atual.valor['preco'] = preco_novo
                        return f"Item atualizado para: {nome_novo} - {preco_novo:.2f}"
                atual = atual.prox
                
            return f"Item '{item_atual}' não encontrado no cardápio."
            
        except ValueError:
            return "Formato inválido. Use: 'Nome - Preço'"
        except Exception as e:
            return f"Erro ao atualizar item: {str(e)}"

    def buscar_um_item(self, nome_alimento):
        """Busca um item no cardápio pelo nome."""
        if not nome_alimento:
            return "Nome do item não pode estar vazio"
        # Trata o caso onde o usuário pode ter inserido o nome com o preço
        try:
            nome_alimento = nome_alimento.split(' - ')[0]
        except:
            pass
        # Normaliza o nome do alimento (remove espaços extras e converte para minúsculo)
        nome_alimento = nome_alimento.strip().lower()
        atual = self.itens.cabeca
        posicao = 1
        
        while atual is not None:
            if isinstance(atual.valor, dict) and 'nome' in atual.valor:
                # Normaliza o nome do item atual para comparação
                nome_atual = atual.valor['nome'].strip().lower()
                
                if nome_atual == nome_alimento:
                    return f"'{atual.valor['nome']}' encontrado na posição {posicao} do cardápio. Preço: R${atual.valor['preco']:.2f}"
                    
            posicao += 1
            atual = atual.prox
            
        return f"'{nome_alimento}' não encontrado no cardápio."

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