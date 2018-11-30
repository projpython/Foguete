
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

