from main import pygame

h_positive = [ord("d"), pygame.K_RIGHT]
h_negative = [ord("a"), pygame.K_LEFT]
v_positive = [ord("w"), pygame.K_UP]
v_negative = [ord("s"), pygame.K_DOWN]

h_dir = 0
v_dir = 0

def GetHorizontalKey():
    keys = pygame.key.get_pressed()
    if keys[h_positive]:
        h_dir = 1
    elif keys[h_negative]:
        h_dir = -1
    else:
        h_dir = 0
    return h_dir

def GetVeritcalKey():
    keys = pygame.key.get_pressed()
    if keys[v_positive]:
        v_dir = 1
    elif keys[v_negative]:
        v_dir = -1
    else:
        v_dir = 0
    return v_dir
