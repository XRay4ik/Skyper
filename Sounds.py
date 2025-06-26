# Skyper for API pygame by KoldI

import pygame

pygame.init()
pygame.mixer.init()

class Sound:
    class Player:
        @staticmethod
        def add(sound, loop=False):
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play(-1 if loop else 0)

        @staticmethod
        def set_volume(level):
            pygame.mixer.music.set_volume(level)

        @staticmethod
        def add_pause():
            pygame.mixer.music.pause()

        @staticmethod
        def add_unpause():
            pygame.mixer.music.unpause()

    class Noise:
        _sound = None

        @staticmethod
        def add(file):
            Sound.Noise._sound = pygame.mixer.Sound(file)

        @staticmethod
        def set_volume(level):
            if Sound.Noise._sound:
                Sound.Noise._sound.set_volume(level)

        @staticmethod
        def play():
            if Sound.Noise._sound:
                Sound.Noise._sound.play()

        @staticmethod
        def stop():
            if Sound.Noise._sound:
                Sound.Noise._sound.stop()