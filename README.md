# GameOfLife
Simple [Game of life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) implementation in python.

Directory structure

```

    ├── README.md               <- The top-level README for developers using this project.

    ├── requirements.txt        <- python requirements.
    |
    ├── game_of_life            <- Source code
    │   ├── game_of_life.py     <- main class
    │   └── init_state.txt      <- initial state pattern file
    └── test                    <- unit tests
```

## How it works

1. Paste the patern of first generationalive cells in file `init_state.txt`. Use `0` for DEAD cells and `1` for ALIVE cells.
2. Default board shape is SQUARE and board size is 25 x 25.
3. You can simulate the next generations by executing the code.

