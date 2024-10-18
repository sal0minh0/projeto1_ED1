import sys
import os
from tkinter import *
from tkinter import Tk, Button

# Adicionar diretorio Pai para verificação no caminho de busca de módulos no Python
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Clinica import Consulta, Instrumento, Paciente
from Eventos import Convidado, Cronograma, Playlist
from Restaurante import Cardapio, Faturamento, Restaurante

# Tela Principal

class Botao:
    def __init__(self, root):
        self.root = root
        # Clinica
        self.consulta = Consulta()
        self.instrumento = Instrumento()
        self.paciente = Paciente()
        # Eventos
        self.convidado = Convidado()
        self.cronograma = Cronograma()
        self.playlist = Playlist()
        # Restaurante
        self.cardapio = Cardapio()
        self.faturamento = Faturamento()
        self.restaurante = Restaurante()

    def botao_clinica(self):
        clinica_window = Toplevel(self.root)
        clinica_window.title("Emergência Clínica")
        
        # Tamanho da tela
        window_width = 100  
        window_height = 150  
        screen_width = clinica_window.winfo_screenwidth()
        screen_height = clinica_window.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        clinica_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        consulta_btn = Button(clinica_window, text="Consulta", command=self.abrir_consulta)
        consulta_btn.pack(pady=10)

        instrumento_btn = Button(clinica_window, text="Instrumento", command=self.abrir_instrumento)
        instrumento_btn.pack(pady=10)

        paciente_btn = Button(clinica_window, text="Paciente", command=self.abrir_paciente)
        paciente_btn.pack(pady=10)

    def botao_evento(self):
        evento_window = Toplevel(self.root)
        evento_window.title("O Evento")
        
        # Tamanho da tela
        window_width = 100 
        window_height = 150 
        screen_width = evento_window.winfo_screenwidth()
        screen_height = evento_window.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        evento_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        convidado_btn = Button(evento_window, text="Convidado", command=self.abrir_convidado)
        convidado_btn.pack(pady=10)

        cronograma_btn = Button(evento_window, text="Cronograma", command=self.abrir_cronograma)
        cronograma_btn.pack(pady=10)

        playlist_btn = Button(evento_window, text="Playlist", command=self.abrir_playlist)
        playlist_btn.pack(pady=10)

    def botao_restaurante(self):
        restaurante_window = Toplevel(self.root)
        restaurante_window.title("Restaurante")

        # Tamanho da tela
        window_width = 100 
        window_height = 150 
        screen_width = restaurante_window.winfo_screenwidth()
        screen_height = restaurante_window.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        restaurante_window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        cardapio_btn = Button(restaurante_window, text="Cardapio", command=self.abrir_cardapio)
        cardapio_btn.pack(pady=10)

        faturamento_btn = Button(restaurante_window, text="Faturamento", command=self.abrir_faturamento)
        faturamento_btn.pack(pady=10)

        restaurante_btn = Button(restaurante_window, text="Restaurante", command=self.abrir_restaurante)
        restaurante_btn.pack(pady=10)

    # Clinica metodos
    def abrir_consulta(self):
        consulta_window = Toplevel(self.root)
        consulta_window.title("Gerenciar Consultas")
        from Clinica.botao_janela import ConsultaInterface
        
        # Tamanho da tela
        window_width = 650 
        window_height = 400  
        screen_width = consulta_window.winfo_screenwidth()
        screen_height = consulta_window.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        consulta_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        ConsultaInterface(consulta_window, self.consulta)

    def abrir_instrumento(self):
        instrumento_window = Toplevel(self.root)
        instrumento_window.title("Gerenciar Instrumentos")
        from Clinica.botao_janela import InstrumentoInterface
        
        # Tamanho da tela
        window_width = 650 
        window_height = 400 
        screen_width = instrumento_window.winfo_screenwidth()
        screen_height = instrumento_window.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        instrumento_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        InstrumentoInterface(instrumento_window, self.instrumento)

    def abrir_paciente(self):
        paciente_window = Toplevel(self.root)
        paciente_window.title("Gerenciar Pacientes")
        from Clinica.botao_janela import PacienteInterface
        
        # Tamanho da tela
        window_width = 650 
        window_height = 400  
        screen_width = paciente_window.winfo_screenwidth()
        screen_height = paciente_window.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        paciente_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        PacienteInterface(paciente_window, self.paciente)

    # Eventos metodos
    def abrir_convidado(self):
        convidado_window = Toplevel(self.root)
        convidado_window.title("Gerenciar Convidados")
        from Eventos.botao_janela import ConvidadoInterface
        
        # Tamanho da tela
        window_width = 650 
        window_height = 400  
        screen_width = convidado_window.winfo_screenwidth()
        screen_height = convidado_window.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        convidado_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        ConvidadoInterface(convidado_window, self.convidado)

    def abrir_cronograma(self):
        cronograma_window = Toplevel(self.root)
        cronograma_window.title("Gerenciar Cronograma")
        from Eventos.botao_janela import CronogramaInterface
        
        # Tamanho da tela
        window_width = 650  
        window_height = 400 
        screen_width = cronograma_window.winfo_screenwidth()
        screen_height = cronograma_window.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        cronograma_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        CronogramaInterface(cronograma_window, self.cronograma)

    def abrir_playlist(self):
        playlist_window = Toplevel(self.root)
        playlist_window.title("Gerenciar Playlist")
        from Eventos.botao_janela import PlaylistInterface
        
        # Tamanho da tela
        window_width = 650 
        window_height = 400 
        screen_width = playlist_window.winfo_screenwidth()
        screen_height = playlist_window.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        playlist_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        PlaylistInterface(playlist_window, self.playlist)

    # Restaurante metodos
    def abrir_cardapio(self):
        cardapio_window = Toplevel(self.root)
        cardapio_window.title("Gerenciar Cardápio")
        from Restaurante.botao_janela import CardapioInterface
        
        # Tamanho da tela
        window_width = 650  
        window_height = 500  
        screen_width = cardapio_window.winfo_screenwidth()
        screen_height = cardapio_window.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        cardapio_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        CardapioInterface(cardapio_window, self.cardapio)

    def abrir_faturamento(self):
        faturamento_window = Toplevel(self.root)
        faturamento_window.title("Gerenciar Faturamento")
        from Restaurante.botao_janela import FaturamentoInterface
        
        # Tamanho da tela
        window_width = 650 
        window_height = 400
        screen_width = faturamento_window.winfo_screenwidth()
        screen_height = faturamento_window.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        faturamento_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        FaturamentoInterface(faturamento_window, self.faturamento)

    def abrir_restaurante(self):
        restaurante_window = Toplevel(self.root)
        restaurante_window.title("Gerenciar Restaurante")
        from Restaurante.botao_janela import RestauranteInterface
        
        # Tamanho da tela
        window_width = 650 
        window_height = 400
        screen_width = restaurante_window.winfo_screenwidth()
        screen_height = restaurante_window.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        restaurante_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        RestauranteInterface(restaurante_window, self.restaurante)

class Main:
    def __init__(self):
        
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
        
        # Criar instância de Botao com a janela principal como root
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

# Executar a aplicação
if __name__ == '__main__':
    app = Main()
    app.run()