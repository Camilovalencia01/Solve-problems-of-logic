#-*-coding:utf-8-*-
'''Construir una función que reciba como parámetro una matriz 4x4 entera y retorne la
posición exacta en donde se encuentre almacenado el mayor número primo'''
matriz = []
def llenar_matriz(elementos1,elementos2):
	lista = [] 
	for a in range(elementos1):
		fila = []
		for b in range(elementos2):
			num = int(raw_input("Introduce un numero: "))
			fila.append(num)
		matriz.append(fila)

	return matriz


def dato_primo(matriz):
	lista_primos = []
	con2 = 0
	mayor = 0
	for c in range(len(matriz)):
		for d in range(len(matriz[c])):
			numero = matriz[c][d]
			con = 0
			for e in range(1,numero + 1):
				if numero % e == 0:
					con += 1

			if con == 2:
				lista_primos.append(numero)
				
	
	if len(lista_primos) == 0:
		return 0

	else:
		for f in range(len(lista_primos)):
			primo = lista_primos[f]
			if primo > mayor:
				mayor = primo

		for g in range(len(matriz)):
			for h in range(len(matriz[g])):
				if matriz[g][h] == mayor:
					pos = g,h

		
		return pos
 			



def main():
	try:
		elementos1 = 4
		elementos2 = 4
		matriz = llenar_matriz(elementos1,elementos2)
		resultado = dato_primo(matriz)
		if resultado > 0:
			print"SOLUCION"
			print"La matriz es"
			print matriz
			print"La pocision exacta del numero primo mayor es"
			print resultado
		else:
			print"SOLUCION"
			print"No hay numeros primos en la matriz"
			print"Introduce otros numeros"
	

	except ValueError:
		print"Error.."

if __name__ == '__main__':
	main()
