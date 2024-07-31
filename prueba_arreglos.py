import arreglos
def main():
    v = [8, 2, 3]
    w = [4, 5, 6]
    
    # producto_punto
    try:
        resultado_punto = arreglos.producto_punto(v, w)
        print(f"Producto punto: {resultado_punto}")
    except ValueError as e:
        print(e)
    
    # calcular_promedio
    promedio = arreglos.calcular_promedio(v)
    print(f"Promedio: {promedio}")
    
    # producto_directo
    resultado_directo = arreglos.producto_directo(v, w)
    print(f"Producto directo: {resultado_directo}")

if __name__ == "__main__":
    main()
