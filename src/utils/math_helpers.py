# ~~~ utils/nath_helpers.py ~~~

#* ----- IMPORTS -----
import math


#* ----- CONSTANTS -----
PHI: float = (1+math.sqrt(5))/2


#* ----- FUNCTIONS -----
# Function to calculate the x pos for a non circuler orbit
def calcOrbitX(star_x: float, semi_major_axis: float, angle: float, delta: float) -> int:
    return int(star_x + semi_major_axis * math.cos(angle) * delta)

# Function to calculate the y pos for a non circuler orbit
def calcOrbitY(star_y: float, semi_minor_axis: float, angle: float, delta: float) -> int:
    return int(star_y + semi_minor_axis * math.sin(angle) / delta)
