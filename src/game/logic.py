"""Snake rules and state. No drawing here, only game state in st.session_state."""
import random

import streamlit as st

GRID = 15
DIRS = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}
OPPOSITE = {"up": "down", "down": "up", "left": "right", "right": "left"}


def spawn_food(snake):
    free = [(x, y) for x in range(GRID) for y in range(GRID) if (x, y) not in snake]
    return random.choice(free) if free else None


def new_game():
    mid = GRID // 2
    snake = [(mid, mid), (mid - 1, mid), (mid - 2, mid)]
    st.session_state.snake = snake
    st.session_state.direction = "right"
    st.session_state.next_direction = "right"
    st.session_state.food = spawn_food(snake)
    st.session_state.score = 0
    st.session_state.running = False
    st.session_state.game_over = False
    st.session_state.won = False


def set_direction(new_dir):
    # Can't reverse straight into yourself
    if new_dir != OPPOSITE[st.session_state.direction]:
        st.session_state.next_direction = new_dir
    st.session_state.running = not st.session_state.game_over


def toggle_running():
    st.session_state.running = not st.session_state.running


def step():
    s = st.session_state
    s.direction = s.next_direction
    dx, dy = DIRS[s.direction]
    hx, hy = s.snake[0]
    new_head = (hx + dx, hy + dy)

    out_of_bounds = not (0 <= new_head[0] < GRID and 0 <= new_head[1] < GRID)
    eating = new_head == s.food
    # The tail moves away this tick unless we're growing
    body = s.snake if eating else s.snake[:-1]

    if out_of_bounds or new_head in body:
        s.game_over = True
        s.running = False
        return

    s.snake = [new_head] + s.snake if eating else [new_head] + s.snake[:-1]

    if eating:
        s.score += 1
        s.high_score = max(s.high_score, s.score)
        s.food = spawn_food(s.snake)
        if s.food is None:  # board is full
            s.game_over = True
            s.won = True
            s.running = False
