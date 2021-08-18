import socket
import pickle
from Mapa import *

HOST = '192.168.0.6'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,4001))

print (" Calcular Ruta Bicipuma ")

print ("1. Anexo de Filosofía y Letras")
print ("2. Estadio")
print ("3. Arquitectura")
print ("4. Filosofía y Letras")
print ("5. Ingeniería")
print ("6. Derecho")
print ("7. Medicina")
print ("8. Química")
print ("9. Anexo de Ingeniería")
print ("10. Estadio Tapatío Méndez")
print ("11. Ciencias")
print ("12. Planta Alta")
print ("13. Planta Baja")
print ("14. Ciencias Políticas")

Ubicaciones=["Anexo de Filosofía y Letras","Estadio", "Arquitectura", "Filosofía y Letras","Ingeniería",
     "Derecho","Medicina","Química","Anexo de Ingeniería","Estadio Tapatío Méndez", "Ciencias",
     "Metro Universidad Planta Alta","Metro Universidad Planta Baja","Ciencias Políticas"]
UbiIndex=["A","B","C","D","E","F","G","H","I","J","K","L","M","N"]

while True:

    try:

        Inicio = int(input("Ingresa tu ubicacion "))
        print("Haz seleccionado: "+str(Inicio)+") "+ Ubicaciones[Inicio-1] )
        print("")
        Destino = int(input("Ingresa tu destino "))
        print("Haz seleccionado: " + str(Destino)+") "+Ubicaciones[Destino - 1])
        print("")
        Ubi = [Ubicaciones[Inicio-1], Ubicaciones[Destino-1]]
        break
    except IndexError:
        print("introduce una ubicacion que exista en la ruta")
    except ValueError:
        print("introduce caracteres validos")


Ubi2=[UbiIndex[Inicio-1],UbiIndex[Destino-1]]

print("Calculando...")
data_string=pickle.dumps(Ubi2)
sock.send(data_string)


data = []
while True:
    msg = sock.recv(4096)
    data.append(msg)
    if not msg:
        break   
vecf = pickle.loads(b"".join(data))

plotMapa(vecf)
print("Tu ruta ha sido calulada")


