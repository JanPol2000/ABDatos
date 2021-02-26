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
 #Imprimir desplazamiento
 #Imprimir tiempo de espera promedio
 pass

def sstf(peticiones, inicial):
 #peticiones -> lista de numeros enteros
 #inicial -> numero entero 
 #Mostrar tabla
 #Imprimir desplazamiento
 #Imprimir tiempo de espera promedio
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

