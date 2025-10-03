#Este programa calcula la ley de ohm 
print("ley de ohm")
print("selecciona la opcion")
opcion=int(input("1=voltaje, 2=corriente, 3=resistencia"))
try:

    if opcion==1:
        resistencia = float(input("ingresa la resistencia en ohmios: "))
        corriente = float(input("ingresa la corriente en amperios: "))
        voltaje = resistencia * corriente
        print(f"El voltaje es: {voltaje} V")
    elif opcion==2:
        voltaje = float(input("ingresa el voltaje en voltios: "))
        resistencia = float(input("ingresa la resistencia en ohmios: "))
        if resistencia == 0:
            print("La resistencia no puede ser cero.")
        else:
            corriente = voltaje / resistencia
            print(f"La corriente es: {corriente} A")
    elif opcion==3:
        voltaje = float(input("ingresa el voltaje en voltios: "))
        corriente = float(input("ingresa la corriente en amperios: "))
        if corriente == 0:
            print("La corriente no puede ser cero.")
        else:
            resistencia = voltaje / corriente
            print(f"La resistencia es: {resistencia} ohmios")
    else:
        print("Opción no válida.")
except Exception as e:
    print(f"Error: {e}")
