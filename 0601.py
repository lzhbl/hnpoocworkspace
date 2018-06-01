from collections import Iterable
print(isinstance([], Iterable))
print(isinstance((), Iterable))
print(isinstance({}, Iterable))
print(isinstance('qwqw', Iterable))
print(isinstance(1211, Iterable))
# print(isinstance(array, Iterable))
# Iterable、Iterator
import pygame
print(pygame.ver)
if pygame.font is None:
    print ('The font module is not available!')
    exit()
print(pygame.font)