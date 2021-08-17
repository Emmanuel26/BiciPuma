# -*- coding: utf-8 -*-
import threading
import socket
import pickle
from PDijkstra import *

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 4001))
sock.listen(5)


def handle_client(clientsocket):
    print("Connection is stablished", address)
    data = clientsocket.recv(4096)
    data_variable = pickle.loads(data)

    G = grafo()
    shortestPath(G, data_variable[0])
    vec = printPath(G, data_variable[1])

    Vertices = []
    Ubicacion = []

    for i in vec:
        Vertices.append(('Lugar', str(i.id)))
        Vertices.append(('Latitud', str(i.la)))
        Vertices.append(('Longitud', str(i.lo)))
        Ubicacion.append(dict(Vertices))
        Vertices.clear()

    print("Algoritmo completado enviando a", address)

    msg = pickle.dumps(Ubicacion)

    clientsocket.send(msg)
    print(Ubicacion)
    clientsocket.close()


try:
    while True:
        clientsocket, address = sock.accept()
        t = threading.Thread(target=handle_client, args=(clientsocket,))
        t.start()


except KeyboardInterrupt:
    print("Finishing. . .")
sock.close()
