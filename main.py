"""Reunir todos os códigos em um só lugar para executar tudo de uma vez"""
"""Rock in Rio 2024"""

from Clinica import Consulta, Instrumento, Paciente
from Eventos import Convidado, Cronograma, Playlist
from Restaurante import Cardapio, Faturamento, Trabalhador
from tkinter import *

class Main:
    def __init__(self):
        # Cuidar da Saúde das pessoas
        consulta = Consulta()
        instrumento = Instrumento()
        paciente = Paciente()
        
        # Planejamento do evento
        convidado = Convidado()
        cronograma = Cronograma()
        playlist = Playlist()
        
        # Restaurante do evento
        cardapio = Cardapio()
        faturamento = Faturamento()
        trabalhador = Trabalhador()
        
    def run(self):
        # Aqui você pode chamar métodos ou interagir com os objetos consulta e instrumento
        pass
    
if __name__ == '__main__':
    app = Main()  # Cria uma instância da classe Main
    app.run()  # Executa o método run (ou o que você desejar)