import tkinter as tk
import tkinter.messagebox as msg
import sys
import tkinter.filedialog as dialog
import subprocess



class Interface_Grafica:
    
    def __init__(self):
        
        self.Cria_Interface()
        self.Roda_Interface()
    
    def Cria_Interface(self):

        janela = tk.Tk()
        janela.title('Telemetop Tabajara Turbo 2000')
        janela.geometry("750x550+300+20")
        
        root = tk.Tk()

        imgPath = r"C:\Users\levib\Pictures\Logo Vetorizada.gif"
        logo = tk.PhotoImage(file = imgPath)
        Logo = tk.Label(image = logo)
        Logo.image = logo
        Logo.place(x = 500, y = 10, width = 200, height = 200)
        
        Titulo = tk.Label(text ='TELEMETOP TABAJARA TURBO 2000')
        Titulo.place(x = 200, y = 10, width = 250, height = 70)
        
        Versao = tk.Label(text ='versão 1.6 alpha')
        Versao.place(x = 10, y = 490, width = 200, height = 50)
        
        Caixa1 = tk.Label(text ='Altura Máxima:')
        Caixa1.place(x = 50, y = 80, width = 200, height = 50)
        
        Caixa2 = tk.Label(text ='Velocidade Máxima:')
        Caixa2.place(x = 50, y = 140, width = 200, height = 50)
    
        Caixa3 = tk.Label(text ='Tempo de voo:')
        Caixa3.place(x = 50, y = 200, width = 200, height = 50)
        
        Caixa4 = tk.Label(text ='Distância percorrida:')
        Caixa4.place(x = 50, y = 260, width = 200, height = 50)
        
        Botao1 = tk.Button(text='Aceleração 3D', command=self.Funcao)
        Botao1.place(x = 50, y = 390, width = 120, height = 100)
        
        Botao2 = tk.Button(text='Velocidade 3D', command=self.Funcao)
        Botao2.place(x = 180, y = 390, width = 120, height = 100)
        
        Botao3 = tk.Button(text='Trajetória 3D', command=self.Funcao)
        Botao3.place(x = 310, y = 390, width = 120, height = 100)
        
        Botao4 = tk.Button(text='Altura x Tempo', command=self.Funcao)
        Botao4.place(x = 440, y = 390, width = 120, height = 100)
        
        Botao5 = tk.Button(text='Projeção Horizontal', command=self.Funcao)
        Botao5.place(x = 570, y = 390, width = 120, height = 100)
        
        Botao_Input = tk.Button(text='Input', command=self.abrir)
        Botao_Input.place(x = 50, y = 330, width = 640, height = 40)
        
        Botao_Sair = tk.Button(text='Sair', command=self.Destroy)
        Botao_Sair.place(x = 650, y = 500, width = 50, height = 20)
        
        janela.protocol("WM_DELETE_WINDOW", self.Destroy)
        
        self.janela = janela
        

    def abrir(self):
        
        filename = dialog.askopenfilename(title='Selecione o arquivo csv')

    def Funcao(self):
        
        msg.showinfo('Hey bro', 'coloca o código')

    def Destroy(self):
    
        self.janela.quit()
        if 'win' in sys.platform:
            self.janela.destroy()
            
    def Roda_Interface(self):
        
        self.janela.mainloop()
        
if __name__ == '__main__':
    
        gui = Interface_Grafica()