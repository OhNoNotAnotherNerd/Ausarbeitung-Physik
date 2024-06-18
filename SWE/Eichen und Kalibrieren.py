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

calibration_voltage = [2.60*10**-3, 1.52*10**-3, -0.01*10**-3] # ACHTUNG IN MILLIVOLT!!!!!!!



def thermo_voltage(a, b, c, T, T_ref,):
    temp_diff = (T - T_ref)
    U_therm = a * temp_diff**2 + b * temp_diff + c
    return U_therm

U = thermo_voltage(a=1, b=1 ,c=1 , T=1 , T_ref=2,  )


# Noch nicht fertig, wird nur hochgeladen um Merging-Konflikte zu vermeiden. Nächste Aufgabe, Koeffizienten bestimmen, entweder mit Scipy oder mit SciDavis, erstmal essen.

A = np.array([
    [60.4**2, 60.4],
    [40.5**2, 40.4]
])
B = np.array(calibration_voltage[0:-1]) # ACHTUNG IN MILLIVOLT!!!!!!!

coefficients = np.linalg.solve(A, B)
a, b = coefficients

print(f'a = {a}, b = {b}')
print(A)

plt.plot(calibration_voltage, calibration_temperature_kelvin, linestyle='-', marker='o')
plt.grid(visible=True, color='black', linewidth=0.5)
plt.title("Eichungskurve")
plt.xlabel("Spannung [mV]")
plt.ylabel("Temparatur [Kelvin]")
plt.show()