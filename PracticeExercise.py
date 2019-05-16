# -*- coding: utf-8 -*-
"""
Editor de Spyder

Write a function that recive 2 numers and return the biggest one
Este es un archivo temporal.
"""
"""
Return the max of 2 num
http://www.pythondiario.com/2013/05/ejercicios-en-python-parte-1.html
"""
# 1
def max2(num1,num2):
    if(num1 > num2):
        return num1
    else:
        return num2

# Return the max of 3 num ie 2

def max3(num1, num2, num3):
    if(num1 > num2 and num1 > num3):
        return num1
    elif (num2 > num1 and num2 > num3):
        return num2
    else: 
        return num3
    

# Count the number of elemnts in a list i.e 3
def lenght_List(lista):
    cont = 0
    for i in lista:
        cont+= 1
    return cont

# validate if the char is a vocal or not 4
def vocal(x):
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        return True
    if x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
        return True
    return False

#  create a function for addition and one for multiplication of all the elements of a LIST
def suma(lista):
    suma = 0
    for i in range (0,(len(lista)),1):
        suma = suma + lista[i]      
    
    return suma

def mult(lista):
    multi = 1
    for i in range (0,(len(lista)),1):
        multi = multi * lista[i]      
    
    return multi
        

# print the invers value that was received 6
def invers(cadena):
    cont = len(cadena)
    for i in range (cont-1,-1,-1):
        print(cadena[i]) 
        
    
    
    

print(max2(10,2))
