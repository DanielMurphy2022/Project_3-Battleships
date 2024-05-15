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
    def __init__(self):
        self.size = 0
        self.board = None
        self.player_board = None
        self.computer_board = None

    def setup(self):
        self.size = int(input("Enter the grid size: "))  # Get grid size from user input
        self.board = Board(self.size)  # Initialize game boards
        self.player_board = Board(self.size)
        self.computer_board = Board(self.size)
        ships = [Ship(5), Ship(4), Ship(3), Ship(3), Ship(2)]  # Create ships of different sizes
        for ship in ships:
            self.board.place_ship(ship)  # Place ships on the game board

    def player_turn(self):
        print("Your Turn!")
        self.player_board.print_board()  # Print player's board
        while True:
            try:
                guess_row = int(input("Guess Row (0 - {}): ".format(self.size - 1)))  # Get player's guess for row
                guess_col = int(input("Guess Col (0 - {}): ".format(self.size - 1)))  # Get player's guess for column

                if guess_row < 0 or guess_row >= self.size or guess_col < 0 or guess_col >= self.size:
                    print("Oops, that's off the grid. Try again.")  # Check if guess is out of bounds
                    continue

                if self.computer_board.grid[guess_row][guess_col] == 'X' or self.computer_board.grid[guess_row][guess_col] == 'H':
                    print("You've already guessed that. Try again.")  # Check if guess has already been made
                    continue

                if self.computer_board.grid[guess_row][guess_col] == 'S':
                    print("Congratulations! You hit a ship!")  # Check if player's guess hit a ship
                    self.computer_board.grid[guess_row][guess_col] = 'H'
                    for row, col, direction, ship in self.computer_board.ships:
                        if direction == 'horizontal':
                            if row == guess_row and col <= guess_col < col + ship.size:
                                ship.hits += 1
                                if ship.is_sunk():
                                    print("You've sunk a ship!")  # Check if a ship has been sunk
                                break
                        else:
                            if col == guess_col and row <= guess_row < row + ship.size:
                                ship.hits += 1
                                if ship.is_sunk():
                                    print("You've sunk a ship!")  # Check if a ship has been sunk
                                break
                else:
                    print("You missed!")  # Player missed the ship
                    self.computer_board.grid[guess_row][guess_col] = 'X'
                break
            except ValueError:
                print("Please enter a valid number.")  # Handle invalid input