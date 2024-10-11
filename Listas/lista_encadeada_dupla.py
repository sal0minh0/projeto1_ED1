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
        no_encontrado, posicao = self.buscar(valor_atual)
        if no_encontrado:
            no_encontrado.valor = novo_valor
        else:
            print("Valor não encontrado na lista para atualização.")

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
            

# Exemplo de uso da lista encadeada dupla
l = ListaEncadeadaDupla()

# Inserindo valores
l.inserir(10)
l.inserir(20)
l.inserir(30)

# Imprimindo a lista
l.imprimir()
print("")

# Atualizando um valor
l.atualizar(20, 25)
l.imprimir()
print("")

# Removendo um valor
l.remover(25)
l.imprimir()
print("")

# Verificando se a lista está vazia
print("A lista está vazia?", "Sim" if l.verificar_lista_vazia() else "Não")
print("")

# Buscando um valor
buscar_no, posicao = l.buscar(30) 
if buscar_no:
    print(f"Encontramos o valor '{buscar_no.valor}' esta na '{posicao+1}°' lugar da lista.")
else:
    print("O valor nao foi encontrado na lista.")

