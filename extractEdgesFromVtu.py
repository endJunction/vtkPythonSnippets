#!/usr/bin/env python2

import sys
from vtk import *

def writePoly(filename, connection):
    w = vtkXMLPolyDataWriter()
    w.SetFileName(filename)
    w.SetDataModeToAscii()
    w.SetInputConnection(connection)
    w.Write()


def extractEdgesFromVtu(filename):
    r = vtkXMLUnstructuredGridReader()
    r.SetFileName(filename)

    g = vtkGeometryFilter()
    g.SetInputConnection(r.GetOutputPort())
    #writePoly('g.vtp', g.GetOutputPort())

    f = vtkFeatureEdges()
    f.BoundaryEdgesOn()
    f.FeatureEdgesOn()
    f.ManifoldEdgesOn()
    f.ColoringOn()
    f.SetInputConnection(g.GetOutputPort())
    f.SetOutputPointsPrecision(vtkAlgorithm.DOUBLE_PRECISION)
    writePoly('f.vtp', f.GetOutputPort())

if __name__ == "__main__":
    extractEdgesFromVtu(sys.argv[1])
