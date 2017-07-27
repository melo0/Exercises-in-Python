import math
st = 0.0
celciusze = 0.0
fahrenheit = 0.0
kelvin = 0.0
st = float(input("podaj tęperaturę na zewnątrz: "))
print("Celcjusza - 1")
print("Kelvin - 2")
print("Fahrenheit - 3")
unit = int(input("w jakiej jednostce jest podana temeperatura?: "))
if unit==1:
	celciusze = st
	kelvin = st + 273.15
	fahrenheit= 9.0 / 5.0 * st + 32.0
elif unit == 2:
	celciusze = st - 273.15
	kelvin = st
	fahrenheit = (st - 273.15) * 1.8 + 32.0
else:
	celciusze = (st - 32.0) * (5 / 9.0)
	kelvin = (st - 32.0) / 1.8 + 273.15
	fahrenheit = st
print(str(celciusze)+" C")
print(str(kelvin)+" K")
print(str(fahrenheit)+" F")
