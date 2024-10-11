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

    def remover(self, valor):
        """Remove o primeiro nó que contém o valor que queremos"""
        atual = self.cabeca
        anterior = None
        while atual and atual.valor != valor:
            anterior = atual
            atual = atual.prox
        if atual is None:
            print("Elemento não encontrado.")
            return
        if anterior is None:
            self.cabeca = atual.prox  # Remove o nó da cabeça
        else:
            anterior.prox = atual.prox  # Remove o nó ligando o anterior ao próximo

    def buscar(self, valor):
        """Busca um nó que contenha o valor que queremos"""
        atual = self.cabeca
        posicao = 0 # Posicao do no
        while atual is not None:  # Vai alcaçar até o final da lista
            if atual.valor == valor: # Verificar se o no atual tem um valor que procuramos
                return atual, posicao
            atual = atual.prox  # Se sim mover para o proximo no
            posicao += 1 
        return None, -1  # Se percorrer toda a lista e não achar
    
    def atualizar_lista(self, anterior, novo_valor):
        """Atualiza o valor de um nó na lista"""
        atual = self.cabeca
        while atual is not None:
            if atual.valor == anterior:
                atual.valor = novo_valor
                return True
            atual = atual.prox
        return False


    def imprimir(self):
        """Exibe os elementos da lista encadeada"""
        elementos = []
        atual = self.cabeca
        while atual:
            elementos.append(atual.valor)
            atual = atual.prox
        print("\n".join(map(str, elementos)))
        
    def trocar_true_false_sim_nao(valor):
        """Trocar True or False por Sim e não"""
        return "Sim" if valor else "Não"
    resposta = True
    resposta = False

# Exemplo de uso das funções

# Objeto da Classe
l = ListaEncadeadaSimples()

# Inserir
l.inserir_no_fim(1)
l.inserir_no_fim(2)
l.inserir_no_fim(3)
l.inserir_no_começo(0)
l.imprimir()  # Saída: 0 -> 1 -> 2 -> 3
print("")

#Remover
l.remover(2)
l.imprimir()  # Saída: 0 -> 1 -> 3
print("")

#Atualizar
l.atualizar_lista(3, 5) 
l.imprimir()
print("")

    # Verificando se a lista está vazia
print("A lista está vazia?", "Sim" if l.verificar_lista_vazia() else "Não")
print("")

# Buscando um valor
buscar_no, posicao = l.buscar(5) 
if buscar_no:
    print(f"Encontramos o valor '{buscar_no.valor}' esta na '{posicao+1}°' lugar da lista.")
else:
    print("O valor nao foi encontrado na lista.")
    

