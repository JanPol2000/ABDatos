def menu():
 n = int(input('Numero de peticiones: '))
 peticiones = []
 i = 0
 print('Ingrese las peticiones en un rango de 0-199')
 while i < n:
  p = int(input('Peticion {0}: '.format(i+1)))
  if p >= 0 and p <= 199:
   peticiones.append(p)
   i += 1
  else:
   print('Rango incorrecto')

 inicial = 0
 while inicial == 0:
  inicial = int(input('Ingrese cilindro inicial: '))
  if not (inicial >=0 and inicial <= 199):
   inicial = 0 
   print('Rango incorrecto')

 print('ALGORITMOS')
 print('[1] FCFS')
 print('[2] SSTF')
 print('[3] SCAN')
 print('[4] C-SCAN')
 print('[5] LOOK')
 print('[6] C-LOOK')
 opc = int(input('Seleccione una opcion: '))
 if opc == 1:
  fcfs(peticiones, inicial)
 elif opc == 2:
  sstf(peticiones, inicial)
 elif opc == 3:
  bit = int(input('Bit de entrada: '))
  scan(peticiones, inicial, bit)
 elif opc == 4:
  bit = int(input('Bit de entrada: '))
  c_scan(peticiones, inicial, bit)
 elif opc == 5:
  bit = int(input('Bit de entrada: '))
  look(peticiones, inicial, bit)
 elif opc == 6:
  bit = int(input('Bit de entrada: '))
  c_look(peticiones, inicial, bit)
 
def fcfs(peticiones, inicial):
  #peticiones -> lista de numeros enteros
  #inicial -> numero entero
  #Mostrar tabla
  contador = 0 #Contador para saber en que posicion estamos del arreglo
  tiempoEspera = 0 #Tiempo de espera de cada disco
  tiempoEsperaTotal = 0 #Tiempo de espera total
  desplazamiento = 0 #Desplazamiento de cada uno de los discos
  desplazamientoTotal = 0 #Desplazamiento total

  print()
  print('|---------------------------------------------------------------------------|')
  print('|                               Algoritmo FCFS                              |')
  print('|---------------------------------------------------------------------------|')
  print('| Cilindro Actual | Cilindro solicitado | Tiempo de espera | Desplazamiento |')
  print('|---------------------------------------------------------------------------|')

  while contador != len(peticiones): #Ciclo para realizar todos los procesos necesarios
    tiempoEspera+=desplazamiento #Calculamos el tiempo de espera
    desplazamiento=abs(inicial-peticiones[contador]) #Calculamos el desplazamiento realizado
    print('|{:^17}|{:^21}|{:^18}|{:^16}|'.format(inicial, peticiones[contador], tiempoEspera, desplazamiento)) #Mostramos los resultados
    print('|---------------------------------------------------------------------------|')
    inicial=peticiones[contador] #Asignamos el nuevo valor actual
    desplazamientoTotal+=desplazamiento #Calculamos el desplazamiento total
    tiempoEsperaTotal+=tiempoEspera #Calculamos el tiempo de espera total
    contador+=1 #Aumentamos el contador
 
  print()
  print('Desplazamiento total: {}'.format(desplazamientoTotal)) #Imprimir desplazamiento
  print('Tiempo de espera promedio: {}'.format(tiempoEsperaTotal/len(peticiones))) #Imprimir tiempo de espera promedio
  pass

def sstf(peticiones, inicial):
  #peticiones -> lista de numeros enteros
  #inicial -> numero entero 
  contador = 0 #Contador para saber en que posicion estamos del arreglo
  punteroMenor = 0 #Puntero para indicar el numero menor al disco actual
  punteroMayor = 0 #Puntero para indicar el numero mayor al actual
  diferenciaMenor = 0 #Sabemos la diferencia del actual con el menor
  diferenciaMayor = 0 #Sabemos la diferencia del actual con el mayor
  tiempoEspera = 0 #Tiempo de espera de cada disco
  tiempoEsperaTotal = 0 #Tiempo de espera total
  desplazamiento = 0 #Desplazamiento de cada uno de los discos
  desplazamientoTotal = 0 #Desplazamiento total
  solicitado = 0 #Cilindro solicitado
  ubicado = True #Para tener todos los datos ubicados
  x = 0 #Solamente para ubicar nuestro inicial y los punteros
  ordenados = sorted(peticiones) #Datos ordenados

  while ubicado != False: #Ciclo para dar los valores de los punteros
    if  x == len(peticiones):
      punteroMenor = x-1
      punteroMayor = x
      ubicado = False
    elif inicial < ordenados[x]:
      punteroMenor = x-1
      punteroMayor = x
      ubicado = False
    else:
      x+=1

  #Mostrar tabla
  print()
  print('|---------------------------------------------------------------------------|')
  print('|                               Algoritmo SSTF                              |')
  print('|---------------------------------------------------------------------------|')
  print('| Cilindro Actual | Cilindro solicitado | Tiempo de espera | Desplazamiento |')
  print('|---------------------------------------------------------------------------|')

  while contador != len(peticiones): #Ciclo para realizar todos los procesos necesarios

    if punteroMenor != -1: #Decision para obtener las diferencias de cada uno
      diferenciaMenor = abs(inicial-ordenados[punteroMenor])
    if punteroMayor != len(peticiones):
      diferenciaMayor = abs(inicial-ordenados[punteroMayor])

    if diferenciaMenor < diferenciaMayor and punteroMenor != -1: #Decision para obtener el ciclindro siguiente
      solicitado = ordenados[punteroMenor]
      punteroMenor -= 1
    elif punteroMayor != len(peticiones):
      solicitado = ordenados[punteroMayor]
      punteroMayor += 1
    else:
      solicitado = ordenados[punteroMenor]
      punteroMenor -= 1
 
    tiempoEspera+=desplazamiento #Calculamos el tiempo de espera
    desplazamiento=abs(inicial-solicitado) #Calculamos el desplazamiento realizado
    print('|{:^17}|{:^21}|{:^18}|{:^16}|'.format(inicial, solicitado, tiempoEspera, desplazamiento)) #Mostramos los resultados
    print('|---------------------------------------------------------------------------|')
    inicial=solicitado #Asignamos el nuevo valor actual
    desplazamientoTotal+=desplazamiento #Calculamos el desplazamiento total
    tiempoEsperaTotal+=tiempoEspera #Calculamos el tiempo de espera total
    contador+=1 #Aumentamos el contador
    
  print()
  print('Desplazamiento total: {0}'.format(desplazamientoTotal)) #Imprimir desplazamiento
  print('Tiempo de espera promedio: {0}'.format(tiempoEsperaTotal/len(peticiones))) #Imprimir tiempo de espera promedio
  pass

def scan(peticiones, inicial, bit):
 #peticiones -> lista de numeros enteros
 #inicial -> numero entero 
 #bit -> numero entero
 #Mostrar tabla
 #Imprimir desplazamiento
 #Imprimir tiempo de espera promedio
 pass

def c_scan(peticiones, inicial, bit):
 #peticiones -> lista de numeros enteros
 #inicial -> numero entero 
 #bit -> numero entero
 #Mostrar tabla
 #Imprimir desplazamiento
 #Imprimir tiempo de espera promedio
 pass

def look(peticiones, inicial, bit):
 #peticiones -> lista de numeros enteros
 #inicial -> numero entero 
 #bit -> numero entero
 #Mostrar tabla
 #Imprimir desplazamiento
 #Imprimir tiempo de espera promedio
 pass

def c_look(peticiones, inicial, bit):
 #peticiones -> lista de numeros enteros
 #inicial -> numero entero 
 #bit -> numero entero
 #Mostrar tabla
 #Imprimir desplazamiento
 #Imprimir tiempo de espera promedio
 pass


menu()

