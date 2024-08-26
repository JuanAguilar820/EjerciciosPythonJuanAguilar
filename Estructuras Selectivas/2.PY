#Ejercicio 2
Nombre=input("ingrese su nombre: ")
Cuantas=int(input("Ingrese Cuantas zapatillas compro: "))
Valor_total_compra=int(input("Valor total de sus zapatillas: "))
if Cuantas>=3:
    Descuento= Valor_total_compra * 0.2
    Valor_final=(Valor_total_compra - Descuento)
    print(f"Señor@" ,Nombre, "su valor de compra es " ,Valor_total_compra, "su descuento es de" ,Descuento, "y el valor total con el descuento es de " ,Valor_final)
elif Cuantas<3:
    Descu= Valor_total_compra * 0.1
    Va_fi=(Valor_total_compra - Descu)
    print(f"señor@" ,Nombre, "su valor de compra es" ,Valor_total_compra, "su descuento es de " ,Descu, "y el valor final con el descuento es de" , Va_fi )
else:
    print(f"No dijito bien los datos")