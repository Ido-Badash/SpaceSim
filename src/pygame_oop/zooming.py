# ~~~ pygame_oop/zooming.py ~~~

#* ----- NORMAL IMPORTS -----
import pygame
import logging as log


#* ----- LOCAL IMPORTS -----
from utils import highlight

#* ----- CLASSES -----
class Zooming:
    def __init__(self, surface: pygame.Surface, surface_w: int, surface_h: int,
                 zoom_level: float = 1.0, max_zoom: float = 5.0, zoom_step: float = 0.25):
        self.surface = surface
        self.surface_w = surface_w
        self.surface_h = surface_h
        self.zoom_level = zoom_level
        self.max_zoom = max_zoom
        self.zoom_step = zoom_step
        self.min_zoom = min(self.zoom_level, self.max_zoom)
        self.current_zoom_debug = lambda: log.debug(highlight(f"Current zoom level: {self.zoom_level}\n"))
        self.cant_zoom_debug = lambda state:\
            log.debug(f"Cant zoom {state} anymore,\
            reached the {"max" if state == "in" else "min"}\
            of {self.max_zoom if state == "in" else "min"}.")
        
    def zoomIn(self) -> float:
        log.debug("Zooming in.")
        if self.zoom_level + self.zoom_step <= self.max_zoom:
            self.zoom_level += self.zoom_step
        else:
            log.debug(f"Cant zoom in anymore, reached the max of {self.max_zoom}.")
        self.current_zoom_debug()
        return self.zoom_level
            
    def zoomOut(self) -> float:
        log.debug("Zooming out")
        if self.zoom_level - self.zoom_step >= self.min_zoom:
            self.zoom_level -= self.zoom_step
        else:
            log.debug(f"Cant zoom out anymore, reached min of {self.min_zoom}")
        self.current_zoom_debug()
        return self.zoom_level
        
    def zoomReset(self) -> float:
        log.debug(f"Reseting zoom back to {self.min_zoom}")
        self.zoom_level = self.min_zoom
        return self.zoom_level

class ZoomController:
    def __init__(self, zoomer: Zooming):
        self.current_zoom = 1.0  # Initial zoom level
        self.zoomer = zoomer  # Store the zooming instance

    def zoomInCommand(self):
        self.current_zoom = self.zoomer.zoomIn()

    def zoomOutCommand(self):
        self.current_zoom = self.zoomer.zoomOut()

    def zoomResetCommand(self):
        self.current_zoom = self.zoomer.zoomReset()

    def getZoomLevel(self):
        return self.current_zoom
        
