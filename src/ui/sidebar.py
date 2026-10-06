import streamlit as st


def _apply_theme():
    """Push the chosen theme into Streamlit's config; the callback triggers a rerun."""
    base = "dark" if st.session_state.dark_mode else "light"
    st._config.set_option("theme.base", base)
    st.session_state._theme_pending = True


def the_sidebar(title: str = "Settings") -> bool:
    """Render a sidebar with a dark mode switch. Returns True if dark mode is on."""
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False

    # Extra rerun so the browser picks up the new theme right away
    if st.session_state.pop("_theme_pending", False):
        st.rerun()

    with st.sidebar:
        st.title(title)
        st.toggle("Dark mode", key="dark_mode", on_change=_apply_theme)
        speed = st.slider("Speed", min_value=1, max_value=10, value=5)
        st.divider()
      
        # Add more sidebar widgets here

    return st.session_state.dark_mode, speed

 


if __name__ == "__main__":
    st.set_page_config(page_title="Demo", layout="wide")
    is_dark, speed = the_sidebar()
    st.write(f"Dark mode is {'on' if is_dark else 'off'}")