import streamlit as st

from game.logic import new_game
from game.view import render_game, register_shortcuts
from ui.sidebar import the_sidebar

st.set_page_config(page_title="Snake", page_icon="🐍")

if "snake" not in st.session_state:
    st.session_state.high_score = 0
    new_game()

is_dark, speed = the_sidebar()
register_shortcuts()

st.title("Snake")
st.caption("Press Start, then steer with the arrow buttons or WASD key.")

# The fragment reruns on a timer, so the snake moves without reloading the whole page
st.fragment(run_every=1.0 / (speed + 1))(render_game)()