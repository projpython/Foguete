
# coding: utf-8

# In[58]:


# Gráficos em python
import matplotlib.pyplot as plt


# In[59]:


# Bibliotecas
import numpy as np #funções numéricas


# In[60]:


# valores de x,y,z:


#x, y, z = #função importar ////// #DADOS DEVEM ENTRAR AQUI (X,Y,Z)


# - EXEMPLO DE GRÁFICO

# In[61]:


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
# $$ v = \int_{t_{0}}^{t} a(\xi) \Delta \xi \times (t-t_{0}) $$ 
# - Velocidade instantânea:
# $$ v(t) = [ a(t) - a(t + \Delta t) ]\times \Delta t ; \Delta t \rightarrow 0 $$
# 
# - - ANALOGAMENTE, DEFINIMOS ESPAÇO INSTÂNEO
# $$ s(t) = [ v(t) - v(t + \Delta t) ] \times \Delta t ; \Delta t \rightarrow 0 $$

# In[98]:


def v_acel_med(j=17, K=1):         #FUNÇÃO VELOCIDADE da aceleração "j", podendo j ser ax,ay e az
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


# In[148]:


def v_acel_inst(a_x_y_z = [1,1,1,1] , K=1 ):                   #FUNÇÃO VELOCIDADE instatânea, da aceleração "a_x_y_z", podendo a_x_y_z ser ax,ay e az
                                          #K é o ritmo em que o input é gerado pela máquina. Exemplo: 100 dados por segundo
                                          #Portanto K = 1dado / 100x1 segudos.
                                          #incremento de integração - com que precisão fazemos a média
    
    
    for i in range ( len(  a_x_y_z[1: , i+1]  ) ):      #para os valores percorrento todos os valores de j; LEN(j) É a função 
                                                        #TAMANHO do vetor (j)
        TEMPO_ESPAÇO[i] = len(a_x_y_z[1: , i+1])             #utilizar esse tamanho como nosso sistema de medida de tempo.
### Esse valor, está em quantidade de dados. ##
##### Usaremos a seguinte lógica: ############
## Se o sensor captura a aceleração a cada K segundos. Então, TEMPO_ESPAÇO vezes K é a quantidade de tempo transcorrida ##
        TEMPO_total_seg[i] = TEMPO_ESPAÇO[i]*K
    
### Criaremos a variável "vetor tempo" para podermos integrar ###
    
        T[:,i] = np.linspace(0, TEMPO_total_seg[i])         # de 0, ao t final
                                        
    
### AGORA, podemos fazer a velocidade média ####

        for t in range (len(TEMPO_ESPAÇO[i])):                       ### criaremos um v_inst para cara coluca i - referente a uma
                                                                      ### aceleração
            v_inst[t,i] = (a_x_y_z[t , i+1]+a_x_y_z[(t-1) , i]) / 2    ### Integração de um trapézio   
            
            


# In[149]:


def s_vel_inst(v_inst, K):                           #FUNÇÃO ESPAÇO instatânea, das velocidade v_inst[:,i], para cara i, um eixo
         
    for i in range (3):
        for t in range (len(TEMPO_ESPAÇO[i])):       ### criaremos um ponto de espaço, para cada t 
                                                                 
            s[t,i] = (v_inst[t , i]+ v_inst[(t-1) , i]) / 2   ##Integração do menor trapézio possível
            
            


# In[150]:


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


# In[151]:


def s__v_inst(v_inst):                    #Espaço instatâneo, derivado da aceleração "a_x_y_z", por meio da velocidade,
                                          #podendo a_x_y_z ser ax,ay e az.
                                          #K é o ritmo em que o input é gerado pela máquina. Exemplo: 100 dados por segundo.
                                          #Portanto K = 1dado / 100x1 segudos.

    for j in range (3):
        for t in range (len(T)):                    ### "MOVIMENTO" da soma de integração, no decorrer do tempo T.

            s[t,j] = v_inst[t,j] - v_inst[t-1,j]


# In[152]:


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


# - - Para facilitar o resto do código, separaremos a_x_y_z, variável com todas as acelerações, em três, a_x, a_y, a_z; assim em diante. Portanto:
# - - a_x_y_z $ \rightarrow $  a_x, a_y, a_z 
# - - v_inst $ \rightarrow $ v_x, v_y, v_z
# - - s $ \rightarrow $ s_x, s_y, s_z

# In[153]:


### a_x_y_z exemplo
j=0
for j in range (4):
    for a in range (10):
        a_x_y_z[:,j] = np.linspace(0, a, float(1/(a+1)))
        j += 1
        a *= j^2 + 8


# In[188]:


a_x_y_z = np.ones((7,7))
for i in range (7):
    a_x_y_z[:,i] = i
print(a_x_y_z)


# In[191]:


a_x_y_z = np.ones((7,7))
for i in range (7):
    a_x_y_z[:,i] = i
print(a_x_y_z)

######################### VAMOS FAZER O SLICING DO CÓDIGO CSV #################


a_x, a_y, a_z, v_x, v_y, v_z, s_x, s_y, s_z, T = [],[],[],[],[],[],[],[],[],[]    # 10 matrizes, 3 aceleração, velocidade, espaço
T = a_x_y_z[1:, 0]                                                                 # e 1 de tempo
print (T)
a_x[1:], a_y[1:], a_z[1:] = a_x_y_z[1:, 1], a_x_y_z[1:, 2], a_x_y_z[1:, 3]        
print(a_x), print(a_y), print(a_z)
v_x[:], v_y[:], v_z[:] = v_inst[:, 0], v_inst[:, 1], v_inst[:, 2]
s_x[:], s_y[:], s_z[:] = s[:, 0], s[:, 1], s[:, 2]


# In[178]:


a = np.ones((5,5))
for i in range (5):
    a[:,i] = i
print(a)


# In[180]:


print(a[1, 2:])


# In[172]:


b = np.ones((5,5))
print(b)

for j in range(5):

    b[ 1: ] = a[ 1: , 3 ]
    print(b)
    print(a)

