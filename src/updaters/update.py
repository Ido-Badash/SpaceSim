# ~~~ update.py ~~~

#* ----- IMPORTS ----- 
import pygame


#* ----- LOCAL IMPORTS ----- 
from space_oop import OrbitRing, Sun
from drawing import makeStars, starsBlit
from paths_and_data import *
from constants import *


#* ----- FUNCTIONS ----- 
# Scale the distances
def updatePlanetsValues(au_to_pixels: float = au_to_pixels):    
    """
    Update and scale the values of planets' properties including radius ratios, distances, and velocities.
    """
    #* --- Dictioneries making ---
    # Planets ratio of radius to sun radius
    for name, ratio in zip(all_planets_names, planets_rad_ratios_vals):
        planets_rad_ratios[name] = ratio
    
    # Planets distances
    for name, distance in zip(all_planets_names, planets_dists_vals):
        planets_dists[name] = distance
        
    # make the planets velocities dict
    for name, planet_velo in zip(all_planets_names, planets_velocities_vals):
        planets_velocities[name] = planet_velo
    
    #* --- Scaling ---
    # Scale the radius ratios
    for key in planets_rad_ratios:
        planets_rad_ratios[key] *= planets_factor
    
    # Scale the velocities
    for key in planets_velocities:
        planets_velocities[key] *= speed_factor
    
    # Scale the planets dists
    for key in planets_dists:
        planets_dists[key] *= au_to_pixels
    
    # --- Planets with all the scaled values
    for planet_name in all_planets_names:
        planets.append({"name": planet_name,
                        "distance": planets_dists[planet_name],
                        "radius": sun_radius / planets_rad_ratios[planet_name]})

def orbitRadiusUpdate(orbit: OrbitRing, planet_index: int, last_orbit: OrbitRing | Sun,
                      surf_w: int, surf_h: int, au_to_pixels: float = au_to_pixels):
    """Updates the radius of an orbit based on the distance of a planet, the radius of the last orbit, and screen dimensions."""
    sun_dist = 1.75 # the dist from the sun to the closest orbit
    factor = sun_dist if isinstance(last_orbit, Sun) else 1
    screen_factor = (surf_w + surf_h) / 2 / 1000  # adjust based on screen size
    orbit.radius = int(planets[planet_index]["distance"] * au_to_pixels * screen_factor + last_orbit.radius * factor)
    
def updateAllOrbits(orbits_list, prev_orbit, surf_w: int, surf_h: int):
    """Updates the positions of all orbits in the orbits_list based on the previous orbit."""
    # Update the orbits positions       
    for i, current_orbit in enumerate(orbits_list):
        orbitRadiusUpdate(current_orbit, i, prev_orbit, surf_w, surf_h)
        current_orbit = prev_orbit
        
def updateBgStars(surface: pygame.Surface, surf_w: int, surf_h: int, background):
    """Update the background stars on the given surface."""
    stars = makeStars(
        surface=background,
        amount=1000,
        surf_w=surf_w,
        surf_h=surf_h) # Make the stars

    starsBlit(
        surface=surface,
        stars_list=stars,
        surf_w=surface.get_width(),
        surf_h=surface.get_height()
    ) # Blit the stars
