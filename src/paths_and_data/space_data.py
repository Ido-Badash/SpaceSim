# ~~~ space_data.py ~~~

#* ----- DATA -----
all_planets_names: list[str] = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

# all planets values
planets_rad_ratios_vals: tuple[float] = (35.4, 23.6, 21.6, 20.5, 13.0, 14.0, 26.0, 27.0)
planets_dists_vals: tuple[float] = (57.91, 108.2, 149.6, 227.94, 778.57, 1433.53, 2872.46, 4495.06)
planets_velocities_vals: tuple[float] = (0.02, 0.015, 0.01, 0.008, 0.004,  0.003, 0.002, 0.001)

# planets dicts
planets_rad_ratios: dict = {}
planets_dists: dict = {}
planets_velocities: dict = {}

# Planets data with scaled values (stored in dicts inside a list)
planets: list = []
planets_y: list = []
