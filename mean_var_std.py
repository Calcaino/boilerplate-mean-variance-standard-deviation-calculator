import numpy as np

def calculate(list):
    try:
        M=np.array(list).reshape(3, 3)
        media=[]
        vari=[]
        des=[]
        maximo=[]
        minimo=[]
        suma=[]
        
        me1=[]
        va1=[]
        de1=[]
        ma1=[]
        mi1=[]
        su1=[]
        for i in range(3):
            me1.append(np.mean(M[:, i]))
            va1.append(np.var(M[:, i]))
            de1.append(np.std(M[:, i]))
            ma1.append(np.max(M[:, i]))
            mi1.append(np.min(M[:, i]))
            su1.append(np.sum(M[:, i]))
        media.append(me1)  
        vari.append(va1) 
        des.append(de1) 
        maximo.append(ma1)  
        minimo.append(mi1)  
        suma.append(su1) 
        
        me1=[]
        va1=[]
        de1=[]
        ma1=[]
        mi1=[]
        su1=[]
        for i in range(3):
            me1.append(np.mean(M[i,:]))
            va1.append(np.var(M[i,:]))
            de1.append(np.std(M[i,:]))
            ma1.append(np.max(M[i,:]))
            mi1.append(np.min(M[i,:]))
            su1.append(np.sum(M[i,:]))
        media.append(me1)  
        vari.append(va1)  
        des.append(de1) 
        maximo.append(ma1)  
        minimo.append(mi1) 
        suma.append(su1) 
        
        media.append(np.mean(list))  
        vari.append(np.var(list))  
        des.append(np.std(list))  
        maximo.append(np.max(list))  
        minimo.append(np.min(list)) 
        suma.append(np.sum(list)) 
        
        dic={}
        dic['mean']=media
        dic['variance']=vari
        dic['standard deviation']=des
        dic['max']=maximo
        dic['min']=minimo
        dic['sum']=suma
        print(M)
        return calculations
    except ValueError:
        return 'List must contain nine numbers.'
 
