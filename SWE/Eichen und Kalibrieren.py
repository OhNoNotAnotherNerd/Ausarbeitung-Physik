import numpy as np 
import matplotlib.pyplot as plt
import scipy as sp
import sympy as sy


#Eichungskurve

calibration_temperature = [60.4, 40.5, 0]
calibration_temperature_kelvin = []

for i in range(len(calibration_temperature)):
    add_kelvin = calibration_temperature[i] + 273.15
    calibration_temperature_kelvin.append(add_kelvin)

print(calibration_temperature_kelvin)

calibration_voltage = [2.60, 1.52, -0.01] # ACHTUNG IN MILLIVOLT!!!!!!!

plt.plot(calibration_voltage, calibration_temperature_kelvin, linestyle='-', marker='o')
plt.grid(visible=True, color='black', linewidth=0.5)
plt.title("Eichungskurve")
plt.xlabel("Spannung [mV]")
plt.ylabel("Temparatur [Kelvin]")
plt.show()

def thermo_voltage(a, b, c, T, T_ref):
    U_therm = a * temp_diff**2 + b * temp_diff + c
    temp_diff = (T - T_ref)
    return U_therm

U = thermo_voltage(a=1, b=1 ,c=1 , T=1 , T_ref=1 )


# Noch nicht fertig, wird nur hochgeladen um Merging-Konflikte zu vermeiden. Nächste Aufgabe, Koeffizienten bestimmen, entweder mit Scipy oder mit SciDavis, erstmal essen.