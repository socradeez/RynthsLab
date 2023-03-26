""" Weapons used by the player and enemies. """
import pygame as pg


class Weapon:
    """ Base class for all weapons. """

    def __init__(self, screen: pg.Surface, *groups) -> None:
        self.screen = screen

        # initialize the weapon
        pass

    def draw(self) -> None:
        """ Draw the weapon to the screen. """
        # weapon rendering not priority
        pass

    def shoot(self) -> None:
        """ Shoot a projectile. """
        pass


class Gun(Weapon):
    """ Simple gun that shoots bullets. """

    def __init__(self, screen: pg.Surface, *groups) -> None:
        super().__init__(self)

        # initialize the weapon
        pass

    def shoot(self) -> None:
        """ Shoot a bullet. """
        pass

    def reload(self) -> None:
        """ Reload the gun. """
        pass