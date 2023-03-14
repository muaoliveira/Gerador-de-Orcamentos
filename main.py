from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from fpdf import FPDF
from datetime import datetime

#criação da janela
corBg = "#cecece"
corFont = "#000"

 = "#D3D3D3"
fontFamily = "Verdana 12"

def on_enter(e):
   buttonGerar['background'] = corBgHover

def on_leave(e):
   buttonGerar['background'] = 'SystemButtonFace'

#funcoes
def fGerarOrcamento():
   projeto = str(nomeProjetoEntrada.get())
   valor_hora = str(valorHoraEntrada.get())
   horas_estimadas = str(horasEstimadasEntrada.get())
   prazo_estimado = str(prazoEstimadoEntrada.get())

   valor_total = int(valor_hora) * int(horas_estimadas)
   data = datetime.today()
   data = "{}-{}-{}".format(data.day, data.month, data.year)

   orcamento = FPDF()
   orcamento.add_page()
   orcamento.set_font("Arial")
   orcamento.image("template.png", x=0, y=0)
   orcamento.text(115, 145, projeto)
   orcamento.text(115, 160, horas_estimadas)
   orcamento.text(115, 175, valor_hora)
   orcamento.text(115, 190, prazo_estimado)
   orcamento.text(115, 205, str(valor_total))
   orcamento.output(f"orcamento_{data}.pdf")
   messagebox.showinfo("Sucesso!", message="Orçamento gerado com sucesso!")
   exit()

janela = Tk()
janela.title("Gerar Orçamento")
janela.geometry("500x350")
janela.configure(bg=corBg)
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)
style = ttk.Style(janela)
style.theme_use('default')

topoTitulo = Label(janela, text="Gerar Orçamento", font="Verdana 18 bold", bg=corBg, fg=corFont)
topoTitulo.place(x=125, y=10)

#campos
nomeProjeto = Label(janela, text="Projeto: ", bg=corBg, fg=corFont, font=fontFamily)
nomeProjeto.place(x=125, y=60)
nomeProjetoEntrada = Entry(janela, width=29)
nomeProjetoEntrada.place(x=200, y=63)

horasEstimadas = Label(janela, text="Horas Estimadas: ", bg=corBg, fg=corFont, font=fontFamily)
horasEstimadas.place(x=125, y=90)
horasEstimadasEntrada = Entry(janela, width=16)
horasEstimadasEntrada.place(x=280, y=93)

valorHora = Label(janela, text="Valor/hora: ", bg=corBg, fg=corFont, font=fontFamily)
valorHora.place(x=125, y=120)
valorHoraEntrada = Entry(janela, width=25)
valorHoraEntrada.place(x=225, y=123)

prazoEstimado = Label(janela, text="Prazo entrega: ", bg=corBg, fg=corFont, font=fontFamily)
prazoEstimado.place(x=125, y=150)
prazoEstimadoEntrada = Entry(janela, width=20)
prazoEstimadoEntrada.place(x=255, y=153)

buttonGerar = Button(janela, text="Gerar", width=20, padx=20, command=fGerarOrcamento, cursor="hand2")
buttonGerar.bind("<Enter>", on_enter)
buttonGerar.bind("<Leave>", on_leave)
buttonGerar.place(x=153, y=220)


janela.mainloop()
