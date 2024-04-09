# importando o tKinter
from cgitb import text
from tkinter import *
from tkinter import font

from tkinter import ttk 
from tkinter import messagebox

#importando TKcalendar
from tkcalendar import Calendar, DateEntry

#importando views
from view import * 

#cores
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue

#criando janela 
janela = Tk()
janela.title("")
janela.geometry('1043x453')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

#dividindo a janela
frame_cima = Frame(janela, width= 310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width= 310, height=403, bg=co3, relief='flat')
frame_baixo.grid(row=1, column=0, padx= 0, pady=1)

frame_direita = Frame(janela, width= 518, height=403, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx= 1, pady=0, sticky=NSEW)


# label cima
app_nome= Label(frame_cima,text="Formulário de Consultoria", anchor= NW, font= ('Ivy 13 bold'),bg=co2, fg= co1, relief='flat')
app_nome.place(x=10, y=20)


#funcao inserir
def inserir():
    nome= e_nome.get()
    email= e_email.get()
    telefone= e_telefone.get()
    dia= e_cal.get()

    lista = [nome, email, telefone, dia]
    
    if nome == " ":
        messagebox.showerror("ERRO", "O nome não pode ser vazio")
    else: 
        inserir_info(lista)
        messagebox.showinfo("Sucesso", "Os dados foram inseridos")
        
        e_nome.delete(0,"end")
        e_email.delete(0,"end")
        e_telefone.edelete(0,"end")
        e_cal.delete(0,"end")
        
    for widget in frame_direita.winfo_children():
        widget.destroy()
        
    mostrar()


    
# configurando frame baixo
#nome
l_nome= Label(frame_baixo,text="Nome", anchor= NW, font= ('Ivy 10 bold'),bg=co3, fg= co0, relief='flat')
l_nome.place(x=10, y=10)
e_nome= Entry(frame_baixo, width=45, justify="left", relief='solid')
e_nome.place(x=15, y=40)

#email
l_email= Label(frame_baixo,text="Email", anchor= NW, font= ('Ivy 10 bold'),bg=co3, fg= co0, relief='flat')
l_email.place(x=10, y=70)
e_email= Entry(frame_baixo, width=45, justify="left", relief='solid')
e_email.place(x=15, y=100)

#telefone
l_telefone= Label(frame_baixo,text="Telefone", anchor= NW, font= ('Ivy 10 bold'),bg=co3, fg= co0, relief='flat')
l_telefone.place(x=10, y=130)
e_telefone= Entry(frame_baixo, width=45, justify="left", relief='solid')
e_telefone.place(x=15, y=160)

#data
l_cal= Label(frame_baixo,text="Data", anchor= NW, font= ('Ivy 10 bold'),bg=co3, fg= co0, relief='flat')
l_cal.place(x=10, y=190)
e_cal= DateEntry(frame_baixo, width=12, background='darkblue', foreground='white', borderwith=2, year=2024)
e_cal.place(x=15, y=220)

#botão inserir
b_inserir= Button(frame_baixo,command=inserir, text="Enviar", width=9, anchor= NW, font= ('Ivy 9 bold'),bg=co6, fg= co1, relief='raised', overrelief='ridge')
b_inserir.place(x=15, y=280)

#botão atualizar 
b_atualizar= Button(frame_baixo,text="Atualizar", width=9, anchor= NW, font= ('Ivy 9 bold'),bg=co2, fg= co1, relief='raised', overrelief='ridge')
b_atualizar.place(x=105, y=280)

#botão deletar 
b_deletar= Button(frame_baixo,text="Deletar", width=9, anchor= NW, font= ('Ivy 9 bold'),bg=co7, fg= co1, relief='raised', overrelief='ridge')
b_deletar.place(x=200, y=280)

#frame direita
def mostrar():
    lista = mostrar_info()

    #lista para o cabecario
    tabela_head =['ID', 'Nome','Email','Telefone', 'Data']

    #criando tabela
    tree = ttk.Treeview(frame_direita, selectmode='extended', columns=tabela_head, show='headings')

    #vertical scrollbar
    vsb= ttk.Scrollbar(frame_direita, orient='vertical', command=tree.yview)

    #horizontal scrollbar
    hsb= ttk.Scrollbar(frame_direita, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0,row=0,sticky='nsew')
    vsb.grid(column=1,row=0,sticky='ns')
    hsb.grid(column=0,row=1,sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)

    hd=['nw','nw','nw', 'nw', 'nw']
    h=[30,170,140,100, 120]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        
        tree.column(col, width=h[n], anchor=hd[n])
        
        n+=1

    for item in lista:
        tree.insert('', "end", values=item)





mostrar()
janela.mainloop()
