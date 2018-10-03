def imprimir(a):
    pr=""
    if a[0][0]=="+":
        pass
    else:
        pr+=str(a[0][0])
    for i in range (len(a[0])-1):
        pr+=str(a[0][i+1])
    pr+=","
    for j in range (len(a[1])):
        pr+=str(a[1][j])
    return (pr)


def suma(a,b):
    c=a[0][:]
    d=a[1][:]
    e=b[0][:]
    f=b[1][:]     
    resd=""      #guarda el resultado  de la parte decimal
    rese=""      #guarda el resultado de la parte entera
    men=""
    if c[0]=="-" and e[0]=="-":
        c[0]="+"
        e[0]="+"
        men="-"
  
    if c[0]=="-":
        a[0][0]="+"
        m=resta(b,a)
        a[0][0]="-"
        return(m)
    if e[0]=="-":    
        b[0][0]="+"
        n=resta(a,b)
        b[0][0]="-"
        return(n)
    else:
        if len(d)<len(f):
            cero=len(f)-len(d)
            for i in range (cero):
                d.insert(len(d),0)
        if len(f)<len(d):
            cero=len(d)-len(f)
            for i in range(cero):
                f.insert(len(f),0)
        if len(c)<len(e):
            cero=len(e)-len(c)
            for j in range(cero):
                c.insert(1,0)
        if len(e)<len(c):
            cero=len(c)-len(e)
            for j in range(cero):
                e.insert(1,0)
        for k in range (len(d)):
            dec=d[-(k+1)]+f[-(k+1)]
            r=dec
            if len(resd)==len(d)-1:
                if dec>9:
                    d.insert(0,0)                    
            if dec>9:
                dec=dec-10
                d[-(k+2)]=d[-(k+2)]+1
            resd+=str(dec)  
        if r>9:
            c[-1]+=1   
        for l in range (len(c)-1):
            ent=c[-(l+1)]+e[-(l+1)]
            r1=ent
            if len(rese)==len(c)-2:
                if r1>9:
                    c.insert(1,0)
                    c.insert(1,0)
            if ent>9:
                ent=ent-10
                c[-(l+2)]+=1
            rese+=str(ent)
        if r1>9:        
            rese+=str(1)
        rese+=str(men)
        a0=list(map(int,resd[::-1]))
        a1=list(map(int,rese[::-1]))
        a1.insert(0,"+")
        resultado=(a1,a0)
        return(resultado)
    

def resta(a,b):  
    if a[0][0]=="-" and b[0][0]=="+":
        a[0][0]="+"
        g=suma(a,b)
        g[0][0]="-"
        a[0][0]="-"
        return(g)
    if a[0][0]=="-" and b[0][0]=="-":
        b[0][0]="+"
        g=suma(a,b)
        b[0][0]="-"
        return(g)
    if a[0][0]=="+" and b[0][0]=="-":
        b[0][0]="+"
        g=suma(a,b)
        b[0][0]="-"
        return (g)
    c1=""
    e1=""
    for n in range(len(a[0])-1):
        c1+=str(a[0][n+1])
    for h in range(len(b[0])-1):
        e1+=str(b[0][h+1])
    c11=int(c1)
    e11=int(e1)
    c=a[0][:]
    cp=a[0][:]
    d=a[1][:]
    dp=a[1][:]
    e=b[0][:]
    ep=b[0][:]
    f=b[1][:]
    fp=b[1][:]
    resd=""      #guarda el resultado de la parte decimal
    rese=""      #guarda el resultado de la parte entera
    if c11<e11:
       e=cp
       c=ep
       d=fp
       f=dp  
    if len(d)<len(f):
        cero=len(f)-len(d)
        for i in range (cero):
            d.insert(len(d),0)
    if len(f)<len(d):
        cero=len(d)-len(f)
        for i in range(cero):
            f.insert(len(f),0)
    if len(c)<len(e):
        cero=len(e)-len(c)
        for j in range(cero):
            c.insert(1,0)
    if len(e)<len(c):
        cero=len(c)-len(e)
        for j in range(cero):
            e.insert(1,0)
    for k in range(len(d)):
        if len(resd)==len(d)-1:
            if d[-(k+1)]<f[-(k+1)]:
                d.insert(0,0)
        if d[-(k+1)]<f[-(k+1)]:
            d[-(k+1)]+=10
            d[-(k+2)]-=1
        dec=d[-(k+1)]-f[-(k+1)]
        resd+=str(dec)
    
    if len(d)>len(f):
        c[-1]-=1
    for l in range(len(c)-1):
        if len(rese)==len(c)-2:
            if c[-(l+1)]<e[-(l+1)]:
                c.insert(1,0)
        if c[-(l+1)]<e[-(l+1)]:
            c[-(l+1)]+=10
            c[-(l+2)]-=1
        ent=c[-(l+1)]-e[-(l+1)]
        rese+=str(ent)
    
    a0=list(map(int,rese[::-1]))
    a1=list(map(int,resd[::-1]))
    if c11<e11:
        a0.insert(0,"-")
    else:
        a0.insert(0,"+")
    for p in range (len(a0)):
        if a0[0]=="0":
            pass
        else:
            ce=0
            m=0
            if c11<e11:
               m=1
            while ce==0:
               if a0[m]=="0":
                   a0.pop(m)
               else:
                   ce=1
            p=len(a0)+1
    resultado=(a0,a1)
    return(resultado)
    
    
def multiplicacion(a,b):
    if (a[0][0]=="-" and b[0][0]=="+") or (a[0][0]=="+" and b[0][0]=="-"):
        signo=0
    else:
        signo=1

    c=a[0]+a[1]
    c.pop(0)
    d=b[0]+b[1]
    d.pop(0)
    sobra=0
    resul=[]
    resultado=[]
    ceros=0
    coma=len(a[1])+len(b[1])
    for j in range(len(d)):
        resul.append([])
        if ceros>=1:
            for k in range(ceros):
                resul[j].insert(0,0)
        for i in range (len(c)):
            mul=((c[-i-1]*d[-j-1])+sobra)%10
            sobra=int(((c[-i-1]*d[-j-1])+sobra)/10)
            resul[j].insert(0,mul)
        if (c[0]*d[-j-1])+sobra>9:
            resul[j].insert(0,sobra)        
        ceros+=1
        sobra=0
    for l in range(len(resul)):
        longitud=len(resul[-1])-len(resul[l])
        for m in range(longitud):
            resul[l].insert(0,0)
    suma=0
    lleva=0
    for p in range (len(resul[0])):
        if len(resultado)==len(resul[0])-1:
            resul[0].insert(0,0)
        for n in range (len(resul)):
            suma=resul[n][-p-1]+suma
        if suma>9:
            total=suma%10
            resultado.insert(0,total)
            lleva=int(suma/10)
        else:
            resultado.insert(0,suma)
            lleva=0
        resul[0][-p-2]+=lleva
        suma=0
    if lleva!=0:
        resultado.insert(0,resul[0][0])
    a0=[]
    a1=[]
    for q in range (coma):
        a1.append(resultado[-coma+q])
    for s in range(len(resultado)-coma):
        a0.append(resultado[s])
    for t in range (len(a1)):
        if len(a1)==1:
            break
        else:
            if a1[-1]==0:
                a1.pop(-1)
    if signo==0:
        a0.insert(0,"-")
    else:
        a0.insert(0,"+")
    final=(a0,a1)
    return(final)


def division(a,b,decimales=101):
    if (a[0][0]=="-" and b[0][0]=="+") or (a[0][0]=="+" and b[0][0]=="-"):
        signo=0
    else:
        signo=1
    signa=a[0][0]
    signb=b[0][0]
    del a[0][0]
    del b[0][0]
    c=[]
    d=[]
    divdecimal=""
    diventero=""
    for i in range (len(a[0])):
        c.append(a[0][i])
    for j in range (len(a[1])):
        c.append(a[1][j])
    if len(a[1])<len(b[1]):
        cero=len(b[1])-len(a[1])
        for k in range(cero):
            c.append(0)
    for l in range(len(b[0])):
        d.append(b[0][l])
    for m in range (len(b[1])):
        d.append(b[1][m])
    if len(b[1])<len(a[1]):
        cero=len(a[1])-len(b[1])
        for k in range(cero):
            d.append(0)
    num1=float("".join(str(n) for n in c))
    num2=float("".join(str(o) for o in d))
    diventero+=str(int(num1/num2))
    mod=(num1%num2)*10
    for p in range (decimales):
        rest=int(mod/num2)
        divdecimal+=str(rest)
        mod=(mod%num2)*10
    a0=list(map(int,diventero))
    a1=list(map(int,divdecimal))
    if signo==0:
        a0.insert(0,"-")
    if signo==1:
        a0.insert(0,"+")
    if decimales==101:
        if num1%num2==0:
            a1=[]
            a1.append(0)
        else:
            q=0
            while q==0:
                if a1[-1]=="0":
                    a1.pop(-1)
                else:
                    q=1
    resultado=(a0,a1)
    a[0].insert(0,signa)
    b[0].insert(0,signb)
    return(resultado)
    

def comparacion(a,b):
    c=a[0]+a[1]
    d=b[0]+b[1]
    if len(a[0])<len(b[0]):
        for j in range (len(b[0])-len(a[0])):
            c.insert(1,0)
    if len(b[0])<len(a[0]):
        for j in range(len(a[0])-len(b[0])):
            d.insert(1,0)
    if len(c)<len(d):   
        cero=len(d)-len(c)
        for i in range(cero):
            c.append(0)
    if len(d)<len(c):
        cero=len(c)-len(d)
        for i in range(cero):
            d.append(0)
    if c==d:
        return(True)
    else:
        return(False)


def pi():
    uno=(["+",1],[0])
    muno=(["-",1],[0])
    r=muno
    dos=(["+",2],[0])
    cuatro=(["+",4],[0])
    resultado=[]
    rango=[]
    sign=["+"]
    for k in range(10000):
        c=k
        if k==0:
            numero=(["+",k],[0])
        else:
            while c>0:
                num=c%10
                c=int(c/10)
                rango.insert(0,num)
            numero=(sign+rango,[0])
        signo=multiplicacion(r,muno)
        r=signo
        mul=multiplicacion(dos,numero)
        denominador=suma(mul,uno)
        termino=division(signo,denominador)
        resultado.append(termino)
        rango=[]
    a=resultado[0]
    for i in range(len(resultado)-1):
        b=suma(a,resultado[i+1])
        a=b
    npi=multiplicacion(b,cuatro)
    fpi=division(npi,uno,30)
    return(fpi)


if __name__ == "__main__":
    print(imprimir(pi()))
