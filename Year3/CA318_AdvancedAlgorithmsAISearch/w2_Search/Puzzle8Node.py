class Node:
    def __init__(self, name, children):
        self.name = name
        self.children = children

    def __str__(self):
        return self.name
        #return "N({0}, {1})".format(self.name, self.children)

    def __repr__(self):
        return str(self)

    def get_children(self):
        return self.children

    # See https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes

    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self.name == other.name
        return NotImplemented

    def __ne__(self, other):
        """Define a non-equality test"""
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        """Override the default hash behavior (that returns the id or the object)"""
        return hash(tuple(sorted(self.__dict__.items())))

class Move:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __str__(self):
        return "({0}, {1})".format(self.row, self.col)

class Puzzle8Node(Node):
    def __init__(self, name, parent=None):
        # The name will be the square
        # The name should only contain the numbers 1 to 8 and a blank
        assert "".join(sorted(name)) == " 12345678"
        self.name = name
        self.parent = parent

    def __str__(self):
        s = ""
        board = self.make_board(self.name)
        for row in range(3):
            for col in range(3):
                if col == 0: s += '\t'
                s += board[row][col]
            s += '\n'
        return s

    def make_board(self, name):
        board = [ ['-' for c in range(3)] for r in range(3)]
        index = 0
        for row in range(3):
            for col in range(3):
                board[row][col] = self.name[index]
                index += 1

        return board

    def make_name(self, board):
        name = ''
        for row in range(3):
            for col in range(3):
                name += board[row][col]

        return name

    def get_blank(self, board):
        # Find the blank
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    return Move(row, col)

        return None # Error, this shouldn't happen. 

    def get_children(self):
        # The children are just the moves.
        children = self.get_moves()
        for child in children:
            child.parent = self
        return children

    def get_parent(self):
        return self.parent

    def get_path(self):
        path = [self]
        child = self
        while child.get_parent() != None:
            child = child.get_parent()
            path.append(child)
        return path

    def check_path(path):
        # return true/false depending on whether the path is valid or not.
        # since child must be in parent's get_moves() aka parent's child, we check if child is there or not
        i = 0
        while i < len(path) - 1:
            currChild = path[i]
            currParent = path[i+1]
            if currChild not in currParent.get_moves():
                return False
            i += 1
        return True

    def get_moves(self):
        # The moves depend on the current board position
        # Lets make the board
        board = self.make_board(self.name)
        blank = self.get_blank(board)

        # Now make the moves. There could be 4
        moves = []
        if blank.col != 0:
            # LEFT
            board[blank.row][blank.col-1], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row][blank.col-1]
            # Convert board to a name and append to moves
            moves.append(self.make_name(board))
            # swap back to undo the move
            board[blank.row][blank.col-1], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row][blank.col-1]
        if blank.row != 0: # Can't move up if already at the top
            # UP
            # swap blank and position above it
            board[blank.row-1][blank.col], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row-1][blank.col]
            # Convert board to a name and append to moves
            moves.append(self.make_name(board))
            board[blank.row-1][blank.col], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row-1][blank.col]
        if blank.col != 2:
            # RIGHT
            board[blank.row][blank.col+1], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row][blank.col+1]
            # Convert board to a name and append to moves
            moves.append(self.make_name(board))
            board[blank.row][blank.col+1], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row][blank.col+1]
        if blank.row != 2:
            # Down
            board[blank.row+1][blank.col], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row+1][blank.col]
            # Convert board to a name and append to moves
            moves.append(self.make_name(board))
            board[blank.row+1][blank.col], board[blank.row][blank.col] = board[blank.row][blank.col], board[blank.row+1][blank.col]

        return [Puzzle8Node(move) for move in moves]

    def test(self):
        p = Puzzle8Node('2831647 5') # Lugar fig 3.17
        moves = p.get_moves()

        assert len(moves) == 3
        assert moves == [Puzzle8Node(move) for move in ['283164 75', '2831 4765', '28316475 ']]

        p = Puzzle8Node('1234 5678')
        moves = p.get_moves()
        assert len(moves) == 4
        # print(moves)
        assert moves == [ Puzzle8Node(move) for move in ['123 45678', '1 3425678', '12345 678', '1234756 8'] ]
        print(p.get_parent())


def main():
    Puzzle8Node('2831647 5').test()

if __name__ == "__main__":
    main()
