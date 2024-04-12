idvlan = int(input("Cual es el id de VLAN? "))
if idvlan >= 1 and idvlan <= 1005:
    print("Esta es un vlan de Rango Normal.")
elif idvlan >=1006 and idvlan <= 4095:
    print("Esta es una vlan de Rango Extendida.")
else:
    print("el número de Vlan ingresado es desconocida.")