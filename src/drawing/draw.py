# ~~~ draw.py ~~~

#* ----- IMPORTS -----
import random
import pygame

#* ----- FUNCTIONS -----
# --- Drawing ---   
def makeStars(surface: pygame.Surface, amount: int, surf_w: int, surf_h: int, stars: list = None) -> list:
    """Blit stars onto the surface"""
    surface_w, surface_h = surface.get_size()
    if stars is None:
        stars = []
        for _ in range(amount):
            x = random.randint(0, surf_w)
            y = random.randint(0, surf_h)
            alpha = random.randint(0, 255)
            size = random.randint(1, 3)
            stars.append((x, y, alpha, size))
    
    for star in stars:
        x, y, alpha, size = star
        # Adjust the position based on the new surface size
        x = int(x * surface_w / surf_w)
        y = int(y * surface_h / surf_h)
        star_w = max(1, int(surface_w * 0.0001 * size))
        star_h = star_w
        color = (255, 255, 255, alpha)
        star_surface = pygame.Surface((star_w, star_h), pygame.SRCALPHA)
        pygame.draw.ellipse(star_surface, color, (0, 0, star_w, star_h))
        surface.blit(star_surface, (x, y))
    
    return stars

def starsBlit(surface: pygame.Surface, stars_list: makeStars, surf_w: int, surf_h: int) -> None:
    """Blit the stars onto the surface"""
    for star in stars_list:
        x, y, alpha, size = star
        # Adjust the position based on the new surface size
        x = int(x * surface.get_width() / surf_w)
        y = int(y * surface.get_height() / surf_h)
        star_w = max(1, int(surface.get_width() * 0.0001 * size))
        star_h = star_w
        color = (255, 255, 255, alpha)
        star_surface = pygame.Surface((star_w, star_h), pygame.SRCALPHA)
        pygame.draw.ellipse(star_surface, color, (0, 0, star_w, star_h))
        surface.blit(star_surface, (x, y))
