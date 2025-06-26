import pygame
#from Skyper import Game

pygame.init()

class Style:
    class text:
        @staticmethod
        def set_text(content, font=None, size=48, smooth=True, color=(255, 255, 255), pos=(0, 0)):
            screen = Game.Window.get_screen()
            used_font = pygame.font.SysFont(font, size)
            rendered = used_font.render(content, smooth, color)
            screen.blit(rendered, pos)
            pygame.display.flip()