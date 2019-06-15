import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry.polygon import  Polygon
###
def threesubtri(tri):
    return ((tri[0],(tri[0]+tri[1])/2,(tri[0]+tri[2])/2),
            (tri[1],(tri[1]+tri[0])/2,(tri[1]+tri[2])/2),
            (tri[2],(tri[2]+tri[0])/2,(tri[2]+tri[1])/2))

def Sierpinski(depth, tri0 = (np.array([-0.5, 0]), np.array([0.5, 0]), np.array([0, 3**(0.5)/2]))):
    if depth==0: return [tri0]
    TR=threesubtri(tri0)
    for i in range(depth-1):
        tmp = tuple()
        for j in range(len(TR)):
            tmp = tmp + threesubtri(TR[j])
        TR=tmp
    return TR

def SierpinskiPlot(depth, tri0 = ( np.array([-0.5, 0]), np.array([0.5, 0]), np.array([0, 3**(0.5)/2]) ), col = 'blue' ):
    if depth > 9: return 'depth is too large!'
    ser = Sierpinski(depth,tri0)
    SerP = plt.figure(figsize=(9,9))
    plt.axes(frameon=False);plt.xticks([]);plt.yticks([])
    
    for i in range(len(ser)):
        x,y=Polygon(ser[i]).exterior.xy
        plt.fill(x,y, color=col,linewidth=0)
    plt.gca().set_aspect(1)
    plt.show()
    return SerP
###Example1:
sier = SierpinskiPlot(3,col='red')
#sier.savefig("Sierpinski.pdf", bbox_inches='tight')
###Example2:
SierpinskiPlot(3,tri0 = (np.array([-2, 0]), np.array([2, 0]), np.array([-4, 3])))
