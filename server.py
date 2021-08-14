# -*- coding: utf-8 -*-
import threading
import socket
import pickle
from PDijkstra import *

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 4001))
sock.listen(5)


def listToString(s):
    # initialize an empty string
    str1 = " -> "

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1

def handle_client(clientsocket):
    print("Connection is stablished", address)
    data=clientsocket.recv(4096)
    data_variable=pickle.loads(data)

    G=grafo()
    shortestPath(G,data_variable[0])
    vec= printPath(G, data_variable[1])
    
    
    
    msg = pickle.dumps(vec)
    
    clientsocket.send(msg)
    clientsocket.close()
    
    
    
    print("Algoritmo completado enviando a", address)
    
    

  
try:
    while True:
        clientsocket, address = sock.accept()
        t = threading.Thread(target=handle_client, args=(clientsocket,))
        t.start()


except KeyboardInterrupt:
    print ("Finishing. . .")
sock.close()
