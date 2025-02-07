# ~~~ pygame_oop/button.py ~~~

#* ----- NORMAL IMPORTS -----
import pygame
import logging as log

#* ----- CLASSES -----
class Button:
    """A class to represent a toggleable and command-executing button"""
    def __init__(self, name: str, x: int, y: int, w: int, h: int, image_path: str, hover_image_path: str, clicked_image_path: str = None):
        self.name = name
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = self.loadImage(image_path)
        self.hover_image = self.loadImage(hover_image_path)
        self.clicked_image = self.loadImage(clicked_image_path) if clicked_image_path else self.image
        self.current_image = self.image

        self.clicked: bool = False  # State: True if clicked, False otherwise
        self.command_executed: bool = False  # Tracks if a click_once command has been executed

    def loadImage(self, path: str) -> pygame.Surface | None:
        """Load an image from the given path"""
        try:
            return pygame.image.load(path).convert_alpha()
        except pygame.error as e:
            log.error(f"Image '{path}' loading error: {e}")
            return None

    def show(self, surface: pygame.Surface, mouse_pos: tuple) -> None:
        """Render the button on the screen based on its state"""
        mouse_x, mouse_y = mouse_pos

        # Current image based on state
        if self.x < mouse_x < self.x + self.w and self.y < mouse_y < self.y + self.h:
            self.current_image = self.hover_image
        else:
            self.current_image = self.image

        # Render the current image
        if self.current_image:
            scaled_image = pygame.transform.scale(self.current_image, (self.w, self.h))
            surface.blit(scaled_image, (self.x, self.y))

    def handleEvent(self, event: pygame.event.Event, other_button=None, command=None, toggle=False) -> bool:
        """
        Handle mouse events to toggle the button's state and execute a command.
        Returns True if the event was handled, False otherwise.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if self.x < mouse_x < self.x + self.w and self.y < mouse_y < self.y + self.h:
                log.debug(f"{self.name} button is clicked.")
                if toggle:
                    self.clicked = not self.clicked  # Toggle state
                    log.debug(f"{self.name} button is toggled to {self.clicked} state.")
                    if other_button:
                        other_button.clicked = False  # Deactivate the other button
                
                if command:
                    command()
                
                return True  # Event was handled by this button
        
        return False  # Event was not handled

    def state(self) -> bool:
        return self.clicked

    def __str__(self) -> str:
        return self.name