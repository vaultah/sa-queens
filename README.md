# SA-Queens

Python implementation of the [Simulated Annealing](https://en.wikipedia.org/wiki/Simulated_annealing) algorithm for solving the [N queens problem](https://en.wikipedia.org/wiki/Eight_queens_puzzle).

Example output for the eight queens puzzle:

```
Initial arrangement:
QueenBoard(8x8, 8 queens,
- - - - - - - -
- - - - - - - -
- - - - - - - -
- - - Q - - Q -
- - - - Q - - -
Q - - - - Q - -
- - - - - - - Q
- Q Q - - - - -
)

Energy (initial): 9

Optimal arrangement:

QueenBoard(8x8, 8 queens,
- - - - - - - Q
- Q - - - - - -
- - - - Q - - -
- - Q - - - - -
Q - - - - - - -
- - - - - - Q -
- - - Q - - - -
- - - - - Q - -
)

Energy (optimal): 0
Elapsed time: 0.2252 seconds
```
