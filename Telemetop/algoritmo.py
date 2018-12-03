import matplotlib.pyplot as plt

def fixText(text): #função intermediaria utilizada na função createtuple
    row = []
    z = text.find(',')
    if z == 0:  row.append('')
    else:   row.append(text[:z])
    for x in range(len(text)):
        if text[x] != ',':  pass
        else:
            if x == (len(text)-1):  row.append('')
            else:
                if ',' in text[(x+1):]:
                    y = text.find(',', (x+1))
                    c = text[(x+1):y]
                else:   c = text[(x+1):]
                row.append(c)
    return row
def createTuple(oldFile): #função que lê o input do usuário em csv e gera uma matriz a ser trabalhada
    ## oldFile é o arquivo csv a ser lido
    f1 = open(oldFile, "r")
    tup = []
    while 1:
        text = f1.readline()
        if text == "":  break
        else:   pass
        if text[-1] == '\n':
            text = text[:-1]
        else:   pass
        row = fixText(text)
        tup.append(row)
    return tup
def deltat(A): #função intermediária para cálculo da integral, gera a variação de tempo entre as medidas
	T=sliceT(A)
	t=T[1]-T[0]
	return t
def integrateentreaspas(lista,Abase): #integração por trapézios, porém esta retorna uma lista de valores de obtidos da grandeza em relação ao tempo em diferentes instantes
    k=deltat(Abase)
    integrada=[]
    inte=0
    for i in range(len(lista)-1):
        inte+=(lista[i]+lista[i+1])*(k/2)
        integrada.append(inte)
    return integrada
def strtofloat(lista): #pega uma lista de valores e os transforma em pontos flutuantes
    novalista = []
    for item in lista:
        novalista.append(float(item))
    return novalista
def Hmax(A): #retorna o maior valor de altura encontrada
    Az=sliceAz(A)
    Vz=integrateentreaspas(Az,A)
    Sz=integrateentreaspas(Vz,A)
    altura_max= max(Sz)
    return altura_max
def distancia_horizontal_percorrida(A):  #encontra a distancia entre o ponto de lançamento e o de pouso da aeonave, a partir dos dados do acelerometro e considerando que os dados param de ser gerados quando o foguete atinge o chão
    Ax=sliceAx(A)
    Vx=integrateentreaspas(Ax,A)
    Sx=integrateentreaspas(Vx,A)
    Ay=sliceAy(A)
    Vy=integrateentreaspas(Ay,A)
    Sy=integrateentreaspas(Vy,A)
    pointx= Sx[-1]    #utiliza os ultimos pontos da posição x e y e calcula a distancia destes até a origem, sendo esta o ponto de lançamento
    pointy= Sy[-1]
    square_sum= (pointy)*(pointy)+(pointx)*(pointx)
    dist=(square_sum)**(.5)
    return dist
def t_voo(A): # determina o tempo de voo apenas retirando o ultimo instante medido
    t=sliceT(A)
    return t[-1]
def vmax(A): #função para velocidade máxima
    Ax=sliceAx(A)
    Vx=integrateentreaspas(Ax,A)  #valores de velocidades são gerados pelo método de "integração" em trapézios
    Ay=sliceAy(A)
    Vy=integrateentreaspas(Ay,A)
    Az=sliceAz(A)
    Vz=integrateentreaspas(Az,A)
    Vmodule=[]
    for i in range(len(Vx)): #Vmodule é uma lista formada pelos módulos das velocidades obtidas atraves da raiz quadrada da soma de seus quadrados
        sqr_sum= (Vx[i]*Vx[i])+(Vy[i]*Vy[i])+(Vz[i]*Vz[i])
        vmod= sqr_sum**(.5)
        Vmodule.append(vmod)
    vmax=max(Vmodule)
    return vmax #a função retorna o maior módulo de velocidade obtida 
def sliceT(Matriz): #corta a primeira coluna da matriz inputada em valores float para cálculos
    T=[x[0] for x in Matriz]
    t=strtofloat(T)
    return t
def sliceAx(Matriz):#corta a segunda coluna da matriz inputada em valores float para cálculos
    Ax=[x[1] for x in Matriz]
    a_x=strtofloat(Ax)
    return a_x
def sliceAy(Matriz):#corta a terceira coluna da matriz inputada em valores float para cálculos
    Ay=[x[2] for x in Matriz]
    a_y=strtofloat(Ay)
    return a_y
def sliceAz(Matriz): #corta a quarta coluna da matriz inputada em valores float para cálculos
    Az=[x[3] for x in Matriz]
    a_z=strtofloat(Az)
    return a_z
def ProjecaoemSolo(A): #função para gerar o gráfico da projeção em solo da trajetória
	Ax=sliceAx(A)
	Vx=integrateentreaspas(Ax,A)
	x=integrateentreaspas(Vx,A)
	Ay=sliceAy(A)
	Vy=integrateentreaspas(Ay,A)
	y=integrateentreaspas(Vy,A)
	plt.plot(x,y)
    
	plt.xlabel('Deslocamento Ox (m)')
    
	plt.ylabel('Deslocamento Oy (m)')
    
	plt.title('Projeção em Solo')
    
	return plt.show()  
def HxT(A): #função básica para gerar o gráfico de altura por tempo
    Ay=sliceAy(A)
    Vy=integrateentreaspas(Ay,A) #gera valores de velocidade
    y=integrateentreaspas(Vy,A)  #gera valores de posição
    T=sliceT(A)
    del(T[-1])                   #são retirados os ultimo e penultimo valor pois ao "integrar" para gerar valores de posição a partir da aceleração, o número de dados é reduzido em 2
    del(T[-1])                   #utiliza-se o instante associado ao primeiro valor do trapézio correspondente
    x=T
    plt.plot(x,y)
    
    plt.xlabel('Tempo (s)')
    
    plt.ylabel('Altura (m)')
    
    plt.title('Altura x Tempo')
    
    return plt.show() 