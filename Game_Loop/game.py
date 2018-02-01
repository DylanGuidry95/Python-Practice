''''''
#pylint: disable=E1101
import pygame

class Application(object):
    def __init__(self, name, dim):
        self.app_name = name
        self.window_dim = dim
        self.screen = pygame.display.set_mode(dim)
        self.screen.fill((0, 0, 0))
        self.deltatime = 0.0
        self.clock = pygame.time.Clock()

    def start(self):
        pygame.init()
        pygame.display.set_caption(self.app_name)

    def update(self):
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                return False
        if pygame.key.get_pressed()[pygame.K_ESCAPE] != 0:
            return False
        return True