# -*- coding: utf-8 -*-
############################################
#     Dijkstra class (python 2.7)          #
############################################

from PGraph import *


def shortestPath(Gr, root):
    Q = list(Gr.get_vertices())  # Queue
    Gr.set_startNode(root)  # start path

    while Q:
        Q.sort(key=lambda x: x.key)
        u = Q.pop(0)
        for v in u.adjacent.keys():
            if v.key > u.key + u.adjacent[v]:
                v.key = u.key + u.adjacent[v]
                v.pi = u


def printPath(Gr, end):
    l = []
    current = Gr.G[end]
    while current != None:
        l.append(current)
        current = current.pi
    l.reverse()
    return l

def grafo():
    G = Graph()
    G.add_vertex('A', 19.333470, -99.190900)  # Anexo Filosofía y Letras
    G.add_vertex('B', 19.331498, -99.189217)  # Estadio
    G.add_vertex('C', 19.332379, -99.186657)  # Arquitectura
    G.add_vertex('D', 19.333682, -99.186989)  # Filosofía y Letras
    G.add_vertex('E', 19.332129, -99.184408)  # Ingeniería
    G.add_vertex('F', 19.333752, -99.183850)  # Derecho
    G.add_vertex('G', 19.333524, -99.180835)  # Medicina
    G.add_vertex('H', 19.330747, -99.181637)  # Química
    G.add_vertex('I', 19.327934, -99.182970)  # Anexo de Ingeniería
    G.add_vertex('J', 19.325760, -99.187818)  # Estado Tapatío Méndez
    G.add_vertex('K', 19.325145, -99.178868)  # Ciencias
    G.add_vertex('L', 19.325101, -99.174549)  # Planta Alta
    G.add_vertex('M', 19.324797, -99.174656)  # Planta Baja
    G.add_vertex('N', 19.319486, -99.176223)  # Ciencias Políticas
    G.add_vertex('V1', 19.332842, -99.190150)
    G.add_vertex('V2', 19.331663, -99.187445)
    G.add_vertex('V4', 19.332630, -99.186694)
    G.add_vertex('V5', 19.333426, -99.186753)
    G.add_vertex('V6', 19.332418, -99.184029)
    G.add_vertex('V7', 19.332483, -99.183662)
    G.add_vertex('V8', 19.332179, -99.183971)
    G.add_vertex('V9', 19.333550, -99.183783)
    G.add_vertex('V10', 19.333705, -99.182110)
    G.add_vertex('V11', 19.333540, -99.182088)
    G.add_vertex('V12', 19.331783, -99.181929)
    G.add_vertex('V13', 19.330735, -99.181491)
    G.add_vertex('V14', 19.327775, -99.182686)
    G.add_vertex('V15', 19.326735, -99.183548)
    G.add_vertex('V16', 19.325720, -99.175412)
    G.add_vertex('V17', 19.324998, -99.174711)
    G.add_vertex('P4', 19.332183, -99.190056)
    G.add_vertex('P5', 19.331506, -99.189939)
    G.add_vertex('P6', 19.333016, -99.187617)
    G.add_vertex('P7', 19.331724, -99.186964)
    G.add_vertex('P8', 19.333499, -99.185840)
    G.add_vertex('P9', 19.333534, -99.185708)
    G.add_vertex('P10', 19.333723, -99.184014)
    G.add_vertex('P11', 19.333826, -99.181430)
    G.add_vertex('P12', 19.333937, -99.180884)
    G.add_vertex('P13', 19.333600, -99.181557)
    G.add_vertex('P14', 19.333423, -99.181520)
    G.add_vertex('P15', 19.331746, -99.181683)
    G.add_vertex('P16', 19.329495, -99.181284)
    G.add_vertex('P17', 19.328108, -99.183494)
    G.add_vertex('P18', 19.327864, -99.183245)
    G.add_vertex('P19', 19.324430, -99.185676)
    G.add_vertex('P20', 19.324326, -99.186151)
    G.add_vertex('P21', 19.324908, -99.186536)
    G.add_vertex('P22', 19.325408, -99.187043)
    G.add_vertex('P23', 19.324866, -99.183274)
    G.add_vertex('P24', 19.324730, -99.182877)
    G.add_vertex('P25', 19.325043, -99.182523)
    G.add_vertex('P26', 19.325194, -99.181548)
    G.add_vertex('P27', 19.325022, -99.181246)
    G.add_vertex('P28', 19.325478, -99.177940)
    G.add_vertex('P29', 19.323339, -99.175206)
    G.add_vertex('P30', 19.323078, -99.176392)

    G.add_edge('A', 'V1', 111.22)
    G.add_edge('B', 'P5', 76.17)
    G.add_edge('B', 'V2', 186.81)
    G.add_edge('C', 'V4', 27.33)
    G.add_edge('C', 'V6', 274.49)
    G.add_edge('D', 'V5', 37.60)
    G.add_edge('E', 'V8', 46.41)
    G.add_edge('F', 'V9', 22.25)
    G.add_edge('G', 'P12', 45.87)
    G.add_edge('G', 'P14', 72.33)
    G.add_edge('H', 'V12', 111.53)
    G.add_edge('H', 'V13', 16.11)
    G.add_edge('I', 'V14', 32, 78)
    G.add_edge('I', 'P18', 30.81)
    G.add_edge('J', 'P22', 90.19)
    G.add_edge('K', 'P27', 250.37)
    G.add_edge('K', 'P28', 104.24)
    G.add_edge('L', 'V16', 136.84)
    G.add_edge('L', 'V17', 23.28)
    G.add_edge('V1', 'A', 111.2)
    G.add_edge('V1', 'P6', 266.87)
    G.add_edge('V1', 'P4', 66.99)
    G.add_edge('V2', 'B', 186.81)
    G.add_edge('V2', 'P6', 150.39)
    G.add_edge('V2', 'P7', 50.11)
    G.add_edge('V4', 'P7', 103.59)
    G.add_edge('V4', 'C', 27.33)
    G.add_edge('V4', 'V5', 89.11)
    G.add_edge('V5', 'V4', 89.11)
    G.add_edge('V5', 'D', 37.60)
    G.add_edge('V5', 'P8', 96.60)
    G.add_edge('V6', 'C', 274.49)
    G.add_edge('V6', 'V7', 40.34)
    G.add_edge('V6', 'V8', 27.48)
    G.add_edge('V7', 'V6', 40.34)
    G.add_edge('V7', 'V9', 119.03)
    G.add_edge('V8', 'V6', 27.48)
    G.add_edge('V8', 'E', 46.41)
    G.add_edge('V8', 'P17', 453.31)
    G.add_edge('V9', 'P10', 31.25)
    G.add_edge('V9', 'V7', 119.03)
    G.add_edge('V9', 'F', 22.25)
    G.add_edge('V9', 'V10', 175.33)
    G.add_edge('V10', 'V9', 31.52)
    G.add_edge('V10', 'V11', 18.56)
    G.add_edge('V10', 'P11', 73.27)
    G.add_edge('V11', 'V10', 18.56)
    G.add_edge('V11', 'P13', 56.03)
    G.add_edge('V11', 'V12', 199.77)
    G.add_edge('V12', 'V11', 199.77)
    G.add_edge('V12', 'H', 111.53)
    G.add_edge('V12', 'P15', 26.64)
    G.add_edge('V13', 'P15', 112.31)
    G.add_edge('V13', 'H', 16.11)
    G.add_edge('V13', 'P16', 140.16)
    G.add_edge('V14', 'P16', 241.31)
    G.add_edge('V14', 'P18', 59.61)
    G.add_edge('V14', 'I', 32.78)
    G.add_edge('V14', 'V15', 145.91)
    G.add_edge('V15', 'V14', 145.91)
    G.add_edge('V15', 'P19', 338.42)
    G.add_edge('V15', 'P23', 208)
    G.add_edge('V16', 'P28', 267.42)
    G.add_edge('V16', 'L', 136.84)
    G.add_edge('V16', 'V17', 50)
    G.add_edge('V17', 'V16', 50)
    G.add_edge('V17', 'M', 23.28)
    G.add_edge('V17', 'P29', 191.19)
    G.add_edge('P4', 'V1', 66.99)
    G.add_edge('P4', 'P5', 79.34)
    G.add_edge('P5', 'P4', 79.34)
    G.add_edge('P5', 'B', 76.17)
    G.add_edge('P6', 'V1', 266.81)
    G.add_edge('P6', 'V2', 150.39)
    G.add_edge('P7', 'V2', 50.11)
    G.add_edge('P7', 'V4', 103.59)
    G.add_edge('P8', 'V5', 96.66)
    G.add_edge('P8', 'P9', 13.93)
    G.add_edge('P9', 'P8', 13.93)
    G.add_edge('P9', 'P10', 178.65)
    G.add_edge('P10', 'P9', 178.65)
    G.add_edge('P10', 'V9', 31.52)
    G.add_edge('P11', 'V10', 73.27)
    G.add_edge('P11', 'P12', 58.41)
    G.add_edge('P12', 'P11', 58.41)
    G.add_edge('P12', 'G', 45.87)
    G.add_edge('P13', 'V11', 56.03)
    G.add_edge('P13', 'P14', 19.71)
    G.add_edge('P14', 'P13', 19.71)
    G.add_edge('P14', 'G', 72.33)
    G.add_edge('P15', 'V12', 26.64)
    G.add_edge('P15', 'V13', 112.31)
    G.add_edge('P16', 'V13', 140.16)
    G.add_edge('P16', 'V14', 241.31)
    G.add_edge('P17', 'V8', 453.31)
    G.add_edge('P17', 'P18', 40.14)
    G.add_edge('P18', 'P17', 40.14)
    G.add_edge('P18', 'I', 30.81)
    G.add_edge('P18', 'V14', 59.61)
    G.add_edge('P19', 'V15', 338.42)
    G.add_edge('P19', 'P20', 52.24)
    G.add_edge('P20', 'P19', 52.24)
    G.add_edge('P20', 'P21', 77.77)
    G.add_edge('P21', 'P20', 77.77)
    G.add_edge('P21', 'P22', 75.58)
    G.add_edge('P22', 'P21', 75.58)
    G.add_edge('P22', 'J', 90.19)
    G.add_edge('P23', 'V15', 208)
    G.add_edge('P23', 'P24', 44.69)
    G.add_edge('P24', 'P23', 44.69)
    G.add_edge('P24', 'P25', 50)
    G.add_edge('P25', 'P24', 50)
    G.add_edge('P25', 'P26', 102.49)
    G.add_edge('P26', 'P25', 102.49)
    G.add_edge('P26', 'P27', 37.86)
    G.add_edge('P27', 'P26', 37.86)
    G.add_edge('P27', 'K', 250.37)
    G.add_edge('P28', 'K', 104.24)
    G.add_edge('P28', 'V16', 267.42)
    G.add_edge('P29', 'V17', 191.19)
    G.add_edge('P29', 'P30', 128.02)
    G.add_edge('P30', 'P29', 128.02)
    G.add_edge('P30', 'N', 398.84)
    return G
