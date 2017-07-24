import math
while True:
	try:
		ile_lat = int(raw_input('Podaj okres inwestycji w latach: '))
		spk = float(raw_input('podaj stan poczatkowy konta: '))
		p = float(raw_input('Podaj oprocentowanie konta: '))
		break
	except ValueError:
		print('Podaj poprawne wartosci!!!')
kp = spk
for i in range (1, ile_lat+1):
	spk = spk + spk*p/100
print('Kwota na Twoim koncie po ' + str(ile_lat) +' latach, to: ' + str(round(spk, 2)))
print('Jest to ' + str(round(spk/kp, 2)) + ' krotnosc kwoty poczatkowej')
