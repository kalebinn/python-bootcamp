import pygame
import random

import game_constants

print(game_constants.FPS)

vector = pygame.math.Vector2

class grid:
    def __init__(self, width, height):
        # width and height of the screen
        self.width = width
        self.height = height
        # list of obstacles
        self.obstacles = [] 

        #distance vectors (direction vectors)
        self.left = vector(-1, 0)
        self.right = vector(1, 0)
        self.up = vector(0, -1)
        self.down = vector(0, 1)
        self.possible_directions = [
            self.left,
            self.right,
            self.up,
            self.down 
        ]
    
    def find_neighbors(self, node):
        possible_neighors = []
        neighbors = []

        for edges in self.possible_directions:
            possible_neighors.append(node + edges) 

        for neighbor in possible_neighors:
            if neighbor not in self.obstacles:
                if 0 <= neighbor.x < self.width and 0 <= neighbor.y < self.height:
                        neighbors.append(neighbor)

        return neighbors

    def add_rand_obstacles(self, num_obstacles):
        count = 0 
        while count <= num_obstacles:
            x = random.randint(0, game_constants.GRIDWIDTH - 1)
            y = random.randint(0, game_constants.GRIDHEIGHT - 1)
            new_obstacle = vector(x, y)
            if new_obstacle not in self.obstacles:
                self.obstacles.append(new_obstacle)
            else:
                count -= 1
            count += 1

    def draw(self, screen):
        for x in range(0, game_constants.GRIDWIDTH_PX, game_constants.TILESIZE):
            pygame.draw.line(screen, game_constants.LIGHT_GREY, (x,0), (x, game_constants.GRIDHEIGHT_PX))

        for y in range(0, game_constants.GRIDHEIGHT_PX, game_constants.TILESIZE):
            pygame.draw.line(screen, game_constants.LIGHT_GREY, (0,y), (game_constants.GRIDWIDTH_PX, y))

        for obstacle in self.obstacles:
            rect = pygame.Rect(obstacle * game_constants.TILESIZE, (game_constants.TILESIZE, game_constants.TILESIZE))
            pygame.draw.rect(screen, game_constants.LIGHT_GREY, rect)

class player:
    def __init__(self, starting_pos = vector(0,0), color = game_constants.GREEN):
        self.color = color 
        self.pos = starting_pos
        self.path = []
    
    def draw(self, screen):
        rect = pygame.Rect(self.pos * game_constants.TILESIZE, (game_constants.TILESIZE, game_constants.TILESIZE))
        pygame.draw.rect(screen, self.color, rect)
    
    def move_up(self, screen, map):
        new_pos = self.pos + vector(0, -1)
        if 0 <= new_pos.y < map.height:
            if new_pos not in map.obstacles:
                self.pos = new_pos
                self.draw(screen)

    def move_down(self, screen, map):
        new_pos = self.pos + vector(0, 1)
        if 0 <= new_pos.y < map.height:
            if new_pos not in map.obstacles:
                self.pos = new_pos
                self.draw(screen)
    
    def move_left(self, screen, map):
        new_pos = self.pos + vector(-1, 0)
        if 0 <= new_pos.x < map.width:
            if new_pos not in map.obstacles:
                self.pos = new_pos
                self.draw(screen)
    
    def move_right(self, screen, map):
        new_pos = self.pos + vector(1, 0)
        if 0 <= new_pos.x < map.width:
            if new_pos not in map.obstacles:
                self.pos = new_pos
                self.draw(screen)

class game(grid, player):
    def __init__(self, width=game_constants.GRIDWIDTH, height=game_constants.GRIDHEIGHT):
        # define the map
        self.width = width
        self.height = height 
        self.map = grid(self.width, self.height)

        # define the player
        self.player = player()

        # define the screen
        self.screen = pygame.display.set_mode((game_constants.GRIDWIDTH_PX, game_constants.GRIDHEIGHT_PX))
        # set the game loop
        self.game_loop = True
        self.game_clock = pygame.time.Clock()
    
    def draw(self):
        self.map.draw(self.screen)
        self.player.draw(self.screen)
    
    def play(self):
        # infinite loop to keep the game going until the user
        # quits the game
        self.map.add_rand_obstacles(10)
        while self.game_loop:
            pygame.display.set_caption("Python Boot Camp")
            self.game_clock.tick(game_constants.FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_loop = False 
                    pygame.quit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = vector(pygame.mouse.get_pos()) // game_constants.TILESIZE
                    if event.button == 1:
                        if mouse_pos in self.map.obstacles:
                            self.map.obstacles.remove(mouse_pos)
                        else:
                            self.map.obstacles.append(mouse_pos)
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player.move_up(self.screen, self.map)
                    elif event.key == pygame.K_DOWN:
                        self.player.move_down(self.screen, self.map)
                    elif event.key == pygame.K_RIGHT:
                        self.player.move_right(self.screen, self.map)
                    elif event.key == pygame.K_LEFT:
                        self.player.move_left(self.screen, self.map)


            self.screen.fill(game_constants.DARK_GREY)
            self.draw()
            pygame.display.flip()

test_game = game()
test_game.play()

