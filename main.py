import pygame
import player
import ground
import physics
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
ground_01 = ground.Ground(0, window_instance._height - 30, window_instance._width, 30)


def RenderObjects():
    game_display.fill(window_instance.bg_color)
    pygame.draw.rect(game_display, game_player.color, (game_player.x, game_player.y, game_player._width, game_player._height))
    pygame.draw.rect(game_display, 
                    (130, 104, 31),
                    (ground_01.x, ground_01.y, ground_01._width, ground_01._height))
    pygame.display.update()


clock = pygame.time.Clock()
is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                game_player.is_jumping = False

    game_player.Move()
    physics.Gravity(game_player, ground_01)
    
    RenderObjects()
    clock.tick(30) #Run at 30 FPS

pygame.quit() #Quit Pygame