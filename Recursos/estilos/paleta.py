"""
Paleta de colores centralizada de room_acoustic.

Reúne los colores que ya estaban en uso, repetidos como literales en
distintas pantallas (cada una definía su propia variante de "blanco
translúcido" o de acento), en una única fuente de referencia. Ningún
valor aquí es nuevo: todos coinciden con los que ya usaba la interfaz.

No reemplaza a `Recursos/estilos/estilo.py` (que contiene hojas de
estilo QSS completas); este módulo solo centraliza los colores base
para que puedan reutilizarse desde distintos archivos sin duplicarlos.
"""

# ── Acento e identidad institucional ────────────────────────────────
# Azul claro, ya dominante en las pantallas rediseñadas (Base de Datos,
# Tiempo de Reverberación).
ACENTO = "#7ec8f7"

# Colores institucionales de la Universidad del Atlántico, ya usados en
# la generación de reportes PDF (Datos/utils/reportePDF.py).
AZUL_UA = "#00458C"
NARANJA_UA = "#DE7019"


def blanco(opacidad: float) -> str:
    """Blanco translúcido con la opacidad indicada (0.0 - 1.0), como rgba()."""
    return f"rgba(255,255,255,{opacidad:.2f})"


# Niveles estándar de blanco translúcido propuestos por la auditoría de
# UI/UX, para dejar de inventar una opacidad distinta en cada archivo.
# Disponibles para uso futuro; no se aplican de forma masiva en esta fase.
BLANCO_10 = blanco(0.10)
BLANCO_25 = blanco(0.25)
BLANCO_45 = blanco(0.45)
BLANCO_80 = blanco(0.80)


# ── Paleta categórica de superficies (Base de Datos) ────────────────
# Mismos valores que ya usaba Vista/ventInfoBD.py de forma local
# (fondo, borde). "frontal" coincide exactamente con ACENTO
# (#7ec8f7 = rgb(126,200,247)).
COLOR_SUPERFICIE_FRONTAL = ("rgba(126,200,247,0.18)", "rgba(126,200,247,0.55)")
COLOR_SUPERFICIE_TRASERA = ("rgba(167,139,250,0.18)", "rgba(167,139,250,0.55)")
COLOR_SUPERFICIE_IZQUIERDA = ("rgba(52,211,153,0.18)", "rgba(52,211,153,0.55)")
COLOR_SUPERFICIE_DERECHA = ("rgba(251,191,36,0.15)", "rgba(251,191,36,0.55)")
COLOR_SUPERFICIE_PISO = ("rgba(251,146,60,0.15)", "rgba(251,146,60,0.55)")
COLOR_SUPERFICIE_TECHO = ("rgba(248,113,113,0.15)", "rgba(248,113,113,0.55)")

# Mismos valores exactos que ya usaba _COLOR_ADICIONALES en ventInfoBD.py
# (0.09 / 0.40, no se redondean a BLANCO_10/BLANCO_45 para no alterar
# el resultado visual actual).
COLOR_OBJETOS_ADICIONALES = (blanco(0.09), blanco(0.40))


# ── Texto (mismos valores que ya usa el formulario de Tiempo de
# Reverberación: etiquetas 0.88, subtítulos 0.55) ────────────────────
TEXTO_PRINCIPAL = blanco(0.88)
TEXTO_SECUNDARIO = blanco(0.55)

# ── Estado del resultado acústico ───────────────────────────────────
# Reutilizan los tonos ya presentes en la paleta categórica de arriba
# (verde menta = rgb(52,211,153), rojo suave = rgb(248,113,113)); antes
# el indicador usaba #4CAF50/#F44336, ajenos al resto de la aplicación.
ESTADO_OPTIMO = "#34d399"
ESTADO_NO_OPTIMO = "#f87171"

# ── Series del gráfico de RT (ya definidas en Modelo/calculoRT2.py) ──
# Se exponen aquí para que las tarjetas de Tr MID puedan asociarse
# visualmente a su curva.
SERIE_SABINE = "#FF6F61"
SERIE_EYRING = "#58B3FF"
