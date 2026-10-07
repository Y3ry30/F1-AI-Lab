import os
import fastf1
import matplotlib.pyplot as plt

# ============================================================
# CONFIGURACIÓN — para el reto del Sprint 0, cambia aquí:
#   PILOTO_1 = 'PIA', PILOTO_2 = 'HAM', GP = 'Belgium'  (Spa 2024)
# ============================================================
ANIO = 2024
GP = 'Belgium'
SESION = 'Q'
PILOTO_1 = 'PIA'
PILOTO_2 = 'HAM'

# Papaya McLaren, turquesa Mercedes
COLOR_1 = '#FF8000'
COLOR_2 = '#00D2BE'

# ------------------------------------------------------------
# Cache: FastF1 guarda aquí lo descargado para no repetir la descarga.
# Esta carpeta ya está en el .gitignore: nunca se sube a GitHub.
# ------------------------------------------------------------
os.makedirs('cache', exist_ok=True)
fastf1.Cache.enable_cache('cache')

print(f"Cargando {GP} {ANIO} ({SESION})... la primera vez tarda 1-2 minutos.")
session = fastf1.get_session(ANIO, GP, SESION)
session.load()

# Vuelta rápida de cada piloto
vuelta_1 = session.laps.pick_drivers(PILOTO_1).pick_fastest()
vuelta_2 = session.laps.pick_drivers(PILOTO_2).pick_fastest()

# Telemetría de cada vuelta: posición (X, Y), velocidad, distancia...
tel_1 = vuelta_1.get_telemetry()
tel_2 = vuelta_2.get_telemetry()

tiempo_1 = vuelta_1['LapTime']
tiempo_2 = vuelta_2['LapTime']
print(f"{PILOTO_1}: {tiempo_1}  |  {PILOTO_2}: {tiempo_2}")
dif = (tiempo_1 - tiempo_2).total_seconds()
ganador = PILOTO_1 if dif < 0 else PILOTO_2
print(f"Diferencia: {abs(dif):.3f}s a favor de {ganador}")

# ------------------------------------------------------------
# Gráfico: dos paneles apilados
# ------------------------------------------------------------
fig, (ax_trazado, ax_velocidad) = plt.subplots(
    2, 1, figsize=(8, 10), gridspec_kw={'height_ratios': [1.2, 1]}
)

# Panel superior: trazado del circuito por donde pasó cada piloto
ax_trazado.plot(tel_1['X'], tel_1['Y'], color=COLOR_1, linewidth=3, label=PILOTO_1)
ax_trazado.plot(tel_2['X'], tel_2['Y'], color=COLOR_2, linewidth=2, linestyle='--', label=PILOTO_2)
ax_trazado.set_title(f"{GP} {ANIO} — Vuelta rápida ({SESION})")
ax_trazado.set_aspect('equal')   # evita que el circuito se deforme
ax_trazado.legend()
ax_trazado.axis('off')

# Panel inferior: velocidad en cada punto de la vuelta
ax_velocidad.plot(tel_1['Distance'], tel_1['Speed'], color=COLOR_1, label=PILOTO_1)
ax_velocidad.plot(tel_2['Distance'], tel_2['Speed'], color=COLOR_2, linestyle='--', label=PILOTO_2)
ax_velocidad.set_xlabel('Distancia (m)')
ax_velocidad.set_ylabel('Velocidad (km/h)')
ax_velocidad.legend()

plt.tight_layout()
plt.savefig('comparativa.png', dpi=150)
plt.show()
print("Gráfico guardado como comparativa.png")