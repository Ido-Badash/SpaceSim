# ~~~ space.py ~~~

#* ----- NORMAL IMPORTS -----
import sys
import pygame
import logging as log
from colorama import Fore, Style


#* ----- LOCAL IMPORTS -----
from constants import *
from utils import highlight
from paths_and_data import *
from space_oop import OrbitRing, Sun, Planet
from pygame_oop import Zooming, ZoomController, Button
from updaters import updatePlanetsValues, updateAllOrbits, updateBgStars

#* ----- SETUP -----
# --- Initiation ---
pygame.init()


#* ----- CLASSES -----
# --- Running ---
class SolarSystemRunner:
    def __init__(self, surf: pygame.Surface, surf_w: int, surf_h: int,
                 min_surf_w: int, min_surf_h: int,
                 clock: pygame.time.Clock, ticks: int = 60):
        self.surf = surf
        self.surf_w = surf_w
        self.surf_h = surf_h
        self.min_surf_w = min_surf_w
        self.min_surf_h = min_surf_h
        self.clock = clock
        self.ticks = ticks
        
        self.background, self.sun,\
        self.all_orbits, self.all_planets,\
        self.zoom_in_button, self.zoom_out_button = self.setupSolar(au_to_pixels)
        
        self.zoomer = Zooming(
            surface=self.surf,
            surface_w=self.surf_w,
            surface_h=self.surf_h,
            zoom_step=1.0)
        self.zoom_controller = ZoomController(self.zoomer)

    def setupSolar(self, au_to_pixels: float = au_to_pixels):
        #* --- Pygame Setup ---
        # Create the background surface
        self.background = pygame.Surface((self.surf_w, self.surf_h))
        self.background.fill((0, 0, 0))
        
        #* ----- Stars and Planets Setup -----
        updatePlanetsValues(au_to_pixels)
        # --- Sun ---
        self.sun = Sun(
            name="Sun",
            x=self.surf_w // 2,
            y=self.surf_h // 2,
            radius=sun_radius,
            image_path=sun_path
        )

        # --- Orbit Rings ---
        orbit_names = ["sun"]  # with the sun
        self.all_orbits = {"sun": self.sun}
        
        # makes names for the `orbit_names`
        for name in all_planets_names:
            orbit_names.append(f"{name.lower()}_orbit")

        # reminder `enumerate` gets the index and the value
        for i, name in enumerate(orbit_names[1:]):
            last_orbit_str = orbit_names[i:-1][0]
            last_orbit = self.all_orbits[last_orbit_str] if last_orbit_str != "sun" else self.sun
            
            self.all_orbits[name] = OrbitRing(
                name=f"{name[:name.index('_')]} Orbit".title(),
                star=self.sun,
                radius=int(planets[i]["distance"] * au_to_pixels) + last_orbit.radius,
                thickness=1
            ) 
        
        # Gives all the orbits a dict with names so it will be a lot more easy to call
        named_orbits = {}
        for name, val in zip(orbit_names, self.all_orbits.values()):
            named_orbits[name] = val
        named_orbits.pop("sun")
        
        self.all_orbits = (named_orbits["mercury_orbit"], named_orbits["venus_orbit"],
                      named_orbits["earth_orbit"], named_orbits["mars_orbit"],
                      named_orbits["jupiter_orbit"], named_orbits["saturn_orbit"],
                      named_orbits["uranus_orbit"], named_orbits["neptune_orbit"])
        
        #* --- Planets ---
        planets_color = (
            (169, 169, 169), (255, 223, 0), (0, 105, 148), (186, 74, 47),
            (220, 163, 95), (230, 214, 146), (90, 210, 255), (35, 51, 122)
        )
        planet_names = ("mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune")
        self.planets_dict = {}
        
        saturn_radii = self.sun.radius // planets_rad_ratios["Saturn"]
        normal_radii = lambda planet_name: self.sun.radius // planets_rad_ratios[planet_name.title()]
        
        for color, name in enumerate(planet_names):
            self.planets_dict[name] = Planet(
                name=name.title(),
                orbit_ring=named_orbits[f"{name}_orbit"],
                radius=normal_radii(name) if name != "saturn" else saturn_radii,
                speed_increase=planets_velocities[name.title()],
                color=planets_color[color],
                image_path=planets_paths[f"{name}_path"],
                image_size=(normal_radii(name)*2, normal_radii(name)*2)\
                    if name != "saturn" else (saturn_radii*2, saturn_radii*2//1.5)
            )

        self.all_planets = []
        for name in planet_names:
            self.all_planets.append(self.planets_dict[name])
            
        #* ----- Buttons -----
        # --- zoom ---
        zoom_buttons_pad = 10
        
        # zoom in
        self.zoom_in_button_w, self.zoom_in_button_h = 50, 50
        self.zoomInButtonX = lambda: self.surf.get_width() - 70 - self.zoom_in_button_w
        self.zoomInButtonY = lambda: self.surf.get_height() - zoom_buttons_pad - self.zoom_in_button_h
        
        self.zoom_in_button = Button(
            name="Zoom In",
            x=self.zoomInButtonX(), y=self.zoomInButtonY(),
            w=self.zoom_in_button_w, h=self.zoom_in_button_h,
            image_path=normal_zoom_in_path,
            hover_image_path=hover_zoom_in_path
        )
        
        # zoom out
        self.zoom_out_button_w, self.zoom_out_button_h = 50, 50
        self.zoomOutButtonX = lambda: self.surf.get_width() - zoom_buttons_pad - self.zoom_out_button_w
        self.zoomOutButtonY = lambda: self.surf.get_height() - zoom_buttons_pad - self.zoom_out_button_h
        
        self.zoom_out_button = Button(
            name="Zoom Out",
            x=self.zoomOutButtonX(), y=self.zoomOutButtonY(),
            w=self.zoom_out_button_w, h=self.zoom_out_button_h,
            image_path=normal_zoom_out_path,
            hover_image_path=hover_zoom_out_path
        )

        # --- Updating Setup ---
        # Updating Functions
        updateBgStars(self.surf, self.surf.get_width(), self.surf.get_height(), self.background)  # bg stars
        updateAllOrbits(self.all_orbits, self.sun, self.surf_w, self.surf_h)
            
        return self.background, self.sun,\
               self.all_orbits, self.all_planets,\
               self.zoom_in_button, self.zoom_out_button

    def execute(self) -> None:
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                # --- Zooming ---
                if event.key == pygame.K_EQUALS:
                    log.debug("Plus key has been clicked.")
                    self.zoom_controller.zoomInCommand()
                    
                elif event.key == pygame.K_MINUS:
                    log.debug("Minus key has been clicked.")
                    self.zoom_controller.zoomOutCommand()
                    
                elif event.key == pygame.K_h and event.mod & pygame.KMOD_CTRL:
                    log.debug("H & ctrl has been clicked.")
                    self.zoom_controller.zoomResetCommand()
                
            elif event.type == pygame.VIDEORESIZE:
                # Handle window resizing
                self.surf_w, self.surf_h = event.size
                self.surf_w = max(self.surf_w, self.min_surf_w)
                self.surf_h = max(self.surf_h, self.min_surf_h)
                self.surf = pygame.display.set_mode((self.surf_w, self.surf_h), pygame.RESIZABLE)
                
                # --- Update positions and sizes ---
                # Update the background for the new size
                self.background = pygame.Surface((self.surf_w, self.surf_h))
                self.background.fill((0, 0, 0))
                
                # Updating Functions
                updateBgStars(self.surf, self.surf.get_width(), self.surf.get_height(), self.background)  # bg stars
                updateAllOrbits(self.all_orbits, self.sun, self.surf_w, self.surf_h)
                
                # Normal Updating
                self.zoom_in_button.x, self.zoom_in_button.y = self.zoomInButtonX(), self.zoomInButtonY()
                self.zoom_out_button.x, self.zoom_out_button.y = self.zoomOutButtonX(), self.zoomOutButtonY()
                
                # Update sun position
                self.sun.x = self.surf_w // 2
                self.sun.y = self.surf_h // 2
                
            # Handle button events
            self.zoom_in_button.handleEvent(event,
                                            command=lambda: self.zoom_controller.zoomInCommand()
                                            )
            self.zoom_out_button.handleEvent(event,
                                            command=lambda: self.zoom_controller.zoomOutCommand()
                                            )
        planets_y.clear()  # clears list so it wont flood
        for planet in self.planets_dict.values(): # appends the y pos of the planets
            planets_y.append(planet.y)
        
        # check if all planet y-values are the same
        if all(y == planets_y[0] for y in planets_y):
            log.debug(highlight(f"All planets have the same y-coordinates: {planets_y}", Fore.GREEN, Style.BRIGHT))
        
            
        # Lower number layer = get runed over by higher layerd numbers
        #* ----- Layer 1 -----
        # --- background ---
        self.surf.blit(self.background, (0, 0))
        
        #* ----- Layer 2 -----
        # --- Display the orbit rings ---
        for orbit in self.all_orbits:
            orbit.show(surface=self.surf)
        
        #* ----- Layer 3 -----
        # --- Display the planets ---
        for planet in self.all_planets:
            planet.show(surface=self.surf)
            planet.updatePos()
            
        #* ----- Layer 4 -----
        # --- Display the sun ---
        self.sun.show(surface=self.surf)
            
        #* ----- Layer 5 -----
        # --- Apply zoom effect ---
        zoom_level = self.zoom_controller.getZoomLevel()
        new_w, new_h = (int(self.surf_w * zoom_level), int(self.surf_h * zoom_level))
        new_x, new_y = self.surf_w/2-new_w/2, self.surf_h/2 - new_h/2
        zoom_surf = pygame.transform.scale(self.surf, (new_w, new_h))
        self.surf.blit(zoom_surf, (new_x, new_y))
        
        #* ----- Layer 6 -----
        # --- Display the buttons ---
        # Zoom in/out buttons
        self.zoom_in_button.show(surface=self.surf, mouse_pos=pygame.mouse.get_pos())
        self.zoom_out_button.show(surface=self.surf, mouse_pos=pygame.mouse.get_pos())

        # Update the display
        pygame.display.flip()
        self.clock.tick(self.ticks)
        
    def run(self, run: bool = True):
        if run == True:
            self.execute()