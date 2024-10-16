class No:
    """A Classe No da estrutura"""
    def __init__(self, valor):
        self.valor = valor # Valor do no
        self.proximo = None # Valor do próximo no

class ListaEncadeadaCircular:
    """Classe da lista circular"""
    def __init__(self):
        self.cauda = None # Elemento cauda, ultimo no

    def verificar_lista_vazia(self):
        """Verifica se a lista está vazia"""
        return self.cauda is None 

    def inserir(self, valor):
        """Insere o no no final da lista"""
        novo_no = No(valor)
        if self.verificar_lista_vazia():
            self.cauda = novo_no # Se a lista está vazia, o novo no aponta para ele mesmo
            novo_no.proximo = novo_no
        else:
            novo_no.proximo = self.cauda.proximo
            self.cauda.proximo = novo_no # Se não inserir o novo no apos a cauda e atualizar a cauda
            self.cauda = novo_no

    def remover(self, valor):
        """Remover o no da lista"""
        if self.verificar_lista_vazia():
            print("A lista está vazia.") # Verificar se a lista esta vazia
            return
        atual = self.cauda.proximo
        anterior = self.cauda
        while True:
            if atual.valor == valor:
                if atual == self.cauda and atual.proximo == self.cauda: # Se for o único no na lista
                    self.cauda = None
                else:
                    anterior.proximo = atual.proximo
                    if atual == self.cauda: # Se for o no da cauda, movemos o no cauda
                        self.cauda = anterior
                print(f"O valor {valor} foi removido.")
                return
            anterior = atual
            atual = atual.proximo
            if atual == self.cauda.proximo:
                print(f"O valor {valor} não foi encontrado.") # Caso não encontramos o valor
                break

    def buscar(self, valor):
        """Busca valores na lista"""
        if self.verificar_lista_vazia():
            return None
        posicao = 0
        atual = self.cauda.proximo
        while True:
            if atual.valor == valor:
                return atual, posicao
            atual = atual.proximo
            posicao += 1
            if atual == self.cauda.proximo:
                return None, -1

    def atualizar(self, valor_atual, novo_valor):
        """Atualizar um valor na lista"""
        no_encontrado, posicao = self.buscar(valor_atual)
        if no_encontrado:
            no_encontrado.valor = novo_valor
        else:
            print(f"Valor {valor_atual} não encontrado para atualizar.")

    def imprimir(self):
        """Imprime a lista até o final"""
        if self.verificar_lista_vazia():
            print("A lista está vazia.")
            return
        atual = self.cauda.proximo
        while True:
            print(atual.valor, end="\n")
            atual = atual.proximo
            if atual == self.cauda.proximo:
                break
        print()
        
    def trocar_true_false_sim_nao(valor):
        """Trocar True or False por Sim e não"""
        return "Sim" if valor else "Não"
    resposta = True
    resposta = False
    
    def contar_elementos(self):
        """Conta o número de elementos na lista"""
        if self.verificar_lista_vazia(): 
            return 0
        atual = self.cauda.proximo  # Começa do nó após a cauda, o primeiro nó
        contador = 1  # Inicia o contador como 1, pois já estamos contando o primeiro nó
        while atual != self.cauda:  # Continua até que o nó atual seja novamente a cauda
            contador += 1
            atual = atual.proximo  # Move para o próximo nó
        return contador
