mensaje="hola, estoy aprendiendo Python"
nombre="Aguilar"
formacion="ADSO"
Edad=18
estatura=1.83
peso=73
#Primer forma de hacer print
print(mensaje, "Mi nombre es:", nombre, "soy de la formacion:", formacion, "tengo:", Edad, 
      "años", "mido:", estatura, "y peso:", peso, "kg") 
#Segunda forma de hacer print
print(f"{mensaje}. Minombre es: {nombre}, soy de la formacion: {formacion}, tengo: {Edad} años, mido: {estatura} y peso: {peso} kg")
#Tercera Froma 
a=7
b=5
suma= a+b
resta= a-b
multiplicacion= a*b
division=a//b
print("La suma es: ",  suma, "La resta es:", resta, "la Division es:", division, "La multiplicacion es:", multiplicacion )
#Ejercicio pididendo datos del usuario
Datonum1=int(input("Digite el primer numero "))
Datonum2=int(input("Digite el segundo numero "))
print("La suma es:", Datonum1+Datonum2, ", La resta es:", Datonum1-Datonum2, ", La division es:", Datonum1/Datonum2)
print("\n")