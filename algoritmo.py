import matplotlib.pyplot as plt

def fixText(text):
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
def createTuple(oldFile):
    ## oldFile is filename (e.g. 'sheet.csv')
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
def deltat(A):
	T=sliceT(A)
	t=T[1]-T[0]
	return t
def integrateentreaspas(lista,Abase):
    k=deltat(Abase)
    integrada=[]
    inte=0
    for i in range(len(lista)-1):
        inte+=(lista[i]+lista[i+1])*(k/2)
        integrada.append(inte)
    return integrada
def strtofloat(lista):
    novalista = []
    for item in lista:
        novalista.append(float(item))
    return novalista
def Hmax(A):
    Az=sliceAz(A)
    Vz=integrateentreaspas(Az,A)
    Sz=integrateentreaspas(Vz,A)
    altura_max= max(Sz)
    return altura_max
def distancia_horizontal_percorrida(A):
    Ax=sliceAx(A)
    Vx=integrateentreaspas(Ax,A)
    Sx=integrateentreaspas(Vx,A)
    Ay=sliceAy(A)
    Vy=integrateentreaspas(Ay,A)
    Sy=integrateentreaspas(Vy,A)
    pointx= Sx[-1]
    pointy= Sy[-1]
    square_sum= (pointy)*(pointy)+(pointx)*(pointx)
    dist=(square_sum)**(.5)
    return dist
def t_voo(A):
    t=sliceT(A)
    return t[-1]
def vmax(A):
    Ax=sliceAx(A)
    Vx=integrateentreaspas(Ax,A)
    Ay=sliceAy(A)
    Vy=integrateentreaspas(Ay,A)
    Az=sliceAz(A)
    Vz=integrateentreaspas(Az,A)
    Vmodule=[]
    for i in range(len(Vx)):
        sqr_sum= (Vx[i]*Vx[i])+(Vy[i]*Vy[i])+(Vz[i]*Vz[i])
        vmod= sqr_sum**(.5)
        Vmodule.append(vmod)
    vmax=max(Vmodule)
    return vmax
def sliceT(Matriz):
    T=[x[0] for x in Matriz]
    t=strtofloat(T)
    return t
def sliceAx(Matriz):
    Ax=[x[1] for x in Matriz]
    a_x=strtofloat(Ax)
    return a_x
def sliceAy(Matriz):
    Ay=[x[2] for x in Matriz]
    a_y=strtofloat(Ay)
    return a_y
def sliceAz(Matriz):
    Az=[x[3] for x in Matriz]
    a_z=strtofloat(Az)
    return a_z
def ProjecaoemSolo(A):
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
def HxT(A):
    Ay=sliceAy(A)
    Vy=integrateentreaspas(Ay,A)
    y=integrateentreaspas(Vy,A)
    T=sliceT(A)
    del(T[-1])
    del(T[-1])
    x=T
    plt.plot(x,y)
    
    plt.xlabel('Tempo (s)')
    
    plt.ylabel('Altura (m)')
    
    plt.title('Altura x Tempo')
    
    return plt.show()
a=createTuple('teste.csv')
HxT(a)