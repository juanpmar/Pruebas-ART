## Juan Pablo Mariño 
# 22/02/2024
# Al problema :
"""
Crear una función (Fn2) que genere numeros aleatorios enteros de 1 a 7 
que  reciba de entrada o use otra función (Fn1) que genera números aleatorios enteros entre 1 a 5.
"""
import random
import time
import matplotlib.pyplot as plt


def FnEntrada():
    """
    Entrega un número aleatorio entero entre 1 y 5
    """
  
    resultado = random.randint(1,5)
    return resultado

def FnSalida(Entrada): 
    """
    Entrega un número aleatorio entero entre 1 y 7 usando como semilla la entrada de la función 1.
    """
    if (Entrada >=1 and Entrada<=5 ) and isinstance(Entrada,int): #Evalua la entrada entre 1 a 5 y que sea entero.
        Factor=time.time()# Extrae el valor desde el Epoch en el CPU en segundos 
        if Entrada>3:# divide el comportamiento de la salida con base a la entrada
            resultado=((12345+Entrada*Factor*1103515245)%0x7fffffff)%7 # Pseudoaleatorios con base en algoritmos GLC limitado a respuestas de 0 a 6.
            # Toma una semilla como multiplicador del tiempo Epoch que tiene el procesador para generar datos pseudo aleatorios.                
            resultado=round(resultado)+1    
        else: 
            resultado=((Factor+Entrada*1103515245)%0x7fffffff)%7# Pseudoaleatorios con base en algoritmos GLC limitado a respuestas de 0 a 6.
            # Toma una semilla como Sumador del tiempo Epoch que tiene el procesador para generar datos pseudo aleatorios.                
            resultado=round(resultado)+1  
        return resultado
    else :                
        print("No válido: ", Entrada)
        return Entrada
        

## Comprobación
"""
R1=FnEntrada()
#R1=R1 ## Para modificar la entrada.
R2=FnSalida(R1)
print("Entrada :",R1," Salida: ", R2)
"""
