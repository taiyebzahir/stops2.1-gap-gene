__author__ = 'Kamil Koziara & Modifications by Taiyeb Zahir'

import cProfile
import numpy
from utils import generate_pop, HexGrid, draw_hex_grid
from stops_ import Stops2

secretion = numpy.array([7, 8])
reception = numpy.array([5, 6])
receptors = numpy.array([-1, -1])
bound=numpy.array([1,1,1,1,1,4,4,1,1,1,1,1])

base1=numpy.array([1,1,0,0,1,0,0,0,0,0,0,0])
base2=numpy.array([1,1,1,0,1,0,0,0,0,0,0,0])
base3=numpy.array([1,1,0,1,1,0,0,0,0,0,0,0])


trans_mat = numpy.array([[0,0,0,0,0,0,0,0,0,0,0,-4], #Hunchback
                       [0,0,0,0,0,0,0,0,0,2,0,2], #Cad
                       [0,0,0,0,0,0,0,0,1,5,0,0], #Bcd
                       [0,0,0,0,0,0,0,1,0,0,0,0], #nanos
                       [3,3,0,0,0,0,0,0,0,-1,0,-1], #g0 dummy gene for thresholds of activations
                       [-1,0,0,0,0,0,-1,0,0,0,0,0], #nanos_receptor
                       [0,-1,0,0,0,-1,0,0,0,0,1,1], #bicoid_receptor
                       [0,0,0,0,0,0,0,0,0,0,0,0], #ligand_bicoid
                       [0,0,0,0,0,0,0,0,0,0,0,0], #ligand_nanos
		                   [0,0,0,0,0,0,0,0,0,0,-5,-5], #Giant
                       [0,0,0,0,0,0,0,0,0,-3,0,0], #Kruppel
                       [0,0,0,0,0,0,0,0,0,0,-2,0] #Knirps		
                       ])

init_pop = generate_pop([(200, base2), (1200, base1), (200, base3)])
grid = HexGrid(80, 20, 1)

def color_fun1(row):
    if row[0]==1:
        return 0.5
    else:
        return 0

def color_fun2(row):
    if row[1]==1:
        return 0.5
    else:
        return 0

def color_fun3(row):
    if row[9]==1:
        return 0.5
    else:
        return 0

def color_fun4(row):
    if row[10]==1:
        return 0.5
    else:
        return 0

def color_fun5(row):
    if row[11]==1:
        return 0.5
    else:
        return 0



def run():
    x = Stops2(trans_mat, init_pop, grid.adj_mat, bound, secretion, reception, receptors, secr_amount=3, leak=0, max_con=10, max_dist=40, opencl=False)
    for i in range(300):
        x.step()
        if i%5 == 0:
            print i
            draw_hex_grid(i, x.pop, grid, color_fun1, color_fun2, color_fun3, color_fun4, color_fun5)


cProfile.run("run()")
