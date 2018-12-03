import tkinter as tk  #para gerar a tabela
import tkinter.messagebox as msg #para abrir mesnsagem de texto
import sys #para checar o sistema operacional
import matplotlib.pyplot as plt #para usar a biblioteca para gráfico
import tkinter.filedialog as dialog #para abrir uma caixa de diálogo
import algoritmo as alg #para puxar o algorítmo
from tkinter import font #para mudar a fonte da caixa de texto
import webbrowser


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
        ajuda.add_command(label="Sobre...", command=self.MostraPDF)
        ajuda.add_command(label="Video...", command=self.AbreLink)
        barra.add_cascade(label="Ajuda", menu=ajuda)
        
         # display menu
        janela.config(menu=barra)
        
        Titulo = tk.Label(text ='TELEMETOP TABAJARA TURBO 2000', font=helv36) #título da interface
        Titulo.place(relx = 0.05, rely = 0.0666, relwidth = 0.9, relheight = 0.08)
        
        Versao = tk.Label(text ='versão 2.0 final', font = helv37) #escrever a versão da interface
        Versao.place(relx = 0.05, rely = 0.9, relwidth = 0.20, relheight = 0.05)
        
        BotaoMain = tk.Button(text='Valores Relevantes', font = helv37, command=self.Calcular) #escrever a Altura máxima obtida do foguete
        BotaoMain.place(relx = 0.1, rely = 0.50, relwidth = 0.32, relheight = 0.08)
                
        Botao1 = tk.Button(text='Altura x Tempo', font = helv37, command=self.GraficoA) #Botão para gerar o gráfico da Altura x Tempo
        Botao1.place(relx = 0.50, rely = 0.30, relwidth = 0.20, relheight = 0.15)
        
        Botao2 = tk.Button(text='Projeção em Solo', font = helv37, command=self.GraficoB) #Botão para gerar o gráfico da Projeção horizontal
        Botao2.place(relx = 0.50, rely = 0.65, relwidth = 0.20, relheight = 0.15)
        
        Botao_Ajuda_Botao1 = tk.Button(text='?', font = helv37, command=self.Ajuda1) 
        Botao_Ajuda_Botao1.place(relx = 0.70, rely = 0.30, relwidth = 0.03, relheight = 0.15)
        
        Botao_Ajuda_Valores = tk.Button(text='?', font = helv37, command=self.AjudaMain) 
        Botao_Ajuda_Valores.place(relx = 0.42, rely = 0.50, relwidth = 0.03, relheight = 0.08)
        
        Botao_Ajuda_Botao2 = tk.Button(text='?', font = helv37, command=self.Ajuda2) 
        Botao_Ajuda_Botao2.place(relx = 0.70, rely = 0.65, relwidth = 0.03, relheight = 0.15)
        
        Botao_Sair = tk.Button(text='Sair', font = helv37, command=self.Destroy) #Botão de saída do programa
        Botao_Sair.place(relx = 0.8, rely = 0.9, relwidth = 0.08, relheight = 0.05)
        
        janela.protocol("WM_DELETE_WINDOW", self.Destroy) #Necessário para fechar o programa em windows
        
        self.janela = janela        
        
    def MostraPDF(self):
        
        webbrowser.open_new('manualfinal2.0.pdf')
        
    def AbreLink(self):
        
        webbrowser.open('https://www.youtube.com/watch?v=l2Ned3ITv6Q') 
        
    def Calcular(self): #função para receber os dados
        Var = dialog.askopenfilename(title='Selecione o arquivo csv')
        Matriz=alg.createTuple(Var)
        
        Daniel=alg.Hmax(Matriz)
        Levi=alg.distancia_horizontal_percorrida(Matriz)
        Kenzo=alg.t_voo(Matriz)
        Mari=alg.vmax(Matriz)
        
        msg.showinfo('ALtura Máxima','O valor da Altura Máxima é %.2f m' % Daniel)
        msg.showinfo('Distância Horizontal Percorrida','O valor da Distância Horizontal Percorrida é %.2f m' % Levi)
        msg.showinfo('Tempo de Voo','O tempo de voo foi de %.0f s' % Kenzo)
        msg.showinfo('Velocidade Máxima','O valor da velocidade máxima é %.2f m/s' % Mari)
      
    def Ajuda1(self):#função para auxiliar o usuário com o botao 1
        
        msg.showinfo("Ajuda","Através deste botão o usuário pode buscar o arquivo em .csv que deseja analisar, com o auxilio do explorador de arquivos. Em seguida, abre-se um pop up no qual há um gráfico da altura em função do tempo. Este gráfico pode ser salvo")
        
    def Ajuda2(self):#função para auxiliar o usuário com o botao 2
        
        msg.showinfo("Ajuda","Através deste botão o usuário pode buscar o arquivo em .csv que deseja analisar, com o auxilio do explorador de arquivos. Em seguida, abre-se um pop up no qual há um gráfico da distância percorrida no eixo X e Y. Estes dados podem ser interpretados como a projeção do trajeto do foguete no solo. Este gráfico pode ser salvo")
    
    def AjudaMain(self):#função para auxiliar o usuário com o botao input
        
        msg.showinfo("Ajuda","Através deste botão o usuário pode buscar o arquivo em .csv que deseja analisar, com o auxilio do explorador de arquivos. Em seguida, aparecerão 4 mensagens para o usuário, informando o valor de 4 medidas importantes: Altura máxima, distância horizontal percorida, tempo de voo, e velocidade máximo, na respectiva ordem")
     
    def Funcao(self): #Função para caixa de texto "yes or no"
        
        msg.askyesno('Pergunta importante','Você está com fome?')
        
    def Destroy(self): # necessário para fechar o programa no windows
    
        self.janela.quit()
        if 'win' in sys.platform:
            self.janela.destroy()
            
    def GraficoA(self): #Função para gerar o gráfico
        Var = dialog.askopenfilename(title='Selecione o arquivo csv')
        Matriz=alg.createTuple(Var)

        alg.HxT(Matriz)       

    def GraficoB(self): #Função para gerar o gráfico
        Var = dialog.askopenfilename(title='Selecione o arquivo csv')
        Matriz=alg.createTuple(Var)
  
        alg.ProjecaoemSolo(Matriz)
   
    def Roda_Interface(self): #para rodar a interface
        
        self.janela.mainloop()
     
if __name__ == '__main__':
    
        gui = Interface_Grafica()
