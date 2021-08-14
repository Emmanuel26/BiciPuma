import socket
import pickle

HOST = '127.0.0.1'
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,4001))

inicio = input("Tu ubicacion actual ")
dest = input("Tu destino ")
datosin=[inicio,dest]
data_string=pickle.dumps(datosin)
sock.send(data_string)


data = []
while True:
    msg = sock.recv(4096)
    data.append(msg)
    if not msg:
        break   
vecf = pickle.loads(b"".join(data))


mapa=[]
for i in vecf:
    mapa.append(i.id)

print (mapa)




