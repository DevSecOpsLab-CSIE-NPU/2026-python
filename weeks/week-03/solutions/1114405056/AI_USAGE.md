# AI_USAGE

## 1. Questions Asked To AI

1. How should `scent` be represented for O(1) lookups?
2. What are the minimal tests to cover turn, boundary, and scent rules?
3. How can I keep `robot_core.py` independent from pygame?
4. What is a simple replay mechanism without exporting GIF?

## 2. Adopted Suggestions And Reasons

- Adopted `set[(x, y, direction)]` for scent.
  - Reason: exact rule matching and fast lookup.
- Adopted dataclass state model (`RobotState`).
  - Reason: clear transitions and easier unit testing.
- Adopted split architecture (`robot_core.py` and `robot_game.py`).
  - Reason: decouples game view from algorithm logic.

## 3. Rejected Suggestions And Reasons

- Rejected storing scent as only `(x, y)`.
  - Reason: incorrect for direction-specific scent behavior.
- Rejected implementing all logic directly in pygame event loop.
  - Reason: hard to test and violates assignment structure.

## 4. One Incomplete AI Suggestion That I Fixed

- Incomplete suggestion: AI proposed replay by only storing command strings.
- Fix: stored full `RobotState` history snapshots so replay can show exact state after each step.
