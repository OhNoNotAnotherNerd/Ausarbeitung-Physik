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