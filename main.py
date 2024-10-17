import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Clinica import Consulta, Instrumento, Paciente
from Clinica.botao_janela import *
from Eventos import Convidado, Cronograma, Playlist
from Eventos.botao_janela import *
from Restaurante import Cardapio, Faturamento, Restaurante
from Restaurante.botao_janela import *
from tkinter import *
from tkinter import Tk, Button

class Main:
    def __init__(self):
        # Cuidar da Saúde das pessoas
        self.consulta = Consulta()
        self.instrumento = Instrumento()
        self.paciente = Paciente()
        
        # Planejamento do evento
        self.convidado = Convidado()
        self.cronograma = Cronograma()
        self.playlist = Playlist()
        
        # Restaurante do evento
        self.cardapio = Cardapio()
        self.faturamento = Faturamento()
        self.restaurante = Restaurante()
        
        # Criar a janela principal
        self.janela_principal = Tk()
        self.janela_principal.title("Rock in Rio 2024")
        
        window_width = 275
        window_height = 75
        screen_width = self.janela_principal.winfo_screenwidth()
        screen_height = self.janela_principal.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.janela_principal.geometry(f"{window_width}x{window_height}+{x}+{y}")
        
        # Create Botao instance with the main window as root
        self.botao = Botao(self.janela_principal)
        
        self.criar_interface()
        
    def criar_interface(self):
        texto_orientacao = Label(self.janela_principal, text="Escolha a sua opção desejada:")
        texto_orientacao.grid(column=0, row=0, columnspan=3, pady=10)

        botao_clinica = Button(self.janela_principal, text="Emergência clínica", command=self.botao_clinica)
        botao_clinica.grid(column=0, row=1, padx=5, pady=5)

        botao_evento = Button(self.janela_principal, text="O Evento", command=self.botao_evento)
        botao_evento.grid(column=1, row=1, padx=5, pady=5)

        botao_restaurante = Button(self.janela_principal, text="Restaurante", command=self.botao_restaurante)
        botao_restaurante.grid(column=2, row=1, padx=5, pady=5)

    def botao_clinica(self):
        self.botao.botao_clinica()
    
    def botao_evento(self):
        self.botao.botao_evento()
    
    def botao_restaurante(self):
        self.botao.botao_restaurante()

    def run(self):
        self.janela_principal.mainloop()

if __name__ == '__main__':
    app = Main()
    app.run()