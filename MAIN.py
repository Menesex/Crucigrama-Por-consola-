import os
# Tableros de juego
matriz = [
    ['B', 'O', 'O', 'K', ' '],
    ['E', ' ', ' ', 'E', ' '],
    [' ', 'W', 'H', 'Y', ' '],
    [' ', 'H', ' ', ' ', ' '],
    [' ', 'I', ' ', ' ', ' '],
    [' ', 'T', 'R', 'Y', ' '],
    [' ', 'E', ' ', ' ', ' ']
]
matrizVacia = [
    ['B', '🕳', '🕳', '🕳', ' '],
    ['🕳', ' ', ' ', '🕳', ' '],
    [' ', '🕳', '🕳', '🕳', ' '],
    [' ', '🕳', ' ', ' ', ' '],
    [' ', '🕳', ' ', ' ', ' '],
    [' ', '🕳', '🕳', '🕳', ' '],
    [' ', '🕳', ' ', ' ', ' ']
]
ls_palabrasAdivinadas = []
resueltaAux = 0
resueltaStr = '0/6'
estado = '...'
def mostrar_tablero(matriz):
    os.system('cls')
    print('......................................: [ CRUCIGRAMA ] :......................................\n\nBy:\n-Menesex\n-Km1l0\n-3ero')
    print('.........................................: [Pistas] :.........................................\n')
    print("[1]: 💡 It's something you often read for enjoyment or to learn new things                ° (4 Letters | Horizontal)")
    print("[2]: 💡 It's a verb that often indicates existence or action                              ° (2 Letters | Vertical)")
    print("[3]: 💡 It's a small object used to unlock doors or start a vehicle                       ° (3 Letters | Vertical)")
    print("[4]: 💡 It's a word often used to express curiosity or to ask about a reason or cause     ° (3 Letters | Horizontal)")
    print("[5]: 💡 It's a color often associated with purity, cleanliness, and innocence             ° (5 Letters | Vertical)")
    print("[6]: 💡 It's a word that suggests attempting to do something or testing out a possibility ° (3 Letters | Horizontal)\n")
    print('..............................................................................................')
    print('................................: [ CRUCIGRAMA TIEMPO REAL ] :................................\n')   
    for fila in matriz:
        print(' '.join(fila))
    print('\n..................................: ↓ [ INSTRUCCIONES ] ↓ :..................................\n')
    print('💠 1.) Selecciona el [NÚMERO] asignado a la palabra que deseas ingresar. pj. [3]\n💠 2.) Ingresa la palabra correspondiente (sin espacios)\n')
    print(f'===============================: ↓ [  RESPONDE AQUÍ DEBAJO  ] ↓ :================================\nPalabras resueltas ({resueltaStr}) {estado}\n')

def determinarCasilla(casilla):
    global fila, columna, direccion
    while True:
        if casilla == 1:
            fila = 0
            columna = 0
            direccion = 'H'
        elif casilla == 2:
            fila = 0
            columna = 0
            direccion = 'V'
        elif casilla == 3:
            fila = 0
            columna = 3
            direccion = 'V'
        elif casilla == 4:
            fila = 2
            columna = 1
            direccion = 'H'
        elif casilla == 5:
            fila = 2
            columna = 1
            direccion = 'V'
        elif casilla == 6:
            fila = 5
            columna = 1
            direccion = 'H'
        break

def ingresar_respuesta(matriz): #Pedir la palabra al usuario- comprobar si la adivinó o no
    
    #MANEJAR ERROR VALUE ERROR/ try (casilla)
    while True:
        casilla = int(input("Seleccione la palabra [1] - [6]\n➡️ ​​​ "))
        if casilla >= 1 and casilla <=6:
            break
        else:
            input('Por favor ingrese un número valido <ENTER>..')    
            
    while True:
        respuesta = input("Digite la palabra \n➡️​​​  ").upper()
        if respuesta != '':
            break
        else:
            input('Por favor ingrese una palabra valida <ENTER>..')    
    
    determinarCasilla(casilla)
    global fila, columna, direccion
    
    #--------Verificar si la fila y la columna están dentro del rango de la matriz-------------
    while True: 
        if fila < 0 or fila >= len(matriz) or columna < 0 or columna >= len(matriz[0]):
            print("¡Las coordenadas están fuera de los límites de la matriz!")
            fila = int(input("Ingrese el número de fila: "))
            columna = int(input("Ingrese el número de columna: "))
        else:
            break
    #-------------------------------------------------------------------------------------------  

    #--------Verificar si la palabra excede los límites de la matriz--------------
    if direccion == 'H':
        if columna + len(respuesta) > len(matriz[0]):
            input("ERROR: ¡La palabra excede los límites de la matriz en la dirección horizontal!")
            return False
        else:
            palabra = ''.join(matriz[fila][columna+i] for i in range(len(respuesta)))
        
    elif direccion == 'V':
        if fila + len(respuesta) > len(matriz):
            input("ERROR: ¡La palabra excede los límites de la matriz en la dirección vertical!")
            return False
        else:
            palabra = ''.join(matriz[fila+i][columna] for i in range(len(respuesta)))
    #----------------------------------------------------------------------------------------
    
    #Retorna FALSE-TRUE para evaluarse luego en la función juego_crucigrama()
    if palabra == respuesta:
        
        if respuesta not in ls_palabrasAdivinadas:
            ls_palabrasAdivinadas.append(respuesta)
            
            #-------ACTUALIZAR EL TABLERO EN PANTALLA--------------
            if direccion == 'H':
                for i in range(len(respuesta)):
                    matrizVacia[fila][columna+i] = respuesta[i]
            elif direccion == 'V':
                for i in range(len(respuesta)):
                    matrizVacia[fila+i][columna] = respuesta[i]
            #-------ACTUALIZAR EL TABLERO EN PANTALLA--------------
            
            #-------ACTUALIZAR Cantidad de Palabras Resueltas--------------
            global resueltaAux, resueltaStr, estado
            resueltaAux += 1
            resueltaStr = str(resueltaAux)+'/6'
            #-------------FIN (Cantidad de Palabras)-----------------------
            estado = '✅'
            
            return True
        else:
            input("Respuesta repetida 😮 <ENTER>..")
    else:
        estado = '❌'
        input("❌Respuesta incorrecta. Inténtalo de nuevo <ENTER>..")
        return False
def juego_crucigrama(matriz):
    
    total_palabras = 6
    palabras_adivinadas = 0
    
    while palabras_adivinadas < total_palabras:
        mostrar_tablero(matrizVacia)
        if ingresar_respuesta(matriz):
            palabras_adivinadas += 1
        else: #SI ingresar_respuesta() = FALSE - PASS
            pass
    mostrar_tablero(matrizVacia) #ACTUALIZAR EL TABLERO POR ÚLTIMA VEZ        
    print("¡Felicidades! Has completado el crucigrama.\n\n\n\n")            
juego_crucigrama(matriz)
