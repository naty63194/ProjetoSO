# Importando as bibliotecas necessárias
from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import Calendar, DateEntry
from view import mostrar_info, inserir_info, atualizar_info, deleta_info

# Cores
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
janela.title("Formulário de Consultoria")
janela.geometry('1043x453')
janela.configure(background=co9)
janela.resizable(width=False, height=False)

# Dividindo a janela em frames
frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, bg=co3, relief='flat')
frame_baixo.grid(row=1, column=0, padx=0, pady=1)

frame_direita = Frame(janela, width=518, height=403, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

# Função para mostrar os dados
def mostrar():
    lista = mostrar_info()

    # Lista para o cabeçalho
    tabela_head = ['ID', 'Nome', 'Email', 'Telefone', 'Data']

    # Criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode='extended', columns=tabela_head, show='headings')

    # Scrollbars
    vsb = ttk.Scrollbar(frame_direita, orient='vertical', command=tree.yview)
    hsb = ttk.Scrollbar(frame_direita, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=1)

    hd = ['nw', 'nw', 'nw', 'nw', 'nw']
    h = [30, 170, 140, 100, 120]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    for item in lista:
        tree.insert('', "end", values=item)

    return tree  # Retornar o tree

# Atribuir o retorno da função mostrar() à variável tree
tree = mostrar()

# Função para inserir dados
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

        for widget in frame_direita.winfo_children():
            widget.destroy()

        mostrar()

# Função para atualizar dados
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario["values"]

        valor_id = treev_lista[0]

        e_nome.delete(0, END)
        e_email.delete(0, END)
        e_telefone.delete(0, END)
        e_cal.delete(0, END)

        e_nome.insert(0, treev_lista[1])
        e_email.insert(0, treev_lista[2])
        e_telefone.insert(0, treev_lista[3])
        e_cal.insert(0, treev_lista[4])

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

                for widget in frame_direita.winfo_children():
                    widget.destroy()
                
                
                mostrar()

        b_confirmar = Button(frame_baixo, command=update, text="Confirmar", width=10, anchor=NW, font=('Ivy 7 bold'),
                             bg=co2, fg=co1, relief='raised', overrelief='ridge')
        b_confirmar.place(x=110, y=370)

    except IndexError:
        messagebox.showerror("ERRO", "Selecione um dos dados na tabela")


#funcao deletar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario["values"]

        valor_id = [treev_lista[0]]
        
        deleta_info(valor_id)
        messagebox.showinfo("Sucesso", "Os dados foram deletados")
        
        for widget in frame_direita.winfo_children():
                    widget.destroy()
                    
        mostrar()
        
    except IndexError:
        messagebox.showerror("ERRO", "Selecione um dos dados na tabela")
    
# Configurando o frame baixo
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

# Botão inserir
b_inserir = Button(frame_baixo, command=inserir, text="Enviar", width=9, anchor=NW, font=('Ivy 9 bold'), bg=co6,
                   fg=co1, relief='raised', overrelief='ridge')
b_inserir.place(x=15, y=280)

# Botão atualizar
b_atualizar = Button(frame_baixo, command=atualizar, text="Atualizar", width=9, anchor=NW, font=('Ivy 9 bold'),
                     bg=co2, fg=co1, relief='raised', overrelief='ridge')
b_atualizar.place(x=105, y=280)

# Botão deletar
b_deletar = Button(frame_baixo, command=deletar, text="Deletar", width=9, anchor=NW, font=('Ivy 9 bold'), bg=co7, fg=co1,
                   relief='raised', overrelief='ridge')
b_deletar.place(x=200, y=280)

# Iniciar o loop principal da interface gráfica
janela.mainloop()
