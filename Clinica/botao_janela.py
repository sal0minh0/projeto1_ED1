from tkinter import *
from tkinter import messagebox
from Clinica.consulta import Consulta
from Clinica.instrumento import Instrumento
from Clinica.paciente import Paciente

class BaseInterface:
    """Base class for all interfaces with common functionality"""
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
        
        self.entry = Entry(self.input_frame, width=30)
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
        """Edit an existing item with a new value"""
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
        current = self.data_manager.itens.cabeca
        items = []
        while current:
            items.append(current.valor)
            current = current.prox
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
                self.output_text.insert(END, f"Não há {self.title_plural} cadastrados.")
        except Exception as e:
            self.output_text.insert(END, f"Erro ao carregar {self.title_plural}.")
            print(f"Error: {e}")
        
        self.output_text.config(state=DISABLED)
        self.root.update_idletasks()

    def adicionar_item(self):
        item_texto = self.entry.get().strip()
        if item_texto:
            try:
                self.data_manager.adicionar_item(item_texto)
                self.entry.delete(0, END)
                self.atualizar_output(f"{self.title} '{item_texto}' adicionado com sucesso!")
                self.refresh_display()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao adicionar {self.title.lower()}: {str(e)}")
        else:
            messagebox.showerror("Erro", f"Por favor, insira um {self.title.lower()} válido.")

    def remover_item(self):
        item_texto = self.entry.get().strip()
        if item_texto:
            try:
                self.data_manager.remover_item(item_texto)  
                self.entry.delete(0, END)
                self.atualizar_output(f"{self.title} '{item_texto}' removido com sucesso!")
                self.refresh_display()
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

class ConsultaInterface(BaseInterface):
    def __init__(self, root, consulta):
        super().__init__(
            root=root,
            data_manager=consulta,
            title="Consulta",
            title_plural="consultas",
            example_text="(ex: Dr(a) - Horario)"
        )

class InstrumentoInterface(BaseInterface):
    def __init__(self, root, instrumento):
        super().__init__(
            root=root,
            data_manager=instrumento,
            title="Instrumento",
            title_plural="instrumentos",
            example_text="(ex: Bisturi - Quantidade)"
        )

class PacienteInterface(BaseInterface):
    def __init__(self, root, paciente):
        super().__init__(
            root=root,
            data_manager=paciente,
            title="Paciente",
            title_plural="pacientes",
            example_text="(ex: Nome, Idade, Condição, Última Consulta)"
        )
        self.historico_button = Button(
            self.action_frame, 
            text=f"Ver Histórico Médico", 
            command=self.ver_historico_medico
        )
        self.historico_button.pack(side=LEFT, padx=5)
    
    def ver_historico_medico(self):
        """Exibe o histórico médico e a data da última consulta do paciente"""
        nome_paciente = self.entry.get().strip()
        
        if nome_paciente:
            paciente = self.data_manager.buscar_paciente_por_nome(nome_paciente)
            if paciente:
                historico = paciente.historico_medico
                ultima_consulta = paciente.ultima_consulta
                messagebox.showinfo(
                    "Histórico Médico",
                    f"Paciente: {paciente.nome}\nIdade: {paciente.idade}\n\nHistórico Médico: {historico}\nÚltima Consulta: {ultima_consulta}"
                )
            else:
                messagebox.showerror("Erro", f"Paciente '{nome_paciente}' não encontrado.")
        else:
            messagebox.showerror("Erro", "Por favor, insira o nome do paciente.")

class Botao:
    def __init__(self, root):
        self.root = root
        self.consulta = Consulta()
        self.instrumento = Instrumento()
        self.paciente = Paciente()

    def botao_clinica(self):
        clinica_window = Toplevel(self.root)
        clinica_window.title("Emergência Clínica")

        consulta_btn = Button(clinica_window, text="Consulta", command=self.abrir_consulta)
        consulta_btn.pack(pady=10)

        instrumento_btn = Button(clinica_window, text="Instrumento", command=self.abrir_instrumento)
        instrumento_btn.pack(pady=10)

        paciente_btn = Button(clinica_window, text="Paciente", command=self.abrir_paciente)
        paciente_btn.pack(pady=10)

    def abrir_consulta(self):
        consulta_window = Toplevel(self.root)
        consulta_window.title("Gerenciar Consultas")
        ConsultaInterface(consulta_window, self.consulta)

    def abrir_instrumento(self):
        instrumento_window = Toplevel(self.root)
        instrumento_window.title("Gerenciar Instrumentos")
        InstrumentoInterface(instrumento_window, self.instrumento)

    def abrir_paciente(self):
        paciente_window = Toplevel(self.root)
        paciente_window.title("Gerenciar Pacientes")
        PacienteInterface(paciente_window, self.paciente)