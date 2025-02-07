# ~~~ space_oop/orbit_ring.py ~~~

#* ----- NORMAL IMPORTS -----
import pygame
import logging as log


#* ----- LOCAL IMPORTS -----
from utils import calcOrbitX, calcOrbitY

#* ----- CLASSES -----
# --- Orbits ---
class OrbitRing:
    """A class to represent an orbit ring"""
    def __init__(self, name: str, star: object, radius: int, thickness: int,
                 color: tuple = (255, 255, 255), radii_delta: float = 1.0):
        
        if not isinstance(star, (Planet, Sun)):  # Check if the star is either a Planet or Star
            raise TypeError(f"star must be an instance of Planet or Star, not {type(star)}")
        
        self.name = name
        self.star = star
        self.radius = radius
        self.thickness = thickness
        self.color = color
        self.radii_delta = radii_delta
        
    def show(self, surface: pygame.Surface):
        """Shows the orbit ring"""
        width = (self.radius * 2) * self.radii_delta
        height = (self.radius * 2) / self.radii_delta
        
        pygame.draw.ellipse(
            surface=surface,
            color=self.color,
            rect=pygame.Rect(self.star.x - width // 2, self.star.y - height // 2, width, height),
            width=self.thickness)
            
    def __str__(self):
        return (f"OrbitRing({self.name}) around {self.star.name} with "
                f"radius {self.radius}, thickness {self.thickness}, "
                f"and color {self.color}")

# --- Planets ---
class Planet:
    """A class to represent a planet"""
    def __init__(self, name: str, orbit_ring: OrbitRing, radius: int, speed_increase: float,
                 color: tuple, image_path: str = None, image_size: tuple = None):
        self.name = name
        self.radius = radius
        self.color = color
        self.orbit_ring = orbit_ring
        self.speed_increase = speed_increase
        self.image_path = image_path

        self.angle = 0
        self.x = 0
        self.y = 0
        self.radii_delta = 1.5
        self.updatePos()

        self.image = None
        self.image_size = (self.radius * 2, self.radius * 2) if image_size is None else image_size

        if self.image_path:
            try:
                self.image = pygame.image.load(self.image_path).convert_alpha()
                self.color = (0, 0, 0, 0)
            except pygame.error as e:
                log.error(f"Image '{image_path}' loading error: {e}")

        # Update the orbit ring's radii_delta to match the planet's
        self.orbit_ring.radii_delta = self.radii_delta

    def updatePos(self):
        """Update the position of the planet based on the orbit radius"""
        self.angle += self.speed_increase
        self.x = calcOrbitX(self.orbit_ring.star.x, self.orbit_ring.radius, self.angle, self.radii_delta)
        self.y = calcOrbitY(self.orbit_ring.star.y, self.orbit_ring.radius, self.angle, self.radii_delta)

    def show(self, surface: pygame.Surface):
        """Show the planet with an optional image"""
        if self.image:
            scaled_image = pygame.transform.scale(self.image, self.image_size)
            img_rect = scaled_image.get_rect(center=(self.x, self.y))
            surface.blit(scaled_image, img_rect)
        else:
            pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def __str__(self):
        image_info = f"  Image Path: {self.image_path}" if self.image else "  No image available"
        return (f"Planet: {self.name}\n"
                f"  Orbiting Star: {self.orbit_ring.star.name}\n"
                f"  Radius: {self.radius * 2} px (diameter)\n"
                f"  Speed Increase: {self.speed_increase} px/s\n"
                f"  Color: {self.color}\n"
                f"  Current Position: ({self.x:.0f} px, {self.y:.0f} px)\n"
                f"  Orbit Radius: {self.orbit_ring.radius} px (from the sun)\n"
                f"{image_info}")


# --- Stars ---
class Sun:
    """A class to represent a sun"""
    def __init__(self, name: str, x: int, y: int, radius: int,
                 color: tuple = (255, 255, 0), image_path: str = None):
        self.name = name
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.image_path = image_path
        
        self.radii_delta = 1
        
        self.image = None
        if self.image_path:
            try:
                self.image = pygame.image.load(self.image_path).convert_alpha()
            except pygame.error as e:
                log.error(f"Image '{image_path}' loading error: {e}")
        
    def show(self, surface: pygame.Surface):
        """Show the sun with an optional image"""
        if self.image:
            # Center the image on the sun's position and scale it to the radius if necessary
            scaled_image = pygame.transform.scale(self.image, (self.radius * 2, self.radius * 2))
            img_rect = scaled_image.get_rect(center=(self.x, self.y))
            surface.blit(scaled_image, img_rect)
        else:
            # If no image, draw a circle for the sun
            pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)
    
    def __str__(self):
        return self.name