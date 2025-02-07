# ~~~ path_helpers.py ~~~

#* ----- IMPORTS -----
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

#* ----- FUNCTIONS -----
# --- Assets ---
def imgPlanetPath(planet_name: str, img_type: str = "png") -> str:
    """Return the path of the planet image"""
    path = os.path.join(project_root, "assets", "images", "planets", f"{planet_name}_planet.{img_type}")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Planet image file not found: {path}")
    return path

def imgUtilsPath(directory: str, img_path: str, img_type: str = "png") -> str:
    """Return the path of the utilities image"""
    path = os.path.join(project_root, "assets", "images", "utils_logos", directory, f"{img_path}.{img_type}")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Utils Image file not found: {path}")
    return path