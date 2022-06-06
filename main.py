import pandas as pd
from dataclasses import dataclass


@dataclass
class State:
    name: str
    x_cor: int
    y_cor: int


def get_states():
    df = pd.read_csv('data/50_states.csv')
    states = []

    for entry in df.values:
        state = State(
            name=entry[0],
            x_cor=entry[1],
            y_cor=entry[2]
        )
        states.append(state)

    return states


def main():
    print(get_states())


if __name__ == '__main__':
    main()
