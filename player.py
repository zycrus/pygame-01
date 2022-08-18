import kb_handler

class Player:
    def __init__(self, color, x, y, _width, _height):
        self.color = color
        self.x = x
        self.y = y
        self._width = _width
        self._height = _height
        self.vel_x = 5
        self.jump_speed = 10
        self.vel_y = self.jump_speed
        self.is_grounded = False
        self.is_jumping = False

    def Jump(self):
        if self.is_jumping is True:
            self.y -= self.vel_y * 2.5
            self.vel_y -= 1
            if self.vel_y <= 0 or self.is_grounded:
                self.is_jumping = False

    def Move(self):
        self.x += self.vel_x * kb_handler.GetHorizontalKey()
        if kb_handler.GetJumpKey():
            self.is_jumping = True
            self.Jump()
        