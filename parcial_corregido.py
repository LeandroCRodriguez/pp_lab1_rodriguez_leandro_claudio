import json
import re


#Estudiante Leandro Claudio Rodríguez

# Examen parcial 

# Escribe un programa en Python que cargue la información de los jugadores del Dream Team desde un archivo
# JSON y realice las siguientes tareas, teniendo en cuenta que cada una de ellas deberá de ser realizada 
# por una función diferente:

############################################################################################
                                  #ACÁ EMPIEZA MI MAIN

def main():
    '''
    Es la función principal del programa
    No recibe nada
    No devuelve nada
    '''
    lista_jugadores = leer_archivo(ruta_json)
    opcion = validar_opcion()
    while opcion != -1:
        ejecutar_opcion(lista_jugadores, opcion)  
        opcion = validar_opcion()



    ##########################################################################################

          #ACÁ ESTÁN LAS FUNCIONES PARA LAS OPCIONES QUE ELIGIÓ EL USUARIO

      

# 1 Mostrar la lista de todos los jugadores del Dream Team. Con el formato:
# Nombre Jugador - Posición. Ejemplo:
# Michael Jordan - Escolta

def mostrar_jugadores(lista:list):
    '''
    Muestra una lista de jugadores
    Recibe una lista
    Devuelve una lista
    '''
    for jugador in lista:
        print("{0}-{1}".format(jugador["nombre"], jugador["posicion"]))         


# 2 Permitir al usuario seleccionar un jugador por su índice y mostrar sus estadísticas completas, 
# incluyendo temporadas jugadas, puntos totales, promedio de puntos por partido, rebotes totales,
# promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, robos totales,
# bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.



def mostrar_estadísticas_logros(lista:list, clave:str):   
    lista_estadisticas = [] 
    mostrar_jugadores_con_indice(lista)
    numero_ingresado_str = input("ingresá el número de jugador: ")
    if numero_ingresado_str.isdigit():
        numero_ingresado_int = int(numero_ingresado_str)
        if numero_ingresado_int <= len(lista) and numero_ingresado_int >= 0: 
            lista_estadisticas.append(lista[numero_ingresado_int]["nombre"])
            lista_estadisticas.append(lista[numero_ingresado_int][clave])
        else:
            return -1  
    else:
        return -1 
    return lista_estadisticas          
            

# 3 Después de mostrar las estadísticas de un jugador seleccionado por el usuario, permite al usuario 
# guardar las estadísticas de ese jugador en un archivo CSV. El archivo CSV debe contener los siguientes
# campos: nombre, posición, temporadas, puntos totales, promedio de puntos por partido, rebotes totales,
# promedio de rebotes por partido, asistencias totales, promedio de asistencias por partido, robos totales, 
# bloqueos totales, porcentaje de tiros de campo, porcentaje de tiros libres y porcentaje de tiros triples.

ruta_csv = "C:\\Users\\Lean\\Documents\\UTN\\UTN programación 1 Python\\parcial_1\\estadísticas_jugador.csv"


def guardar_csv(ruta_csv:str,estadisticas:list):
    '''
    Guarda en un csv el diccionario donde se encuentra el jugador
    Recibe un dict
    No retorna
    '''
    encabezados = estadisticas.keys()
    valores = estadisticas.values()
    with open(ruta_csv, 'w') as archivo_csv:
        archivo_csv.write(','.join(encabezados) + '\n')
        archivo_csv.write(','.join(map(str, valores)) + '\n')



# 4 Permitir al usuario buscar un jugador por su nombre y mostrar sus logros, como campeonatos de la NBA, 
# participaciones en el All-Star y pertenencia al Salón de la Fama del Baloncesto, etc.

def mostrar_logros_jugador(lista:list):
    '''
    Muestra los logros de un jugador seleccionado por el usuario
    Recibe una lista de jugadores
    Devuelve un diccionario con los logros del jugador o un -1 en caso incorrecto
    '''
    mostrar_jugadores_con_indice(lista)
    nombre_jugador_ingresado = input("Ingresa el nombre del jugador: ")
    nombre_casteado = es_solo_texto(nombre_jugador_ingresado)
    if nombre_casteado == True:
        for jugador in lista:
            nombre_jugador = jugador["nombre"]
            if nombre_jugador_ingresado == nombre_jugador:
                return jugador["logros"]          
        return "no se encontró el nombre"
    else:
        return "No has ingresado un nombre válido"

# 5 Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team,
#  ordenado por nombre de manera ascendente.

def calcula_muestra_promedio_puntos_por_partido_ordenado_por_nombre(lista:list):
    '''
    Calcula y muestra el promedio de los puntos por partido de todo el equipo
    Recibe una lista de jugadores
    No devuelve 
    '''
    promedio = calcular_promedio_puntos_por_partido(lista)
    lista_resultante = []
    lista_ordenada = nuevo_ordenar_equipo_por_clave(lista,"estadisticas","promedio_puntos_por_partido")
    for jugador in lista_ordenada:
        resultado = "{0}-{1}".format(jugador["nombre"], jugador["estadisticas"]["promedio_puntos_por_partido"])
        lista_resultante.append(resultado)
    print("La lista de puntos por partido de cada jugador es:")
    print(lista_resultante)
    print("Y el promedio es: {0}".format(promedio))




# 6 Permitir al usuario ingresar el nombre de un jugador y mostrar si ese jugador es miembro del 
#   Salón de la Fama del Baloncesto.


def mostrar_logro_jugador(lista:list):
    '''
    Muestra los jugadores y devuelve si es miembro o no del salón de la fama del Baloncesto
    Recibe una lista de jugadores
    Devuelve un string según el caso.
    '''
    mostrar_jugadores_con_indice(lista)
    nombre_jugador_ingresado = input("Ingresa el nombre del jugador: ")
    nombre_casteado = es_solo_texto(nombre_jugador_ingresado)
    if nombre_casteado == True:
        for jugador in lista:
            if jugador["nombre"] == nombre_jugador_ingresado:
                if jugador["logros"][-1] == "Miembro del Salon de la Fama del Baloncesto":
                    return "El jugador {0} es Miembro del Salon de la Fama del Baloncesto".format(jugador["nombre"])
                else:
                    return "El jugador {0} no es Miembro del Salon de la Fama del Baloncesto".format(jugador["nombre"])
        return "El jugador no está dentro del equipo"
    else:            
        return "No has ingresado un nombre"

# 7 Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.
# 8 Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.
# 9 Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.
# 13 Calcular y mostrar el jugador con la mayor cantidad de robos totales.
# 14 Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.
# 17 Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos
# 19 Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas



def calcular_max_clave(lista:list, clave_1:str, clave_2:str):
    '''
    Calcula el máximo jugador según la clave
    Recibe una lista de jugadores y dos claves
    Devuelve un string
    '''
    max_clave = 0 #Acordarse de inicializar la variable fuera del for
    for indice in range(1,len(lista)):
        if(lista[indice][clave_1][clave_2] > max_clave):                
            max_clave = lista[indice][clave_1][clave_2]
            nombre_jugador = lista[indice]["nombre"]
    resultado = "Jugador {0} mayor cantidad de {1}: {2}".format(nombre_jugador, clave_2, max_clave)  
    return resultado

def calcular_max_logros(lista:list):
    '''
    Calcula el máximo jugador según la clave
    Recibe una lista de jugadores y dos claves
    Devuelve un string
    '''
    max_clave = 0 #Acordarse de inicializar la variable fuera del for
    for indice in range(len(lista)):
        if(len(lista[indice]["logros"]) > max_clave):                
            max_clave = len(lista[indice]["logros"])
            nombre_jugador = lista[indice]["nombre"]
    resultado = "Jugador con mayor cantidad de logros: {0} {1}".format(nombre_jugador, max_clave)  
    return resultado



# 10 Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más puntos por
#  partido que ese valor.

# 11 Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más rebotes por
#  partido que ese valor.

# 12 Permitir al usuario ingresar un valor y mostrar los jugadores que han promediado más asistencias
#  por partido que ese valor.

# 15 Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje
#  de tiros libres superior a ese valor.

# 18 Permitir al usuario ingresar un valor y mostrar los jugadores que hayan tenido un porcentaje 
# de tiros triples superior a ese valor.


def mostrar_mayor_promedio_y_porcentaje_al_valor_ingresado(lista:list, clave:str):
    '''
    Muestra jugadores que superan el valor ingresado por el usuario, según la clave
    Recibe una lista de jugadores
    Devuelve una lista con el nombre del jugador y un valor, dependiendo de la clave ingresada
    '''
    lista_jugadores = []
    numero_ingresado = input("Ingrese un número: ")
    numero_decimal = es_decimal(numero_ingresado)
    if numero_decimal:
        numero_valido = float(numero_ingresado)
    elif numero_ingresado.isdigit():
        numero_valido = int(numero_ingresado)
    else:
        return -1
    for jugador in lista:
        if jugador["estadisticas"][clave] > numero_valido:
            lista_jugadores.append(jugador["nombre"])
            lista_jugadores.append(jugador["estadisticas"][clave]) 
    return lista_jugadores
    

# 16 Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con 
# la menor cantidad de puntos por partido.

def calcula_y_muestra_promedio_puntos_por_partido_sacando_al_minimo(lista:list):
    '''
    Calcula el promedio de puntos por partido sacando al jugador con el puntaje más bajo
    Recibe una lista
    Devuelve un string
    '''
    nueva_lista = []
    lista_ordenada = nuevo_ordenar_equipo_por_clave(lista,"estadisticas","promedio_puntos_por_partido")
    for jugador in range(1, len(lista_ordenada)):
        nueva_lista.append(lista_ordenada[jugador])
    promedio = calcular_promedio_puntos_por_partido(nueva_lista)
    print("El promedio, sacando al jugador más bajo de puntos por partido es: {0} ".format(promedio))

def nuevo_ordenar_equipo_por_clave(lista:list,clave_1,clave_2):
    '''
    Ordena una lista de jugadores según la clave
    Recibe una lista de jugadores y dos claves
    Devuelve la lista ordenada
    '''
    rango_a = len(lista)
    flag_swap = True
    while(flag_swap):
        flag_swap = False
        rango_a = rango_a - 1
        for indice_A in range(rango_a):
                if  lista[indice_A][clave_1][clave_2] > lista[indice_A+1][clave_1][clave_2]:
                    lista[indice_A],lista[indice_A+1] = lista[indice_A+1],lista[indice_A]
                    flag_swap = True
    return lista


# 20 Permitir al usuario ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha,
#  que hayan tenido un porcentaje de tiros de campo superior a ese valor.

def muestra_porcentaje_de_tiros_de_campo_ordenado_por_posicion(lista:list):
    lista_jugadores = []
    rango_a = len(lista)
    flag_swap = True
    while(flag_swap):
        flag_swap = False
        rango_a = rango_a - 1
        for indice_A in range(rango_a):
                if  lista[indice_A]["posicion"] > lista[indice_A+1]["posicion"]:
                    lista[indice_A],lista[indice_A+1] = lista[indice_A+1],lista[indice_A]
                    flag_swap = True
    numero_ingresado = input("Ingrese un número: ")
    numero_decimal = es_decimal(numero_ingresado)
    if numero_decimal:
        numero_valido = float(numero_ingresado)
    elif numero_ingresado.isdigit():
        numero_valido = int(numero_ingresado)
    else:
        return -1
    for jugador in lista:
        if jugador["estadisticas"]["porcentaje_tiros_de_campo"] > numero_valido:
            lista_jugadores.append(jugador["nombre"])
            lista_jugadores.append(jugador["posicion"])
            lista_jugadores.append(jugador["estadisticas"]["porcentaje_tiros_de_campo"])
    print(lista_jugadores)


# Recuerda utilizar el archivo JSON proporcionado para cargar la información de los jugadores. 
# Puedes utilizar las bibliotecas estándar de Python, como json, para leer el archivo JSON y 
# procesar la información.

# Todas las funciones deberán estar correctamente documentadas. 
# Las funciones y las variables deberán estar claramente nombradas y seguir las reglas de estilos
# utilizadas en la materia. 
# Todos los puntos deberán poder ser accedidos a través de un menú de opciones.

# 23) Bonus 

# Calcular de cada jugador cuál es su posición en cada uno de los siguientes ranking
# Puntos 
# Rebotes 
# Asistencias 
# Robos

# Exportar a csv.



###########################################################################################
                  #ACÁ HAY FUNCIONES GLOBALES Y FUNCIONES 


def mostrar_jugadores_con_indice(lista:list):
    '''
    Muestra todos los jugadores enumerandolos de 0 a 12
    Recibe una lista de diccionarios
    Devuelve un diccionario o un -1 en caso incorrecto
    '''
    contador = 0
    for jugador in lista:
        print("{0} - {1}".format(contador, jugador["nombre"]))
        contador += 1

def calcular_promedio_puntos_por_partido(lista:list):
    '''
    Calcula el promedio de los puntos por partido
    recibe una lista de jugadores
    Devuelve el promedio
    '''
    suma = 0
    for jugador in lista:
       suma = suma + jugador["estadisticas"]["promedio_puntos_por_partido"]
       promedio = suma / len(lista)
    return promedio


def es_solo_texto(solo_texto:str):
    '''
    Verifica que todos los caracteres sean alfabéticos, se permite espacio
    Recibe un texto
    Devuelve un true o false
    '''
    # print(re.search(r"^([a-zA-Z])+$",solo_texto))
    if re.search(r"(^[a-zA-Z ]+$)",solo_texto):        
        return True
    else:
        return False
    
def es_decimal(num_decimal:str):
    '''
    Verifica que el número que le llega es decimal o no
    Recibe un string
    Devuelve True o false 
    '''
    numero_1 = re.search(r"^([0-9]+)\.([0-9]+$)",num_decimal)
    if(numero_1):
        return True               
    else:
        return False 


def imprimir_dato(texto:str):
    '''
    Imprime un texto string por pantalla
    Recibe un string
    no devuelve 
    '''
    print(texto)

ruta_json = "C:\\Users\\Lean\\Documents\\UTN\\UTN programación 1 Python\\parcial_1\\dt.json"
def leer_archivo(ruta:str)->list:
    '''
    Lee un archivo json
    recibe una ruta
    Devuelve una lista 
    '''
    lista_jugadores=[]
    with open(ruta, 'r') as f:
        diccionario = json.load(f) 
        lista_jugadores = diccionario["jugadores"] 
    return lista_jugadores


def imprimir_menu():
    mensaje = """
    Elija la opción del menú que quiera ejercutar...
    Opción 1 Muestra la lista de todos los jugadores del Dream Team.
    Opción 2 Seleccione un jugador por su número para acceder a sus estadísticas completas.
    Opción 3 Guarde las estadísticas de ese jugador (pasar primero por opción 2).
    Opción 4 Busque un jugador por su nombre para ver sus logros.
    Opción 5 Mostrar el promedio de puntos por partido de todo el equipo del Dream Team.
    opción 6 Ingresar el nombre de un jugador para saber si ese jugador es miembro del Salón de la Fama del Baloncesto.
    opción 7 Mostrar el jugador con la mayor cantidad de rebotes totales.
    opción 8 Mostrar el jugador con el mayor porcentaje de tiros de campo.
    opción 9 Mostrar el jugador con la mayor cantidad de asistencias totales.
    opción 10 Ingresar un valor para mostrar los jugadores que han promediado más puntos por partido que ese valor.
    opción 11 Ingresar un valor para mostrar los jugadores que han promediado más rebotes por partido que ese valor.
    opción 12 Ingresar un valor para mostrar los jugadores que han promediado más asistencias por partido que ese valor..
    opción 13 Mostrar el jugador con la mayor cantidad de robos totales
    opción 14 Mostrar el jugador con la mayor cantidad de bloqueos totales
    opción 15 Ingresar un valor para mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a ese valor.
    opción 16 mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.
    opción 17 Mostrar el jugador con la mayor cantidad de logros obtenidos
    opción 18 Ingresar un valor para mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a ese valor.
    opción 19 Mostrar el jugador con la mayor cantidad de temporadas jugadas
    opción 20 Ingresar un valor para mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor.
    opción bonus
    """
    imprimir_dato(mensaje)

def validar_opcion():
    '''
    Imprime el menú y valida una opción desde el 1 hasta el 20
    No recibe nada
    Devuelve la opción o un -1 en caso incorrecto
    '''
    imprimir_menu()
    opcion = input()
    opcion_valida = re.match("^[1-9]|1[0-9]|20$", opcion)
    if opcion_valida:
        return opcion 
    else:
        return -1
    
def ejecutar_opcion(lista_jugadores:list, opcion):
    if opcion == "1":
        mostrar_jugadores(lista_jugadores)
           
    elif opcion == "2":   
        estadisticas_jugador = mostrar_estadísticas_logros(lista_jugadores, "estadisticas")        
        imprimir_dato(estadisticas_jugador)

    elif opcion == "3":
        print(estadisticas_jugador)
        guardar_csv(ruta_csv, estadisticas_jugador)

    elif opcion == "4":      
        logros_jugador = mostrar_logros_jugador(lista_jugadores)
        imprimir_dato(logros_jugador)

    elif opcion == "5":  
        calcula_muestra_promedio_puntos_por_partido_ordenado_por_nombre(lista_jugadores)

    elif opcion == "6":
        logros_jugador =  mostrar_logro_jugador(lista_jugadores)
        imprimir_dato(logros_jugador)

    elif opcion == "7":
        resultado = calcular_max_clave(lista_jugadores,"estadisticas","rebotes_totales")
        imprimir_dato(resultado)

    elif opcion == "8":
        resultado = calcular_max_clave(lista_jugadores,"estadisticas","porcentaje_tiros_de_campo")            
        imprimir_dato(resultado)

    elif opcion == "9":
        resultado = calcular_max_clave(lista_jugadores,"estadisticas","asistencias_totales")
        imprimir_dato(resultado)

    elif opcion == "10":
        lista_promedio = mostrar_mayor_promedio_y_porcentaje_al_valor_ingresado(lista_jugadores,"promedio_puntos_por_partido")
        imprimir_dato(lista_promedio)

    elif opcion == "11":
        lista_promedio = mostrar_mayor_promedio_y_porcentaje_al_valor_ingresado(lista_jugadores,"promedio_rebotes_por_partido")
        imprimir_dato(lista_promedio)

    elif opcion == "12":
        lista_promedio = mostrar_mayor_promedio_y_porcentaje_al_valor_ingresado(lista_jugadores,"promedio_asistencias_por_partido")
        imprimir_dato(lista_promedio)    

    elif opcion == "13":
        resultado = calcular_max_clave(lista_jugadores,"estadisticas","robos_totales")
        imprimir_dato(resultado)

    elif opcion == "14":
        resultado = calcular_max_clave(lista_jugadores,"estadisticas","bloqueos_totales")
        imprimir_dato(resultado)
        
    elif opcion == "15":
        lista_porcentaje = mostrar_mayor_promedio_y_porcentaje_al_valor_ingresado(lista_jugadores,"porcentaje_tiros_libres")
        imprimir_dato(lista_porcentaje)            


    elif opcion == "16":
        print("if 16")
        calcula_y_muestra_promedio_puntos_por_partido_sacando_al_minimo(lista_jugadores)

    elif opcion == "17":
        print("if 17")
        jugador_mayor_logros = calcular_max_logros(lista_jugadores)
        imprimir_dato(jugador_mayor_logros)

    elif opcion == "18":
        print("if 18")
        lista_promedio = mostrar_mayor_promedio_y_porcentaje_al_valor_ingresado(lista_jugadores,"porcentaje_tiros_triples")
        imprimir_dato(lista_promedio)                        

    elif opcion == "19":
        print("if 19")
        resultado = calcular_max_clave(lista_jugadores,"estadisticas","temporadas")
        imprimir_dato(resultado)
    elif opcion == "20":
        print("if 20")
        lista_ordenada = muestra_porcentaje_de_tiros_de_campo_ordenado_por_posicion(lista_jugadores)
        imprimir_dato(lista_ordenada)

    else:
        print(opcion)

main()