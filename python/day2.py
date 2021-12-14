from typing import Callable
from dataclasses import dataclass

@dataclass
class State:
    h_pos: int
    depth: int

@dataclass
class StateDay2(State):
    aim: int

def star1(lst: list[str]) -> int:
    """Star 1 done with python 3.10 structural pattern matching"""
    state = State(0, 0)
    for el in lst:
        word, number = el.split(' ')
        match word:
            case 'forward':
                state.h_pos += int(number)
            case 'down':
                state.depth += int(number)
            case 'up':
                state.depth -= int(number)
    return state.h_pos * state.depth

def star2(lst: list[str]) -> int:
    """Star 2 done with old dictionary-style"""
    state = StateDay2(0, 0, 0)
    state_mapping = {
        'forward': lambda state, number: StateDay2(
            state.h_pos + number,
            state.depth + state.aim * number,
            state.aim,
        ),
        'down': lambda state, number: StateDay2(
            state.h_pos,
            state.depth,
            state.aim + number,
        ),
        'up': lambda state, number: StateDay2(
            state.h_pos,
            state.depth,
            state.aim - number,
        )
    }
    for el in lst:
        word, number = el.split(' ')
        state = state_mapping[word](state, int(number))
    return state.h_pos * state.depth

if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        inp_lst = [line.strip() for line in f.readlines()]
    print(f"First star: {star1(inp_lst)}")
    print(f"Second star: {star2(inp_lst)}")
