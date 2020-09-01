

# NUMEROS PAR E IMPAR

def hallarParOImpar(number):
	if isinstance(number, int):
		if number % 2 == 0:
			return 'Par'
		else:
			return 'Impar'
	else:
		return 'Debes introducir un numero entero'


numberOfUser = int(input('Indroduce un número, para saber si es par o impar.'))
print(hallarParOImpar(numberOfUser))