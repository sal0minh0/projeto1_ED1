import sys
import os

# Adicionando o diretorio "Eventos" para a pasta Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Listas import lista_encadeada_circular

class Playlist:
    """Representa uma playlist de músicas usando lista encadeada circular"""
    def __init__(self):
        self.musicas = lista_encadeada_circular.ListaEncadeadaCircular()
        
    def adicionar_musica(self, musica):
        """Adiciona uma música na playlist"""
        self.musicas.inserir(musica)
        print(f"'{musica}' adicionado à playlist.")
    
    def remover_musica(self, musica):
        """Remove uma música da playlist"""
        self.musicas.remover(musica)
    
    def atualizar_musica(self, musica_atual, nova_musica):
        """Atualiza uma música na playlist"""
        if self.musicas.atualizar(musica_atual, nova_musica):
            print(f"'{musica_atual}' foi atualizado para '{nova_musica}'.")
        else:
            print(f"'{musica_atual}' não está na playlist.")
    
    def buscar_uma_musica(self, musica):
        """Busca uma música na playlist"""
        _, posicao = self.musicas.buscar(musica)
        if posicao != -1:
            print(f"'{musica}' está no {posicao+1}° lugar da playlist.")
        else:
            print(f"'{musica}' não está na playlist.")
    
    def exibir_playlist(self):
        """Exibe a playlist de músicas"""
        print("Playlist de músicas:")
        self.musicas.imprimir()
    
    def verificar_vazio(self):
        """Verifica se a playlist está vazia"""
        vazio = self.musicas.verificar_lista_vazia()
        print(f"A playlist está vazia? {'Sim' if vazio else 'Não'}")
    
    def contar_musicas(self):
        """Conta quantas músicas tem na playlist"""
        quantidade_musicas = self.musicas.contar_elementos()
        print(f"A playlist tem {quantidade_musicas} músicas.")
        
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
p.verificar_vazio()
print("")

# Buscar uma música
p.buscar_uma_musica("Deep Purple - Burn")
print("")

# Contar músicas
p.contar_musicas()