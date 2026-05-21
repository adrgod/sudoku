# Sudoku Board Generator

A Python-based Sudoku board generator that creates valid 9x9 Sudoku puzzles by intelligently filling cells with numbers 1-9 according to Sudoku rules.

## Overview

This project generates a complete, valid Sudoku board by:
1. Creating a 9x9 grid divided into nine 3x3 boxes
2. Filling in numbers 1-9 such that each number appears exactly once in every row, column, and 3x3 box
3. Using an intelligent algorithm to avoid dead-ends during board generation

## Features

- **Smart Board Generation**: Uses a lookahead algorithm to check if future cells can be filled before committing to the current cell's value
- **Shuffle Algorithm**: Randomly shuffles available numbers to create varied puzzles
- **Validation**: Ensures all Sudoku constraints are satisfied during generation
- **Display Methods**: Multiple ways to view and test the generated board

## Project Structure

- **`sudoku.py`**: Main entry point that initializes and generates the board
- **`sudoku_board.py`**: Core class containing all board logic and generation algorithms

## Usage

To generate a Sudoku board, run:

```bash
python sudoku.py
```

This will:
1. Create a 9x9 board
2. Fill it with valid numbers according to Sudoku rules
3. Display the completed board in list format

## Algorithm Details

The board generation uses a constraint satisfaction approach:

- **Sequential Filling**: Processes the board row by row, column by column
- **Lookahead Strategy**: Before placing a number, checks if remaining numbers can fit in subsequent columns to prevent dead-ends
- **Backtracking Support**: If a cell cannot be filled, attempts alternative placements or swaps values
- **Missing Value Completion**: After initial filling, identifies and fills any remaining empty cells with missing values

## Requirements

- Python 3.x
- No external dependencies

## Future Enhancements

- Board difficulty levels (easy, medium, hard)
- Puzzle solving functionality
- Visual board representation (GUI)
- Performance optimization for faster generation
