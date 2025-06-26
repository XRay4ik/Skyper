import pygame

screen = None
_initialized = False

class Game:
    class Window:
        @staticmethod
        def init():
            global _initialized
            if not _initialized:
                pygame.init()
                _initialized = True

        @staticmethod
        def set_scale(x, y):
            global screen
            Game.Window.init()
            screen = pygame.display.set_mode((x, y))
            return screen

        @staticmethod
        def set_title(text):
            Game.Window.init()
            pygame.display.set_caption(str(text))
            return text

        @staticmethod
        def set_color(red, green, blue):
            global screen
            Game.Window.init()
            if screen:
                screen.fill((red, green, blue))
                pygame.display.flip()
                return red, green, blue

        @staticmethod
        def get_screen():
            global screen
            return screen if screen else None

    @staticmethod
    def run():
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False