"""Everything that draws the game: board, scores, buttons."""
import streamlit as st
from streamlit_shortcuts import add_shortcuts

from game.logic import GRID, new_game, set_direction, step, toggle_running


def board_html():
    s = st.session_state
    head = s.snake[0]
    body = set(s.snake[1:])
    cells = []
    for y in range(GRID):
        for x in range(GRID):
            pos = (x, y)
            radius = "4px"
            if pos == head:
                color = "#15803d"
            elif pos in body:
                color = "#22c55e"
            elif pos == s.food:
                color, radius = "#ef4444", "50%"
            else:
                color = "rgba(128,128,128,0.18)"
            cells.append(
                f'<div style="width:22px;height:22px;background:{color};border-radius:{radius};"></div>'
            )
    return (
        f'<div style="display:grid;grid-template-columns:repeat({GRID},22px);'
        f'gap:2px;justify-content:center;">{"".join(cells)}</div>'
    )


def register_shortcuts():
    """Bind keys to the direction buttons (by their `key`).

    Call this ONCE from the main script, outside the timer fragment, so the
    hidden listener isn't recreated on every game tick.
    """
    add_shortcuts(
        up=["arrowup", "w"],
        left=["arrowleft", "a"],
        down=["arrowdown", "s"],
        right=["arrowright", "d"],
    )


def render_controls():
    s = st.session_state
    _, up, _ = st.columns(3)
    left, down, right = st.columns(3)
    for col, label, key_name in [
        (up, "⬆️", "up"),
        (left, "⬅️", "left"),
        (down, "⬇️", "down"),
        (right, "➡️", "right"),
    ]:
        col.button(
            label,
            key=key_name,
            on_click=set_direction,
            args=(key_name,),
            use_container_width=True,
        )

    b1, b2 = st.columns(2)
    b1.button(
        "⏸️ Pause" if s.running else "▶️ Start",
        key="toggle",
        on_click=toggle_running,
        disabled=s.game_over,
        use_container_width=True,
    )
    b2.button("🔄 New game", key="new", on_click=new_game, use_container_width=True)


def render_game():
    """Runs on a timer (see snake.py): advance one tick, then draw."""
    s = st.session_state
    if s.running and not s.game_over:
        step()

    c1, c2 = st.columns(2)
    c1.metric("Score", s.score)
    c2.metric("High score", s.high_score)

    st.markdown(board_html(), unsafe_allow_html=True)

    if s.game_over:
        if s.won:
            st.success(f"You filled the board! Score: {s.score}")
        else:
            st.error(f"Game over! Score: {s.score}")

    st.write("")
    render_controls()