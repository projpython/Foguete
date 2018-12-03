import tkinter as tk  #para gerar a tabela
import tkinter.messagebox as msg #para abrir mesnsagem de texto
import sys #para checar o sistema operacional
import matplotlib.pyplot as plt #para usar a biblioteca para gráfico
import tkinter.filedialog as dialog #para abrir uma caixa de diálogo
import csv #para ler arquivo csv
import algoritmos as alg #para puxar o algorítmo
from tkinter import font #para mudar a fonte da caixa de texto

class Interface_Grafica: # abrir a classe interface
    
    def __init__(self): # para iniciar a interface gráfica
        
        self.Cria_Interface()
        self.Roda_Interface()
    
    def Cria_Interface(self): # para criar a interface

        janela = tk.Tk() # definindo a janela
        janela.title('Telemetop Tabajara Turbo 2000') #título da interface
        janela.geometry("750x550+300+20") #tamanho da interface
        helv36 = font.Font(family='Helvetica', size=18, weight=font.BOLD) #primeira fonte
        helv37 = font.Font(family='Helvetica', size=13, weight=font.BOLD) #segunda fonte
        
        
        CaminhoFundo = "fundo interface.gif"  #imagem de fundo da interface
        fundo = tk.PhotoImage(file = CaminhoFundo)
        Fundo = tk.Label(image = fundo)
        Fundo.image = fundo
        Fundo.place(relx = 0.0, rely = 0.0, relwidth = 1, relheight = 1)
        
        
        # cria a barra de menus
        barra = tk.Menu(janela)
        
        # menu de ajuda
        ajuda = tk.Menu(barra, tearoff=0)
        ajuda.add_command(label="Sobre...", command=self.Funcao)
        ajuda.add_command(label="Video...", command=self.Funcao)
        barra.add_cascade(label="Ajuda", menu=ajuda)
        
         # display menu
        janela.config(menu=barra)
        
        Titulo = tk.Label(text ='TELEMETOP TABAJARA TURBO 2000', font=helv36) #título da interface
        Titulo.place(relx = 0.05, rely = 0.0666, relwidth = 0.9, relheight = 0.08)
        
        Versao = tk.Label(text ='versão 1.6 alpha', font = helv37) #escrever a versão da interface
        Versao.place(relx = 0.05, rely = 0.9, relwidth = 0.20, relheight = 0.05)
        
        Caixa1 = tk.Label(text ='Altura Máxima: .2%f m', font = helv37) #escrever a Altura máxima obtida do foguete
        Caixa1.place(relx = 0.1, rely = 0.35, relwidth = 0.32, relheight = 0.08)
        
        Caixa2 = tk.Label(text ='Velocidade Máxima: .2%f m/s', font = helv37) #escrever a velocidade máxima do foguete
        Caixa2.place(relx = 0.1, rely = 0.48, relwidth = 0.32, relheight = 0.08)
    
        Caixa3 = tk.Label(text ='Tempo de voo: .2%f s', font = helv37) #escrever Tempo de voo
        Caixa3.place(relx = 0.1, rely = 0.61, relwidth = 0.32, relheight = 0.08)
        
        Caixa4 = tk.Label(text ='Distância percorrida: .2%f m', font = helv37) #escrever a distância percorrida
        Caixa4.place(relx = 0.1, rely = 0.74, relwidth = 0.32, relheight = 0.08)
        
        Botao1 = tk.Button(text='Altura x Tempo', font = helv37, command=self.GraficoA) #Botão para gerar o gráfico da Altura x Tempo
        Botao1.place(relx = 0.6, rely = 0.45, relwidth = 0.20, relheight = 0.15)
        
        Botao2 = tk.Button(text='Projeção em Solo', font = helv37, command=self.GraficoB) #Botão para gerar o gráfico da Projeção horizontal
        Botao2.place(relx = 0.6, rely = 0.65, relwidth = 0.20, relheight = 0.15)
        
        Botao_Input = tk.Button(text='Input', font = helv37, command=self.abrir) #Botão para pedir o arquivo .csv
        Botao_Input.place(relx = 0.1, rely = 0.2, relwidth = 0.7, relheight = 0.1)
        
        Botao_Sair = tk.Button(text='Sair', font = helv37, command=self.Destroy) #Botão de saída do programa
        Botao_Sair.place(relx = 0.8, rely = 0.9, relwidth = 0.08, relheight = 0.05)
        
        janela.protocol("WM_DELETE_WINDOW", self.Destroy) #Necessário para fechar o programa em windows
        
        self.janela = janela        
        
    def abrir(self): #função para receber os dados
        Var = dialog.askopenfilename(title='Selecione o arquivo csv')
        Matriz=alg.createTuple(Var)
        print(Matriz)
        
    def Funcao(self): #Função para caixa de texto "yes or no"
        
        msg.askyesno('Pergunta importante','Você está com fome?')
        
    def Destroy(self): # necessário para fechar o programa no windows
    
        self.janela.quit()
        if 'win' in sys.platform:
            self.janela.destroy()
            
    def GraficoA(self): #Função para gerar o gráfico
        
        a = [1,2,3,4]
        b = [1,2,3,4]

        Figura1 = plt.figure()
        Figura1, plt.plot(a, b) 
      
        #eixo x 
        plt.xlabel('Tempo') 
        #eixo y 
        plt.ylabel('Altura') 
          
        # título
        plt.title('Gráfico Altura x Tempo') 
              
        #mostra o gráfico 
        return plt.show()        
                    
       
    def GraficoB(self): #Função para gerar o gráfico
            
        c = [1,2,3,4]
        d = [1,2,3,4]
        
        plt.plot(c, d) 
          
        #eixo x 
        plt.xlabel('Distancia em X') 
        #eixo y 
        plt.ylabel('Distancia em Y') 
      
        # título
        plt.title('Projeção em Solo') 
              
        #mostra o gráfico 
        return plt.show()
   
    def Roda_Interface(self): #para rodar a interface
        
        self.janela.mainloop()
        
        
if __name__ == '__main__':
    
        gui = Interface_Grafica()
