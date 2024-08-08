producto = (input("Ingresa el nombre del producto"))
cantidad = int(input("Ingresa la cantidad"))
valor = float(input("Ingresa el valor del producto"))
descuento = float(input("Ingresa el descuento"))

valor_total = (valor - descuento)

print("El valor total a pagar:", valor_total)