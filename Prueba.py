## Juan Pablo Mariño 
# 26/02/2024
# Al problema :
"""
Crear una función (Fn2) que genere numeros aleatorios enteros de 1 a 7 
que  reciba de entrada o use otra función (Fn1) que genera números aleatorios enteros entre 1 a 5.
 
Actualización: se elimina el uso del tiempo del sistema como generador de semillas pseudo aleatorias,
y se agrega la comprobación de  15.000 iteraciones para gráficar el histograma de distribución aleatoria.
"""
import random
import matplotlib.pyplot as plt


def FnEntrada():
    """
    Entrega un número aleatorio entero entre 1 y 5
    """
  
    resultado = random.randint(1,5)
    return resultado

def FnSalida7():
    """
    Entrega un número aleatorio entero entre 1 y 7 apartir de los numeros aleatorios de la FnEntrada que arroja valores enteros de 1 a 5.
    """
    while True: # mientras que el comprobador sea menor a 
        Resultado = 5 * (FnEntrada() - 1) + (FnEntrada()- 1) # Genera un rango de valores más grande, en este caso de (0 a 24)
        if Resultado < 21: # se verifica cuando el Rango del Comprobador sea menor a 14 o 21 tiene que ser múltiplo de 7 mayor a 7
            #(depende de la cantidad de números invocados de FnEntrada)       
            Resultado=Resultado % 7 + 1 # Normalización de valores de 1 a 7
            return  round(Resultado)
        

## Comprobación
num=FnSalida7()
print("Numero Aleatorio= ", num)

Lista_R2 = []
for i in range (15000): # para evaluar multiples veces >10.000
    R2=FnSalida7() 
    Lista_R2.append(R2)
#Histograma 
His2=plt.hist(Lista_R2,bins=7) #plot del histograma de salida
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('Lista Función FnSalida7')
plt.show()
