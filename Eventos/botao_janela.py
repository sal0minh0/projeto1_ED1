from tkinter import *
from tkinter import messagebox
from Eventos.convidado import Convidado
from Eventos.cronograma import Cronograma
from Eventos.playlist import Playlist

class BaseInterface:
    """Classe base para todas as interfaces com funcionalidades comuns"""
    def __init__(self, root, data_manager, title, title_plural, example_text):
        self.root = root
        self.data_manager = data_manager
        self.title = title
        self.title_plural = title_plural
        
        self.button_frame = Frame(root)
        self.button_frame.pack(pady=5)
        
        self.refresh_button = Button(
            self.button_frame, 
            text="↻ Atualizar Lista", 
            command=self.refresh_display,
            pady=5,
            padx=10
        )
        self.refresh_button.pack(side=LEFT, padx=5)
        
        self.input_frame = Frame(root)
        self.input_frame.pack(pady=10)
    
        self.label = Label(self.input_frame, text=f"Inserir {title} {example_text}:")
        self.label.pack(side=LEFT)
        
        self.entry = Entry(self.input_frame, width=15)
        self.entry.pack(side=LEFT, padx=5)
        
        self.new_value_frame = Frame(root)
        self.new_value_frame.pack(pady=5)
        
        self.new_value_label = Label(self.new_value_frame, text=f"Novo(a) {title}:")
        self.new_value_label.pack(side=LEFT)
        
        self.new_value_entry = Entry(self.new_value_frame, width=30)
        self.new_value_entry.pack(side=LEFT, padx=5)
        
        self.action_frame = Frame(root)
        self.action_frame.pack(pady=5)
        
        self.add_button = Button(
            self.action_frame, 
            text=f"Adicionar {title}",
            command=self.adicionar_item
        )
        self.add_button.pack(side=LEFT, padx=5)
        
        self.remove_button = Button(
            self.action_frame, 
            text=f"Remover {title}",
            command=self.remover_item
        )
        self.remove_button.pack(side=LEFT, padx=5)
        
        self.edit_button = Button(
            self.action_frame, 
            text=f"Editar {title}",
            command=self.editar_item
        )
        self.edit_button.pack(side=LEFT, padx=5)
        
        self.search_button = Button(
            self.action_frame, 
            text=f"Buscar {title}",
            command=self.buscar_item
        )
        self.search_button.pack(side=LEFT, padx=5)
        
        self.list_frame = Frame(root, relief=SOLID, borderwidth=1)
        self.list_frame.pack(padx=10, pady=10, fill=BOTH, expand=True)
        
        self.scrollbar = Scrollbar(self.list_frame)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        
        self.output_text = Text(
            self.list_frame, 
            height=10, 
            width=50, 
            yscrollcommand=self.scrollbar.set
        )
        self.output_text.pack(side=LEFT, fill=BOTH, expand=True)
        self.scrollbar.config(command=self.output_text.yview)
        
        self.entry.bind('<Return>', lambda event: self.adicionar_item())
        
        self.refresh_display()

    def editar_item(self):
        """Editar um item existente com um novo valor"""
        item_atual = self.entry.get().strip()
        novo_item = self.new_value_entry.get().strip()
        
        if item_atual and novo_item:
            try:
                self.data_manager.atualizar_item(item_atual, novo_item) 
                self.entry.delete(0, END)
                self.new_value_entry.delete(0, END)
                self.atualizar_output(f"{self.title} '{item_atual}' atualizado para '{novo_item}'!")
                self.refresh_display()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao editar {self.title.lower()}: {str(e)}")
        else:
            messagebox.showerror("Erro", f"Por favor, preencha tanto o valor atual quanto o novo valor do {self.title.lower()}.")

    def get_items_list(self):
        if self.data_manager.verificar_lista_vazia():
            return []
        items = []
        if self.data_manager.itens.cauda is not None:
            atual = self.data_manager.itens.cauda.proximo
            while True:
                items.append(atual.valor)
                atual = atual.proximo
                if atual == self.data_manager.itens.cauda.proximo:
                    break
        return items

    def refresh_display(self):
        self.output_text.config(state=NORMAL)
        self.output_text.delete(1.0, END)
    
        try:
            items = self.get_items_list()
            if items:
                for i, item in enumerate(items, 1):
                # Formatando a exibição dos dados no formato desejado
                    if isinstance(item, dict):  # Verifica se o item é um dicionário
                        formatted_item = f"Nome: {item.get('nome', '')}, Número de Inscrição: {item.get('numero_inscricao', '')}, Evento: {item.get('evento', '')}"
                        self.output_text.insert(END, f"{i}. {formatted_item}\n")
                    else:
                        self.output_text.insert(END, f"{i}. {item}\n")
            else:
                self.output_text.insert(END, f"Não há {self.title_plural} cadastrados.")
        except Exception as e:
            self.output_text.insert(END, f"Erro ao carregar {self.title_plural}.")
            print(f"Error: {e}")
    
        self.output_text.config(state=DISABLED)
        self.root.update_idletasks()

    def adicionar_item(self):
        """Método base para adicionar um item. Deve ser sobrescrito pelas subclasses."""
        item = self.entry.get().strip()
        if item:
            try:
                self.data_manager.adicionar_item(item)
                self.entry.delete(0, END)
                self.atualizar_output(f"{self.title} '{item}' adicionado com sucesso!")
                self.refresh_display()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao adicionar {self.title.lower()}: {str(e)}")
        else:
            messagebox.showerror("Erro", f"Por favor, insira um {self.title.lower()} válido.")


    def remover_item(self):
        item_texto = self.entry.get().strip()
        if item_texto:
            try:
                if self.data_manager.itens.remover(item_texto):
                    self.entry.delete(0, END)
                    self.atualizar_output(f"{self.title} '{item_texto}' removido com sucesso!")
                    self.refresh_display()
                else:
                    messagebox.showerror("Erro", f"{self.title} não encontrado.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao remover {self.title.lower()}: {str(e)}")
        else:
            messagebox.showerror("Erro", f"Por favor, insira um {self.title.lower()} para remover.")

    def buscar_item(self):
        item_texto = self.entry.get().strip()
        if item_texto:
            try:
                result = self.data_manager.buscar_um_item(item_texto)
                self.atualizar_output(result)
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao buscar {self.title.lower()}: {str(e)}")
        else:
            messagebox.showerror("Erro", f"Por favor, insira um {self.title.lower()} para buscar.")
  
    def atualizar_output(self, message):
        self.output_text.config(state=NORMAL)
        self.output_text.insert(END, f"\n{message}\n")
        self.output_text.see(END)
        self.output_text.config(state=DISABLED)

class ConvidadoInterface(BaseInterface):
    def __init__(self, root, convidado):
        super().__init__(
            root=root,
            data_manager=convidado,
            title="Convidado",
            title_plural="convidados",
            example_text="(ex: Nome)"
        )
        
        # Adicionar o campo "Número de Inscrição" abaixo de "Nome"
        self.label_numero_inscricao = Label(self.input_frame, text="Número de Inscrição:")
        self.label_numero_inscricao.pack(side=LEFT, padx=5)
        self.entry_numero_inscricao = Entry(self.input_frame, width=10)
        self.entry_numero_inscricao.pack(side=LEFT, padx=5)
        
        # Adicionar o campo "Evento" abaixo de "Número de Inscrição"
        self.label_evento = Label(self.input_frame, text="Evento:")
        self.label_evento.pack(side=LEFT, padx=5)
        self.entry_evento = Entry(self.input_frame, width=10)
        self.entry_evento.pack(side=LEFT, padx=5)

    def adicionar_item(self):
        nome = self.entry.get().strip()
        numero_inscricao = self.entry_numero_inscricao.get().strip()
        evento = self.entry_evento.get().strip()

        if nome and numero_inscricao and evento:
            try:
                self.data_manager.adicionar_item(nome, numero_inscricao, evento)
                self.entry.delete(0, END)
                self.entry_numero_inscricao.delete(0, END)
                self.entry_evento.delete(0, END)
                self.atualizar_output(f"Convidado '{nome}' adicionado ao evento '{evento}' com sucesso!")
                self.refresh_display()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao adicionar convidado: {str(e)}")
                
        else:
            messagebox.showerror("Erro", "Por favor, insira nome, número de inscrição e evento válidos.")
            
class CronogramaInterface(BaseInterface):
    def __init__(self, root, cronograma):
        super().__init__(
            root=root,
            data_manager=cronograma,
            title="Cronograma",
            title_plural="cronogramas",
            example_text="(ex: Atividade - Horário)"
        )

class PlaylistInterface(BaseInterface):
    def __init__(self, root, playlist):
        super().__init__(
            root=root,
            data_manager=playlist,
            title="Música",
            title_plural="músicas",
            example_text="(ex: Cantor(a)/Banda - Música)"
        )

    def get_items_list(self):
        if self.data_manager.verificar_lista_vazia():
            return []
        items = []
        if self.data_manager.itens.cauda is not None:
            atual = self.data_manager.itens.cauda.proximo
            while True:
                items.append(atual.valor)
                atual = atual.proximo
                if atual == self.data_manager.itens.cauda.proximo:
                    break
        return items

    def refresh_display(self):
        self.output_text.config(state=NORMAL)
        self.output_text.delete(1.0, END)
    
        try:
            items = self.get_items_list()
            if items:
                for i, item in enumerate(items, 1):
                    self.output_text.insert(END, f"{i}. {item}\n")
            else:
                self.output_text.insert(END, f"Não há {self.title_plural} na playlist.")
        except Exception as e:
            self.output_text.insert(END, f"Erro ao carregar {self.title_plural}.")
            print(f"Error: {e}")
    
        self.output_text.config(state=DISABLED)
        self.root.update_idletasks()

    def adicionar_item(self):
        item = self.entry.get().strip()
        if item:
            try:
                self.data_manager.adicionar_item(item)
                self.entry.delete(0, END)
                self.atualizar_output(f"{self.title} '{item}' adicionada à playlist com sucesso!")
                self.refresh_display()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao adicionar {self.title.lower()}: {str(e)}")
        else:
            messagebox.showerror("Erro", f"Por favor, insira uma {self.title.lower()} válida.")

    def remover_item(self):
        item_texto = self.entry.get().strip()
        if item_texto:
            try:
                self.data_manager.remover_item(item_texto)
                self.entry.delete(0, END)
                self.atualizar_output(f"{self.title} '{item_texto}' removida da playlist com sucesso!")
                self.refresh_display()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao remover {self.title.lower()}: {str(e)}")
        else:
            messagebox.showerror("Erro", f"Por favor, insira uma {self.title.lower()} para remover.")

    def buscar_item(self):
        item_texto = self.entry.get().strip()
        if item_texto:
            try:
                result = self.data_manager.buscar_um_item(item_texto)
                self.atualizar_output(result)
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao buscar {self.title.lower()}: {str(e)}")
        else:
            messagebox.showerror("Erro", f"Por favor, insira uma {self.title.lower()} para buscar.")
            
class Botao:
    def __init__(self, root):
        self.root = root
        self.convidado = Convidado()
        self.cronograma = Cronograma()
        self.playlist = Playlist()
        
    def center_window(self, window, width, height):
            window.update_idletasks()  # Garantir que o tamanho da janela esteja atualizado
            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()
            x = (screen_width - width) // 2
            y = (screen_height - height) // 2
            window.geometry(f"{width}x{height}+{x}+{y}")

    def botao_evento(self):
        evento_window = Toplevel(self.root)
        evento_window.title("O Evento")

        convidado_btn = Button(evento_window, text="Convidado", command=self.abrir_convidado)
        convidado_btn.pack(pady=10)

        cronograma_btn = Button(evento_window, text="Cronograma", command=self.abrir_cronograma)
        cronograma_btn.pack(pady=10)

        playlist_btn = Button(evento_window, text="Playlist", command=self.abrir_playlist)
        playlist_btn.pack(pady=10)

    def abrir_convidado(self):
        convidado_window = Toplevel(self.root)
        convidado_window.title("Gerenciar Convidados")
        ConvidadoInterface(convidado_window, self.convidado)

    def abrir_cronograma(self):
        cronograma_window = Toplevel(self.root)
        cronograma_window.title("Gerenciar um Cronograma")
        CronogramaInterface(cronograma_window, self.cronograma)

    def abrir_playlist(self):
        playlist_window = Toplevel(self.root)
        playlist_window.title("Gerenciar uma Playlist")
        PlaylistInterface(playlist_window, self.playlist)