import tkinter as tk         #para gerar a tabela
import tkinter.messagebox as msg
import sys
import matplotlib.pyplot as plt
import tkinter.filedialog as dialog
import csv
from mpl_toolkits.mplot3d import axes3d
import algoritmos as alg


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
        arquivo.add_command(label="Salvar...", command=self.Funcao)
        arquivo.add_command(label="Abrir...", command=self.abrir)
        arquivo.add_command(label="Salvar como...", command=self.Funcao)
        barra.add_cascade(label="Arquivo", menu=arquivo)
        
        # menu de ajuda
        ajuda = tk.Menu(barra, tearoff=0)
        ajuda.add_command(label="Sobre...", command=self.Funcao)
        ajuda.add_command(label="Video...", command=self.Funcao)
        barra.add_cascade(label="Ajuda", menu=ajuda)
        
         # display menu
        janela.config(menu=barra)
        
        Titulo = tk.Label(text ='TELEMETOP TABAJARA TURBO 2000') #título da interface
        Titulo.place(relx = 200, rely = 10, relwidth = 250, relheight = 70)
        
        Versao = tk.Label(text ='versão 1.6 alpha') #escrever a versão da interface
        Versao.place(relx = 10, rely = 490, relwidth = 200, relheight = 50)
        
        Caixa1 = tk.Label(text ='Altura Máxima: .2%f m') #escrever a Altura máxima obtida do foguete
        Caixa1.place(relx = 50, rely = 140, relwidth = 200, relheight = 50)
        
        Caixa2 = tk.Label(text ='Velocidade Máxima: .2%f m/s') #escrever a velocidade máxima do foguete
        Caixa2.place(relx = 50, rely = 200, relwidth = 200, relheight = 50)
    
        Caixa3 = tk.Label(text ='Tempo de voo: .2%f s') #escrever Tempo de voo
        Caixa3.place(relx = 50, rely = 260, relwidth = 200, relheight = 50)
        
        Caixa4 = tk.Label(text ='Distância percorrida: .2%f m') #escrever a distância percorrida
        Caixa4.place(x = 50, y = 320, width = 200, height = 50)
        
        Botao1 = tk.Button(text='Altura x Tempo', command=self.Funcao) #Botão para gerar o gráfico da Altura x Tempo
        Botao1.place(x = 95, y = 390, width = 120, height = 100)
        
        Botao2 = tk.Button(text='Projeção Horizontal', command=self.Funcao) #Botão para gerar o gráfico da Projeção horizontal
        Botao2.place(relx = 0.2, rely = 0.15, relwidth = 0.120, relheight = 0.100)
        
        Botao_Input = tk.Button(text='Input', command=self.abrir) #Botão para pedir o arquivo .csv
        Botao_Input.place(x = 50, y = 80, width = 400, height = 40)
        
        Botao_Sair = tk.Button(text='Sair', command=self.Destroy) #Botão de saída do programa
        Botao_Sair.place(x = 650, y = 500, width = 50, height = 20)
        
        janela.protocol("WM_DELETE_WINDOW", self.Destroy) #Necessário para fechar o programa em windows
        
        self.janela = janela        
        
    def abrir(self): #função para receber os dados
        Var = dialog.askopenfilename(title='Selecione o arquivo csv')
        Matriz=alg.createTuple(Var)
        print(Matriz)
        
    def Funcao(self): #Função para caixa de texto "yes or no"
        
        msg.askyesno('Pergunta importante','Você está com fome?')
        
    def Destroy(self):
    
        self.janela.quit()
        if 'win' in sys.platform:
            self.janela.destroy()
            
    def Roda_Interface(self):
        
        self.janela.mainloop()
        
        
if __name__ == '__main__':
    
        gui = Interface_Grafica()
