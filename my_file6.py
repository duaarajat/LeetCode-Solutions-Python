import pygame
import random
import time
# NOTE: While numpy/pandas/matplotlib are taught, they are generally designed for 
# data analysis and plotting, not real-time graphics or simple grid manipulation. 
# We'll stick to core Python lists, tuples, and dictionaries for performance 
# and simplicity, which is standard practice in Pygame development.

# --- 1. CONFIGURATION ---
# Use basic Python variables (strings, tuples, lists, dictionary-like settings)
CELL_SIZE = 40  # Size of each cell in pixels (integer)
MAZE_W = 15     # Maze width (number of cells)
MAZE_H = 10     # Maze height (number of cells)
SCREEN_WIDTH = MAZE_W * CELL_SIZE
SCREEN_HEIGHT = MAZE_H * CELL_SIZE + 50 # Extra space for the button

# Define Colors using tuples
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0) # Start color
RED = (200, 0, 0)   # End color
BLUE = (50, 50, 200) # Player color
YELLOW = (255, 255, 0) # Button highlight/Congrats color
PURPLE = (150, 50, 200) # This color is no longer used for hints, but kept defined.
DARK_GREEN = (0, 100, 0) # For start text contrast

# --- 2. MAZE CLASS DEFINITION ---
# A class to handle the maze data structure and its visual representation.
class Maze:
    """
    Manages the maze grid, walls, generation, and drawing.
    Uses lists of lists (analogous to a 2D Numpy array) for the grid data.
    """
    def __init__(self, w, h):
        # Grid is a 2D list. Each cell is a dictionary storing its walls.
        # { 'walls': [top, right, bottom, left], 'visited': False }
        self.w = w
        self.h = h
        self.grid = [[{'walls': [True, True, True, True], 'visited': False} 
                      for _ in range(w)] for _ in range(h)]
        self.start_pos = (0, 0)
        self.end_pos = (w - 1, h - 1)
        
        # Initialize Pygame components
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Dynamic Maze Solver Game")
        
        # Font settings
        self.font_small = pygame.font.Font(None, 24)
        self.font_label = pygame.font.Font(None, 30) 
        
        # Game State Variables (Hint/Solver state removed)
        self.running = True
        self.time_text = ""
        
        # Game State for Player Control and Victory
        self.game_won = False  # Tracks if the player has reached the end
        self.player_pos = self.start_pos # Player's current position (tuple)
        
        # State variable to track if the mouse button is held down for continuous movement
        self.mouse_down = False 

        # Generate the maze immediately upon creation
        self.generate_maze()

    # Utility function using a dictionary lookup for neighbors
    def get_neighbors(self, x, y):
        """Returns valid (x, y) coordinates of neighbors."""
        neighbors = []
        # Directions are defined using tuples: (dx, dy, wall_index)
        # Wall indices: 0=Top, 1=Right, 2=Bottom, 3=Left
        for dx, dy, wall_index in [(0, -1, 0), (1, 0, 1), (0, 1, 2), (-1, 0, 3)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.w and 0 <= ny < self.h:
                # Store neighbor coordinates and the index of the wall to break (if needed)
                neighbors.append(((nx, ny), wall_index))
        return neighbors

    # --- 3. MAZE GENERATION (Recursive Backtracker) ---
    def generate_maze(self):
        """
        Dynamically generates a perfect maze using the Recursive Backtracker algorithm.
        """
        # Reset grid for new generation
        self.grid = [[{'walls': [True, True, True, True], 'visited': False} 
                      for _ in range(self.w)] for _ in range(self.h)]
        
        # Start at the top-left corner
        stack = [self.start_pos]
        cx, cy = self.start_pos
        self.grid[cy][cx]['visited'] = True
        
        while stack:
            neighbors = []
            for (nx, ny), wall_index in self.get_neighbors(cx, cy):
                if not self.grid[ny][nx]['visited']:
                    opposite_wall_index = (wall_index + 2) % 4
                    neighbors.append(((nx, ny), wall_index, opposite_wall_index))

            if neighbors:
                (nx, ny), current_wall, neighbor_wall = random.choice(neighbors)
                
                self.grid[cy][cx]['walls'][current_wall] = False
                self.grid[ny][nx]['walls'][neighbor_wall] = False
                
                stack.append((nx, ny))
                cx, cy = nx, ny
                self.grid[cy][cx]['visited'] = True
            else:
                stack.pop()
                if stack:
                    cx, cy = stack[-1]

        # Reset state on regeneration
        self.time_text = ""
        self.game_won = False
        self.player_pos = self.start_pos 
        
    def draw_cell(self, screen, x, y, color):
        """Draws a solid colored square for the cell (used for path/start/end/player)."""
        pygame.draw.rect(screen, color, 
                         (x * CELL_SIZE + 2, y * CELL_SIZE + 2, 
                          CELL_SIZE - 4, CELL_SIZE - 4))

    def draw_label(self, screen, pos, text, color):
        """Helper function to draw centered text label on a cell."""
        x, y = pos
        center_x = x * CELL_SIZE + CELL_SIZE // 2
        center_y = y * CELL_SIZE + CELL_SIZE // 2
        
        text_surf = self.font_label.render(text, True, color)
        text_rect = text_surf.get_rect(center=(center_x, center_y))
        screen.blit(text_surf, text_rect)


    def draw_maze(self):
        """Renders the entire maze grid, walls, and special points to the screen."""
        self.screen.fill(BLACK)
        
        # Draw the grid and walls (using loops and list access)
        for y in range(self.h):
            for x in range(self.w):
                cell = self.grid[y][x]
                
                rect_x, rect_y = x * CELL_SIZE, y * CELL_SIZE
                walls = cell['walls']
                line_width = 2
                
                # Draw Walls
                if walls[0]: pygame.draw.line(self.screen, WHITE, (rect_x, rect_y), (rect_x + CELL_SIZE, rect_y), line_width)
                if walls[1]: pygame.draw.line(self.screen, WHITE, (rect_x + CELL_SIZE, rect_y), (rect_x + CELL_SIZE, rect_y + CELL_SIZE), line_width)
                if walls[2]: pygame.draw.line(self.screen, WHITE, (rect_x, rect_y + CELL_SIZE), (rect_x + CELL_SIZE, rect_y + CELL_SIZE), line_width)
                if walls[3]: pygame.draw.line(self.screen, WHITE, (rect_x, rect_y), (rect_x, rect_y + CELL_SIZE), line_width)

        # Removed: Drawing of the solved path (HINT)

        # Draw the start and end points
        self.draw_cell(self.screen, self.start_pos[0], self.start_pos[1], GREEN)
        self.draw_cell(self.screen, self.end_pos[0], self.end_pos[1], RED)
        
        # Draw Player position
        if self.player_pos != self.end_pos:
             # Draw the player (slightly smaller blue circle for aesthetics)
            px, py = self.player_pos
            center_x = px * CELL_SIZE + CELL_SIZE // 2
            center_y = py * CELL_SIZE + CELL_SIZE // 2
            pygame.draw.circle(self.screen, BLUE, (center_x, center_y), CELL_SIZE // 3)

        # Draw Labels on Start and End Points
        self.draw_label(self.screen, self.start_pos, "START", DARK_GREEN) 
        self.draw_label(self.screen, self.end_pos, "END", WHITE) 

        # Draw the button area and text
        # Regenerate button is now centered at the bottom
        BUTTON_WIDTH = 200
        regenerate_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, SCREEN_HEIGHT - 40, BUTTON_WIDTH, 30)
        
        # Draw the Regenerate Button
        pygame.draw.rect(self.screen, YELLOW, regenerate_rect, border_radius=5)
        regen_text_surf = self.font_small.render("Regenerate Maze", True, BLACK)
        regen_text_rect = regen_text_surf.get_rect(center=regenerate_rect.center)
        self.screen.blit(regen_text_surf, regen_text_rect)

        # Draw the Status Text (moved to the right)
        time_surf = self.font_small.render(self.time_text, True, WHITE)
        self.screen.blit(time_surf, (SCREEN_WIDTH - time_surf.get_width() - 10, SCREEN_HEIGHT - 35))

        # --- Draw Victory Message Overlay ---
        if self.game_won:
            # Create a semi-transparent overlay rectangle
            overlay = pygame.Surface((SCREEN_WIDTH, MAZE_H * CELL_SIZE))
            overlay.set_alpha(200) # 200/255 transparency
            overlay.fill(BLACK)
            self.screen.blit(overlay, (0, 0))
            
            # Draw the congratulations text
            font_congrats = pygame.font.Font(None, 70) 
            congrats_text = "CONGRATULATIONS!"
            # Use the user's requested success message
            message_text = "You have successfully completed the maze!" 
            
            congrats_surf = font_congrats.render(congrats_text, True, YELLOW)
            message_surf = self.font_label.render(message_text, True, WHITE)
            
            congrats_rect = congrats_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))
            message_rect = message_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10))
            
            self.screen.blit(congrats_surf, congrats_rect)
            self.screen.blit(message_surf, message_rect)

        pygame.display.flip()

    # --- 4. MAZE SOLVER (REMOVED) ---
    # The DFS solver function has been removed.
        
    def try_move_player(self, target_pos):
        """
        Attempts to move the player to target_pos if it's adjacent and the path is open.
        This function is called by both single clicks and continuous dragging.
        """
        px, py = self.player_pos
        
        # 1. Check if the move is one cell away (adjacent)
        is_adjacent = abs(target_pos[0] - px) + abs(target_pos[1] - py) == 1
        
        if is_adjacent and target_pos != self.player_pos:
            # Determine which wall separates player and target
            dx = target_pos[0] - px
            dy = target_pos[1] - py
            
            wall_index = -1
            if dx == 1: wall_index = 1  # Moving Right (Wall 1)
            elif dx == -1: wall_index = 3 # Moving Left (Wall 3)
            elif dy == 1: wall_index = 2 # Moving Down (Wall 2)
            elif dy == -1: wall_index = 0 # Moving Up (Wall 0)
            
            # Check if the wall is broken (must be False)
            if wall_index != -1 and not self.grid[py][px]['walls'][wall_index]:
                # Successful move! 
                self.player_pos = target_pos
                
                # Check for Victory Condition
                if self.player_pos == self.end_pos:
                    self.game_won = True
                    self.time_text = "VICTORY!"
                return True
        return False

    # --- 5. MAIN GAME LOOP AND INTERACTION ---
    def run(self):
        """The main game loop, handling events and drawing."""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                # --- MOUSE DOWN: Start Dragging or Handle Button Clicks ---
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: # Left click
                        self.mouse_down = True
                        mouse_x, mouse_y = event.pos
                        
                        # Regenerate button coordinates moved to the center
                        BUTTON_WIDTH = 200
                        regenerate_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, SCREEN_HEIGHT - 40, BUTTON_WIDTH, 30)

                        # Check for interaction with the Regenerate Button
                        if regenerate_rect.collidepoint(mouse_x, mouse_y):
                            print("Regenerate button clicked!")
                            self.generate_maze()
                            
                        # Handle single-click movement (if click is in the maze area)
                        elif mouse_y < SCREEN_HEIGHT - 50 and not self.game_won: 
                            cell_x = mouse_x // CELL_SIZE
                            cell_y = mouse_y // CELL_SIZE
                            target_pos = (cell_x, cell_y)
                            
                            self.try_move_player(target_pos)
                            
                # --- MOUSE UP: Stop Dragging ---
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.mouse_down = False
                        
                # --- MOUSE MOTION: Continuous Dragging Movement ---
                if event.type == pygame.MOUSEMOTION:
                    # Only move if the button is down AND the game is active
                    if self.mouse_down and not self.game_won: 
                        mouse_x, mouse_y = event.pos
                        
                        # Only check for movement if cursor is within the maze grid
                        if mouse_y < MAZE_H * CELL_SIZE:
                            cell_x = mouse_x // CELL_SIZE
                            cell_y = mouse_y // CELL_SIZE
                            target_pos = (cell_x, cell_y)
                            
                            # Attempt to move the player to the cell the mouse is over
                            self.try_move_player(target_pos)
                            
            # Always draw the maze
            self.draw_maze()
            
            # Small delay to keep CPU usage low
            pygame.time.Clock().tick(60)

        pygame.quit()

# --- 6. EXECUTION BLOCK ---
if __name__ == "__main__":
    # Create an instance of the class and run the game
    game = Maze(MAZE_W, MAZE_H)
    game.run()