# Importing all from circleshape.py as a new class needs to inherit
from circleshape import *

# Importing PLAYER_RADIUS from contstants.py for use here
from constants import PLAYER_RADIUS

# The following defines the player class
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        return

    # in the player class (code provided by Boot.dev course)
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # Overriding the draw function from CircleShape
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        return
