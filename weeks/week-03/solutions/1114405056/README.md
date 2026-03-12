# Week 03 - Robot Lost

![gameplay](assets/gameplay.png)

## 1. Feature List

- Grid map rendering from `(0, 0)` to `(W, H)`
- Robot rendering with direction indicator (`N/E/S/W`)
- `scent` rendering on dangerous cells
- Step-by-step controls for `L`, `R`, and `F`
- New robot reset while preserving scent (`N`)
- Scent clear (`C`)
- In-app replay mode (`P`) for the latest run

## 2. How To Run

- Python: `3.10+`
- Install dependency:

```bash
pip install pygame
```

- Start game:

```bash
python robot_game.py
```

## 3. How To Test

Run in `weeks/week-03/solutions/1114405056/`:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

Result summary: 11 tests passed.

## 4. Data Structure Choices

- `set[tuple[int, int, str]]` for `scent`:
  - O(1) average lookup for dangerous forward moves.
  - Keeps rule precision with `(x, y, direction)`.
  - Avoids duplicates naturally.
- `RobotState` dataclass for state snapshots:
  - Clear and testable state transitions.
  - Easy to append into replay history.
- Direction lookup tables:
  - Makes turn and move logic deterministic.
  - Reduces branching complexity.

## 5. One Bug And Fix

- Bug: first draft of movement treated `y+1` as screen-down, which inverted map behavior.
- Fix: separated world coordinates from rendering coordinates and added `world_to_screen` conversion.

## 6. Gameplay Screenshot

- Required file path: `assets/gameplay.png`
- Current file is a placeholder. Replace it with your own gameplay screenshot before submission.

## 7. Replay Method

- Press `P` in the game window to replay the latest movement history.
- This submission uses in-app replay instead of GIF export.
