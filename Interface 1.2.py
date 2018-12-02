import tkinter as tk #para gerar a tabela
import tkinter.messagebox as msg
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter.filedialog as dialog
import csv
from mpl_toolkits.mplot3d import axes3d
import numpy as np

a = [1,2,3,4]
b = [1,2,3,4]
c = [1,5,6,7]

class Interface_Grafica:
    
    def __init__(self):
        
        self.Cria_Interface()
        self.Roda_Interface()
    
    def Cria_Interface(self):

        janela = tk.Tk()
        janela.title('Telemetop Tabajara Turbo 2000') #título da interface
        janela.geometry("750x550+300+20") #tamanho da interface

        CaminhoLogo = r"C:\Users\Pessoal\Desktop\Logo Vetorizada.gif" 
        logo = tk.PhotoImage(file = CaminhoLogo)
        Logo = tk.Label(image = logo)
        Logo.image = logo
        Logo.place(x = 500, y = 10, width = 200, height = 200)
        
        # cria a barra de menus
        barra = tk.Menu(janela)
        
        # menu arquivo
        arquivo = tk.Menu(barra, tearoff=0)
        arquivo.add_command(label="Salvar...", command=self.hello)
        arquivo.add_command(label="Abrir...", command=self.hello)
        arquivo.add_command(label="Salvar como...", command=self.hello)
        barra.add_cascade(label="Arquivo", menu=arquivo)
        
        # menu de ajuda
        ajuda = tk.Menu(barra, tearoff=0)
        ajuda.add_command(label="Sobre...", command=self.hello)
        ajuda.add_command(label="Video...", command=self.Sobre)
        barra.add_cascade(label="Ajuda", menu=ajuda)
        
         # display menu
        janela.config(menu=barra)
        
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
        
        Botao1 = tk.Button(text='Aceleração 3D', command=self.graf_a) #Botão para gerar o gráfico da aceleração 3D
        Botao1.place(x = 50, y = 390, width = 120, height = 100)
        
        Botao2 = tk.Button(text='Velocidade 3D', command=self.graf_v) #Botão para gerar o gráfico da Velocidade em 3D
        Botao2.place(x = 180, y = 390, width = 120, height = 100)
        
        Botao3 = tk.Button(text='Trajetória 3D', command=self.graf_s) #Botão para gerar o gráfico da Trajetória em 3D
        Botao3.place(x = 310, y = 390, width = 120, height = 100)
        
        Botao4 = tk.Button(text='Altura x Tempo', command=self.Funcao) #Botão para gerar o gráfico da Altura x Tempo
        Botao4.place(x = 440, y = 390, width = 120, height = 100)
        
        Botao5 = tk.Button(text='Projeção Horizontal', command=self.Funcao) #Botão para gerar o gráfico da Projeção horizontal
        Botao5.place(x = 570, y = 390, width = 120, height = 100)
        
        Botao_Input = tk.Button(text='Input', command=self.abrir) #Botão para pedir o arquivo .csv
        Botao_Input.place(x = 50, y = 80, width = 400, height = 40)
        
        Botao_CalculaA = tk.Button(text='A', command=self.a)
        Botao_CalculaA.place(x = 650, y = 200, width = 40, height = 40)
        
        Botao_CalculaT = tk.Button(text='T', command=self.T) 
        Botao_CalculaT.place(x = 650, y = 250, width = 40, height = 40)
        
        Botao_CalculaS = tk.Button(text='S', command=self.s_vel_inst) 
        Botao_CalculaS.place(x = 650, y = 350, width = 40, height = 40)
        
        Botao_CalculaV = tk.Button(text='V', command=self.v_acel_inst)
        Botao_CalculaV.place(x = 650, y = 300, width = 40, height = 40)
        
        Botao_Sair = tk.Button(text='Sair', command=self.Destroy) #Botão de saída do programa
        Botao_Sair.place(x = 650, y = 500, width = 50, height = 20)
        
        janela.protocol("WM_DELETE_WINDOW", self.Destroy) #Necessário para fechar o programa em windows
        
        self.janela = janela        
        
    
    def abrir(self): #função para receber os dados
        ## código csv ##
        #Var = dialog.askopenfilename(title='Selecione o arquivo csv')
       # CaminhoCSV = r"C:\Users\Pessoal\Desktop\teste.csv"
        a_x_y_z = open(r'C:\Users\Pessoal\Desktop\teste.csv')
        a_x_y_z = csv.reader(a_x_y_z)
    
    def Funcao(self): #Função para caixa de texto "yes or no"
        
        msg.askyesno('Pergunta importante','Você está com fome?')
    
    def GraficoA(self): #Função para gerar o gráfico
        
        
        Figura1 = plt.figure()
        Figura1, plt.plot(a, b) 
      
        #eixo x 
        plt.xlabel('x - axis') 
        #eixo y 
        plt.ylabel('y - axis') 
      
        # título
        plt.title('My first graph!') 
          
        #mostra o gráfico 
        return plt.show()
    
    def GraficoB(self): #Função para gerar o gráfico
        

        plt.plot(c, b) 
      
        #eixo x 
        plt.xlabel('x - axis') 
        #eixo y 
        plt.ylabel('y - axis') 
      
        # título
        plt.title('My first graph!') 
          
        #mostra o gráfico 
        return plt.show()
    
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
    
        
    def Sair(self):
        resposta = msg.askyesno('Cuidado!', 'Deseja realmente sair?')
        if resposta is True:
            self.janela.quit()
            if 'win' in sys.platform: 
                self.janela.destroy() # Precisa disso no Windows 
        
    def hello(self):
    
        seu_nome = 'Seu nome é ' + texto1.get() 
        msg.showinfo('Informação', seu_nome)

    def Sobre(self):
    
        msg.showinfo('Sobre...', 'Minha interface em python')
        
    
    def a(a_x_y_z=[]):
    
        a_x, a_y, a_z, v_x, v_y, v_z, s_x, s_y, s_z, T = [],[],[],[],[],[],[],[],[],[]
    
        a_x[1:], a_y[1:], a_z[1:] = a_x_y_z[1:, 1], a_x_y_z[1:, 2], a_x_y_z[1:, 3] 
    
        return a_x, a_y, a_z
    
    def T(a_x_y_z = []):
    
        T = a_x_y_z[1: , 0]
        return T 
    
    def v_acel_inst(a_x_y_z = [] , K=1 ):         #FUNÇÃO VELOCIDADE instatânea, da aceleração "a_x_y_z", podendo a_x_y_z ser ax,ay e az
                                              #K é o ritmo em que o input é gerado pela máquina. Exemplo: 100 dados por segundo
                                              #Portanto K = 1dado / 100x1 segudos.
                                              #incremento de integração - com que precisão fazemos a média

        for j in range(4):
            for i in range ( len(  a_x_y_z[1: , 0]  ) ):      
                                                                               ### criaremos um v_inst para cara coluca j 
                                                                               ### referente a uma a uma aceleração
                v_inst[i,j] = (a_x_y_z[1: , j+1] + a_x_y_z[(i-1) , j+1]) / 2       ### Integração de um trapézio   
            
                v_x[:], v_y[:], v_z[:] = v_inst[:, 0], v_inst[:, 1], v_inst[:, 2]
            
                return v_x, v_y, v_z
            
    def s_vel_inst(v_inst, K):                           #FUNÇÃO ESPAÇO instatânea, das velocidade v_inst[:,i], para cara i, um eixo
         
        for j in range (3):
            for i in range (len(  v_inst[1: , 0]  ) ) :       ### criaremos um ponto de espaço, para cada t 
                                                                 
                s[i,j] = (v_inst[i , j]+ v_inst[(i-1) , j]) / 2   ##Integração do menor trapézio possível
            
                s_x[:], s_y[:], s_z[:] = s[:, 0], s[:, 1], s[:, 2]
            
                return s_x, s_y, s_z
    
    def graf_s(s_x, s_y, s_z):
 
# Criando a figura e projeção em 3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
 
# Utilizando dados de teste
        s_x, s_y, s_z = axes3d.get_test_data(0.10)
 
# Criando um Plot básico
        ax.plot_wireframe(s_x, s_y, s_z, rstride=10, cstride=10)

# Título do Gráfico
        plt.title('POSIÇÃO')

# Título dos Eixos
        plt.xlabel('POSIÇÃO EM X')
        plt.ylabel('POSIÇÃO EM Y')
        plt.zlabel('POSIÇÃO EM Z')
 
# Exibindo o gráfico criado
        plt.show()


    def graf_v(v_x, v_y, v_z):
 
# Criando a figura e projeção em 3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
 
# Utilizando dados de teste
        v_x, v_y, v_z = axes3d.get_test_data(0.10)
 
# Criando um Plot básico
        ax.plot_wireframe(v_x, v_y, v_z, rstride=10, cstride=10)

# Título do Gráfico
        plt.title('VELOCIDADE')

# Título dos Eixos
        plt.xlabel('VELOCIDADE EM X')
        plt.ylabel('VELOCIDADE EM Y')
        plt.zlabel('VELOCIDADE EM Z')
 
# Exibindo o gráfico criado
        plt.show()


    def graf_a(a_x, a_y, a_z):
 
# Criando a figura e projeção em 3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
 
# Utilizando dados de teste
        a_x, a_y, a_z = axes3d.get_test_data(0.10)
 
# Criando um Plot básico
        ax.plot_wireframe(a_x, a_y, a_z, rstride=10, cstride=10)

# Título do Gráfico
        plt.title('ACELERAÇÃO')

# Título dos Eixos
        plt.xlabel('ACELERAÇÃO EM X')
        plt.ylabel('ACELERAÇÃO EM Y')
        plt.zlabel('ACELERAÇÃO EM Z')
 
# Exibindo o gráfico criado
        plt.show()


if __name__ == '__main__':
    
        gui = Interface_Grafica()
