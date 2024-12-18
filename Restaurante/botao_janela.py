from tkinter import *
from tkinter import Entry, Button, END, messagebox
from Restaurante.cardapio import Cardapio
from Restaurante.faturamento import Faturamento
from Restaurante.restaurante import Restaurante


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
        """Sobrescreve editar_item para Faturamento com prints de depuração"""
        item_atual = self.entry.get().strip()
        novo_item = self.new_value_entry.get().strip()
        
        print(f":Tentando editar faturamento")
        print(f":Novo item: {novo_item}")
        print(f":Item atual: {item_atual}")
        print(f":Novo item: {novo_item}")
        
        if item_atual and novo_item:
            try:
                # Analisar o item atual
                data_atual, valor_atual = item_atual.split('-')
                data_atual = data_atual.strip()
                valor_atual = float(valor_atual.strip().replace('R$', '').replace(',', '.'))
                
                # Analisar o novo item
                nova_data, novo_valor = novo_item.split('-')
                nova_data = nova_data.strip()
                novo_valor = float(novo_valor.strip().replace('R$', '').replace(',', '.'))
                
                # Criar dicionários para itens atuais e novos
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
            itens = self.data_manager.exibir_itens()
            self.output_text.insert(END, "Itens do cardápio:\n")
            for item in itens.split('\n'):
                if item:
                    nome, preco = item.split(' - ')
                    self.output_text.insert(END, f"{nome}: R${float(preco):.2f}\n")
        
            mesas_status = self.data_manager.exibir_status_mesas()
            self.output_text.insert(END, "\n\n")
            self.output_text.insert(END, mesas_status)
        except Exception as e:
            self.output_text.insert(END, f"Erro ao carregar informações: {str(e)}")

        self.output_text.config(state=DISABLED)
        self.root.update_idletasks()

    def adicionar_item(self):
        print("Método adicionar_item chamado")  
        item = self.entry.get().strip()
        print(f"Item a ser adicionado: '{item}'")  
        if item:
            try:
                print("Chamando self.data_manager.adicionar_item")  
                result = self.data_manager.adicionar_item(item)
                print(f"Resultado da adição: {result}")  
                self.entry.delete(0, END)
                print("Chamando self.atualizar_output")  
                self.atualizar_output(result)
                print("Chamando self.refresh_display")  
                self.refresh_display()
            except Exception as e:
                print(f"Erro ao adicionar item: {str(e)}")  
                messagebox.showerror("Erro", f"Erro ao adicionar item: {str(e)}")
        else:
            print("Item vazio")  
            messagebox.showerror("Erro", f"Por favor, insira um {self.title.lower()} válido.")

    def remover_item(self):
        item_texto = self.entry.get().strip().lower()  # Converte para minúsculas para evitar problemas de
        print(f"Tentando remover o item: {item_texto}")  

        if item_texto:
            try:
            # Verificar se o nome está presente na lista de itens (dicionário com chave 'nome')
                if self.data_manager.itens.remover(item_texto):
                    print(f"Item '{item_texto}' removido com sucesso!")  
                    self.entry.delete(0, END)
                    self.atualizar_output(f"'{item_texto}' removido com sucesso!")
                    self.refresh_display()
                else:
                    print(f"Item '{item_texto}' não encontrado.")  
                    messagebox.showerror("Erro", f"'{item_texto}' não encontrado.")
            except Exception as e:
                print(f"Erro ao remover item: {str(e)}")  
                messagebox.showerror("Erro", f"Erro ao remover: {str(e)}")
        else:
            messagebox.showerror("Erro", "Por favor, insira um nome para remover.")

    def imprimir_lista(self):
        atual = self.cabeca
        print("Lista de itens:")
        while atual:
            if isinstance(atual.valor, dict):
                print(atual.valor.get('nome', 'Nome não encontrado'))
            atual = atual.prox                       

    def buscar_um_item(self, item):
        # Extrai apenas o nome do item, ignorando o preço
        try:
            nome_item, _ = item.split(' - ')  # Ignora o preço no split
        except ValueError:
            return "Erro: Formato de busca inválido. O formato deve ser 'nome - preço'."

        atual = self.cabeca
        while atual is not None:
            print(f"Verificando nó com valor: {atual.valor}")

            # Compara apenas o nome do item
            if atual.valor['nome'] == nome_item:
                return f"Item encontrado: {atual.valor['nome']} por R${atual.valor['preco']:.2f}"
            
            atual = atual.prox

        return f"'{item}' não encontrado no cardápio."


            
    def atualizar_output(self, message):
        print(f"Atualizando output com: '{message}'")  
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
        self.create_additional_widgets()
        self.create_promocao_widgets()
    def create_promocao_widgets(self):
        # Frame para promoção
        self.promocao_frame = Frame(self.root)
        self.promocao_frame.pack(pady=10)

        # Botão para mostrar promoção do dia
        self.promocao_btn = Button(
            self.promocao_frame, 
            text="Promoção do Dia", 
            command=self.mostrar_promocao_dia,
            bg="#FFFF00", 
            fg="black"
        )
        self.promocao_btn.pack(side=LEFT, padx=5)

        # Botão para registrar pedido
        self.registrar_pedido_btn = Button(
            self.promocao_frame,
            text="Registrar Pedido",
            command=self.registrar_pedido
        )
        self.registrar_pedido_btn.pack(side=LEFT, padx=5)

    def mostrar_promocao_dia(self):
        promocao = self.data_manager.obter_item_menos_pedido()
        if promocao:
            mensagem = (f"⭐ PROMOÇÃO DO DIA ⭐\n"
                        f"Item: {promocao['nome']}\n"
                        f"Preço Original: R${promocao['preco_original']:.2f}\n"
                        f"Preço Promocional: R${promocao['preco_promocional']:.2f}\n"
                        f"Pedidos até agora: {promocao['quantidade_pedidos']}")
            self.atualizar_output(mensagem)
        else:
            self.atualizar_output("Não há itens disponíveis para promoção.")

    def registrar_pedido(self):
        item = self.entry.get().strip()
        if item:
            # Se o item foi inserido com preço, pega só o nome
            nome_item = item.split('-')[0].strip()
            result = self.data_manager.registrar_pedido(nome_item)
            self.atualizar_output(result)
            self.entry.delete(0, END)
        else:
            messagebox.showerror("Erro", "Por favor, insira o nome do item pedido.")
    def create_additional_widgets(self):
        self.mesa_frame = Frame(self.root)
        self.mesa_frame.pack(pady=10)

        self.mesa_label = Label(self.mesa_frame, text="Número da Mesa:")
        self.mesa_label.pack(side=LEFT)

        self.mesa_entry = Entry(self.mesa_frame, width=10)
        self.mesa_entry.pack(side=LEFT, padx=5)

        self.cliente_frame = Frame(self.root)
        self.cliente_frame.pack(pady=10)

        self.cliente_label = Label(self.cliente_frame, text="Nome do Cliente:")
        self.cliente_label.pack(side=LEFT)

        self.cliente_entry = Entry(self.cliente_frame, width=30)
        self.cliente_entry.pack(side=LEFT, padx=5)

        self.mesa_buttons_frame = Frame(self.root)
        self.mesa_buttons_frame.pack(pady=10)

        self.adicionar_mesa_btn = Button(self.mesa_buttons_frame, text="Adicionar Mesa", command=self.adicionar_mesa)
        self.adicionar_mesa_btn.pack(side=LEFT, padx=5)

        self.ocupar_mesa_btn = Button(self.mesa_buttons_frame, text="Ocupar Mesa", command=self.ocupar_mesa)
        self.ocupar_mesa_btn.pack(side=LEFT, padx=5)

        self.liberar_mesa_btn = Button(self.mesa_buttons_frame, text="Liberar Mesa", command=self.liberar_mesa)
        self.liberar_mesa_btn.pack(side=LEFT, padx=5)

        self.status_mesas_btn = Button(self.mesa_buttons_frame, text="Status das Mesas", command=self.exibir_status_mesas)
        self.status_mesas_btn.pack(side=LEFT, padx=5)
        

    def create_button(self, text, command):
        button = Button(self.mesa_buttons_frame, text=text, command=command)
        button.pack(side=LEFT, padx=5)

    def clear_example_text(self, event, entry):
        if entry.get() == "Ex: 1":
            entry.delete(0, END)

    def restore_example_text(self, event, entry):
        if not entry.get():
            entry.insert(0, "Ex: 1")
            
    def adicionar_mesa(self):
        numero_mesa = self.mesa_entry.get().strip()
        if numero_mesa:
            result = self.data_manager.adicionar_mesa(numero_mesa)
            self.atualizar_output(result)
            self.mesa_entry.delete(0, END)
        else:
            messagebox.showerror("Erro", "Por favor, insira um número de mesa.")

    def ocupar_mesa(self):
        numero_mesa = self.mesa_entry.get().strip()
        cliente = self.cliente_entry.get().strip()
        if numero_mesa and cliente:
            result = self.data_manager.ocupar_mesa(numero_mesa, cliente)
            self.atualizar_output(result)
            self.mesa_entry.delete(0, END)
            self.cliente_entry.delete(0, END)
        else:
            messagebox.showerror("Erro", "Por favor, insira o número da mesa e o nome do cliente.")

    def liberar_mesa(self):
        numero_mesa = self.mesa_entry.get().strip()
        if numero_mesa:
            result = self.data_manager.liberar_mesa(numero_mesa)
            self.atualizar_output(result)
            self.mesa_entry.delete(0, END)
        else:
            messagebox.showerror("Erro", "Por favor, insira o número da mesa.")

    def exibir_status_mesas(self):
        status = self.data_manager.exibir_status_mesas()
        self.atualizar_output(status)

    def refresh_display(self):
        self.output_text.config(state=NORMAL)
        self.output_text.delete(1.0, END)

        try:
            itens = self.data_manager.exibir_itens()
            self.output_text.insert(END, "Itens do cardápio:\n")
            self.output_text.insert(END, itens)
            
            mesas_status = self.data_manager.exibir_status_mesas()
            self.output_text.insert(END, "\n\n")
            self.output_text.insert(END, mesas_status)
        except Exception as e:
            self.output_text.insert(END, f"Erro ao carregar informações: {str(e)}")

        self.output_text.config(state=DISABLED)
        self.root.update_idletasks()

    def adicionar_item(self):
        item = self.entry.get().strip()
        if item:
            result = self.data_manager.adicionar_item(item)
            self.entry.delete(0, END)
            self.atualizar_output(result)
            self.refresh_display()
        else:
            messagebox.showerror("Erro", f"Por favor, insira um {self.title.lower()} válido.")

    def remover_item(self):
        item_nome = self.entry.get().strip().split(' - ')[0]  # Remove apenas pelo nome
        if item_nome:
            print(f"Tentando remover item: '{item_nome}'")  
            result = self.data_manager.remover_item(item_nome)
            if "removido" in result:
                self.entry.delete(0, END)
                self.atualizar_output(result)
                self.refresh_display()  # Atualiza a exibição após remover o item
            else:
                self.atualizar_output(result)
        else:
            messagebox.showerror("Erro", "Por favor, insira o nome do item para remover.")

    def buscar_item(self):
        item = self.entry.get().strip()
        if item:
            result = self.data_manager.buscar_um_item(item)
            self.atualizar_output(result)
        else:
            messagebox.showerror("Erro", f"Por favor, insira um {self.title.lower()} para buscar.")

    def editar_item(self):
        item_atual = self.entry.get().strip()
        novo_item = self.new_value_entry.get().strip()

        if item_atual and novo_item:
            # Verifique se o item atual existe antes de tentar atualizar
            item_existe = self.data_manager.buscar_um_item(item_atual)
            if item_existe:  # Se o item foi encontrado
                result = self.data_manager.atualizar_item(item_atual, novo_item)
                self.entry.delete(0, END)
                self.new_value_entry.delete(0, END)
                self.atualizar_output(result)
                self.refresh_display()  # Atualiza a exibição após a edição
            else:
                messagebox.showerror("Erro", f"O item '{item_atual}' não existe no cardápio.")
        else:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para atualização.")

            
    def atualizar_output(self, message):
        self.output_text.config(state=NORMAL)
        self.output_text.insert(END, f"\n{message}\n")
        self.output_text.see(END)
        self.output_text.config(state=DISABLED)

class FaturamentoInterface(BaseInterface):
    def __init__(self, root, faturamento, restaurante_interface=None):
        self.restaurante_interface = restaurante_interface
        self.total_frame = Frame(root)
        self.total_frame.pack(pady=5)
        
        self.faturamento_total_label = Label(
            self.total_frame, 
            text="Faturamento Total Bruto: R$ 0.00"
        )
        self.faturamento_total_label.pack()
        
        super().__init__(
            root=root,
            data_manager=faturamento,
            title="Faturamento",
            title_plural="faturamentos",
            example_text="(ex: DD/MM/AA - XX.XX)"
        )

    def refresh_display(self):
        self.output_text.config(state=NORMAL)
        self.output_text.delete(1.0, END)

        try:
            itens = self.data_manager.exibir_itens()
            self.output_text.insert(END, itens)
            
            total = self.data_manager.somar_e_faturamento()
            self.faturamento_total_label.config(
                text=f"Faturamento Total Bruto: R$ {total:.2f}"
            )
        except Exception as e:
            self.output_text.insert(END, f"Erro ao carregar informações: {str(e)}")

        self.output_text.config(state=DISABLED)
        self.root.update_idletasks()

    def adicionar_item(self):
        item = self.entry.get().strip()
        if item:
            try:
                result = self.data_manager.adicionar_item(item)
                self.entry.delete(0, END)
                self.atualizar_output(f"Faturamento adicionado: {item}")
                self.refresh_display()
                
                # Atualiza a interface do restaurante se ela existir
                if self.restaurante_interface:
                    self.restaurante_interface.refresh_display()
                    
            except ValueError as e:
                messagebox.showerror("Erro", str(e))
        else:
            messagebox.showerror("Erro", "Por favor, insira um faturamento válido.")

    def remover_item(self):
        data = self.entry.get().strip()
        if data:
            result = self.data_manager.remover_item(data)
            if "removido" in result:
                self.entry.delete(0, END)
                self.atualizar_output(result)
                self.refresh_display()
            else:
                self.atualizar_output(result)
        else:
            messagebox.showerror("Erro", "Por favor, insira a data do faturamento para remover.")
            
    def buscar_item(self):
        item = self.entry.get().strip()
        if item:
            try:
                result, posicao = self.data_manager.buscar_um_item(item)
                if result:
                    self.atualizar_output(f"Faturamento encontrado na posição {posicao + 1}:\n"
                                          f"Data: {result['data']}, Valor: R$ {result['valor']:.2f}")
                else:
                    self.atualizar_output(f"Faturamento não encontrado: {item}")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao buscar faturamento: {str(e)}")
        else:
            messagebox.showerror("Erro", "Por favor, insira um faturamento para buscar.")

    def editar_item(self):
        item_atual = self.entry.get().strip()
        novo_item = self.new_value_entry.get().strip()
        
        if item_atual and novo_item:
            try:
                item_atual_dict, _ = self.data_manager.buscar_um_item(item_atual)
                if item_atual_dict:
                    nova_data, novo_valor = novo_item.split('-')
                    novo_item_dict = {
                        'data': nova_data.strip(),
                        'valor': float(novo_valor.strip())
                    }
                    if self.data_manager.atualizar_item(item_atual_dict, novo_item_dict):
                        self.entry.delete(0, END)
                        self.new_value_entry.delete(0, END)
                        self.atualizar_output(f"Faturamento atualizado com sucesso!")
                        self.refresh_display()
                    else:
                        messagebox.showerror("Erro", "Falha ao atualizar o faturamento.")
                else:
                    messagebox.showerror("Erro", "Faturamento não encontrado.")
            except ValueError:
                messagebox.showerror("Erro", "Formato inválido. Use: DD/MM/AA - XX.XX")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao editar faturamento: {str(e)}")
        else:
            messagebox.showerror("Erro", "Por favor, insira valores válidos para atualização.")

class RestauranteInterface(BaseInterface):
    def __init__(self, root, data_manager):
        # Criar quadro de entrada de faturamento
        self.revenue_frame = Frame(root)
        self.revenue_frame.pack(pady=5)
        
        self.revenue_label = Label(
            self.revenue_frame,
            text="Faturamento (Data - Valor): "
        )
        self.revenue_label.pack(side=LEFT)
        
        self.revenue_entry = Entry(self.revenue_frame, width=20)
        self.revenue_entry.pack(side=LEFT, padx=5)
        
        self.add_revenue_button = Button(
            self.revenue_frame,
            text="Adicionar Faturamento",
            command=self.adicionar_faturamento
        )
        self.add_revenue_button.pack(side=LEFT, padx=5)

        # Criar quadro de entrada de taxa
        self.tax_frame = Frame(root)
        self.tax_frame.pack(pady=5)
        
        self.tax_label = Label(
            self.tax_frame,
            text="Taxa (%): "
        )
        self.tax_label.pack(side=LEFT)
        
        self.tax_entry = Entry(self.tax_frame, width=10)
        self.tax_entry.pack(side=LEFT, padx=5)
        self.tax_entry.insert(0, "0") 
        
        self.apply_tax_button = Button(
            self.tax_frame,
            text="Aplicar Taxa",
            command=self.apply_tax
        )
        self.apply_tax_button.pack(side=LEFT, padx=5)

        # Criar quadro para exibir informações financeiras totais
        self.total_frame = Frame(root)
        self.total_frame.pack(pady=5)

        self.total_salary_label = Label(
            self.total_frame,
            text="Total em Salários: R$ 0.00"
        )
        self.total_salary_label.pack()

        # Adicionar rótulo de faturamento
        self.faturamento_label = Label(
            self.total_frame,
            text="Faturamento Total: R$ 0.00"
        )
        self.faturamento_label.pack()

        self.profit_before_tax_label = Label(
            self.total_frame,
            text="Lucro (Antes dos Impostos): R$ 0.00"
        )
        self.profit_before_tax_label.pack()

        self.tax_amount_label = Label(
            self.total_frame,
            text="Impostos: R$ 0.00"
        )
        self.tax_amount_label.pack()

        self.profit_after_tax_label = Label(
            self.total_frame,
            text="Lucro (Após Impostos): R$ 0.00"
        )
        self.profit_after_tax_label.pack()

        # Chamar inicialização da classe pai
        super().__init__(
            root=root,
            data_manager=data_manager,
            title="Funcionário",
            title_plural="funcionários",
            example_text="(ex: Nome, Cargo na Empresa, Salário)"
        )
        self.data_manager.faturamento.adicionar_observador(self.refresh_display)
        
    def adicionar_faturamento(self):
        """Adicionar nova entrada de faturamento"""
        entrada = self.revenue_entry.get().strip()
        if entrada:
            try:
                self.data_manager.faturamento.adicionar_item(entrada)
                self.revenue_entry.delete(0, END)
                self.atualizar_output(f"Faturamento adicionado com sucesso!")
                self.refresh_display()
            except ValueError as e:
                messagebox.showerror("Erro", str(e))
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao adicionar faturamento: {str(e)}")
        else:
            messagebox.showerror("Erro", "Por favor, insira os dados do faturamento no formato 'data - valor'")

    def refresh_display(self):
        """Substituir refresh_display para mostrar funcionários e atualizar informações financeiras"""
        faturamento_items = self.data_manager.faturamento.exibir_itens()
        
        self.output_text.config(state=NORMAL)
        self.output_text.delete(1.0, END)
        
        # 1. Exibir lista de funcionários
        items = self.get_items_list()
        total_salary = 0

        if items:
            for i, item in enumerate(items, 1):
                try:
                    nome = item.get('nome', '')
                    cargo = item.get('cargo', '')
                    salario = float(item.get('salario', 0))
                    total_salary += salario

                    formatted_item = f"Nome: {nome}, Cargo: {cargo}, Salário: R$ {salario:.2f}"
                    self.output_text.insert(END, f"{i}. {formatted_item}\n")
                except (ValueError, TypeError) as e:
                    print(f"Erro ao processar funcionário {i}: {e}")
                    continue
        else:
            self.output_text.insert(END, f"Não há {self.title_plural} cadastrados.")

        # 2. Atualizar rótulo de total de salários
        self.total_salary_label.config(
            text=f"Total em Salários: R$ {total_salary:.2f}"
        )
        
        # 3. Obter e exibir faturamento
        try:
            faturamento_total = self.data_manager.set_faturamento_total_bruto()
            if faturamento_total is None:
                print("Faturamento não está definido ou está retornando None.")
                faturamento_total = 0
            else:
                self.faturamento_label.config(
                    text=f"Faturamento Total: R$ {faturamento_total:.2f}"
                )
                 
            atual = self.data_manager.faturamento.itens.cabeca
            while atual:
                print(f"- {atual.valor}")
                atual = atual.prox
        except Exception as e:
            print(f"Erro ao calcular faturamento: {e}")
            faturamento_total = 0
        
        # 4. Calcular e exibir lucros e impostos
        try:
            # Calcula lucro antes dos impostos
            lucro_before_tax = faturamento_total - total_salary
            
            # Processa taxa de imposto
            tax_rate = float(self.tax_entry.get()) / 100
            tax_amount = lucro_before_tax * tax_rate
            lucro_after_tax = lucro_before_tax - tax_amount
        except ValueError:
            # Se houver erro na conversão da taxa de imposto
            tax_rate = 0
            tax_amount = 0
            lucro_after_tax = lucro_before_tax
        
        # 5. Atualizar rótulos financeiros
        self.profit_before_tax_label.config(
            text=f"Lucro (Antes dos Impostos): R$ {lucro_before_tax:.2f}"
        )
        self.tax_amount_label.config(
            text=f"Impostos ({tax_rate*100:.1f}%): R$ {tax_amount:.2f}"
        )
        self.profit_after_tax_label.config(
            text=f"Lucro (Após Impostos): R$ {lucro_after_tax:.2f}"
        )

        self.output_text.config(state=DISABLED)
        self.root.update_idletasks()
    
    def apply_tax(self):
        """Calcular e aplicar imposto ao lucro"""
        try:
            tax_rate = float(self.tax_entry.get()) / 100  # Converte porcentagem para decimal
            if tax_rate < 0 or tax_rate > 1:
                messagebox.showerror("Erro", "Taxa deve estar entre 0 e 100%")
                return
            self.refresh_display()
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira uma taxa válida")

    def adicionar_item(self):
        """Adicionar novo funcionário"""
        entrada = self.entry.get().strip()
        if entrada:
            try:
                # Divide a entrada em nome, cargo e salário
                nome, cargo, salario = entrada.split(',')
                salario = float(salario.strip())
                
                funcionario = {
                    'nome': nome.strip(),
                    'cargo': cargo.strip(),
                    'salario': salario
                }
                
                self.data_manager.adicionar_item(funcionario)
                self.entry.delete(0, END)
                self.atualizar_output(f"Funcionário '{nome.strip()}' adicionado com sucesso!")
                self.refresh_display()
            except ValueError:
                messagebox.showerror("Erro", "Formato inválido. Use: Nome,Cargo,Salário")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao adicionar funcionário: {str(e)}")
        else:
            messagebox.showerror("Erro", "Por favor, insira os dados do funcionário.")

    def remover_item(self):
        """Remover funcionário"""
        entrada = self.entry.get().strip()
        if entrada:
            try:
                nome = entrada.split(',')[0].strip()
                if self.data_manager.itens.remover(nome, chave_comparacao='nome'):
                    self.entry.delete(0, END)
                    self.atualizar_output(f"Funcionário '{nome}' removido com sucesso!")
                    self.refresh_display()
                else:
                    messagebox.showerror("Erro", "Funcionário não encontrado.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao remover funcionário: {str(e)}")
        else:
            messagebox.showerror("Erro", "Por favor, insira o nome do funcionário para remover.")

    def buscar_item(self):
        """Buscar funcionário pelo nome"""
        entrada = self.entry.get().strip()
        if entrada:
            try:
                nome = entrada.split(',')[0].strip()
                result = self.data_manager.buscar_um_item(nome)  # Passa apenas o nome
                if result:
                    self.atualizar_output(
                        f"Funcionário encontrado:\n"
                        f"Nome: {result['nome']}\n"
                        f"Cargo: {result['cargo']}\n"
                        f"Salário: R$ {float(result['salario']):.2f}"
                    )
                else:
                    self.atualizar_output(f"Funcionário '{nome}' não encontrado.")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao buscar funcionário: {str(e)}")
        else:
            messagebox.showerror("Erro", "Por favor, insira o nome do funcionário para buscar.")

    def editar_item(self):
        """Editar informações de um funcionário existente"""
        item_atual = self.entry.get().strip()
        novo_item = self.new_value_entry.get().strip()
        
        if item_atual and novo_item:
            try:
                # Extrai o nome atual
                nome_atual = item_atual.split(',')[0].strip()
                
                # Extrai os novos valores
                novo_nome, novo_cargo, novo_salario = novo_item.split(',')
                novo_salario = float(novo_salario.strip())
                
                # Atualiza o funcionário
                if self.data_manager.atualizar_item(nome_atual, novo_nome.strip(), novo_cargo.strip(), novo_salario):
                    self.entry.delete(0, END)
                    self.new_value_entry.delete(0, END)
                    self.atualizar_output(f"Funcionário atualizado com sucesso!")
                    self.refresh_display()
                else:
                    messagebox.showerror("Erro", "Funcionário não encontrado.")
            except ValueError:
                messagebox.showerror("Erro", "Formato inválido. Use: Nome,Cargo,Salário")
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
        self.restaurante_interface = None

    def abrir_restaurante(self):
        """Abrir interface de gerenciamento de funcionários"""
        restaurante_window = Toplevel(self.root)
        restaurante_window.title("Gerenciar Funcionários")
        self.restaurante_interface = RestauranteInterface(restaurante_window, self.restaurante)

    def abrir_faturamento(self):
        """Abrir interface de gerenciamento de faturamento"""
        faturamento_window = Toplevel(self.root)
        faturamento_window.title("Gerenciar Faturamento")
        FaturamentoInterface(faturamento_window, self.faturamento, self.restaurante_interface)

    def abrir_cardapio(self):
        """Abrir interface de gerenciamento de cardápio"""
        cardapio_window = Toplevel(self.root)
        cardapio_window.title("Gerenciar Cardápio")
        CardapioInterface(cardapio_window, self.cardapio)
