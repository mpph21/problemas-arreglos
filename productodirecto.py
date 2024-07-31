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

v = [1, 2, 3]
w = [4, 5, 6]
print(producto_directo(v, w))