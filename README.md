# Snake Demo: Modular Code Structure

A simple Snake game built with Streamlit to demonstrate a modular code structure.

## Install

```bash
# 1. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate     # macOS / Linux
# venv\Scripts\activate        # Command Prompt / PowerShell
# source venv/Scripts/activate   # Git Bash on Windows

# 2. Install dependencies
pip install -r requirements.txt
```

## Run

```bash
streamlit run src/app.py
```

## Structure

```
src/
├── app.py            # entry point: wiring only
├── ui/
│   └── sidebar.py    # sidebar (dark mode, speed)
└── game/
    ├── logic.py      # game rules and state
    └── view.py       # drawing and controls
 ```
