import sys
import os
import networkx as nx 
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPlainTextEdit
from PyQt5.QtGui import QIcon, QPixmap
from Graph import *



class ChildWindow(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("ChildWindow.ui",self)
        self.parent = parent
        self.setWindowTitle("Mapa")
        self.setFocus()
        self.createGraph()
        
    def createGraph(self):
        G = Graph()#Creo una instancia de grafo para poder enviar la informacion del qplaintext e ingresarla
        graph = G.convert(self.parent.array)
        a = self.parent.root_node.toPlainText()
        b = self.parent.last_node.toPlainText()
        self.printGraph(graph)#Llamo a la funcion que crea la imagen del grafo
        return list(self.dfs_paths(G.toRoad,a,b))

    def printGraph(self,graph):
        D = nx.DiGraph()
        for vertex, edges in graph.items():
            D.add_node("%s"%vertex)
            for edge in edges:
                D.add_node("%s"%"".join(edge))
                D.add_edge("%s" %vertex,"%s"%"".join(edge))
                #D.add_edge("%s"%"".join(edge),"%s"%vertex)
                #print("'%s' se conecta con '%s'"%(vertex,edge))
                #print(pos)
        pos = nx.drawing.layout.shell_layout(D)
        nx.draw(D,pos, with_labels=True, node_size = 4000, arrowsize = 20, node_color = "darkgray", width = 3.0 , font_size = 20, font_weight = "bold")#Dibuja el grafo
        #nx.draw_networkx_edge_labels(D,pos,edge_labels={('A','B'):'4.5',('A','C'):'25.4'},font_color='darkblue', font_size = 20)
        plt.savefig("image.png", dpi = 55)#Guarda el dibujo del grafo
        plt.clf()#Para que al agregar nueva info se borre el grafo anterior y no aparezca repetido en la ventana
        self.showGraph()
        os.remove("image.png")#Para que no se cree el archivo en la carpeta del proyecto

    def showGraph(self): #Funcion para que aparezca la imagen en la ventana
        label = QLabel(self)
        pixmap = QPixmap('image.png')
        label.resize(pixmap.width(),pixmap.height())       
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())

    def dfs_paths(self, graph, start, end):
        # Define stack variabledef dfs_paths(graph, start, end):
        stack = [(start, [start])]
        while stack:
            (vertex, path) = stack.pop()
            for next in graph[vertex] - set(path):
                if next == end:
                    yield path + [next]
                else:
                    stack.append((next, path + [next]))

