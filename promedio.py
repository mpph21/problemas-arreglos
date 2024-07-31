def calcular_promedio(arreglo):
    if len(arreglo) == 0:
        return 0 
        
    suma= sum(arreglo)
    
    x= suma/len(arreglo)
    
    return x
    
    
a= [1,2,3,4,5,6]
b= calcular_promedio(a)
print (b)