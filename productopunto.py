def producto_punto(v, w):
    if len(v) != len(w):
        raise ValueError("Los arreglos deben tener el mismo tamaño")
    
    resultado = sum(v[i] * w[i] for i in range(len(v)))
    return resultado

# Ejemplo de uso
v = [1, 2, 3, 4]
w = [5, 6, 7, 8]

resultado = producto_punto(v, w)
print(f"El producto punto de {v} y {w} es: {resultado}")