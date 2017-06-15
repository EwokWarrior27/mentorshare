import arcade
import sys
#import random
import math
#import time

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

MOVEMENT_SPEED = 10
BULLET_SPEED = 7

"""MOVE_LEFT = 500
MOVE_RIGHT = 500

RELOAD_SPEED = 600

clock = pygame.time.Clock()
move_left_event = pygame.USEREVENT + 1
move_right_event = pygame.USEREVENT + 2
reloaded_event  = pygame.USEREVENT + 3
move_left, move_right, reloaded = True, True, True"""
window = None

class Bullet(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.texture_default = arcade.load_texture("rowlet.png", scale=SPRITE_SCALING)
        self.texture_left = arcade.load_texture("rowlet_fly_left.png", scale=SPRITE_SCALING)
        self.texture_right = arcade.load_texture("rowlet_fly_left.png", mirrored=True, scale=SPRITE_SCALING)
        self.texture_down = arcade.load_texture("rowlet_fly_right.png", scale=SPRITE_SCALING)
        self.texture_up = arcade.load_texture("rowlet_fly_left.png", scale=SPRITE_SCALING)
        self.texture = self.texture_default

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.change_x < 0:
            self.texture = self.texture_left
        if self.change_x > 0:
            self.texture = self.texture_right
        if self.change_y < 0:
            self.texture = self.texture_down
        if self.change_y > 0:
            self.texture = self.texture_up

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


class MyApplication(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, screen_width, screen_height):
        """
        Initializer
        """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "My Pokemon Battling Game; Courtesy of the Python Arcade Library")
        self.frame_count = 0
        #self.background = None
        self.background = arcade.load_texture("pokemon_background.png")

        # Variables that will hold sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.enemy_list = None
        self.bullet_list = arcade.SpriteList()
        self.ebullet_list = arcade.SpriteList()

        # Set up the player info
        self.player_sprite = None
        self.health = 0
        self.ehealth = 0
        self.enemy = None
        """self.player_sprite.center_x = 100
        self.player_sprite.center_y = 120
        self.all_sprites_list.append(self.player_sprite)"""

        # Set the background color
        #arcade.set_background_color(arcade.color.SKY_BLUE)

        """for i in range(5):
            chandelure = arcade.Sprite("chandelure.png", SPRITE_SCALING / 3)

            chandelure.center_x = random.randrange(screen_width)
            chandelure.center_y = random.randrange(70, screen_height)

            self.all_sprites_list.append(chandelure)
            self.enemy_list.append(chandelure)"""
        #pygame.time.set_timer(move_left_event, MOVE_LEFT)
        #pygame.time.set_timer(move_right_event, MOVE_RIGHT)

    def setup(self):
        #Set up the game and initialize the variables.

        #self.background = arcade.load_texture("pokemon_background.png")

        # Sprite lists
        self.all_sprites_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()

        self.enemy = arcade.Sprite("chandelure.png", 0.5)
        self.enemy.center_x = 120
        self.enemy.center_y = SCREEN_HEIGHT - self.enemy.height
        self.enemy.angle = 180
        self.all_sprites_list.append(self.enemy)
        self.enemy_list.append(self.enemy)

        self.health = 20
        #self.ehealth = 25
        self.player_sprite = Player()
        self.player_sprite.center_x = SCREEN_WIDTH / 2
        self.player_sprite.center_y = SCREEN_HEIGHT / 2
        self.all_sprites_list.append(self.player_sprite)

        """for i in range(50):
            haunter = arcade.Sprite("haunter_sprite.png", SPRITE_SCALING / 3)

            haunter.center_x = random.randrange(SCREEN_WIDTH)
            haunter.center_y = random.randrange(120, SCREEN_HEIGHT)
            self.all_sprites_list.append(haunter)
            self.haunter_list.append(haunter)"""

        # Set up the player
        """self.score = 0
        self.player_sprite = Player("rowlet.png", SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.all_sprites_list.append(self.player_sprite)"""

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.all_sprites_list.draw()

        output = "Your Health: {}".format(self.health)
        arcade.draw_text(output, 10, 20, arcade.color.BRICK_RED, 18)

        """output1 = "Chandelure's Health: {}".format(self.ehealth)
        arcade.draw_text(output1, 560, 590, arcade.color.BRICK_RED, 18)"""

        """arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)"""

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.all_sprites_list.update()

    """while True:
        clock.tick(40)
        #if pygame.event.get(pygame.QUIT): break
        for e in pygame.event.get():
            if e.type == move_left_event:
                for enemy in self.enemy_list:
                    enemy.move_ip((-10 if move_left else 10, 0))
                move_left = not move_left
            elif e.type == move_right_event:
                for enemy in self.enemy_list:
                    enemy.move_ip(0, 10)
            elif e.type == reloaded_event:
                # when the reload timer runs out, reset it
                reloaded = True
                pygame.time.set_timer(reloaded_event, 0)"""



    def on_mouse_press(self, x, y, button, modifiers):
        #Called whenever the mouse moves.

        # Create a bullet
        bullet = Bullet("energy_ball1.png", SPRITE_SCALING * 1.5)

        # Position the bullet at the player's current location
        start_x = self.player_sprite.center_x
        start_y = self.player_sprite.center_y
        bullet.center_x = start_x
        bullet.center_y = start_y

        # Get from the mouse the destination location for the bullet
        dest_x = x
        dest_y = y

        # Do math to calculate how to get the bullet to the destination.
        # Calculation the angle in radians between the start points
        # and end points. This is the angle the bullet will travel.
        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)
        #print("Bullet angle: {:.2f}".format(bullet.angle))

        # Angle the bullet sprite so it doesn't look like it is flying
        # sideways.
        bullet.angle = math.degrees(angle)

        # Taking into account the angle, calculate our change_x
        # and change_y. Velocity is how fast the bullet travels.
        bullet.change_x = math.cos(angle) * BULLET_SPEED
        bullet.change_y = math.sin(angle) * BULLET_SPEED

        # Add the bullet to the appropriate lists
        self.all_sprites_list.append(bullet)
        self.bullet_list.append(bullet)
        """reloaded = False
        # when shooting, create a timeout of RELOAD_SPEED
        pygame.time.set_timer(reloaded_event, RELOAD_SPEED)"""



    def on_key_press(self, key, modifiers):

        if key == arcade.key.W:
            self.player_sprite.change_y = MOVEMENT_SPEED * 1.5
        elif key == arcade.key.S:
            self.player_sprite.change_y = -MOVEMENT_SPEED * 1.5
        elif key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED * 1.5
        elif key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED * 1.5


    def on_key_release(self, key, modifiers):
        """self.player_sprite.texture_default = arcade.load_texture("rowlet.png", scale=SPRITE_SCALING)
        self.player_sprite.texture = self.player_sprite.texture_default"""

        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0


    def update(self, delta_time):
        """ Movement and game logic """
        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.all_sprites_list.update()

        self.frame_count += 1
        for bullet in self.bullet_list:

            """rand = random.randrange(3)

            hit1 = arcade.check_for_collision(bullet, self.enemy)
            if hit1 == True and rand == 1:
                bullet.kill()
                self.ehealth -= 2
            elif hit1 == True and rand != 1:
                bullet.kill()
                arcade.draw_text("Miss", 300, 500, arcade.color.RED_DEVIL, 25)

            if bullet.top < 0:
                bullet.kill()"""

            hit_list1 = arcade.check_for_collision_with_list(bullet, self.ebullet_list)

            # If it did, get rid of the bullet
            if len(hit_list1) > 0:
                bullet.kill()

            # For every coin we hit, add to the score and remove the coin
            for ebullet in hit_list1:
                ebullet.kill()
                #self.score += 1

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.kill()
        self.frame_count += 1

        for self.enemy in self.enemy_list:

            # First, calculate the angle to the player. We could do this
            # only when the bullet fires, but in this case we will rotate
            # the enemy to face the player each frame, so we'll do this
            # each frame.

            # Position the start at the enemy's current location
            start_x = self.enemy.center_x
            start_y = self.enemy.center_y

            # Get the destination location for the bullet
            dest_x = self.player_sprite.center_x
            dest_y = self.player_sprite.center_y

            # Do math to calculate how to get the bullet to the destination.
            # Calculation the angle in radians between the start points
            # and end points. This is the angle the bullet will travel.
            x_diff = dest_x - start_x
            y_diff = dest_y - start_y
            angle = math.atan2(y_diff, x_diff)

            # Set the enemy to face the player.
            self.enemy.angle = math.degrees(0)


            # Shoot every 60 frames change of shooting each frame
            if self.frame_count % 90 == 0:
                bullet1 = arcade.Sprite("fireball1.png")
                bullet1.center_x = start_x
                bullet1.center_y = start_y

                # Angle the bullet sprite
                bullet1.angle = math.degrees(angle)-180

                # Taking into account the angle, calculate our change_x
                # and change_y. Velocity is how fast the bullet travels.
                bullet1.change_x = math.cos(angle) * BULLET_SPEED*4/5
                bullet1.change_y = math.sin(angle) * BULLET_SPEED*4/5


                self.ebullet_list.append(bullet1)
                self.all_sprites_list.append(bullet1)

        for bullet1 in self.ebullet_list:
            hit = arcade.check_for_collision(bullet1, self.player_sprite)

            if hit == True:
                bullet1.kill()
                self.health -= 2

            if bullet1.top < 0:
                bullet1.kill()

        self.ebullet_list.update()

        if self.health == 0:
            arcade.draw_text("You Lose...", 300, 300, arcade.color.RED_DEVIL, 60)
            self.player_sprite.kill()
            #self.on_draw.output.kill()
            """for i in range(100):
                time.sleep(0.3)
                print(i)
                if i == 5:"""
            sys.exit()
        elif self.ehealth <= 0:
            self.enemy.kill()
            #self.on_draw.output1.kill()
            arcade.draw_text("Victory!", 300, 300, arcade.color.GO_GREEN, 60)
            """for i in range(100):
                time.sleep(0.3)
                print(i)
                if i == 5:"""
            arcade.draw_text("Victory!", 300, 300, arcade.color.GO_GREEN, 60)
            sys.exit()


def main():
    """ Main method """
    #In the line below, write 'window=' at the very front of the line
    window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
