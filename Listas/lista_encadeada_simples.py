class No:
    """Classe que é nó na lista"""
    def __init__(self, valor):
        self.valor = valor  # Valor do nó
        self.prox = None  # Referência para o próximo nó

class ListaEncadeadaSimples:
    """Classe que representa a lista encadeada"""
    def __init__(self):
        self.cabeca = None  # Elemento cabeça, primeiro nó
        
    def verificar_lista_vazia(self):
        """Verifica se a lista está vazia"""
        return self.cabeca is None

    def inserir_no_começo(self, valor):
        """Insere um novo nó no início da lista"""
        novo_no = No(valor)  # Cria um novo nó
        novo_no.prox = self.cabeca  # O próximo do novo nó é o antigo primeiro nó
        self.cabeca = novo_no  # O novo nó passa a ser o primeiro nó

    def inserir_no_fim(self, valor):
        """Insere um novo nó no final da lista"""
        novo_no = No(valor)
        if self.verificar_lista_vazia():
            self.cabeca = novo_no  # Se a lista está vazia, o novo nó é o primeiro
        else:
            atual = self.cabeca
            while atual.prox:  # Percorre até o último nó
                atual = atual.prox
            atual.prox = novo_no  # O último nó aponta para o novo nó
            
    def remover(self, valor_alvo, chave_comparacao=None, compare_func=None):
        atual = self.cabeca
        anterior = None

        while atual is not None:
            if compare_func:
                # Use a função de comparação personalizada se fornecida
                if compare_func(atual.valor, valor_alvo):
                    if anterior:
                        anterior.prox = atual.prox
                    else:
                        self.cabeca = atual.prox
                    return True
            elif isinstance(atual.valor, dict) and isinstance(valor_alvo, dict):
                # Comparar dicionários
                if all(atual.valor.get(k) == v for k, v in valor_alvo.items()):
                    if anterior:
                        anterior.prox = atual.prox
                    else:
                        self.cabeca = atual.prox
                    return True
            elif isinstance(atual.valor, dict) and chave_comparacao:
                # Comparar valor do dicionário com uma chave específica
                if atual.valor.get(chave_comparacao) == valor_alvo:
                    if anterior:
                        anterior.prox = atual.prox
                    else:
                        self.cabeca = atual.prox
                    return True
            elif atual.valor == valor_alvo:
                # Comparação direta para valores que não são dicionários
                if anterior:
                    anterior.prox = atual.prox
                else:
                    self.cabeca = atual.prox
                return True
            anterior = atual
            atual = atual.prox

        return False

    def buscar(self, valor):
        """Busca um nó que contenha o valor que queremos"""
        atual = self.cabeca
        posicao = 0 # Iniciamos a posicao do no
        while atual is not None:  # Vai alcaçar até o final da lista
            if atual.valor == valor: # Verificar se o no atual tem um valor que procuramos
                return atual, posicao
            atual = atual.prox  # Se sim mover para o proximo no
            posicao += 1 
        return None, -1  # Se percorrer toda a lista e não achar

    def atualizar_lista(self, anterior, novo_valor):
        """Atualiza o valor de um nó na lista, baseado no nome"""
        atual = self.cabeca  # Começa no início da lista

        # Quebra o valor anterior no formato 'nome - preco'
        try:
            nome_anterior, _ = anterior.split(' - ')  # Ignora o preço na busca
        except ValueError:
            return "Erro: Formato inválido. O formato deve ser 'nome - preço'."

        while atual is not None:
            print(f"Verificando nó com valor: {atual.valor}")  # Log de depuração

            # Verifica se o nome do item atual corresponde ao 'nome_anterior'
            if atual.valor['nome'] == nome_anterior:
                print(f"Encontrado! Atualizando '{anterior}' para '{novo_valor}'")

                # Quebra o novo valor no formato 'nome - preco'
                try:
                    nome_novo, preco_novo = novo_valor.split(' - ')
                    preco_novo = float(preco_novo)  # Converte o preço para float
                except ValueError:
                    return "Erro: Formato inválido. O novo valor deve estar no formato 'nome - preço'."

                # Atualiza o nome e o preço do item
                atual.valor['nome'] = nome_novo
                atual.valor['preco'] = preco_novo
                return True

            atual = atual.prox  # Move para o próximo nó

        print(f"Valor '{anterior}' não encontrado na lista.")  # Log se o valor não for encontrado
        return False


    def imprimir(self):
        """Exibe os elementos da lista encadeada"""
        elementos = [] # Vetor para armazenar os elementos
        atual = self.cabeca 
        while atual: # Vamos até o final da lista
            elementos.append(atual.valor) # Adiciona o valor atual ao vetor
            atual = atual.prox 
        print("\n".join(map(str, elementos))) # Imprime os elementos, um por linha
        
    def trocar_true_false_sim_nao(valor):
        """Trocar True or False por Sim e não"""
        return "Sim" if valor else "Não"
    resposta = True
    resposta = False

    def somar(self):
        """Soma os valores da lista"""
        atual = self.cabeca 
        soma = 0 # Inicializa a soma
        while atual: # Percorre a lista até o final
            soma += atual.valor # Adiciona o valor do nó atual à soma
            atual = atual.prox 
        return soma

    def contar_elementos(self):
        """Conta o número de elementos na lista"""
        atual = self.cabeca 
        contador = 0 # Inicializamos
        while atual:
            contador += 1  # Incrementa o contador a cada nó encontrado
            atual = atual.prox
        return contador
