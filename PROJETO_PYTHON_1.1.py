
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
# $$ v(t) = [ a(t) - a(t + \Delta t) ]\times \Delta t $$

# In[13]:


def v_acel_med(j, K, incremento):         #FUNÇÃO VELOCIDADE da aceleração "j", podendo j ser ax,ay e az
                                          #K é o ritmo em que o input é gerado pela máquina. Exemplo: 100 dados por segundo
                                          #Portanto K = 1dado / 100x1 segudos.
                                          #incremento de integração - com que precisão fazemos a média
    
   ### VARIÁVEIS BOBAS - VARIÁVEIS AS QUAIS USAREMOS PARA ESTRUTURAR O CÓDIGO  ###
    ### pense o código, e fará sentido ###
    soma=0       
    v=0
    t_fut=0
    
    
    for i range len(j):      #para os valores percorrento todos os valores de j; LEN(j) É a funçaõ TAMANHO do vetor (j)
    TEMPO_ESPAÇO = len(j)    #utilizar esse tamanho como nosso sistema de medida de tempo.
### Esse valor, está em quantidade de dados. ##
##### Usaremos a seguinte lógica: ############
## Se o sensor captura a aceleração a cada K segundos. Então, TEMPO_ESPAÇO vezes K é a quantidade de tempo transcorrida ##

    TEMPO_total_seg = TEMPO_ESPAÇO/K
    
### Criaremos a variável "vetor tempo" para podermos integrar ###
    
    T = np.linspace(0, TEMPO_total_seg, K)         # de 0, ao t final
                                        
    
### AGORA, podemos fazer a velocidade média ####

        for t in range len(T):                    ### "MOVIMENTO" da soma de integração, no decorrer do tempo T

        soma += a[t]* (K)
        
        return v_med = soma/len(T)

