# Importing from circleshape as it will be the shot's parent
from circleshape import *

# Importing the shot radius from constants
from constants import SHOT_RADIUS

# Let's start shooting!
class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        return

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        return

    def update(self, dt):
        self.position += self.velocity * dt
        return