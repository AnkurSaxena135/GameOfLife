# GameOfLife
Simple [Game of life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) implementation in python.

Directory structure

```

    ├── README.md               <- The top-level README for developers using this project.
    |
    ├── requirements.txt        <- python requirements.
    |
    ├── Dockerfile              <- dockerfile
    |
    ├── game_of_life            <- Source code
    │   ├── game_of_life.py     <- main class
    │   └── init_state.txt      <- initial state pattern file
    └── test                    <- unit tests
```

## How it works

1. Paste the patern of first generationalive cells in file `init_state.txt`. Use `0` for DEAD cells and `1` for ALIVE cells.
2. Default board shape is SQUARE and board size is 25 x 25.
3. Simulate the next generations by executing the code on a docker container.


## Steps to run

1. Clone the repo at tag `v1.0.0`: `git clone --depth 1 --branch v1.0.0 https://github.com/AnkurSaxena135/GameOfLife.git`
2. Change directory to `GameOfLife`
3. Paste the pattern in `game_of_life/init_pattern.txt` file.
4. Build the docker image: `docker build . -t game-of-life`
5. Run image in interactive shell to view output on console: `docker run --rm -it  game-of-life:latest`


## Interacting with package

### Package CLI

Cli for the package is as follows

```
usage: game_of_life.py [-h] [--size SIZE] gens

Game of life simulation

positional arguments:
  gens         number of generations to simulate

optional arguments:
  -h, --help   show help message and exit
  --size SIZE  board size
```

### Docker commands 

+ **Example 1**: To run 20 generations, for board size 5 command is: `docker run --rm -it  game-of-life:latest --size 5 20`
+ **Example 2**: To run 10 generations, for board size 25 command is: `docker run --rm -it  game-of-life:latest --size 25 10`

## NOTE
 For every change in `init_pattern.txt`, new build is required.



## Sample output for Glider pattern:
```
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 0, 0]
[0, 1, 0, 1, 0, 0]
[0, 0, 1, 1, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
-----------------------------------------------------------------------
[0, 0, 0, 0, 0, 0]
[0, 0, 1, 0, 0, 0]
[0, 0, 0, 1, 1, 0]
[0, 0, 1, 1, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
-----------------------------------------------------------------------
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 0, 0]
[0, 0, 0, 0, 1, 0]
[0, 0, 1, 1, 1, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
-----------------------------------------------------------------------
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 1, 0, 1, 0]
[0, 0, 0, 1, 1, 0]
[0, 0, 0, 1, 0, 0]
[0, 0, 0, 0, 0, 0]
-----------------------------------------------------------------------
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0]
[0, 0, 1, 0, 1, 0]
[0, 0, 0, 1, 1, 0]
[0, 0, 0, 0, 0, 0]
-----------------------------------------------------------------------
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 0, 0]
[0, 0, 0, 0, 1, 1]
[0, 0, 0, 1, 1, 0]
[0, 0, 0, 0, 0, 0]
-----------------------------------------------------------------------
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 0, 1]
[0, 0, 0, 1, 1, 1]
[0, 0, 0, 0, 0, 0]
-----------------------------------------------------------------------
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 0, 1]
[0, 0, 0, 0, 1, 1]
[0, 0, 0, 0, 1, 0]
-----------------------------------------------------------------------
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 1]
[0, 0, 0, 1, 0, 1]
[0, 0, 0, 0, 1, 1]
-----------------------------------------------------------------------
```