import copy

class Nodo:
    def __init__ (self,valor): #Ajustar el valor de la puntuacion
        self.valor=valor
        self.hijos=[]
        self.puntuacion=0

class Arbol:
    def __init__ (self):
        self.raiz=None

    def agregar(self,nodo,jugador): #Agrega un nodo al arbol
        if self.raiz==None:
            self.raiz=nodo
            posibles_jugadas(self.raiz,jugador)
            puntuar(self.raiz,jugador)

def es_ganador(tablero, jugador):
        # Revisa las filas
        for fila in tablero:
            if fila == [jugador, jugador, jugador]:
                return True
        
        # Revisa las columnas
        for i in range(3):
            if tablero[0][i] == jugador and tablero[1][i] == jugador and tablero[2][i] == jugador:
                return True
        
        # Revisa las diagonales
        if tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador:
            return True
        if tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == jugador:
            return True
        
        # Si no hay ganador, devuelve False
        return False

def posibles_jugadas(nodo, jugador):
        jugadas = []
        for i in range(3):
            for j in range(3):
                if nodo.valor[i][j] == 0:
                    nuevo_nodo = copy.deepcopy(nodo)
                    nuevo_nodo.valor[i][j] = jugador
                    jugadas.append(nuevo_nodo)
                    nodo.hijos = jugadas

def puntuar(nodo,jugador):
        for a in nodo.hijos:
            posibles_jugadas(a,jugador)
            if es_ganador(a.valor,jugador)==True:
                 a.puntuacion=10
            else:
                for b in a.hijos:
                    posibles_jugadas(b,3-jugador)
                    if es_ganador(b.valor,3-jugador)==True:
                        a.puntuacion=-10
                        break
                    else:
                        for c in b.hijos:
                            posibles_jugadas(c,jugador)
                            if es_ganador(c.valor,jugador)==True:
                                a.puntuacion=5
                                break
                            else:
                                for d in c.hijos:
                                    posibles_jugadas(d,3-jugador)
                                    if es_ganador(d.valor,3-jugador)==True:
                                        a.puntuacion=-5

def juguemos(nodo, jugador):
    if es_ganador(nodo.valor, jugador):
        print("El tablero ha finalizado")
        return
    print("------------------")
    print("Tablero actual: ")
    for x in nodo.valor:
        print([("X" if cell == 2 else "O" if cell == 1 else "-") for cell in x])
    print("------------------")
    print("Jugadas sugeridas:")
    print("------------------")
    for i in nodo.hijos:
        print("Puntuación: " + str(i.puntuacion))
        for x in i.valor:
            print([("X" if cell == 2 else "O" if cell == 1 else "-") for cell in x])
        print("------------------")
    while True:
        Fila = input("Ingrese la fila: ")
        Columna = input("Ingrese la columna: ")
        if nodo.valor[int(Fila)][int(Columna)] == 0 and int(Fila) < 3 and int(Columna) < 3:
            nodo.valor[int(Fila)][int(Columna)] = jugador
            break
        else:
            print("Posición no válida")
    if es_ganador(nodo.valor, jugador):
        print("Ganaste")
        return
    else:
        posibles_jugadas(nodo, 3 - jugador)
        nodo_seleccionado = min(nodo.hijos, key=lambda x: x.puntuacion)
        nodo.valor = nodo_seleccionado.valor
        nodo.hijos = []
        posibles_jugadas(nodo, jugador)
        puntuar(nodo, jugador)
        juguemos(nodo, jugador)

tableros = [[2, 1, 1], 
            [2, 0, 0], 
            [0, 0, 0]]   
 
tictactoe = Arbol()
tictactoe.agregar(Nodo(tableros),2)

juguemos(tictactoe.raiz,2)