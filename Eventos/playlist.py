import sys
import os

# Adicionando o diretorio "Eventos" para a pasta Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Listas import lista_encadeada_circular

class Playlist:
    """Representa uma playlist de músicas usando lista encadeada circular"""
    def __init__(self):
        self.itens = lista_encadeada_circular.ListaEncadeadaCircular()
        
    def adicionar_item(self, musica):
        """Adiciona uma música na playlist"""
        self.itens.inserir(musica)
        print(f"'{musica}' adicionado à playlist.")
    
    def remover_item(self, musica):
        """Remove uma música da playlist"""
        self.itens.remover(musica)
    
    def atualizar_item(self, musica_atual, nova_musica):
        """Atualiza uma música na playlist"""
        if self.itens.atualizar(musica_atual, nova_musica):
            print(f"'{musica_atual}' foi atualizado para '{nova_musica}'.")
        else:
            print(f"'{musica_atual}' não está na playlist.")
    
    def buscar_um_item(self, musica):
        """Busca um item e retorna uma string com as informações"""
        atual = self.itens.cauda.proximo if self.itens.cauda else None
        posicao = 0
        while atual:
            if atual.valor == musica: 
                return f"'{musica}' encontrado na posicao {posicao+1} da lista."
            atual = atual.proximo
            posicao += 1
            if atual == self.itens.cauda.proximo:
                break
        return f"'{musica}' não encontrado na lista."
    
    def exibir_itens(self):
        """Exibe a playlist de músicas"""
        print("Playlist de músicas:")
        self.itens.imprimir()
    
    def verificar_lista_vazia(self):
        """Verifica se a playlist está vazia"""
        return self.itens.verificar_lista_vazia()
    
    def contar_itens(self):
        """Conta quantas músicas tem na playlist"""
        return self.itens.contar_elementos()
    
"""       
# Exemplo de uso da playlist

# Criar objeto playlist
p = Playlist()

# Adicionando músicas à playlist
p.adicionar_musica("David Bowie - Ziggy Stardust")
p.adicionar_musica("Deep Purple - Burn")
p.adicionar_musica("Soundgarden - Rusty Cage")
p.adicionar_musica("Kansas - Dust in the Wind")
print("")

# Remover uma música
p.remover_musica("Soundgarden - Rusty Cage")
print("")

# Exibir a playlist
p.exibir_playlist()
print("")

# Atualizar uma música
p.atualizar_musica("Kansas - Dust in the Wind", "Led Zeppelin - Rock and Roll")
print("")

# Exibir a playlist
p.exibir_playlist()
print("")

# Verificar se a playlist está vazia
p.verificar_lista_vazia()
print("")

# Buscar uma música
p.buscar_uma_musica("Deep Purple - Burn")
print("")

# Contar músicas
p.contar_musicas()
"""