# ~~~ paths.py ~~~

#* ----- NORMAL IMPORTS -----
import os


#* ----- LOCAL IMPORTS -----
from .space_data import all_planets_names
from utils import imgPlanetPath, imgUtilsPath


#* --- Paths ---
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# stars
sun_path = os.path.join(project_root, "assets", "images", "stars", "solar_system_sun.png")

# planets
planets_ver_names: tuple[str] = ("mercury_path", "venus_path", "earth_path", "mars_path",
                     "jupiter_path", "saturn_path", "uranus_path", "neptune_path")

planets_paths: dict = {
    ver_name: imgPlanetPath(planet_name) for ver_name, planet_name
    in zip(planets_ver_names, all_planets_names)}

# zoom in
normal_zoom_in_path = imgUtilsPath("zoom_in", "zoom_in_logo")
hover_zoom_in_path = imgUtilsPath("zoom_in", "zoom_in_logo_hover")
clicked_zoom_in_path = imgUtilsPath("zoom_in", "zoom_in_logo_clicked")

# zoom out
normal_zoom_out_path = imgUtilsPath("zoom_out", "zoom_out_logo")
hover_zoom_out_path = imgUtilsPath("zoom_out", "zoom_out_logo_hover")
clicked_zoom_out_path = imgUtilsPath("zoom_out", "zoom_out_logo_clicked")
current_zoom: float = 1.0
