import pygame

# Initialize Pygame
pygame.init()

# Board dimensions
board_width, board_height = 800, 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((board_width, board_height))
pygame.display.set_caption("Legends of Runeterra Board")

# Board class
class Board:
    def __init__(self):
        self.background_color = white
        self.hand_zone = pygame.Rect(50, 500, 700, 100)  # Rect for player's hand zone
        self.deck_zone = pygame.Rect(700, 200, 50, 100)  # Rect for player's deck zone
        self.battlefield_zone = pygame.Rect(50, 50, 700, 400)  # Rect for the battlefield zone

        self.slots = []
        self.create_slots()

    def create_slots(self):
        slot_width, slot_height = 100, 150
        for x in range(6):
            player_slot = pygame.Rect(self.battlefield_zone.left + (x * slot_width), self.battlefield_zone.bottom, slot_width, slot_height)
            opponent_slot = pygame.Rect(self.battlefield_zone.left + (x * slot_width), self.battlefield_zone.top - slot_height, slot_width, slot_height)
            self.slots.append(player_slot)
            self.slots.append(opponent_slot)

    def draw_board(self):
        screen.fill(self.background_color)

        # Draw zones on the board
        pygame.draw.rect(screen, black, self.hand_zone, 2)
        pygame.draw.rect(screen, black, self.deck_zone, 2)
        pygame.draw.rect(screen, black, self.battlefield_zone, 2)

        # Draw slots on the battlefield
        for slot in self.slots:
            pygame.draw.rect(screen, black, slot, 1)

# Main game loop
running = True
board = Board()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the game board
    board.draw_board()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()





