# Importando o Tkinter
from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry, Calendar

############### cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5 = "#e06636"  # - profit
co6 = "#038cfc"  # azul
co7 = "#ef5350"  # vermelha
co8 = "#00FF00"  # + verde
co9 = "#e9edf5"  # sky blue

############### criando Janela ###############
janela = Tk()
janela.title("Formulário de Consultoria")
janela.geometry('1043x453')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

################### dividindo a Janela ###################
frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

################ label cima ################
app_nome = Label(frame_cima, text='Formulário de Consultoria', anchor=NW, font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat')
app_nome.place(x=10, y=20)

################ Configurando label baixo ################

## Nome ##
l_nome = Label(frame_baixo, text='Nome', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_nome.place(x=10, y=10)
e_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_nome.place(x=10, y=40)

## Email ##
l_email = Label(frame_baixo, text='Email', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')  
l_email.place(x=10, y=70)
e_email = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_email.place(x=15, y=100)

## Telefone ##
l_telefone = Label(frame_baixo, text='Telefone', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_telefone.place(x=10, y=130)
e_tel = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_tel.place(x=15, y=160)

## Data da consulta ##
l_cal = Label(frame_baixo, text='Data da consulta', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_cal.place(x=10, y=190)
e_cal = DateEntry(frame_baixo, width=12, background='darkblue', foreground='white', borderwidth=2)
e_cal.place(x=15, y=220)

## Estado da consulta ##
l_estado = Label(frame_baixo, text='Estado da Consulta', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_estado.place(x=160, y=190)
e_estado = Entry(frame_baixo, width=20, justify='left', relief='solid')
e_estado.place(x=160, y=220)

## Sobre ##
l_sobre = Label(frame_baixo, text='Sobre a Consulta', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_sobre.place(x=15, y=260)
e_sobre = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_sobre.place(x=15, y=290)

# Botão inserir
b_inserir = Button(frame_baixo, text='Inserir', width=10, font=('Ivy 9 bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge')
b_inserir.place(x=15, y=340)

# Botão atualizar
b_atualizar = Button(frame_baixo, text='Atualizar', width=10, font=('Ivy 9 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
b_atualizar.place(x=110, y=340)

# Botão deletar
b_deletar = Button(frame_baixo, text='Deletar', width=10, font=('Ivy 9 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge')
b_deletar.place(x=200, y=340)


## Criando o local das tabelas ##

lista = [[1, 'Joaquim', 'j@j.com', 119999-9999, '01/01/2022', 'SP', 'Gostaria de o consultar pessoalmente'],
         [2, 'Ana', 'a@a.com', 119999-9999, '01/01/2022', 'GO', 'Gostaria de o consultar pessoalmente'],
         [3, 'Maria', 'm@m.com', 119999-9999, '01/01/2022', 'MG', 'Gostaria de o consultar pessoalmente'],
         [4, 'Paulo', 'p@p.com', 119999-9999, '01/01/2022', 'RJ', 'Gostaria de o consultar pessoalmente'],
         [5, 'Carlos', 'c@c.com', 119999-9999, '01/01/2022', 'SP', 'Gostaria de o consultar pessoalmente']
         ]

# lista para cabeçalho
tabela_head = ['ID', 'Nome', 'Email', 'Telefone', 'Data', 'Estado', 'Sobre']

# criando a tabela
tree = ttk.Treeview(frame_direita, selectmode='extended', columns=tabela_head, show='headings')

# vertical scrollbar
vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

# horizontal scrollbar
hsb = ttk.Scrollbar(frame_direita, orient='horizontal', command=tree.xview)

# configurando a vertical scrollbar
tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
tree.grid(column=0, row=0, sticky='nsew')
vsb.grid(column=1, row=0, sticky='ns')
hsb.grid(column=0, row=1, sticky='ew')


frame_direita.grid_rowconfigure(0, weight=12)

hd = ['nw', 'nw', 'nw', 'nw', 'nw', 'center', 'center']
h = [30, 170, 140, 100, 120, 50, 100]
n = 0

for col in tabela_head:
    tree.heading(col, text=col.title(), anchor=CENTER)
    tree.column(col, width=h[n], anchor=hd[n])
    n += 1
    
for item in lista:
    tree.insert('', 'end', values=item)

# Iniciando o loop principal
janela.mainloop()