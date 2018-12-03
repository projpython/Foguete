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
def trapezoide(A):
    T=sliceT(A)
    del.T[-1]
    deltat=T[1]-T[0]
    Ax=sliceAx(A)
    Ay=sliceAy(A)
    Az=sliceAz(A)
    vx=[0]
    vy=[0]
    vz=[0]
    v=[T,vx,vy,vz]
    for i in range(len(Ax)-1):
        vn=(float(Ax[i])+float(Ax[i+1])) deltat/2
        vx.append(vn)
    for i in range(len(Ay)-1):
        vndois=(float(Ay[i])+float(Ay[i+1]))deltat/2
        vy.append(vndois)
    for i in range(len(Az)-1):
        vntres=(float(Az[i])+float(Az[i+1]))*deltat/2
        vz.append(vntres)
    return v
def strtofloat(lista):
    novalista = []
    for item in lista:
        novalista.append(float(item))
    return novalista
def Hmax(A):
    v=trapezoide(A)
    M=trapezoide(v)
    Sz=sliceAz(M)
    altura_max= max(Sz)
    return altura_max
def distância_horizontal_percorrida(A):
    V=trapezoide(A)
    M=trapezoide(V)
    Sx=sliceAx(M)
    Sy=sliceAy(M)
    pointx= Sx[-1]
    pointy= Sy[-1]
    square_sum= (pointy)*(pointy)+(pointx)*(pointx)
    dist=(square_sum)**(.5)
    return dist
def t_voo(A):
    t=sliceT(A)
    return t[-1]
def vmax(A):
    M=trapezoide(A)
    Vx=sliceAx(M)
    Vy=sliceAy(M)
    Vz=sliceAz(M)
    Vmodule=[]
    for i in range(Vx):
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
def ProjeçãoemSolo(A):
    V=trapezoide(A)
    S=trapezoide(V)
    x=sliceAx(S)
    y=sliceAy(S)
    plt.plot(x,y)
    
    plt.xlabel('Deslocamento Ox (m)')
    
    plt.ylabel('Deslocamento Oy (m)')
    
    plt.title('Projeção em Solo')
    
    return plt.show()
def HxT(A):
    V=trapezoide(A)
    S=trapezoide(V)
    x=sliceT(S)
    y=sliceAz(S)
    plt.plot(x,y)
    
    plt.xlabel('Tempo (s)')
    
    plt.ylabel('Altura (m)')
    
    plt.title('Altura x Tempo')
    
    return plt.show()