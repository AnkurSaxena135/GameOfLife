"""
Implementation of Game Of Life

Usage:
>>> alive_cells = [(2, 1), (2, 3), (0, 2), (2, 2), (1, 3)]
>>> GameOfLife(10, alive_cells).run(10)
"""
DEAD = 0
ALIVE = 1
EIGHT_NEIGHBOURS = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
]


class GameOfLife(object):
    def __init__(self, size: int, alive_cells: list):
        """Create a SQUARE board of dimension (size x size)
        All cells except those in alive_cells are initialized to DEAD.

        Args:
            size: length of side for a Square board
            alive_cells: list of x,y coordinates for alive cells
                e.g. [(1,1), (1,2)]
        """
        self._grid_size = (size, size)
        self._board = [[DEAD for _ in range(size)] for _ in range(size)]
        self._alive_cells = set(alive_cells)
        self._update_board(self._alive_cells, ALIVE)

    @property
    def alive_cells(self):
        """list: alive cells in current generation"""
        return self._alive_cells

    def run(self, generations: int = 10):
        """Simulate for given number of generations
        Args:
            generations: number of generations to simulate
        """
        for _ in range(generations):
            self.print_board()
            self.next_generation()

    def next_generation(self):
        """Move forward one generation. Iterates through possible
        candidate cells based on current state and applies
        the check whether they'll be alive in next generation as well.

        Once alive cells for next generation are selected,
        existing ones are set to DEAD and new ones are set to ALIVE.

        """
        new_alive_cells = set()
        current_alive_cells = self._alive_cells
        board = self._board

        for cell, count in self._traverse(
            unvisited=current_alive_cells.copy(),  # current living cells (a copy, to maintain state)
            visited=set(),  # empty set
        ):
            if not cell and not count:
                break
            r, c = cell
            # Survival conditions
            if (board[r][c] == DEAD and count == 3) or (
                board[r][c] == ALIVE and count in [2, 3]
            ):
                new_alive_cells.add(cell)
        # Update state ONLY after new generation is selected
        self._update_board(current_alive_cells, DEAD)
        self._update_board(new_alive_cells, ALIVE)
        self._alive_cells = new_alive_cells

    def print_board(self):
        """Print board to console"""
        for row in self._board:
            print(row)
        print("-----------------------------------------------------------------------")

    def _update_board(self, cells: list, state: int):
        """Update state of cells to given state.
        Ignores incorrect cell coordinates
        Args:
            cells: list of cells
            state: ALIVE/DEAD
        """
        board = self._board
        out_of_bound_cells = []
        for r, c in cells:
            try:
                board[r][c] = state
            except IndexError:
                out_of_bound_cells.append((r, c))
                continue
        # Remove cells that are out of bound
        for cell in out_of_bound_cells:
            cells.remove(cell)

    def _get_neighbours(self, cell):
        """Get neighbours of the cell
        Args:
            cell: cell coordinates
        Returns:
            (list of neighbours, count of alive neighbours)
        """
        board = self._board
        r, c = cell
        count = 0
        neighbours = []
        for r1, c1 in EIGHT_NEIGHBOURS:
            n_r, n_c = r + r1, c + c1  # neighbour cell indices
            # boundary conditions for square board
            if min(n_r, n_c) < 0 or max(n_r, n_c) > len(board) - 1:
                continue
            if board[n_r][n_c] == ALIVE:
                count += 1
            neighbours.append((n_r, n_c))
        return neighbours, count

    def _traverse(self, unvisited: set, visited: set):
        """Traverse through matrix to get candidate cells for next
        generation - current alive cells and their neighbours
        Args:
            unvisited: set of cells waiting to be visited
            visited: set of cells already visited
        Returns:
            (candidate cell, count of alive neighbours)
        """
        board = self._board
        if not unvisited:
            return None, None

        curr = unvisited.pop()
        visited.add(curr)
        neighbours, count = self._get_neighbours(curr)
        yield curr, count

        r, c = curr
        if board[r][c] == ALIVE:
            for n in neighbours:
                if n not in visited:
                    unvisited.add(n)

        yield from self._traverse(unvisited, visited)


if __name__ == "__main__":
    alive_cells = [(2, 1), (2, 3), (0, 2), (2, 2), (1, 3)]
    GameOfLife(10, alive_cells).run(10)
