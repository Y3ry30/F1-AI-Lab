"""
02_pide_pilotos.py — Mi primer script propio.
Pide dos pilotos y un GP por teclado, imprime sus vueltas rápidas.
"""
import fastf1
import os
from wcwidth.table_grapheme import GRAPHEME_REGIONAL_INDICATOR

ANIO = 2024
SESION = 'Q'
piloto_1 = input("Piloto 1: ")
piloto_2 = input("Piloto 2: ")
gp = input("GP: ")
print(f"Comprobación: {piloto_1} | {piloto_2} | GP: {gp}")
os.makedirs('cache', exist_ok=True)
fastf1.Cache.enable_cache('cache')
print("Cargando sesión...")
session = fastf1.get_session(ANIO, gp, SESION)
session.load()
vuelta_1 = session.laps.pick_drivers(piloto_1).pick_fastest()
vuelta_2 = session.laps.pick_drivers(piloto_2).pick_fastest()
tiempo_1 = vuelta_1['LapTime']
tiempo_2 = vuelta_2['LapTime']
dif = (tiempo_1 - tiempo_2).total_seconds()
print (f"{piloto_1}: {tiempo_1}  |  {piloto_2}: {tiempo_2}")
print(f"Diferencia: {abs(dif):.3f}s a favor de {piloto_1 if dif < 0 else piloto_2}")