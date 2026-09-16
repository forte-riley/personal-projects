class Grid:
    def __init__(self, width, height):
        """Assigns the dimensions of the array."""
        self.width = width
        self.height = height

        self.array = [['-' for _ in range(width)] for _ in range(height)]

    def in_bounds(self, x, y):
        """checks that given x and y are within bound of the array"""
        if 0 <= x < self.width and 0 <= y < self.height:
            return True
        else:
            return False

    def get(self, x, y):
        """Gets row and then returns the x value through indexing"""
        if self.in_bounds(x, y):
            array = self.array
            row = array[y]
            return row[x]
        else:
            raise IndexError

    def set(self, x, y, val):
        """This function checks if an x and y value are within the range.
        If they are, it uses indexing to locate the value corresponding to the
        given x and y and saves it as the input value."""
        if 0 <= x < self.width and 0 <= y < self.height:
            array = self.array
            row = array[y]
            row[x] = val
        else:
            raise IndexError

    def __str__(self):
        """Join each row with a space, and each row with a newline"""
        return '\n'.join(' '.join(str(cell) for cell in row) for row in self.array)


def get_move(grid):
    move = input("Enter the coordinates you would like to ""play: (ex: 1,1 or 2,3)"
                 " or type 'exit' to exit. ")
    if move == 'exit':
        return False
    x, y = move.split(',')
    x = int(x) - 1
    y = int(y) - 1
    sym = input("What symbol would you like to enter? ")
    if grid.in_bounds(x, y):
        grid.set(x, y, sym)
    if not grid.in_bounds(x,y):
        print("Coordinates not in bounds.")
    print(grid)


def main():
    try:
        dim = input("What would you like 'n' to be for your nxn board? ")
        dim = int(dim)
        grid = Grid(dim, dim)
        while True:
            val = get_move(grid)
            if val is False:
                print("Thank you for playing!")
                break

    except ValueError as e:
        print(f"{e}: please enter integer")


if __name__ == '__main__':
    main()
