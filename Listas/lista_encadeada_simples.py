class No:
    """Classe que é nó na lista"""
    def __init__(self, dado):
        self.dado = dado  # Dado do nó
        self.prox = None  # Referência para o próximo nó

class ListaEncadeadaSimples:
    """Classe que representa a lista encadeada"""
    def __init__(self):
        self.cabeca = None  # Inicialmente, a lista está vazia

    def lista_vazia(self):
        """Verifica se a lista está vazia"""
        return self.cabeca is None

    def inserir_no_começo(self, dado):
        """Insere um novo nó no início da lista"""
        novo_no = No(dado)  # Cria um novo nó
        novo_no.prox = self.cabeca  # O próximo do novo nó é o antigo primeiro nó
        self.cabeca = novo_no  # O novo nó passa a ser o primeiro nó

    def inserir_no_fim(self, dado):
        """Insere um novo nó no final da lista"""
        novo_no = No(dado)
        if self.lista_vazia():
            self.cabeca = novo_no  # Se a lista está vazia, o novo nó é o primeiro
        else:
            atual = self.cabeca
            while atual.prox:  # Percorre até o último nó
                atual = atual.prox
            atual.prox = novo_no  # O último nó aponta para o novo nó

    def remover(self, dado):
        """Remove o primeiro nó que contém o dado especificado"""
        atual = self.cabeca
        anterior = None
        while atual and atual.dado != dado:
            anterior = atual
            atual = atual.prox
        if atual is None:
            print("Elemento não encontrado.")
            return
        if anterior is None:
            self.cabeca = atual.prox  # Remove o nó da cabeça
        else:
            anterior.prox = atual.prox  # Remove o nó ligando o anterior ao próximo

    def busca(self, dado):
        """Busca um nó que contenha o dado especificado"""
        atual = self.cabeca
        while atual is not None:  # Vai alcaçar até o final da lista
            if atual.dado == dado: # Verificar se o no atual tem um dado que procuramos
                return True
            atual = atual.prox  # Se sim mover para o proximo no
        return False  # Se percorrer toda a lista e não achar
    
    def atualizar_lista(self, anterior, novo_valor):
        """Atualiza o valor de um nó na lista"""
        atual = self.cabeca
        while atual is not None:
            if atual.dado == anterior:
                atual.dado = novo_valor
                return True
            atual = atual.prox
        return False


    def imprimir(self):
        """Exibe os elementos da lista encadeada"""
        elementos = []
        atual = self.cabeca
        while atual:
            elementos.append(atual.dado)
            atual = atual.prox
        print(" - ".join(map(str, elementos)))

# Usagens das funções

# Objeto da Classe
l = ListaEncadeadaSimples()

#Inserir
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

# Atualizar
l.atualizar_lista(3, 3) 
l.imprimir()
print("")

# Busca
print(l.busca(1))  # Saída: True
print("")
print(l.busca(9))  # Saída: False