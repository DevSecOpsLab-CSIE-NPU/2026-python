# AI Usage Record

## Questions I asked AI
- How to preserve insertion order while removing duplicates?
- How to express multi-key sorting in Python clearly?
- How to design boundary tests for empty input?
- How to keep top-action tie-break deterministic?

## Suggestions adopted
- Use `sorted` with tuple key `(-score, age, name)`.
- Use `defaultdict(int)` and `Counter` for counting tasks.
- Split parsing and pure logic functions for better unit testing.

## Suggestions rejected
- Rejected using `set(numbers)` directly for dedupe output because it breaks required order.
- Rejected writing custom bubble sort because homework requires `sorted(..., key=...)`.

## One potentially misleading AI suggestion and my correction
- Misleading suggestion: selecting top action with `Counter.most_common(1)` only, which can be unstable on ties.
- Correction: manually find max frequency and resolve ties by lexical order to ensure deterministic output.
