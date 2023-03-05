horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

resultado = (3600 * horas) + (60 * minutos) + segundos

print("Se passaram %d segundos desde a meia noite" %(resultado))

