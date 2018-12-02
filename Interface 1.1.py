import tkinter as tk #para gerar a tabela
import tkinter.messagebox as msg
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter.filedialog as dialog
import csv

a = [1,2,3,4]
b = [1,2,3,4]

class Interface_Grafica:
    
    def __init__(self):
        
        self.Cria_Interface()
        self.Roda_Interface()
    
    def Cria_Interface(self):

        janela = tk.Tk()
        janela.title('Telemetop Tabajara Turbo 2000') #título da interface
        janela.geometry("750x550+300+20") #tamanho da interface

        imgPath = r"C:\Users\Pessoal\Desktop\Logo Vetorizada.gif" 
        logo = tk.PhotoImage(file = imgPath)
        Logo = tk.Label(image = logo)
        Logo.image = logo
        Logo.place(x = 500, y = 10, width = 200, height = 200)
        
        Titulo = tk.Label(text ='TELEMETOP TABAJARA TURBO 2000') #título da interface
        Titulo.place(x = 200, y = 10, width = 250, height = 70)
        
        Versao = tk.Label(text ='versão 1.6 alpha') #escrever a versão da interface
        Versao.place(x = 10, y = 490, width = 200, height = 50)
        
        Caixa1 = tk.Label(text ='Altura Máxima:') #escrever a Altura máxima obtida do foguete
        Caixa1.place(x = 50, y = 140, width = 200, height = 50)
        
        Caixa2 = tk.Label(text ='Velocidade Máxima:') #escrever a velocidade máxima do foguete
        Caixa2.place(x = 50, y = 200, width = 200, height = 50)
    
        Caixa3 = tk.Label(text ='Tempo de voo:') #escrever Tempo de voo
        Caixa3.place(x = 50, y = 260, width = 200, height = 50)
        
        Caixa4 = tk.Label(text ='Distância percorrida:') #escrever a distância percorrida
        Caixa4.place(x = 50, y = 320, width = 200, height = 50)
        
        Botao1 = tk.Button(text='Aceleração 3D', command=self.grafico2d(a,b)) #Botão para gerar o gráfico da aceleração 3D
        Botao1.place(x = 50, y = 390, width = 120, height = 100)
        
        Botao2 = tk.Button(text='Velocidade 3D', command=self.Funcao) #Botão para gerar o gráfico da Velocidade em 3D
        Botao2.place(x = 180, y = 390, width = 120, height = 100)
        
        Botao3 = tk.Button(text='Trajetória 3D', command=self.Funcao) #Botão para gerar o gráfico da Trajetória em 3D
        Botao3.place(x = 310, y = 390, width = 120, height = 100)
        
        Botao4 = tk.Button(text='Altura x Tempo', command=self.Funcao) #Botão para gerar o gráfico da Altura x Tempo
        Botao4.place(x = 440, y = 390, width = 120, height = 100)
        
        Botao5 = tk.Button(text='Projeção Horizontal', command=self.Funcao) #Botão para gerar o gráfico da Projeção horizontal
        Botao5.place(x = 570, y = 390, width = 120, height = 100)
        
        Botao_Input = tk.Button(text='Input', command=self.abrir) #Botão para pedir o arquivo .csv
        Botao_Input.place(x = 50, y = 80, width = 400, height = 40)
        
        Botao_Sair = tk.Button(text='Sair', command=self.Destroy) #Botão de saída do programa
        Botao_Sair.place(x = 650, y = 500, width = 50, height = 20)
        
        janela.protocol("WM_DELETE_WINDOW", self.Destroy) #Necessário para fechar o programa em windows
        
        self.janela = janela        
        
    def abrir(self): #função para receber os dados
        ## código csv ##
        a_x_y_z = dialog.askopenfilename(title='Selecione o arquivo csv')
        a_x_y_z = open('a_x_y_z.csv')
        a_x_y_z = csv.reader(a_x_y_z)
    
    def Funcao(self): #Função para caixa de texto "yes or no"
        
        msg.askyesno('Pergunta importante','Você está com fome?')
    
    def GraficoA(self): #Função para gerar o gráfico
        
        janela1 = tk.Tk()
        janela1.title('Gráfico')
        janela1.geometry("750x550+400+80")
        
        Botao_Salvar = tk.Button(janela1, text='Salvar', command=self.Funcao)
        Botao_Salvar.place(x = 600, y = 200, width = 60, height = 30)
    
    def Cria_Grafico(self, lugar):
        
        self.fig = plt.figure()
        plt.axhline(0, color='k')
        plt.axvline(0, color='k')
        plt.title('Power Graph Plotter Tabajara 1.0')
        self.linha, =  plt.plot([1, 2],[3, 4])

        # frame
        grafico_frame = tk.Frame(lugar)
        grafico_frame.pack()

        # canvas
        canvas = FigureCanvasTkAgg(self.fig, master=grafico_frame)
        canvas.get_tk_widget().pack()

    def Destroy(self):
    
        self.janela.quit()
        if 'win' in sys.platform:
            self.janela.destroy()
        

    def Roda_Interface(self):
        
        self.janela.mainloop()
    
    def Diz_Eae(self):
        
        msg.showinfo('Eae','Eae meu amigo, tudo bom?')
        
        
    def Sair(self):
        resposta = msg.askyesno('Cuidado!', 'Deseja realmente sair?')
        if resposta is True:
            self.janela.quit()
            if 'win' in sys.platform: 
                self.janela.destroy() # Precisa disso no Windows 
                
    def grafico2d(self,x,y):  # plota grafico 2d 
        plt.plot(x, y) 
      
        #eixo x 
        plt.xlabel('x - axis') 
        #eixo y 
        plt.ylabel('y - axis') 
      
        # título
        plt.title('My first graph!') 
          
        #mostra o gráfico 
        return plt.show()

if __name__ == '__main__':
    
        gui = Interface_Grafica()
