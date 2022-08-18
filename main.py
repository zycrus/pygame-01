import pygame
import player
import kb_handler

pygame.init() #Initialize Pygame

# Window Object
class Window:
    def __init__(self, _width, _height):
        self._width = _width
        self._height = _height
        self.bg_color = (48, 61, 71)

window_instance = Window(750, 500)

game_display = pygame.display.set_mode((window_instance._width, window_instance._height))
pygame.display.set_caption("zzz")


game_player = player.Player((103, 191, 121), 375, 250, 50, 50)


clock = pygame.time.Clock()
is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    
    game_display.fill(window_instance.bg_color)
    pygame.draw.rect(game_display, game_player.color, (375, 250, game_player._width, game_player._height))
    pygame.display.update()
    clock.tick(30) #Run at 30 FPS

pygame.quit() #Quit Pygame