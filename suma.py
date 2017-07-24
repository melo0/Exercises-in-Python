while True:
	try:
		a = input('podaj pierwsza liczbe: ')
		b = input('podaj druga liczbe: ')
		break
	except:
		print('nie podales liczb calkowitych!!!')
lista = [a, b]
print('suma tych liczb to: ')
print(str(sum(lista)))
