from tkinter import *
from tkinter import ttk

class Funcs():

    def Limpar(self):
        self.tx_cont.config(state= NORMAL)
        self.tx_vis.config(state= NORMAL)
        self.tx_cont.delete(1.0, END)
        self.tx_vis.delete(1.0, END)
        self.tx_cont.config(state= DISABLED)
        self.tx_vis.config(state= DISABLED)

    def Inserir_valor(self, valor):
        self.tx_vis.config(state=NORMAL)
        self.tx_vis.insert(END, valor)
        self.tx_vis.config(state=DISABLED)

    def Calc(self):
        conta = self.tx_vis.get(1.0, END).strip()
        self.tx_cont.config(state= NORMAL)
        self.tx_cont.insert(INSERT, f'{conta} = ')
        self.tx_cont.config(state= DISABLED)
        try:
            resul = eval(conta)
            self.tx_vis.config(state=NORMAL)
            self.tx_vis.delete(1.0, END)
            self.tx_vis.insert(END, resul)
            self.tx_vis.config(state=DISABLED)
        except ZeroDivisionError:
            self.tx_vis.config(state=NORMAL)
            self.tx_vis.delete(1.0, END)
            self.tx_vis.insert(END, "Erro: Divisão por zero")
            self.tx_vis.config(state=DISABLED)
        except Exception as e:
            self.tx_vis.config(state=NORMAL)
            self.tx_vis.delete(1.0, END)
            self.tx_vis.insert(END, "MathError")
            self.tx_vis.config(state=DISABLED)

class App(Funcs):
    def __init__(self):
        self.root = Tk()
        self.Tela()
        self.Frames()
        self.Visor()
        self.Teclado()
        self.root.mainloop()

    def Tela(self):
        self.root.title('Calculadora')
        self.root.geometry('400x500')

    def Frames(self):
        self.visor = Frame(self.root, bg = 'lightblue')
        self.tec = Frame(self.root, bg= 'lightgray')
        self.visor.place(relx= 0.02, rely=0.02, relwidth= 0.96, relheight= 0.2)
        self.tec.place(relx= 0.02, rely= 0.24, relwidth= 0.96, relheight= 0.74)

    def Visor(self):
        #Text
        self.tx_cont = Text(self.visor, wrap=WORD)
        self.tx_vis = Text(self.visor, wrap=WORD)
        #config ninicial
        self.tx_cont.config(state=DISABLED)
        self.tx_vis.config(state=DISABLED)
        #places
        self.tx_cont.place(relx= 0.0, rely= 0.0, relwidth= 1.0, relheight= 0.3)
        self.tx_vis.place(relx=0.0, rely= 0.35, relwidth= 1.0, relheight= 0.65)

    def Teclado(self):
        y = 0.02
        x= 0.02
        #botões funcs
        self.bt_off = ttk.Button(self.tec, text= 'OFF', command=exit)
        self.bt_add = ttk.Button(self.tec, text= '+', command=lambda: self.Inserir_valor(' + '))
        self.bt_min = ttk.Button(self.tec, text= '-', command=lambda: self.Inserir_valor(' - '))
        self.bt_mult = ttk.Button(self.tec, text= 'X', command=lambda: self.Inserir_valor(' * '))
        self.bt_div = ttk.Button(self.tec, text= '/', command=lambda: self.Inserir_valor(' / '))
        self.bt_ce = ttk.Button(self.tec, text= 'CE', command=self.Limpar)
        self.bt_ig = ttk.Button(self.tec,text= '=', command=self.Calc)
        self.bt_pt = ttk.Button(self.tec, text= '.', command=lambda: self.Inserir_valor('.'))
        self.bt_el = ttk.Button(self.tec, text= '^', command=lambda: self.Inserir_valor(' ** '))
        self.bt_r2 = ttk.Button(self.tec, text= '√', command=lambda: self.Inserir_valor(' ** 0.5'))
        self.bt_pa = ttk.Button(self.tec, text= '(', command=lambda: self.Inserir_valor('( '))
        self.bt_pf = ttk.Button(self.tec, text= ')', command=lambda: self.Inserir_valor(' )'))
        #botões numéricos
        self.bt_n1 = ttk.Button(self.tec, text= '1', command=lambda: self.Inserir_valor('1'))
        self.bt_n2 = ttk.Button(self.tec, text= '2', command=lambda: self.Inserir_valor('2'))
        self.bt_n3 = ttk.Button(self.tec, text= '3', command=lambda: self.Inserir_valor('3'))
        self.bt_n4 = ttk.Button(self.tec, text= '4', command=lambda: self.Inserir_valor('4'))
        self.bt_n5 = ttk.Button(self.tec, text= '5', command=lambda: self.Inserir_valor('5'))
        self.bt_n6 = ttk.Button(self.tec, text= '6', command=lambda: self.Inserir_valor('6'))
        self.bt_n7 = ttk.Button(self.tec, text= '7', command=lambda: self.Inserir_valor('7'))
        self.bt_n8 = ttk.Button(self.tec, text= '8', command=lambda: self.Inserir_valor('8'))
        self.bt_n9 = ttk.Button(self.tec, text= '9', command=lambda: self.Inserir_valor('9'))
        self.bt_n0 = ttk.Button(self.tec, text= '0', command=lambda: self.Inserir_valor('0'))
        #places funcs
        self.bt_off.place(relx= 0.02, rely= y, relwidth= 0.15, relheight= 0.15)
        self.bt_add.place(relx= 0.19, rely= y, relwidth= 0.15, relheight= 0.15)
        self.bt_min.place(relx= 0.36, rely= y, relwidth= 0.15, relheight= 0.15)
        self.bt_mult.place(relx= 0.53, rely= y, relwidth= 0.15, relheight= 0.15)
        self.bt_div.place(relx= 0.7, rely= y, relwidth= 0.15, relheight= 0.15)
        self.bt_ce.place(relx= 0.53, rely= 0.19, relwidth= 0.15, relheight= 0.32)
        self.bt_ig.place(relx= 0.7, rely= 0.19, relwidth= 0.15, relheight= 0.32)
        self.bt_pt.place(relx= x, rely= 0.7, relwidth= 0.15, relheight= 0.15)
        self.bt_el.place(relx= 0.36, rely= 0.7, relwidth= 0.15, relheight= 0.15)
        self.bt_r2.place(relx= 0.53, rely= 0.53, relwidth= 0.15, relheight= 0.15)
        self.bt_pa.place(relx= 0.53, rely= 0.7, relwidth= 0.15, relheight= 0.15)
        self.bt_pf.place(relx= 0.7, rely= 0.7, relwidth= 0.15, relheight= 0.15)

        #places numéricos
        self.bt_n1.place(relx= x, rely= 0.19, relwidth= 0.15, relheight= 0.15)
        self.bt_n2.place(relx= 0.19, rely= 0.19, relwidth= 0.15, relheight= 0.15)
        self.bt_n3.place(relx= 0.36, rely= 0.19, relwidth= 0.15, relheight= 0.15)
        self.bt_n4.place(relx= x, rely= 0.36, relwidth= 0.15, relheight= 0.15)
        self.bt_n5.place(relx= 0.19, rely= 0.36, relwidth= 0.15, relheight= 0.15)
        self.bt_n6.place(relx= 0.36, rely= 0.36, relwidth= 0.15, relheight= 0.15)
        self.bt_n7.place(relx= x, rely= 0.53, relwidth= 0.15, relheight= 0.15)
        self.bt_n8.place(relx= 0.19, rely= 0.53, relwidth= 0.15, relheight= 0.15)
        self.bt_n9.place(relx= 0.36, rely= 0.53, relwidth= 0.15, relheight= 0.15)
        self.bt_n0.place(relx= 0.19, rely= 0.7, relwidth= 0.15, relheight= 0.15)

App()