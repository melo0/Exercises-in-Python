while True:
	try:
		x = float(raw_input('podaj wysokosc trojkata: '))
		y = float(raw_input('podaj dlugosc podstawy trojkata: '))
		break
	except ValueError:
		print("podales bledna wartosc")
pole = x*y*1/2
print(pole)
