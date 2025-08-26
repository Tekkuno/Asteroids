# More pygame is needed, and also randomness
import pygame # type: ignore
import random

# Importing all from circleshape.py as a new class needs to inherit
from circleshape import *
from constants import *

# Time to create asteroids baby!
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        return

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        return

    def update(self, dt):
        self.position += self.velocity * dt
        return
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # randomize the angle of the split
        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2


