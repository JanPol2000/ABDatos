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

 inicial = -1
 while inicial == -1:
  inicial = int(input('Ingrese cilindro inicial: '))
  if not (inicial >=0 and inicial <= 199):
   inicial = -1
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
  look_and_c_look(peticiones, inicial, bit,1)
 elif opc == 6:
  bit = int(input('Bit de entrada: '))
  look_and_c_look(peticiones, inicial, bit,0)
 
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

def c_scan(peticiones, inicial, bit):
  
  peticiones.append(inicial)

  if bit == 0:
    cilindro_solicitado = [199,0]
    peticiones.sort()
    for x in range(peticiones.index(inicial)):
      cilindro_solicitado.append(peticiones[x])
    for x in range(peticiones.index(inicial),-1,-1):
      peticiones.pop(x)
    cilindro_solicitado.reverse()
    peticiones.reverse()
    for x in range(len(peticiones)):
      cilindro_solicitado.append(peticiones[x])

  elif bit == 1:
    cilindro_solicitado = [0,199]
    peticiones.sort(reverse = True)
    for x in range(peticiones.index(inicial)):
      cilindro_solicitado.append(peticiones[x])
    cilindro_solicitado.reverse()
    for x in range(peticiones.index(inicial),-1,-1):
      peticiones.pop(x)
    peticiones.reverse()
    for x in range(len(peticiones)):
      cilindro_solicitado.append(peticiones[x])

  else:
    print("Fuera de rango")  

  cilindro_actual, tiempo, desplazamiento = [inicial], [0], []

  for x in range(len(cilindro_solicitado)):
    desplazamiento.append(abs(cilindro_actual[x]-cilindro_solicitado[x]))
    cilindro_actual.append(cilindro_solicitado[x])
    tiempo.append(tiempo[x]+desplazamiento[x])

  cilindro_actual.pop(len(cilindro_actual)-1)
  tiempo.pop(len(tiempo)-1)
  promedio = 0
  desp = 0

  print("\n|---------------------------------------------------------------------------|")
  print("|{:^75}|".format("Algoritmo C-SCAN"))
  print("|---------------------------------------------------------------------------|")
  print("| Cilindro Actual | Cilindro Solicitado | Tiempo de Espera | Desplazamiento |")
  print("|---------------------------------------------------------------------------|")
  for x in range(len(cilindro_actual)):
    print("|{:^17}".format(cilindro_actual[x]),end="")
    print("|{:^21}".format(cilindro_solicitado[x]),end="")     
    print("|{:^18}".format(tiempo[x]),end="")
    print("|{:^16}|".format(desplazamiento[x]))
    print("|---------------------------------------------------------------------------|")
    promedio = promedio + tiempo[x]
    desp = desp + desplazamiento[x]
  
  print("")
  print("Desplazamiento total: "+str(desp))
  print("Tiempo de espera promedio: ","{:.2f}".format(promedio/(len(tiempo)-2))+"\n")  

pass

def look_and_c_look(peticiones, inicial, bit, look):
 peticiones.sort()#Ordenar peticiones
 suma_tiempo = 0
 suma_despl = 0
 total = len(peticiones)
 index = 0
 
  
 if bit:  #Si bit es 1, obtener el indice de inicial menor al mayor [inicial, mayor]
  for i, v in enumerate(peticiones):
   if inicial < v:
    index = i
    break
 else: #En otro caso obtener el indice de incial mayor al menor [menor, inicial]
  peticiones = peticiones[::-1]
  for i, v in enumerate(peticiones):
   if inicial > v:
    index = i
    break
 print()

 print('|---------------------------------------------------------------------------|')

 if look: #Si el algoritmo es look
  print('|                               Algoritmo LOOK                              |')
 
 else:# Sino es c-look
  print('|                              Algoritmo C-LOOK                             |')

 print('|---------------------------------------------------------------------------|')
  
 print('| Cilindro Actual | Cilindro solicitado | Tiempo de espera | Desplazamiento |')
  
 print('|---------------------------------------------------------------------------|')

 siguiente = peticiones[index]#peticion siguiente
 tiempo = 0
 desplazamiento = abs(inicial-siguiente)#Calcular el desplazamiento
  
 print('|{:^17}|{:^21}|{:^18}|{:^16}|'.format(inicial, siguiente, 0, desplazamiento))
 print('|---------------------------------------------------------------------------|')
 
 suma_despl = desplazamiento
 for v in peticiones[index+1:]:#para todas las peticiones al indice mas 1, iniciar algoritmo
  inicial = siguiente
  siguiente = v
  tiempo += desplazamiento
  desplazamiento = abs(inicial-siguiente)
  print('|{:^17}|{:^21}|{:^18}|{:^16}|'.format(inicial, siguiente, tiempo, desplazamiento))
  print('|---------------------------------------------------------------------------|')
  suma_tiempo += tiempo
  suma_despl += desplazamiento

 peticiones = peticiones[:index]#extraer las peticiones faltantes
 if look:#si el algoritmo es look, invertir las peticiones
  peticiones = peticiones[::-1]
 for v in peticiones:#Para todas las peticiones, realizar algoritmo
  inicial = siguiente
  siguiente = v
  tiempo += desplazamiento
  desplazamiento = abs(inicial-siguiente)
  print('|{:^17}|{:^21}|{:^18}|{:^16}|'.format(inicial, siguiente, tiempo, desplazamiento))
  print('|---------------------------------------------------------------------------|')
  suma_tiempo += tiempo
  suma_despl += desplazamiento
 
 print()
 print('Desplazamiento total:', suma_despl) 
 print('Tiempo de espera promedio: {:.2f}'.format(suma_tiempo/total))


menu()

