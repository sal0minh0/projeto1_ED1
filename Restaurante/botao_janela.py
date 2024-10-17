from tkinter import *
from tkinter import messagebox
from Restaurante.cardapio import Cardapio
from Restaurante.faturamento import Faturamento
from Restaurante.trabalhador import Restaurante

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
        """Override editar_item for Faturamento with debug prints"""
        item_atual = self.entry.get().strip()
        novo_item = self.new_value_entry.get().strip()
        
        print(f": Tentando editar faturamento")
        print(f": Novo item: {novo_item}")
        print(f": Current item: {item_atual}")
        print(f": New item: {novo_item}")
        
        if item_atual and novo_item:
            try:
                # Parse the current item
                data_atual, valor_atual = item_atual.split('-')
                data_atual = data_atual.strip()
                valor_atual = float(valor_atual.strip().replace('R$', '').replace(',', '.'))
                
                # Parse the new item
                nova_data, novo_valor = novo_item.split('-')
                nova_data = nova_data.strip()
                novo_valor = float(novo_valor.strip().replace('R$', '').replace(',', '.'))
                
                # Create dictionaries for current and new items
                item_atual_dict = {'data': data_atual, 'valor': valor_atual}
                novo_item_dict = {'data': nova_data, 'valor': novo_valor}
                
                print(f": Item atual analisado: {item_atual_dict}")
                print(f": Novo item analisado: {novo_item_dict}")
                
                if self.data_manager.atualizar_item(item_atual_dict, novo_item_dict):
                    print("Item atualizado com sucesso")
                    self.entry.delete(0, END)
                    self.new_value_entry.delete(0, END)
                    self.atualizar_output(f"Faturamento atualizado com sucesso!")
                    self.refresh_display()
                else:
                    print("Item não encontrado para atualização")
                    messagebox.showerror("Erro", "Faturamento não encontrado.")
            except ValueError as e:
                print(f"Ocorreu um ValueError: {str(e)}")
                messagebox.showerror("Erro", "Formato inválido. Use: DD/MM/AA - XX.XX")
            except Exception as e:
                self.new_method(e)
                messagebox.showerror("Erro", f"Erro ao editar faturamento: {str(e)}")
        else:
            print("Campos de entrada vazios")
            messagebox.showerror("Erro", "Por favor, insira valores válidos para atualização.")

    def new_method(self, e):
        print(f"Ocorreu um erro inesperado: {str(e)}")

    def get_items_list(self):
        if self.data_manager.verificar_lista_vazia():
            return []
        items = []
        atual = self.data_manager.itens.cabeca
        while atual:
            items.append(atual.valor)
            atual = atual.prox
        return items

    def refresh_display(self):
        self.output_text.config(state=NORMAL)
        self.output_text.delete(1.0, END)
    
        try:
            items = self.get_items_list()
            if items:
                for i, item in enumerate(items, 1):
                    formatted_item = f"Data: {item.get('data', '')}, Valor: R$ {item.get('valor', '')}"
                    self.output_text.insert(END, f"{i}. {formatted_item}\n")
            else:
                self.output_text.insert(END, f"Não há {self.title_plural} cadastrados.")
        
        except Exception as e:
            self.output_text.insert(END, f"Erro ao carregar {self.title_plural}.")
            print(f"Error: {e}")
    
        self.output_text.config(state=DISABLED)
        self.root.update_idletasks()

    def adicionar_item(self):
        """Base method for adding an item. To be overridden by subclasses."""
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
        item_texto = self.entry.get().strip().lower()  # Converte para minúsculas para evitar problemas de maiúsculas/minúsculas
        if item_texto:
            try:
            # Verificar se o nome está presente na lista de funcionários
                if self.data_manager.itens.remover(item_texto):
                    self.entry.delete(0, END)
                    self.atualizar_output(f"'{item_texto}' removido com sucesso!")
                    self.refresh_display()
                else:
                    messagebox.showerror("Erro", f"'{item_texto}' não encontrado.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao remover : {str(e)}")
        else:
            messagebox.showerror("Erro", "Por favor, insira um nome para remover.")


    def buscar_item(self):
        item_texto = self.entry.get().strip()
        if item_texto:
            try:
                result, posicao = self.data_manager.buscar_um_item(item_texto)
                if result:
                    self.atualizar_output(f"Faturamento encontrado na posição {posicao + 1}: Data {result['data']}, Valor R$ {result['valor']:.2f}")
                else:
                    self.atualizar_output(f"'{item_texto}' não encontrado no faturamento.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao buscar faturamento: {str(e)}")
        else:
            messagebox.showerror("Erro", "Por favor, insira um faturamento para buscar.")

    def atualizar_output(self, message):
        self.output_text.config(state=NORMAL)
        self.output_text.insert(END, f"\n{message}\n")
        self.output_text.see(END)
        self.output_text.config(state=DISABLED)

class CardapioInterface(BaseInterface):
    def __init__(self, root, cardapio):
        super().__init__(
            root=root,
            data_manager=cardapio,
            title="Item",
            title_plural="itens",
            example_text="(ex: Nome do Prato - Preço)"
        )

    def adicionar_item(self):
        item = self.entry.get().strip()
        if item:
            try:
                self.data_manager.adicionar_item(item)
                self.entry.delete(0, END)
                self.atualizar_output(f"{self.title} '{item}' adicionado ao cardápio com sucesso!")
                self.refresh_display()
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao adicionar {self.title.lower()}: {str(e)}")
        else:
            messagebox.showerror("Erro", f"Por favor, insira um {self.title.lower()} válido.")

class FaturamentoInterface(BaseInterface):
    def __init__(self, root, faturamento):
        # Create the label before calling super().__init__
        self.total_frame = Frame(root)
        self.total_frame.pack(pady=5)
        
        self.faturamento_total_label = Label(
            self.total_frame, 
            text="Faturamento Total Bruto: R$ 0.00"
        )
        self.faturamento_total_label.pack()
        
        # Now call the parent's init
        super().__init__(
            root=root,
            data_manager=faturamento,
            title="Faturamento",
            title_plural="faturamentos",
            example_text="(ex: XX/XX/XX - XX.X)"
        )

    def refresh_display(self):
        """Override refresh_display to update total"""
        super().refresh_display()
        # Use the existing somar_e_faturamento method
        total = self.data_manager.somar_e_faturamento()
        self.faturamento_total_label.config(
            text=f"Faturamento Total Bruto: R$ {total:.2f}"
        )

    def adicionar_item(self):
        """Override adicionar_item to update total after adding"""
        super().adicionar_item()
        total = self.data_manager.somar_e_faturamento()
        self.faturamento_total_label.config(
            text=f"Faturamento Total Bruto: R$ {total:.2f}"
        )

    def remover_item(self):
        entrada = self.entry.get().strip()
        if entrada:
            try:
                # Split the input into date and value
                partes = entrada.split('-')
                if len(partes) == 2:
                    data = partes[0].strip()
                    valor = float(partes[1].strip())
                    
                    # Create the item dictionary in the same format it was added
                    item = {'data': data, 'valor': valor}
                    
                    # Debugging step: print item to ensure it's correct
                    print(f"Tentando remover item: {item}")
                    
                    if self.data_manager.itens.remover(item):
                        self.entry.delete(0, END)
                        self.atualizar_output(f"Faturamento de {data} removido com sucesso!")
                        self.refresh_display()
                        
                        # Update the total after removal
                        total = self.data_manager.somar_e_faturamento()
                        self.faturamento_total_label.config(
                            text=f"Faturamento Total Bruto: R$ {total:.2f}"
                        )
                    else:
                        messagebox.showerror("Erro", "Faturamento não encontrado.")
                else:
                    messagebox.showerror("Erro", "Formato inválido. Use: DD/MM/AA - XX.X")
            except ValueError:
                messagebox.showerror("Erro", "Valor inválido. Use números para o valor.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao remover faturamento: {str(e)}")
        else:
            messagebox.showerror("Erro", "Por favor, insira um faturamento para remover.")
            
    def editar_item(self):
        item_atual = self.entry.get().strip()
        novo_item = self.new_value_entry.get().strip()
        
        print(f"Tentando editar faturamento")
        print(f"Item atual: {item_atual}")
        print(f"Novo item: {novo_item}")
        
        if item_atual and novo_item:
            try:
                # Parse the current item
                data_atual, valor_atual = item_atual.split('-')
                data_atual = data_atual.strip()
                valor_atual = float(valor_atual.strip().replace('R$', '').replace(',', '.'))
                
                # Parse the new item
                nova_data, novo_valor = novo_item.split('-')
                nova_data = nova_data.strip()
                novo_valor = float(novo_valor.strip().replace('R$', '').replace(',', '.'))
                
                # Create dictionaries for current and new items
                item_atual_dict = {'data': data_atual, 'valor': valor_atual}
                novo_item_dict = {'data': nova_data, 'valor': novo_valor}
                
                print(f"Item atual analisado: {item_atual_dict}")
                print(f"Novo item analisado: {novo_item_dict}")
                
                if self.data_manager.atualizar_item(item_atual_dict, novo_item_dict):
                    print("Item atualizado com sucesso")
                    self.entry.delete(0, END)
                    self.new_value_entry.delete(0, END)
                    self.atualizar_output(f"Faturamento atualizado com sucesso!")
                    self.refresh_display()
                else:
                    print("Item não encontrado para atualização")
                    messagebox.showerror("Erro", "Faturamento não encontrado.")
            except ValueError as e:
                print(f"Ocorreu um ValueError: {str(e)}")
                messagebox.showerror("Erro", "Formato inválido. Use: DD/MM/AA - XX.XX")
            except Exception as e:
                print(f"Ocorreu um erro inesperado: {str(e)}")
                messagebox.showerror("Erro", f"Erro ao editar faturamento: {str(e)}")
        else:
            print("Campos de entrada vazios")
            messagebox.showerror("Erro", "Por favor, insira valores válidos para atualização.")

class RestauranteInterface(BaseInterface):
    def __init__(self, root, restaurante):
        super().__init__(
            root=root,
            data_manager=restaurante,
            title="Funcionário",
            title_plural="funcionários",
            example_text="(ex: Nome - Cargo - Salário)"
        )
        
        # Add the "Cargo" field
        self.label_cargo = Label(self.input_frame, text="Cargo:")
        self.label_cargo.pack(side=LEFT, padx=5)
        self.entry_cargo = Entry(self.input_frame, width=10)
        self.entry_cargo.pack(side=LEFT, padx=5)
        
        # Add the "Salário" field
        self.label_salario = Label(self.input_frame, text="Salário:")
        self.label_salario.pack(side=LEFT, padx=5)
        self.entry_salario = Entry(self.input_frame, width=10)
        self.entry_salario.pack(side=LEFT, padx=5)

    def editar_item(self):
        """Override edit method specifically for funcionários"""
        nome_atual = self.entry.get().strip()
        novo_nome = self.new_value_entry.get().strip()
        novo_cargo = self.entry_cargo.get().strip()
        novo_salario = self.entry_salario.get().strip()
    
        if nome_atual and (novo_nome or novo_cargo or novo_salario):
            try:
                if self.data_manager.atualizar_funcionario(nome_atual, novo_nome, novo_cargo, novo_salario):
                    self.entry.delete(0, END)
                    self.new_value_entry.delete(0, END)
                    self.entry_cargo.delete(0, END)
                    self.entry_salario.delete(0, END)
                    self.atualizar_output(f"Funcionário '{nome_atual}' atualizado com sucesso!")
                    self.refresh_display()
                else:
                    messagebox.showerror("Erro", f"Funcionário '{nome_atual}' não encontrado.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao editar funcionário: {str(e)}")
        else:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para atualização.")
             
class Botao:
    def __init__(self, root):
        self.root = root
        self.restaurante = Restaurante()
        self.faturamento = Faturamento()
        self.cardapio = Cardapio()

    def botao_restaurante(self):
        restaurante_window = Toplevel(self.root)
        restaurante_window.title("O Restaurante")

        restaurante_btn = Button(restaurante_window, text="Funcionários", command=self.abrir_restaurante)
        restaurante_btn.pack(pady=10)

        faturamento_btn = Button(restaurante_window, text="Faturamento", command=self.abrir_faturamento)
        faturamento_btn.pack(pady=10)

        cardapio_btn = Button(restaurante_window, text="Cardápio", command=self.abrir_cardapio)
        cardapio_btn.pack(pady=10)

    def abrir_restaurante(self):
        restaurante_window = Toplevel(self.root)
        restaurante_window.title("Gerenciar Funcionários")
        RestauranteInterface(restaurante_window, self.restaurante)

    def abrir_faturamento(self):
        faturamento_window = Toplevel(self.root)
        faturamento_window.title("Gerenciar Faturamento")
        FaturamentoInterface(faturamento_window, self.faturamento)

    def abrir_cardapio(self):
        cardapio_window = Toplevel(self.root)
        cardapio_window.title("Gerenciar Cardápio")
        CardapioInterface(cardapio_window, self.cardapio)
        