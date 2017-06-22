import argparse
import math
import random
import time
from itertools import combinations


class QueenBoard:

    def __init__(self, size=8, queens=None):
        self.size, self.queens = size, queens or size
        self._generate_random_state()

    def _generate_random_state(self):
        # No two queens will share a column
        xs = random.sample(range(self.size), self.queens)
        self.state = {(i, random.randrange(self.size)) for i in xs}

    @staticmethod
    def count_attacks(queens):
        return sum(x0 == x1 or y0 == y1 or x0 + y0 == x1 + y1 or y0 - x0 == y1 - x1
                   for (x0, y0), (x1, y1) in combinations(queens, 2))

    def attacks(self):
        return QueenBoard.count_attacks(self.state)

    def next_state(self):
        # Move a random queen up or down
        (x, y) = random.choice(tuple(self.state))
        while True:
            new = (x, (y + random.randrange(self.size)) % self.size)
            if new not in self.state:
                break

        return self.state ^ {(x, y), new}

    def __str__(self):
        cells = '\n'.join(' '.join('Q' if (i, j) in self.state else '-'
                          for i in range(self.size)) for j in range(self.size))
        return f'QueenBoard({self.size}x{self.size}, {self.queens} queens,\n{cells}\n)'


def accept_move(temperature, delta):
    return delta <= 0 or random.random() < math.exp(-delta / temperature)


def simulated_annealing(board, temperature=40, cooling_factor=0.001,
                               freezing_temperature=0, max_steps=None):
    current_energy = board.attacks()
    step = 0

    if max_steps is None:
        max_steps = math.inf

    while temperature > freezing_temperature and step < max_steps:
        neighbour = board.next_state()
        energy = QueenBoard.count_attacks(neighbour)
        delta = energy - current_energy

        if accept_move(temperature, delta):
            current_energy = energy
            board.state = neighbour

        if current_energy <= 0:
            break

        temperature -= cooling_factor
        step += 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--board-size', type=int, default=8)
    parser.add_argument('--queens', type=int)
    args = parser.parse_args()

    board = QueenBoard(args.board_size, args.queens)
    print('Initial arrangement:', board, sep='\n\n', end='\n\n')
    print('Energy (initial):', board.attacks(), end='\n\n')

    start = time.perf_counter()
    simulated_annealing(board)
    elapsed = time.perf_counter() - start

    print('Optimal arrangement:', board, sep='\n\n', end='\n\n')
    print('Energy (optimal):', board.attacks())
    print(f'Elapsed time: {elapsed:.4f} seconds')
