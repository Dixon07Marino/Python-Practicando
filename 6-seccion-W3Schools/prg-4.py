# Python datetime module

import datetime

fecha = datetime.datetime.now()

print(fecha)

print(fecha.year)
print(fecha.strftime("%A"))

fecha2 = datetime.datetime(2020, 2, 11)
print(fecha2.strftime("%B"))

# %A, %a para el día | %B, %b para el mes | %d es el día pero en número


