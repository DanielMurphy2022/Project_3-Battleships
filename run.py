import random

class Ship:
    def __init__(self, size):
        self.size = size
        self.hits = 0

    def is_sunk(self):
        return self.hits == self.size

class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [['O'] * size for _ in range(size)]  # Initialize the grid with 'O's representing empty cells
        self.ships = []  # List to store information about placed ships

    def place_ship(self, ship):
        while True:
            direction = random.choice(['horizontal', 'vertical'])  # Randomly choose ship direction
            if direction == 'horizontal':
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - ship.size)
                # Check if there's enough space to place the ship horizontally without overlapping
                if all(self.grid[row][col+i] == 'O' for i in range(ship.size)):
                    for i in range(ship.size):
                        self.grid[row][col+i] = 'S'  # Place the ship on the grid
                    self.ships.append((row, col, 'horizontal', ship))  # Add ship information to the list
                    break
            else:
                row = random.randint(0, self.size - ship.size)
                col = random.randint(0, self.size - 1)
                # Check if there's enough space to place the ship vertically without overlapping
                if all(self.grid[row+i][col] == 'O' for i in range(ship.size)):
                    for i in range(ship.size):
                        self.grid[row+i][col] = 'S'  # Place the ship on the grid
                    self.ships.append((row, col, 'vertical', ship))  # Add ship information to the list
                    break

    def print_hidden(self):
        print("  " + " ".join(str(i) for i in range(self.size)))  # Print column numbers
        for i in range(self.size):
            print("{} {}".format(i, " ".join(self.grid[i])))  # Print each row of the grid

    def print_board(self):
        print("  " + " ".join(str(i) for i in range(self.size)))  # Print column numbers
        for i in range(self.size):
            print("{} {}".format(i, " ".join('X' if cell == 'H' else cell for cell in self.grid[i])))  # Print each row of the grid, hiding ships' locations


class BattleshipsGame: