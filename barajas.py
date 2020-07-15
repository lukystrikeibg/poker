
import random
import collections
PALOS =['espada ', 'corazon', 'rombo' , 'trebol']
VALORES=['as','2','3','4','5','6','7 ','8', '9',' 10', 'j', 'q', ' k']

//cambio de prueba
// otra prueba




    probabilidad_par = pares / intentos
    print(f' la probabilidad de obtener un par en una mano de {tamano_mano} barajas es {probabilidad_par}')



if __name__ == '__main__':
    tamano_mano= int(input('De cuantas barajas sera la mano:  '))
    intentos= int (input(' ¿cuantos intetos para calcular probabilidad?: '))
    main (tamano_mano, intentos)
