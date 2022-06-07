import pandas as pd
from turtle import Turtle
from dataclasses import dataclass


@dataclass
class State:
    name: str
    x_cor: int
    y_cor: int


class GameHandler(Turtle):
    font = ('Courier', 12, 'normal')

    def __init__(self):
        super().__init__()
        self.score = 0
        self.states = []

        self.hideturtle()
        self.penup()
        self.speed(0)
        self.get_states()

    def update_game(self, state):
        self.score += 1
        self.goto(state.x_cor, state.y_cor)
        self.write(
            state.name, align='center', font=self.font
        )

    def get_states(self):
        df = pd.read_csv('data/50_states.csv')

        for entry in df.values:
            state = State(
                name=entry[0],
                x_cor=entry[1],
                y_cor=entry[2]
            )
            self.states.append(state)

    def check_answer(self, answer):
        for i, state in enumerate(self.states):
            if answer == state.name:
                self.update_game(state)
                self.states.pop(i)
                return True
        return False

    def save_states(self):
        df = pd.DataFrame(self.states)
        df.columns = ['Name', 'X', 'Y']
        df['Name'].to_csv('data/states_to_learn.csv')
