# Python Chess Engine ♟️

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A command-line chess game implementation in Python with complete chess rules, move validation, and game play features.

![Chess CLI Demo](demo.gif) <!-- Add actual demo gif/png if available -->

## Features ✨
- ♟️ Full chess rules implementation
- ✓ Move validation and legal move highlighting
- ♜ Check/checkmate/stalemate detection
- 📜 Move history with algebraic notation
- ♙ Pawn promotion and special moves (en passant, castling)
- 💾 Save/Load game functionality
- 🕒 Turn timer support
- 🎨 Colored terminal interface

## Requirements 📋
- Python 3.10+
- pip package manager

## Installation 🛠️
```bash
# Clone the repository
git clone https://github.com/Ramiferjanii/chess.git
cd chess

# Install dependencies
pip install -r requirements.txt

chess/
├── src/
│   ├── game/              # Core game logic
│   │   ├── board.py       # Board representation
│   │   ├── pieces.py      # Piece classes and movement
│   │   └── engine.py      # Game engine and rules
│   ├── interface/         # CLI interface
│   │   ├── cli.py         # Command-line interface
│   │   └── display.py     # Board rendering
│   ├── utils/             # Utilities
│   │   ├── helpers.py     # Helper functions
│   │   └── exceptions.py  # Custom exceptions
│   └── main.py            # Main entry point
├── tests/                 # Unit tests
├── saved_games/           # Saved game states
├── requirements.txt       # Dependencies
└── LICENSE
