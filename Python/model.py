from tkinter import Tk, Canvas, BOTH
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

root = Tk()
root.geometry('1000x700')
canv = Canvas(root, width=800, height=600, bg='white')
canv.pack(fill=BOTH, expand=1)


class Point:
    """
    Class of junctions (further called points) of the web
    """
    def __init__(self):
        """
    x, y, z -- coordinates of a junction
    vx, vy, vz -- velocity projections of a junction
        """
        self.x = 0
        self.y = 0
        self.z = 0
        self.vx = 0
        self.vy = 0
        self.vz = 0


def line_masiv(n):  # Создание n нитей без шариков, создание двумерного масива
    for i in range(n):
        membrane.append([])
        
def zapolnenie_membrane(n, m): # на каждую нити создается по m шариков
    for i in range(n):
        masiv = []
        for j in range(m):
            masiv.append(Point())   
        membrane[i] = masiv


def line_otrisovka(n):  # Создание n нитей без шариков, создание двумерного масива
    for i in range(n):
        otrisovka.append([])

def zapolnenie_otrisovka (n, m): # на каждую нити создается по m шариков
    for i in range(n):
        masiv = []
        for j in range(m):
            masiv.append(Point())   
        otrisovka[i] = masiv


def entry_conditions (x_0, y_0, z_0, Vx_0, Vy_0, Vz_0):
    '''
    initial conditions (coordinates and scorti) for each point
    '''
    for i in range(len(membrane)):
        for j in range(len(membrane[i])):
            membrane[i][j].x = (i+1) * x_0 + 150
            membrane[i][j].y = (j+1) * y_0 + 250
            membrane[i][j].z = z_0 + 150
            membrane[i][j].Vx = Vx_0
            membrane[i][j].Vy = Vy_0
            membrane[i][j].Vz = Vz_0
    '''for i in range(len(membrane)):
        for j in range(len(membrane[i])):
            masiv1 = []
            mas = []
            x = membrane[i][j].x
            y = membrane[i][j].y
            z = membrane[i][j].z
            print(x, y, z)
            mas.append(x)
            mas.append(y)
            mas.append(z)
            masiv1.append(mas)
            print(masiv1)'''

def centrel(V_cx, V_cy, V_cz, i_c, j_c):
    membrane[i_c - 1][j_c - 1].Vx = V_cx
    membrane[i_c - 1][j_c - 1].Vy = V_cy
    membrane[i_c - 1][j_c - 1].Vz = V_cz


def move_point():
    for i in range(len(membrane)):
        for j in range(len(membrane[i])):            
            membrane[i][j].x += membrane[i][j].Vx
            membrane[i][j].y += membrane[i][j].Vy
            membrane[i][j].z += membrane[i][j].Vz

def acceleration(parameter, l_0, i_c, j_c):
    '''
    l_0 is the length of the spring in the unstretched condition 
    parameter = stiffness / mass
    '''
    for i in range(len(membrane)):
        for j in range(len(membrane[i])):
            '''for i in range(len(membrane)):
                for j in range(len(membrane[i])):
                    masiv1 = []
                    mas = []
                    x = membrane[i][j].x
                    y = membrane[i][j].y
                    z = membrane[i][j].z
                    mas.append(x)
                    mas.append(y)
                    mas.append(z)
                    masiv1.append(mas)
                    print(masiv1)'''
            if i == 0 and j == 0:
                c = membrane[i][j]
                b = Point()
                b.x, b.y, b.z = c.x + l_0, c.y, c.z
                r = Point()
                r.x, r.y, r.z = c.x - l_0, c.y, c.z
                l = membrane[i+1][j]
                #print(membrane[i][j].y)
                #print(membrane[i][j].y)
                t = membrane[i][j+1]
                '''environment = []
                environment.append(r)
                environment.append(l)
                environment.append(t)
                environment.append(b)
                for k in range(len(environment)):
                    print(environment[k].x, environment[k].y, environment[k].z)
                print(c.x, c.y, c.z)'''
            elif j == 0 and i != 0 and i != len(membrane) - 1:
                c = membrane[i][j]
                b = Point()
                b.x, b.y, b.z = c.x + l_0, c.y, c.z
                r = membrane[i-1][j]
                l = membrane[i+1][j]
                t = membrane[i][j+1]
            elif  j == 0 and i == len(membrane) - 1:
                c = membrane[i][j]
                b = Point()
                b.x, b.y, b.z = c.x + l_0, c.y, c.z
                l = Point()
                l.x, l.y, l.z = c.x + l_0, c.y, c.z
                r = membrane[i-1][j]
                t = membrane[i][j+1]
            elif i == len(membrane) - 1 and j != len(membrane[i]) - 1 and j != 0:
                c = membrane[i][j]
                l = Point()
                l.x, l.y, l.z = c.x + l_0, c.y, c.z
                b = membrane[i][j-1]
                r = membrane[i-1][j]
                t = membrane[i][j-1]
            elif i == len(membrane) - 1 and j == len(membrane[i]) - 1:
                c = membrane[i][j]
                l = Point()
                l.x, l.y, l.z = c.x + l_0, c.y, c.z
                t = Point()
                t.x, t.y, t.z = c.x + l_0, c.y, c.z
                b = membrane[i][j-1]
                r = membrane[i-1][j]
            elif i != len(membrane) - 1 and i != 0 and j == len(membrane[i]) - 1:
                c = membrane[i][j]
                t = Point()
                t.x, t.y, t.z = c.x + l_0, c.y, c.z
                r = membrane[i-1][j]
                b = membrane[i][j-1]
                l = membrane[i+1][j]
            elif i == 0 and j == len(membrane[i]) - 1:
                c = membrane[i][j]
                t = Point()
                t.x, t.y, t.z = c.x + l_0, c.y, c.z
                r = Point()
                r.x, r.y, r.z = c.x + l_0, c.y, c.z
                l = membrane[i+1][j]
                b = membrane[i][j-1]
            elif i == 0 and j != len(membrane[i]) - 1 and j != 0:
                c = membrane[i][j]
                r = Point()
                r.x, r.y, r.z = c.x + l_0, c.y, c.z
                l = membrane[i+1][j]
                b = membrane[i][j-1]
                t = membrane[i][j+1]
            elif i == i_c - 1 and j == j_c - 1:
                c = membrane[i][j]
                l = Point()
                l.x, l.y, l.z = c.x + l_0, c.y, c.z
                t = Point()
                t.x, t.y, t.z = c.x + l_0, c.y, c.z
                r = Point()
                r.x, r.y, r.z = c.x + l_0, c.y, c.z
                b = Point()
                b.x, b.y, b.z = c.x + l_0, c.y, c.z
            else:
                c = membrane[i][j]
                b = membrane[i][j-1]
                t = membrane[i][j+1]
                l = membrane[i+1][j]
                r = membrane[i-1][j]
            environment = []
            environment.append(r)
            environment.append(l)
            environment.append(t)
            environment.append(b)
            '''for k in range(len(environment)):
                masiv = [environment[k].x, environment[k].y, environment[k].z]
                print(masiv)
            print(c.x, c.y, c.z)'''  
            for k in range(len(environment)):
                length = math.sqrt((environment[k].x - c.x) ** 2 + (environment[k].y - c.y) ** 2 + (environment[k].z - c.z)**2)
                gamma = parameter * (1 - l_0 / length)
                c.Vx += gamma * (environment[k].x - c.x) 
                c.Vy += gamma * (environment[k].y - c.y)
                c.Vz += gamma * (environment[k].z - c.z)

def rendering(): # отрисовка линии
    for i in range(len(otrisovka)):
        for j in range(0, len(otrisovka[i]) - 1):
            canv.create_line(otrisovka[i][j].x, otrisovka[i][j].y, otrisovka[i][j+1].x, otrisovka[i][j+1].y)
        for j in range(len(otrisovka[i])):
            for i in range(len(otrisovka) - 1):
                canv.create_line(otrisovka[i][j].x, otrisovka[i][j].y, otrisovka[i+1][j].x, otrisovka[i+1][j].y)

'''def rendering(): # отрисовка линии
    for i in range(len(otrisovka)):
        for j in range(0, len(otrisovka[i]) - 1):
            canv.create_line(otrisovka[i][j].x, otrisovka[i][j].z, otrisovka[i][j+1].x, otrisovka[i][j+1].z)
        for j in range(len(otrisovka[i])):
            for i in range(len(otrisovka) - 1):
                canv.create_line(otrisovka[i][j].x, otrisovka[i][j].z, otrisovka[i+1][j].x, otrisovka[i+1][j].z)'''


def grafic():
    x = []
    y = []
    z = []
    s = []
    for i in range(len(membrane)):
        for j in range(len(membrane[i])):
            x.append(membrane[i][j].x)
            y.append(membrane[i][j].y)
            z.append(membrane[i][j].z)
            s.append(2)
    print(x, y, z)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_wireframe(x, y, z, s)
    plt.show()

def rotation(ux, uy, uz):
     for i in range(len(membrane)):
        for j in range(len(membrane[i])):
            a = Point()
            b = Point()
            c = Point()
            a.x = membrane[i][j].x
            a.y = membrane[i][j].y
            a.z = membrane[i][j].z
            #print(membrane[i][j].x)
            
            b.x = a.x
            b.y = np.cos(ux) * a.y - np.sin(ux)* a.z
            b.z = np.cos(ux) * a.z + np.sin(ux)* a.y
            c.x = b.x * np.cos(uy) + b.z * np.sin(uy)
            c.y = b.y
            c.z = b.z * np.cos(uy) - b.x * np.sin(uy)
            otrisovka[i][j].x = c.x * np.cos(uz) - c.y * np.sin(uz)
            otrisovka[i][j].y = c.z * np.cos(uz) + c.y * np.sin(uz)
            otrisovka[i][j].z = c.z


            

def modeling():
    canv.delete("all")
    centrel(0, 0, 0.25, 2, 2)
    move_point()
    acceleration(0.7, 90, 2, 2)
    rotation(0.3, 0.4, 0.1)
    rendering()
    root.after(20, modeling)


membrane = []
otrisovka = []
line_otrisovka(3)
zapolnenie_otrisovka(3, 3)
line_masiv(3)
zapolnenie_membrane(3, 3)
entry_conditions (90, 90, 90, 0, 0, 0)
modeling()
#grafic()
root.mainloop()
