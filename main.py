#IMPORTANDO O TKINTER
from email import message
from tarfile import PAX_FIELDS
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
from requests import delete



# IMPORTANDO tkcalendar
from tkcalendar import Calendar, DateEntry


# Importando views
from view import *



################# cores ###############
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


# CRIANDO JANELA
janela = Tk()
janela.title("")
janela.geometry('1043x453')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)



# DIVIDINDO A JANELA
frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita= Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)



# LABEL CIMA
app_nome = Label(frame_cima, text='Formulário de Consultoria', anchor=NW, font=('Ivy 13 bold'), fg=co1, bg=co2, relief='flat')
app_nome.place(x=10, y=20)


# FUNÇÃO INSERIR
def inserir():
    nome = e_nome.get()
    email = e_email.get()
    telefone = e_telefone.get()
    cal = e_cal.get()
    estado = e_estado.get()
    assunto = e_assunto.get()

    lista = [nome, email, telefone, cal, estado, assunto]

    if nome=='':
        messagebox.showerror("Error", 'O nome não pode ser vazio') 
    else:
        inserir_info(lista)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

        
        e_nome.delete(0,'end')
        e_email.delete(0,'end')
        e_telefone.delete(0,'end')
        e_cal.delete(0,'end')
        e_estado.delete(0,'end')
        e_assunto.delete(0,'end')

    for widget in frame_direita.winfo_children():
        widget.destroy()

        mostrar()


# VARIÁVEL TREE GLOBAL
global tree

# FUNÇÃO ATUALIZAR
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor = tree_lista[0]

        e_nome.delete(0,'end')
        e_email.delete(0,'end')
        e_telefone.delete(0,'end')
        e_cal.delete(0,'end')
        e_estado.delete(0,'end')
        e_assunto.delete(0,'end')


        e_nome.insert(0,tree_lista[1])
        e_email.insert(0,tree_lista[2])
        e_telefone.insert(0,tree_lista[3])
        e_cal.insert(0,tree_lista[4])
        e_estado.insert(0,tree_lista[5])
        e_assunto.insert(0,tree_lista[6])


        def update():
            nome = e_nome.get()
            email = e_email.get()
            telefone = e_telefone.get()
            cal = e_cal.get()
            estado = e_estado.get()
            assunto = e_assunto.get()

            lista = [nome, email, telefone, cal, estado, assunto]

            if nome==' ':
                messagebox.showerror("Error", "O nome não pode ser vazio") 
            else:
                atualizar_info(lista)
                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

                
                e_nome.delete(0,'end')
                e_email.delete(0,'end')
                e_telefone.delete(0,'end')
                e_cal.delete(0,'end')
                e_estado.delete(0,'end')
                e_assunto.delete(0,'end')

            for widget in frame_direita.winfo_children():
                widget.destroy()


        # BOTÃO CONFIRMAR
        b_confirmar = Button(frame_baixo, command=update, text='Confirmar', width=10, font=('Ivy 7 bold'), fg=co1, bg=co2, relief='raised', overrelief='ridge')
        b_confirmar.place(x=110, y=370)


        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'selecione um dos dados na tabela') 



# NOME
l_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
l_nome.place(x=10, y=10)
e_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_nome.place(x=15, y=40)


# EMAIL
l_email = Label(frame_baixo, text='Email *', anchor=NW, font=('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
l_email.place(x=10, y=80)
e_email = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_email.place(x=15, y=100)


# TELEFONE
l_telefone = Label(frame_baixo, text='Telefone *', anchor=NW, font=('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
l_telefone.place(x=10, y=130)
e_telefone = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_telefone.place(x=15, y=160)


# DATA DA CONSULTA
l_cal = Label(frame_baixo, text='Data da consulta *', anchor=NW, font=('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
l_cal.place(x=10, y=190)
e_cal = DateEntry(frame_baixo, width=12, background='darkblue', foreground='white', borderwidth=2, year=2022)
e_cal.place(x=15, y=220)


# ESTADO
l_estado = Label(frame_baixo, text='Estado da consulta *', anchor=NW, font=('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
l_estado.place(x=160, y=190)
e_estado = Entry(frame_baixo, width=20, justify='left', relief='solid')
e_estado.place(x=160, y=220)


# SOBRE
l_assunto = Label(frame_baixo, text='Informações extra *', anchor=NW, font=('Ivy 10 bold'), fg=co4, bg=co1, relief='flat')
l_assunto.place(x=15, y=260)
e_assunto = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_assunto.place(x=15, y=290)


# BOTÃO INSERIR
b_inserir = Button(frame_baixo,command=inserir, text='Inserir ', width=10, font=('Ivy 9 bold'), fg=co1, bg=co6, relief='raised', overrelief='ridge')
b_inserir.place(x=15, y=340)



# BOTÃO ATUALIZAR
b_atualizar = Button(frame_baixo, command=atualizar, text='Atualizar ', width=10, font=('Ivy 9 bold'), fg=co1, bg=co2, relief='raised', overrelief='ridge')
b_atualizar.place(x=110, y=340)



# BOTÃO DELETAR
b_deletar = Button(frame_baixo, text='Deletar ', width=10, font=('Ivy 9 bold'), fg=co1, bg=co7, relief='raised', overrelief='ridge')
b_deletar.place(x=205, y=340)


# FRAME DIREITA


def mostrar():

    global tree

    lista = mostrar_info()

    # lista para cabecario 
    tabela_head = ['ID','Nome',  'email','telefone', 'Data', 'Estado','Sobre']


    # criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar( frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)


    hd=["nw","nw","nw","nw","nw","center","center"]
    h=[30,170,140,100,120,50,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)



# Chamando a função mostrar
mostrar()

janela.mainloop()
















