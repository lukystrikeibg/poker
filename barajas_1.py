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
