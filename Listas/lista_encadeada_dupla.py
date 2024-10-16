class No:
    """Classe nó nessa lista"""
    def __init__(self, valor):
        self.valor = valor # Atribuindo valor do no
        self.anterior = None # Valor anterior do no
        self.prox = None # Valor proximo do no
        
class ListaEncadeadaDupla:
    """Classe da lista dupla"""
    def __init__(self):
        self.cabeca = None # Elemento cabeça, primeiro no
        self.cauda = None # Elemento cauda, ultimo no

    def verificar_lista_vazia(self):
        """Será que essa lista está vazia?"""
        return self.cabeca is None

    def inserir(self, valor):
        """Inserir no final da lista"""
        novo_no = No(valor) # Declara a variavel novo no     
        if self.verificar_lista_vazia(): 
            self.cabeca = self.cauda = novo_no # Verifica se a lista esta vazia e coloca o novo no
        else:
            self.cauda.prox = novo_no
            novo_no.anterior = self.cauda # Se não ele coloca no ultimo elemento, o cauda
            self.cauda = novo_no

    def remover(self, valor):
        """Remover um nó da lista"""
        if self.verificar_lista_vazia():
            print("A lista está vazia, nada para remover.")
            return
        atual = self.cabeca
        while atual: # Verificar percorrendo a lista, se o no é cauda ou cabeça e remover
            if atual.valor == valor:
                if atual.anterior:
                    atual.anterior.prox = atual.prox
                else:
                    self.cabeca = atual.prox

                if atual.prox:
                    atual.prox.anterior = atual.anterior
                else:
                    self.cauda = atual.anterior
                
                print(f"O valor {valor} foi removido da lista.")
                return
            atual = atual.prox
        print("Valor não encontrado na lista.")

    def buscar(self, valor):
        """Busca valores na lista"""
        atual = self.cabeca
        posicao = 0
        while atual:
            if atual.valor == valor: # Se o valor atual for o que queremos retorne ele
                return atual, posicao
            atual = atual.prox      
            posicao += 1
        return None, -1 # Se não retorne falso

    def atualizar(self, valor_atual, novo_valor):
        """Atualizar um valor na lista"""
        no_encontrado, _ = self.buscar(valor_atual)
        if no_encontrado:
            no_encontrado.valor = novo_valor
            print(f"'{valor_atual}' foi atualizado para '{novo_valor}'.")
            return True
        else:
            print(f"'{valor_atual}' não foi encontrado na lista para atualização.")
            return False

    def imprimir(self):
        """Imprime a lista até o final"""
        if self.verificar_lista_vazia():
            print("A lista está vazia.")
            return
        atual = self.cabeca
        while atual:
            print(atual.valor, end = "\n" if atual.prox else "\n")
            atual = atual.prox
            
            
    def trocar_true_false_sim_nao(valor):
        """Trocar True or False por Sim e não"""
        return "Sim" if valor else "Não"
    resposta = True
    resposta = False
    
    def contar_elementos(self):
        """Conta o número de elementos na lista"""
        atual = self.cabeca
        contador = 0
        while atual:
            contador += 1  # Incrementa o contador a cada nó encontrado
            atual = atual.prox  # Move para o próximo nó
        return contador


