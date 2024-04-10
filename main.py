# Importação do módulo datetime
from datetime import datetime

# Importação das bibliotecas necessárias
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from tkcalendar import Calendar, DateEntry
from view import mostrar_info, inserir_info, atualizar_info, deleta_info

# Definição das cores utilizadas na interface
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # Branca
co2 = "#4fa882"  # Verde
co3 = "#38576b"  # Valor
co4 = "#403d3d"  # Letra
co5 = "#e06636"  # - Profit
co6 = "#038cfc"  # Azul
co7 = "#ef5350"  # Vermelha
co8 = "#263238"  # + Verde
co9 = "#e9edf5"  # Sky blue

# Criando a janela principal
janela = Tk()
janela.title("Formulário de Consulta")
janela.geometry('890x453')
janela.configure(background=co9)
janela.resizable(width=False, height=False)

# Divisão da janela em frames
frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, bg=co3, relief='flat')
frame_baixo.grid(row=1, column=0, padx=0, pady=1)

frame_direita = Frame(janela, width=518, height=403, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

# Criação da tabela utilizando o widget Treeview
tabela_head = ['ID', 'Nome', 'Email', 'Telefone', 'Data']
tree = ttk.Treeview(frame_direita, selectmode='extended', columns=tabela_head, show='headings')

# Adição de scrollbars à tabela
vsb = ttk.Scrollbar(frame_direita, orient='vertical', command=tree.yview)
hsb = ttk.Scrollbar(frame_direita, orient='horizontal', command=tree.xview)

tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

tree.grid(column=0, row=0, sticky='nsew')
vsb.grid(column=1, row=0, sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')

frame_direita.grid_rowconfigure(0, weight=1)

# Definição das larguras das colunas da tabela
hd = ['nw', 'nw', 'nw', 'nw', 'nw']
h = [30, 170, 140, 100, 120]
n = 0

for col in tabela_head:
    tree.heading(col, text=col.title(), anchor=CENTER)
    tree.column(col, width=h[n], anchor=hd[n])
    n += 1

# Função para mostrar os dados na tabela
def mostrar():
    # Limpa os itens existentes na árvore
    for item in tree.get_children():
        tree.delete(item)

    lista = mostrar_info()
    
    for item in lista:
        tree.insert('', "end", values=item)

# Atribuição do retorno da função mostrar() à variável tree
mostrar()

# Função para inserir dados na tabela
def inserir():
    nome = e_nome.get()
    email = e_email.get()
    telefone = e_telefone.get()
    dia = e_cal.get()

    lista = [nome, email, telefone, dia]

    if not nome.strip():
        messagebox.showerror("ERRO", "O nome não pode ser vazio")
    else:
        inserir_info(lista)
        messagebox.showinfo("Sucesso", "Os dados foram inseridos")

        e_nome.delete(0, END)
        e_email.delete(0, END)
        e_telefone.delete(0, END)
        e_cal.delete(0, END)

        mostrar()

# Função para atualizar dados na tabela
def atualizar():
    try:
        # Obter o item selecionado na tabela
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario["values"]

        valor_id = treev_lista[0]

        # Limpar os campos de entrada e preenchê-los com os dados selecionados
        e_nome.delete(0, END)
        e_email.delete(0, END)
        e_telefone.delete(0, END)
        e_cal.delete(0, END)

        e_nome.insert(0, treev_lista[1])
        e_email.insert(0, treev_lista[2])
        e_telefone.insert(0, treev_lista[3])
        e_cal.insert(0, treev_lista[4])

        # Função para atualizar os dados após a confirmação
        def update():
            nome = e_nome.get()
            email = e_email.get()
            telefone = e_telefone.get()
            dia = e_cal.get()

            lista = [nome, email, telefone, dia, valor_id]

            if not nome.strip():
                messagebox.showerror("ERRO", "O nome não pode ser vazio")
            else:
                atualizar_info(lista)
                messagebox.showinfo("Sucesso", "Os dados foram atualizados")

                e_nome.delete(0, END)
                e_email.delete(0, END)
                e_telefone.delete(0, END)
                e_cal.delete(0, END)

                mostrar()

        # Botão de confirmação da atualização
        b_confirmar = Button(frame_baixo, command=update, text="Confirmar", width=10, anchor=NW, font=('Ivy 8 bold'),
                             bg=co2, fg=co1, relief='raised', overrelief='ridge')
        b_confirmar.place(x=105, y=320)

    except IndexError:
        messagebox.showerror("ERRO", "Selecione um dos dados na tabela")


# Função para deletar dados da tabela
def deletar():
    try:
        # Obter o item selecionado na tabela
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario["values"]

        valor_id = [treev_lista[0]]
        
        deleta_info(valor_id)
        messagebox.showinfo("Sucesso", "Os dados foram deletados")
        
        mostrar()
        
    except IndexError:
        messagebox.showerror("ERRO", "Selecione um dos dados na tabela")
    
# Configuração dos widgets de entrada na parte inferior do frame
# Nome
l_nome = Label(frame_baixo, text="Nome", anchor=NW, font=('Ivy 10 bold'), bg=co3, fg=co0, relief='flat')
l_nome.place(x=10, y=10)
e_nome = Entry(frame_baixo, width=45, justify="left", relief='solid')
e_nome.place(x=15, y=40)

# Email
l_email = Label(frame_baixo, text="Email", anchor=NW, font=('Ivy 10 bold'), bg=co3, fg=co0, relief='flat')
l_email.place(x=10, y=70)
e_email = Entry(frame_baixo, width=45, justify="left", relief='solid')
e_email.place(x=15, y=100)

# Telefone
l_telefone = Label(frame_baixo, text="Telefone", anchor=NW, font=('Ivy 10 bold'), bg=co3, fg=co0, relief='flat')
l_telefone.place(x=10, y=130)
e_telefone = Entry(frame_baixo, width=45, justify="left", relief='solid')
e_telefone.place(x=15, y=160)

# Data
l_cal = Label(frame_baixo, text="Data", anchor=NW, font=('Ivy 10 bold'), bg=co3, fg=co0, relief='flat')
l_cal.place(x=10, y=190)
e_cal = DateEntry(frame_baixo, width=12, background='darkblue', foreground='white', borderwidth=2, year=2024)
e_cal.place(x=15, y=220)

# Botões para inserir, atualizar, deletar e gerar extrato
b_inserir = Button(frame_baixo, command=inserir, text="Enviar", width=9, anchor=NW, font=('Ivy 9 bold'), bg=co6,
                   fg=co1, relief='raised', overrelief='ridge')
b_inserir.place(x=15, y=280)

b_atualizar = Button(frame_baixo, command=atualizar, text="Atualizar", width=9, anchor=NW, font=('Ivy 9 bold'),
                     bg=co2, fg=co1, relief='raised', overrelief='ridge')
b_atualizar.place(x=105, y=280)

b_deletar = Button(frame_baixo, command=deletar, text="Deletar", width=9, anchor=NW, font=('Ivy 9 bold'), bg=co7, fg=co1,
                   relief='raised', overrelief='ridge')
b_deletar.place(x=200, y=280)

def gerar_extrato():
    # Obter os dados da tabela
    dados = mostrar_info()

    # Abrir o diálogo para selecionar o local de salvamento do arquivo
    arquivo_salvo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivo de Texto", "*.txt")])

    # Verificar se o usuário selecionou um local para salvar o arquivo
    if arquivo_salvo:
        # Abrir o arquivo em modo de escrita
        with open(arquivo_salvo, "w") as arquivo:
            # Escrever o título "EXTRATO" em negrito
            arquivo.write("**EXTRATO**\n\n")

            # Escrever os dados da tabela em forma de tabela
            colunas = ['ID', 'Nome', 'Email', 'Telefone', 'Data']
            arquivo.write("{:<5} {:<25} {:<30} {:<15} {:<12}\n".format(*colunas))
            arquivo.write("=" * 87 + "\n")
            for linha in dados:
                arquivo.write("{:<5} {:<25} {:<30} {:<15} {:<12}\n".format(*linha))
            arquivo.write("\n")

            # Adicionar a data de geração do arquivo
            data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            arquivo.write("Data de geração do arquivo: {}\n".format(data_atual))

        # Exibir uma mensagem de sucesso
        messagebox.showinfo("Sucesso", "O arquivo foi gerado com sucesso.")

# Botão para gerar o extrato
b_gerar_extrato = Button(frame_baixo, command=gerar_extrato, text="Gerar Extrato", width=11, anchor=NW,
                         font=('Ivy 9 bold'), bg=co8, fg=co1, relief='raised', overrelief='ridge')
b_gerar_extrato.place(x=105, y=350)

# Iniciar o loop principal da interface gráfica
janela.mainloop()
