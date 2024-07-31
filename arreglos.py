def producto_punto(v, w):
    if len(v) != len(w):
        raise ValueError("Los arreglos deben tener el mismo tamaño")
    
    resultado = sum(v[i] * w[i] for i in range(len(v)))
    return resultado

def calcular_promedio(arreglo):
    if len(arreglo) == 0:
        return 0 
        
    suma= sum(arreglo)
    
    x= suma/len(arreglo)
    
    return x

def producto_directo(v, w):
    if len(v) != len(w):
        return "Error"
    resultado = []
    for i in range(len(v)):
        fila = []
        for j in range(len(w)):
            fila.append(v[i] * w[j])
        resultado.append(fila)
    return resultado
