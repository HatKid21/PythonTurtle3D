from turtle import *
import time
import math

class Object:
    
    vs = []
    fs = []

    def __init__(self, path : str):
        self.readData(path)

    def readData(self,path : str):
        try:
            with open(path,"r") as file:
                for line in file:
                    if (line.startswith("v ")):
                        ar = line[2:].split(" ");
                        point = (float(ar[0]),float(ar[1]),float(ar[2]))
                        self.vs.append(point)
                    if (line.startswith("f ")):
                        ind = line[2:].split(" ")
                        ar = []
                        for i in ind:
                            if ("/" in i):
                                ar.append(int(i.split("/")[0]));
                            else:
                                ar.append(int(i))
                        self.fs.append(ar)

        except FileNotFoundError:
            print(f"Error, file {path} not found!");

ht()
tracer(0)


obj = Object("assets/Cube.obj")
SCALE = 250
DOT_SIZE = 5

def project(cord : tuple) -> tuple:
    x,y,z = cord
    dx = x/z * SCALE
    dy = y/z * SCALE
    return (dx,dy)

def draw_dot(cord : tuple):
    up()
    cord = project(cord)
    dx, dy = cord
    goto(dx,dy)
    dot(DOT_SIZE,"green")

def transform(cord : tuple, dz : int):
    x,y,z = cord
    return (x,y,z+dz)

def rotate(cord : tuple, angle : float):
    x,y,z = cord
    c = math.cos(angle)
    s = math.sin(angle)
    return (x*c -z*s,y,x*s + z*c)

def draw_line(start: int, end : int, dz : int, dr : int):
    up()
    dx1,dy1 = project(transform(rotate(obj.vs[start-1],dr),dz))
    dx2,dy2 = project(transform(rotate(obj.vs[end-1],dr),dz))
    goto(dx1,dy1)
    down()
    goto(dx2,dy2)
    up()


FPS = 24
dt = 1/FPS

def frames():
    angle = 0
    dz = 2
    sleepTime = FPS/1000; 
    for i in range(0,50000):
        clear()
        angle += 2 * math.pi*dt * 0.25
        time.sleep(sleepTime)
        for v in obj.vs:
            draw_dot(transform(rotate(v,angle),dz))
        for f in obj.fs:
            for i in range(0,len(f)):
                draw_line(f[i],f[(i+1)%len(f)],dz,angle)
        #dz+=1*dt
        update()


frames()

done()

