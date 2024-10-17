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

class Restaurante:
    def __init__(self):
        self.trabalhadores = lista_encadeada_simples.ListaEncadeadaSimples()
        self.mesas = lista_encadeada_simples.ListaEncadeadaSimples()
        
    def adicionar_trabalhador(self, trabalhador):
        self.trabalhadores.inserir_no_fim(trabalhador)
        print(f"'{trabalhador}' adicionado como trabalhador.")
    
    def remover_trabalhador(self, trabalhador):
        self.trabalhadores.remover(trabalhador)
    
    def atualizar_trabalhador(self, trabalhador_atual, novo_trabalhador):
        if self.trabalhadores.atualizar_lista(trabalhador_atual, novo_trabalhador):
            print(f"'{trabalhador_atual}' foi atualizado para '{novo_trabalhador}'.")
        else:
            print(f"'{trabalhador_atual}' não trabalha no restaurante.")
            
    def buscar_um_trabalhador(self, trabalhador):
        _, posicao = self.trabalhadores.buscar(trabalhador)
        if posicao != -1:
            print(f"'{trabalhador}' encontrado na posição {posicao+1} da equipe.")
        else:
            print(f"'{trabalhador}' não trabalha no restaurante ou não está cadastrado.")
            
    def exibir_trabalhadores(self):
        print("Trabalhadores do restaurante:")
        self.trabalhadores.imprimir()
    
    def contar_trabalhadores(self):
        quantidade_trabalhadores = self.trabalhadores.contar_elementos()
        print(f"O restaurante tem {quantidade_trabalhadores} trabalhadores cadastrados.")

    def adicionar_mesa(self, numero):
        nova_mesa = Mesa(numero)
        self.mesas.inserir_no_fim(nova_mesa)
        print(f"Mesa {numero} adicionada ao restaurante.")

    def ocupar_mesa(self, numero_mesa, nome_cliente):
        atual = self.mesas.cabeca
        while atual:
            if atual.valor.numero == numero_mesa:
                if not atual.valor.ocupada:
                    atual.valor.ocupada = True
                    atual.valor.cliente = nome_cliente
                    print(f"Mesa {numero_mesa} ocupada por {nome_cliente}.")
                else:
                    print(f"Mesa {numero_mesa} já está ocupada.")
                return
            atual = atual.prox
        print(f"Mesa {numero_mesa} não encontrada.")

    def liberar_mesa(self, numero_mesa):
        atual = self.mesas.cabeca
        while atual:
            if atual.valor.numero == numero_mesa:
                if atual.valor.ocupada:
                    atual.valor.ocupada = False
                    atual.valor.cliente = None
                    print(f"Mesa {numero_mesa} liberada.")
                else:
                    print(f"Mesa {numero_mesa} já está livre.")
                return
            atual = atual.prox
        print(f"Mesa {numero_mesa} não encontrada.")

    def exibir_status_mesas(self):
        print("Status das mesas:")
        atual = self.mesas.cabeca
        while atual:
            print(atual.valor)
            atual = atual.prox

# Exemplo de uso do sistema de gerenciamento do restaurante

restaurante = Restaurante()

# Adicionando trabalhadores
restaurante.adicionar_trabalhador("João")
restaurante.adicionar_trabalhador("Maria")
restaurante.adicionar_trabalhador("Pedro")
print("")

# Exibindo trabalhadores
restaurante.exibir_trabalhadores()
print("")

# Adicionando mesas
restaurante.adicionar_mesa(1)
restaurante.adicionar_mesa(2)
restaurante.adicionar_mesa(3)
print("")

# Ocupando mesas
restaurante.ocupar_mesa(1, "Carlos")
restaurante.ocupar_mesa(2, "Ana")
print("")

# Exibindo status das mesas
restaurante.exibir_status_mesas()
print("")

# Liberando uma mesa
restaurante.liberar_mesa(1)
print("")

# Exibindo status atualizado das mesas
restaurante.exibir_status_mesas()
print("")

# Contando trabalhadores
restaurante.contar_trabalhadores()