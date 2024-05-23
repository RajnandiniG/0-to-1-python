import numpy as np
VectorAsArray = np.array([10,20,30,40,50]) #1D
rowAsArray = np.array([[1,2,3,4,5]]) #2D
columnAsArray=np.array([[1],[2],[3],[4],[5]])
#dimensions matters
print(VectorAsArray + rowAsArray)
#Each column element adds up with all row element and create arrays#For row, column addition any dimension works
print(columnAsArray + rowAsArray)
#dimensions don't matter
print(columnAsArray + VectorAsArray)

#Perform subtraction
print(VectorAsArray - rowAsArray)
print(rowAsArray - columnAsArray)
print(VectorAsArray - columnAsArray)

#Perform multiplication
print(VectorAsArray*rowAsArray)
print(columnAsArray*rowAsArray)
print(columnAsArray*VectorAsArray)

#Perform division
print(VectorAsArray/rowAsArray)
print(columnAsArray/rowAsArray)
print(columnAsArray/VectorAsArray)

#Perform floor division
print(VectorAsArray//rowAsArray)
print(columnAsArray//rowAsArray)
print(columnAsArray//VectorAsArray)

Perform %
print(VectorAsArray%rowAsArray)
print(columnAsArray%rowAsArray)
print(columnAsArray%VectorAsArray)

#Perform a to the power of b
print(VectorAsArray**rowAsArray)
print(columnAsArray**rowAsArray)
print(columnAsArray**VectorAsArray)
