precio_producto = float(input("¿Cual es el precio original del producto?"))
descuento_producto = float(input("¿Cual es el descuento aplicado al producto?"))

def calcularDescuento(precio, descuento):
    return precio * (descuento/100)

def calcularPrecioTotal(precio, descuento):
    return precio - descuento

if precio_producto <= 0 or descuento_producto <= 0:
    print("Valores no validos para ser operados!")
else:
    descuento_final = calcularDescuento(precio_producto, descuento_producto)
    precio_total = calcularPrecioTotal(precio_producto, descuento_final)
    print(f"El precio total del producto con el descuento de un {descuento_producto}% es: {precio_total:.3f}$")