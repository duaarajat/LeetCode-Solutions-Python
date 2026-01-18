import pygame
import random

# ==============================================================================
# I. CONFIGURATION & COLOR PALETTE (Simplified)
# ==============================================================================

# --- Core Dimensions ---
CELL_SIZE = 40      # Size of each cell in pixels (e.g., 40x40)
MAZE_W = 15         # Maze width (number of cells)
MAZE_H = 10         # Maze height (number of cells)
BUTTON_AREA_HEIGHT = 50

# Calculate screen dimensions
SCREEN_WIDTH = MAZE_W * CELL_SIZE
SCREEN_HEIGHT = MAZE_H * CELL_SIZE + BUTTON_AREA_HEIGHT

# --- Color Palette (Standard RGB Tuples) ---
NAVY_BG = (72, 61, 139)       # Dark Slate Blue (Main background)
CYAN_WALL = (0, 255, 255)     # Cyan (Wall color)
NEON_GREEN_START = (0, 255, 127) # Spring Green (Start point)
VIOLET_END = (138, 43, 226)   # Dark Violet (End point)
BLACK_PLAYER = (0, 0, 0)      # Player color
BRIGHT_PINK = (255, 20, 147)  # Deep Pink (Button/Victory color)
WHITE = (255, 255, 255)       # General text color

# ==============================================================================
# II. MAZE CLASS DEFINITION
# ==============================================================================

class Maze:
    """
    Manages the maze environment, generation, player movement, and drawing.
    Uses standard Python types for simplicity.
    """
    def __init__(self, w_cells, h_cells):
        self.w = w_cells
        self.h = h_cells
        
        self.start_pos = (0, 0)
        self.end_pos = (self.w - 1, self.h - 1)
        self.player_pos = self.start_pos 
        
        # --- Pygame Setup ---
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Simple Dynamic Maze Game")
        self.clock = pygame.time.Clock() 
        
        # Font definitions
        self.font_small = pygame.font.Font(None, 28) 
        self.font_label = pygame.font.Font(None, 18) 
        
        # --- Game State Variables ---
        self.running = True
        self.status_text = "Click to regenerate!" # Simplified status text
        self.game_won = False      
        self.mouse_down = False    # Tracking if the left mouse button is pressed

        # Generate the very first maze
        self.generate_maze()
        
    # --------------------------------------------------------------------------
    # A. Maze Generation Core Logic (Recursive Backtracker)
    # --------------------------------------------------------------------------

    def get_neighbors(self, x, y):
        """Calculates all valid neighbors of a cell (x, y)."""
        neighbors = []
        # Movement vectors: (dx, dy, wall_index)
        # Wall Indices: 0: Up, 1: Right, 2: Down, 3: Left
        movements = [(0, -1, 0), (1, 0, 1), (0, 1, 2), (-1, 0, 3)]
        
        for dx, dy, wall_index in movements:
            nx, ny = x + dx, y + dy
            # Check boundaries
            if 0 <= nx < self.w and 0 <= ny < self.h:
                neighbors.append(((nx, ny), wall_index))
        return neighbors

    def generate_maze(self):
        """Creates a perfect maze using the Recursive Backtracker algorithm."""
        
        # Reset the grid: all walls up, all cells unvisited
        # Grid structure: [{'walls': [Up, Right, Down, Left], 'visited': False}]
        self.grid = [[{'walls': [True] * 4, 'visited': False} 
                      for _ in range(self.w)] for _ in range(self.h)]
        
        stack = [self.start_pos]
        cx, cy = self.start_pos 
        self.grid[cy][cx]['visited'] = True
        
        while stack:
            unvisited_neighbors = []
            
            # Find unvisited neighbors and calculate wall indices
            for (nx, ny), current_wall in self.get_neighbors(cx, cy):
                if not self.grid[ny][nx]['visited']:
                    # Neighbor's wall index is opposite of current cell's wall index
                    neighbor_wall = (current_wall + 2) % 4
                    unvisited_neighbors.append(((nx, ny), current_wall, neighbor_wall))

            if unvisited_neighbors:
                # Pick a random neighbor
                (nx, ny), current_wall, neighbor_wall = random.choice(unvisited_neighbors)
                
                # Break the walls!
                self.grid[cy][cx]['walls'][current_wall] = False
                self.grid[ny][nx]['walls'][neighbor_wall] = False
                
                # Move to the new cell
                stack.append((nx, ny))
                cx, cy = nx, ny
                self.grid[cy][cx]['visited'] = True
            else:
                # Dead end - backtrack
                if stack:
                    cx, cy = stack.pop()
        
        # Reset player and status after regeneration
        self.status_text = "Maze Ready! Drag the player to the END."
        self.game_won = False
        self.player_pos = self.start_pos 
        
    # --------------------------------------------------------------------------
    # B. Drawing Functions (Pygame Graphics)
    # --------------------------------------------------------------------------

    def _get_cell_screen_coords(self, x, y):
        """Helper to get the top-left screen coordinate of a cell."""
        return x * CELL_SIZE, y * CELL_SIZE
        
    def draw_cell_fill(self, x, y, color):
        """Draws a solid colored square inside the cell borders."""
        rect_x, rect_y = self._get_cell_screen_coords(x, y)
        # Draw a rectangle slightly smaller than the cell size for a nice effect
        pygame.draw.rect(self.screen, color, 
                         (rect_x + 2, rect_y + 2, 
                          CELL_SIZE - 4, CELL_SIZE - 4))

    def draw_label(self, pos, text, color):
        """Helper function to draw centered text label on a cell."""
        x, y = pos
        rect_x, rect_y = self._get_cell_screen_coords(x, y)
        
        center_x = rect_x + CELL_SIZE // 2
        center_y = rect_y + CELL_SIZE // 2
        
        text_surf = self.font_label.render(text, True, color)
        text_rect = text_surf.get_rect(center=(center_x, center_y))
        self.screen.blit(text_surf, text_rect)

    def draw_maze(self):
        """Renders the entire maze grid, walls, and game elements."""
        self.screen.fill(NAVY_BG) 
        
        # --- Draw Grid and Walls ---
        line_width = 2
        for y in range(self.h):
            for x in range(self.w):
                cell = self.grid[y][x]
                rect_x, rect_y = self._get_cell_screen_coords(x, y)
                walls = cell['walls']
                
                # Wall drawing logic (Up, Right, Down, Left)
                if walls[0]: # Up
                    pygame.draw.line(self.screen, CYAN_WALL, (rect_x, rect_y), (rect_x + CELL_SIZE, rect_y), line_width)
                if walls[1]: # Right
                    pygame.draw.line(self.screen, CYAN_WALL, (rect_x + CELL_SIZE, rect_y), (rect_x + CELL_SIZE, rect_y + CELL_SIZE), line_width)
                if walls[2]: # Down
                    pygame.draw.line(self.screen, CYAN_WALL, (rect_x, rect_y + CELL_SIZE), (rect_x + CELL_SIZE, rect_y + CELL_SIZE), line_width)
                if walls[3]: # Left
                    pygame.draw.line(self.screen, CYAN_WALL, (rect_x, rect_y), (rect_x, rect_y + CELL_SIZE), line_width)

        # --- Draw Start/End Points and Labels ---
        self.draw_cell_fill(self.start_pos[0], self.start_pos[1], NEON_GREEN_START)
        self.draw_cell_fill(self.end_pos[0], self.end_pos[1], VIOLET_END)     
        
        self.draw_label(self.start_pos, "START", NAVY_BG)
        self.draw_label(self.end_pos, "END", WHITE)  

        # --- Draw Player ---
        if not self.game_won:
            px, py = self.player_pos
            rect_x, rect_y = self._get_cell_screen_coords(px, py)
            center_x = rect_x + CELL_SIZE // 2
            center_y = rect_y + CELL_SIZE // 2
            # Draw a black circle for the player
            pygame.draw.circle(self.screen, BLACK_PLAYER, (center_x, center_y), CELL_SIZE // 3)

        # --- Draw Button and Status Area ---
        self.draw_button_and_status()
        
        # --- Draw Victory Message Overlay ---
        if self.game_won:
            self.draw_victory_overlay()

        pygame.display.flip()
        
    def draw_button_and_status(self):
        """Renders the regenerate button and game status text at the bottom."""
        BUTTON_WIDTH = 250 
        # Define the rectangle for the button
        self.regenerate_rect = pygame.Rect((SCREEN_WIDTH - BUTTON_WIDTH) // 2, 
                                            SCREEN_HEIGHT - 40, 
                                            BUTTON_WIDTH, 35)

        # Draw the button itself
        pygame.draw.rect(self.screen, BRIGHT_PINK, self.regenerate_rect, border_radius=8)
        
        # Draw the button text
        regen_text_surf = self.font_small.render("REGENERATE MAZE", True, NAVY_BG)
        regen_text_rect = regen_text_surf.get_rect(center=self.regenerate_rect.center)
        self.screen.blit(regen_text_surf, regen_text_rect)

        # Draw the Status Text
        status_surf = self.font_small.render(self.status_text, True, WHITE)
        self.screen.blit(status_surf, (SCREEN_WIDTH - status_surf.get_width() - 10, SCREEN_HEIGHT - 35))

    def draw_victory_overlay(self):
        """Draws the transparent overlay and congratulations text upon winning."""
        # Create a semi-transparent surface
        overlay = pygame.Surface((SCREEN_WIDTH, MAZE_H * CELL_SIZE))
        overlay.set_alpha(220) 
        overlay.fill(NAVY_BG) 
        self.screen.blit(overlay, (0, 0))
        
        # Draw the congratulations text
        font_congrats = pygame.font.Font(None, 80)
        congrats_text = "CONGRATULATIONS!"
        message_text = "You have successfully completed the maze!" 
        
        congrats_surf = font_congrats.render(congrats_text, True, BRIGHT_PINK)
        message_surf = self.font_label.render(message_text, True, WHITE)
        
        # Center the text
        center_y_maze = (MAZE_H * CELL_SIZE) // 2
        
        congrats_rect = congrats_surf.get_rect(center=(SCREEN_WIDTH // 2, center_y_maze - 45))
        message_rect = message_surf.get_rect(center=(SCREEN_WIDTH // 2, center_y_maze + 5))
        
        self.screen.blit(congrats_surf, congrats_rect)
        self.screen.blit(message_surf, message_rect)

    # --------------------------------------------------------------------------
    # C. Player Movement Logic
    # --------------------------------------------------------------------------
        
    def try_move_player(self, target_pos):
        """
        Attempts to move the player to target_pos if it's adjacent and the wall is down.
        """
        if self.game_won:
            return False

        px, py = self.player_pos
        tx, ty = target_pos
        
        # 1. Check if the move is one cell away
        is_adjacent = abs(tx - px) + abs(ty - py) == 1
        
        if is_adjacent:
            dx = tx - px
            dy = ty - py
            
            # Determine the wall index in the current cell's walls list
            wall_index = -1
            if dx == 1: wall_index = 1    # Moving Right
            elif dx == -1: wall_index = 3 # Moving Left
            elif dy == 1: wall_index = 2  # Moving Down
            elif dy == -1: wall_index = 0 # Moving Up
            
            # 2. Check the wall status: A path is open if the wall value is False
            if wall_index != -1 and not self.grid[py][px]['walls'][wall_index]:
                # SUCCESS! Update player position
                self.player_pos = target_pos
                
                # 3. Check for Victory Condition
                if self.player_pos == self.end_pos:
                    self.game_won = True
                    self.status_text = "VICTORY!"
                return True
                
        return False

    # --------------------------------------------------------------------------
    # D. Main Game Loop and Event Handling
    # --------------------------------------------------------------------------

    def run(self):
        """The main game loop."""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                # --- MOUSE DOWN: Start Dragging or Handle Button Clicks ---
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mouse_down = True
                    mouse_x, mouse_y = event.pos
                    
                    # 1. Check for Regenerate Button click
                    if self.regenerate_rect.collidepoint(mouse_x, mouse_y):
                        self.generate_maze()
                        
                    # 2. Handle single-click movement (if click is in the maze area)
                    elif mouse_y < (MAZE_H * CELL_SIZE): 
                        cell_x = mouse_x // CELL_SIZE
                        cell_y = mouse_y // CELL_SIZE
                        self.try_move_player((cell_x, cell_y))
                            
                # --- MOUSE UP: Stop Dragging ---
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouse_down = False
                        
                # --- MOUSE MOTION: Continuous Dragging Movement ---
                if event.type == pygame.MOUSEMOTION:
                    if self.mouse_down and not self.game_won: 
                        mouse_x, mouse_y = event.pos
                        
                        # Only check for movement if cursor is within the maze grid
                        if mouse_y < (MAZE_H * CELL_SIZE):
                            cell_x = mouse_x // CELL_SIZE
                            cell_y = mouse_y // CELL_SIZE
                            self.try_move_player((cell_x, cell_y))
                            
            # Always draw the maze elements in every frame
            self.draw_maze()
            
            # Limit the framerate
            self.clock.tick(60)

        # Cleanly shut down Pygame
        pygame.quit()

# ==============================================================================
# III. EXECUTION BLOCK
# ==============================================================================

if __name__ == "__main__":
    try:
        game = Maze(MAZE_W, MAZE_H)
        game.run()
    except Exception as e:
        print(f"An error occurred during game execution: {e}")
        pygame.quit()