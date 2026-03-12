# TEST_CASES

## Case 1: N + L = W

- Input: state `(0, 0, N)`, commands `L`
- Expected: `(0, 0, W)`, not lost
- Actual: `(0, 0, W)`, not lost
- PASS/FAIL: PASS
- Related test: `test_n_plus_l_equals_w`

## Case 2: N + R = E

- Input: state `(0, 0, N)`, commands `R`
- Expected: `(0, 0, E)`, not lost
- Actual: `(0, 0, E)`, not lost
- PASS/FAIL: PASS
- Related test: `test_n_plus_r_equals_e`

## Case 3: Four right turns

- Input: direction `N`, operations `R R R R`
- Expected: back to `N`
- Actual: back to `N`
- PASS/FAIL: PASS
- Related test: `test_four_right_turns_returns_to_original`

## Case 4: Move inside boundary

- Input: state `(0, 0, N)`, map `(5, 3)`, commands `F`
- Expected: `(0, 1, N)`, not lost
- Actual: `(0, 1, N)`, not lost
- PASS/FAIL: PASS
- Related test: `test_forward_inside_boundary_not_lost`

## Case 5: Out of boundary causes LOST

- Input: state `(5, 3, N)`, map `(5, 3)`, commands `F`
- Expected: `(5, 3, N) LOST`
- Actual: `(5, 3, N) LOST`
- PASS/FAIL: PASS
- Related test: `test_forward_outside_boundary_becomes_lost`

## Case 6: First robot leaves scent

- Input: state `(5, 3, N)`, scent `{}` then `F`
- Expected: robot lost and scent contains `(5, 3, N)`
- Actual: robot lost and scent contains `(5, 3, N)`
- PASS/FAIL: PASS
- Related test: `test_first_robot_leave_scent_after_fall`

## Case 7: Same (x,y,dir) ignores dangerous F

- Input: state `(5, 3, N)`, scent `{(5, 3, N)}`, commands `F`
- Expected: no movement and not lost
- Actual: no movement and not lost
- PASS/FAIL: PASS
- Related test: `test_second_robot_ignores_dangerous_forward_with_same_mark`

## Case 8: Same cell different direction does not share scent

- Input: state `(5, 3, E)`, scent `{(5, 3, N)}`, commands `F`
- Expected: lost, scent adds `(5, 3, E)`
- Actual: lost, scent adds `(5, 3, E)`
- PASS/FAIL: PASS
- Related test: `test_same_position_different_direction_does_not_share_scent`

## Case 9: LOST robot stops processing

- Input: state `(5, 3, N)`, commands `FRFRF`
- Expected: lost on first `F`, no further state change
- Actual: lost on first `F`, no further state change
- PASS/FAIL: PASS
- Related test: `test_lost_robot_stops_following_commands`

## Case 10: Invalid command strategy

- Input: command `X`
- Expected: raise `ValueError`
- Actual: raise `ValueError`
- PASS/FAIL: PASS
- Related test: `test_invalid_command_raises_value_error`
