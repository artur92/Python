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
 
#list.append(elem)

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

#  create a function for addition and one for multiplication of all the elements of a LIST 5
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
    cadena2 = ""
    for i in range (cont-1,-1,-1):
        cadena2 += cadena[i]
    return cadena2

# Check if a word is palindrome or no 7
def palindrome(cadena):
    
    cadena2 = invers(cadena)   
    if cadena == cadena2:
        return True
    return False

# Compare 2 list and check if one of the elemnts of 1 list is in the other one 8
def superposicion (lista1, lista2):
    for i in lista1:
        for x in lista2:
            if i == x:
                return True
    return False

'''
Create a function the get an int n and a char as parameters the return
the character repeated 9
'''
def generated_n_char (n, c):
    result = ""
    '''
    Another way to do this will be only writing this
    return n * c
    '''
    for i in range(n):
        result += c    
    return result

'''
Definir un histograma procedimiento() que tome una lista 
de números enteros e imprima un histograma en la pantalla. 10
'''
def procedimiento(values):
    for i in values:
        print( i*"x") 
        
# Print the first repeat letter inside a word 11
def repeat(word):
   
    for i in range(len(word)):
        print(i)
      
        for j in range(i +1, len(word), +1):
            if(word[i] == word[j]):
                return word[i]
            
    return False
# Part 2   
            
# Print the biggest number on a lis 12
def max_in_list(lista):
    mayor=0
    for i in range (len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
    return mayor

# Print the biggest string of a list 13
def longer_String (lista):
    mayor = 0
    largo = ""
    for i in lista:
        #print(i)
        if len(i) > mayor:
            mayor = len(i)
            largo = i
    return largo

'''Wirte a function with 2 input, a list of words and the other only a number n. The 
function should return the words that have more letters that the secon parameter n 14
'''
def filter_words(lista,n):
    result = []
    for i in lista:
        if len(i)>n:
            result.append(i)
            
    return result

'''
Ask to the user to input a string a return  how many upper case are in the list 15
'''
def input_list():
    
   txt = input("Type something to test this out: ")  
   print( "Is this what you just said?", txt)  
   print(txt[1])
   count = 0
   for i in range(len(txt)):
       if txt[i].isupper():
           count +=1       
    
   return count

#Input a bin number and convert to int 16
def binary_hex(num): 
       
    return int(num,2)

#Input a list of numbers and print the ones that are bigger than 20
def filter_ages(lista):
    lista2 = []
    for i in lista:
        if i>20:            
            lista2.append(i)
    return lista2 

#Input a list of names and find which ones start with the second parameter
# Print the biggest string of a list 13
def ini_name(lista, n):
    result = []
    for i in range (len(lista)):
        if lista[i][0] == "A":
            result.append(lista[i])
        print(lista[i][0])
    
    return result 


   
       
        
        
       



    
   
            
        
        




