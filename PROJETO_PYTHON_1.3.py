
# coding: utf-8

# In[1]:


# Gráficos em python
import matplotlib.pyplot as plt


# In[2]:


# Bibliotecas
import numpy as np #funções numéricas


# In[4]:


# valores de x,y,z:


#x, y, z = #função importar ////// #DADOS DEVEM ENTRAR AQUI (X,Y,Z)


# - EXEMPLO DE GRÁFICO

# In[7]:


## PRECISAMOS ACHAR COMANDOS/BIBLIOTECAS AS QUAIS PLOTAM 3D
x = np.linspace(-100 , 100, 4000)
y = (x+3) /(x**2+7)
plt.figure()
plt.plot(x, y, 'r')   ##y2=x
plt.xlabel("x")
plt.ylabel("y=cos(x) e y=x")
plt.grid()
#plt.xlim(0.2 , 0.3)                 ##MONSTRA LUGARES ESPECÍFICOS DO GRÁFICO
plt.show()


# ### OS DADOS SÃO ENTRADOS DE ACELERAÇÂO
# - Isso requere que façamos algumas operações para derivar a velocidade e espaço
# - Velocidade média:
# $$ v = \frac{\int_{t_{0}}^{t} a(\xi) \Delta \xi}{t-t_{0}} $$ 
# - Velocidade instantânea:
# $$ v(t) = \frac{[ a(t) - a(t + \Delta t) ]} {\Delta t} ; \Delta t \rightarrow 0 $$
# 
# - - ANALOGAMENTE, DEFINIMOS ESPAÇO INSTÂNEO
# $$ s(t) = \frac{[ v(t) - v(t + \Delta t) ]} {\Delta t} ; \Delta t \rightarrow 0 $$

# In[12]:


def v_acel_med(j, K, incremento):         #FUNÇÃO VELOCIDADE da aceleração "j", podendo j ser ax,ay e az
                                          #K é o ritmo em que o input é gerado pela máquina. Exemplo: 100 dados por segundo
                                          #Portanto K = 1dado / 100x1 segudos.
                                          #incremento de integração - com que precisão fazemos a média
    
   ### VARIÁVEIS BOBAS - VARIÁVEIS AS QUAIS USAREMOS PARA ESTRUTURAR O CÓDIGO  ###
    ### pense o código, e fará sentido ###
    soma=0       
    v=0
    t_fut=0
    
    
    for i in range (len(j)):      #para os valores percorrento todos os valores de j; LEN(j) É a funçaõ TAMANHO do vetor (j)
        TEMPO_ESPAÇO = len(j)    #utilizar esse tamanho como nosso sistema de medida de tempo.
### Esse valor, está em quantidade de dados. ##
##### Usaremos a seguinte lógica: ############
## Se o sensor captura a aceleração a cada K segundos. Então, TEMPO_ESPAÇO vezes K é a quantidade de tempo transcorrida ##
        TEMPO_total_seg = TEMPO_ESPAÇO/K
    
### Criaremos a variável "vetor tempo" para podermos integrar ###
    
        T = np.linspace(0, TEMPO_total_seg, K)         # de 0, ao t final
                                        
    
### AGORA, podemos fazer a velocidade média ####

        for t in range (len(T)):                    ### "MOVIMENTO" da soma de integração, no decorrer do tempo T

            soma += a[t]* (K)
        
            return soma/len(T)


# In[14]:


def v_acel_inst(a_x_y_z, K):                   #FUNÇÃO VELOCIDADE instatânea, da aceleração "a_x_y_z", podendo a_x_y_z ser ax,ay e az
                                          #K é o ritmo em que o input é gerado pela máquina. Exemplo: 100 dados por segundo
                                          #Portanto K = 1dado / 100x1 segudos.
                                          #incremento de integração - com que precisão fazemos a média
    
   ### VARIÁVEIS BOBAS - VARIÁVEIS AS QUAIS USAREMOS PARA ESTRUTURAR O CÓDIGO  ###
    ### pense o código, e fará sentido ###
    soma=0       
    v=0
    t_fut=0
    
    
    for i in range (len(a_x_y_z)):      #para os valores percorrento todos os valores de j; LEN(j) É a funçaõ TAMANHO do vetor (j)
        TEMPO_ESPAÇO = len(a_x_y_z)    #utilizar esse tamanho como nosso sistema de medida de tempo.
### Esse valor, está em quantidade de dados. ##
##### Usaremos a seguinte lógica: ############
## Se o sensor captura a aceleração a cada K segundos. Então, TEMPO_ESPAÇO vezes K é a quantidade de tempo transcorrida ##
        TEMPO_total_seg = TEMPO_ESPAÇO/K
    
### Criaremos a variável "vetor tempo" para podermos integrar ###
    
        T = np.linspace(0, TEMPO_total_seg, K)         # de 0, ao t final
                                        
    
### AGORA, podemos fazer a velocidade média ####

        for t in range (len(T)):                    ### "MOVIMENTO" da soma de integração, no decorrer do tempo T

            v_inst[t,j] = a[t]-a[t-1]


# In[18]:


############ GRÁFICO DA VELOCIDADE INSTATÂNEA POR TEMPO ##########
def graf_v_T(v_isnt,T):
    
    plt.figure()
    plt.plot(v_inst, T, 'black')   ##y2=x
    plt.xlabel("velocidade instantânea")
    plt.ylabel("tempo")
    plt.grid()
    #plt.xlim(0.2 , 0.3)          ##MONSTRA LUGARES ESPECÍFICOS DO GRÁFICO
    plt.show()
################################################################################


# In[20]:


def s__v_inst(v_inst):                   #FUNÇÃO VELOCIDADE instatânea, da aceleração "a_x_y_z", podendo a_x_y_z ser ax,ay e az
                                          #K é o ritmo em que o input é gerado pela máquina. Exemplo: 100 dados por segundo
                                          #Portanto K = 1dado / 100x1 segudos.

        for t in range (len(T)):                    ### "MOVIMENTO" da soma de integração, no decorrer do tempo T

            s[t,j] = v_inst[t,j] - v_inst[t-1,j]


# In[21]:


############ GRÁFICO DO ESPAÇO INSTATÂNEO POR TEMPO ##########
def graf_v_T(s__v_inst,T):
    
    plt.figure()
    plt.plot(s__v_inst, T, 'red')   ##y2=x
    plt.xlabel("Espaço")
    plt.ylabel("Tempo")
    plt.grid()
    #plt.xlim(0.2 , 0.3)          ##MONSTRA LUGARES ESPECÍFICOS DO GRÁFICO
    plt.show()
################################################################################

