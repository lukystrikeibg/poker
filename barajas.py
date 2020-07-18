// esta es  version de prueba
import random
import collections
PALOS =['espada ', 'corazon', 'rombo' , 'trebol']
VALORES=['as','2','3','4','5','6','7 ','8', '9',' 10', 'j', 'q', ' k']

def crear_baraja():
    barajas=[]
    for palo in PALOS:
      for valor in VALORES:
            barajas.append ((palo , valor))

    return barajas



def main (tamano_mano, intento):
    barajas = crear_baraja()

    manos = []

    for _ in range (intentos):
        mano = obtener_mano(barajas,tamano_mano)
        manos.append(mano)

    pares = 0

    for mano in manos:
        valores=[]
        for carta in mano:
            valores.append(carta[1])


        counter= dict(collections.Counter(valores))
        for val in counter.values():
            if val==3:
                pares +=1
                break




    probabilidad_par = pares / intentos
    print(f' la probabilidad de obtener un par en una mano de {tamano_mano} barajas es {probabilidad_par}')



if __name__ == '__main__':
    tamano_mano= int(input('De cuantas barajas sera la mano:  '))
    intentos= int (input(' ¿cuantos intetos para calcular probabilidad?: '))
    main (tamano_mano, intentos)
