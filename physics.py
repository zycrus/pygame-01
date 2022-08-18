grav_max = 25
grav_vel = 0

def Gravity(player, other):
    global grav_vel

    if not Collide(player, other):
        
        if not player.is_jumping:
            player.y += grav_vel

        if grav_vel < grav_max:
            grav_vel += 1
        
        player.is_grounded = False
    else:
        player.y = other.y - player._height
        player.is_grounded = True
        player.vel_y = player.jump_speed
        grav_vel = 0


def Collide(player, other):
    if player.y + player._height + player.vel_x > other.y:
        return True