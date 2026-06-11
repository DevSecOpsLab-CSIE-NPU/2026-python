# AI Collaboration Log

## Project Overview
Week 16 - Sorting Algorithm Performance Experiment
Student ID: 1114405003

## AI Usage Log

### Stage 1: @timeit Decorator

**Prompt**: "Create a @timeit decorator that:
- Preserves the return value of the decorated function
- Uses functools.wraps to preserve __name__ and __doc__
- Tracks elapsed time in seconds and stores it in last_elapsed and records attributes
- Does not use print statements in the decorator
- Has at least 3 test cases covering all specifications"

**AI Response**: Provided implementation of timeit decorator with proper timing tracking and metadata preservation.

**Changes Made**:
- Created timing.py with @timeit decorator
- Added test_timing.py with comprehensive tests
- Verified decorator correctly tracks elapsed time and preserves function metadata

### Stage 2: Sorting Algorithms

**Prompt**: "Implement bubble_sort, quick_sort, and merge_sort functions that:
- Return new sorted lists without modifying input
- Disable built-in sorted() and list.sort()
- Have proper type hints and documentation
- Pass comprehensive tests including edge cases"

**AI Response**: Provided implementations of all three sorting algorithms with proper error handling and documentation.

**Changes Made**:
- Created sorts.py with three sorting algorithms
- Added test_sorts.py with comprehensive test cases
- Verified algorithms correctly sort various data types and edge cases

### Stage 2: Benchmark Framework

**Prompt**: "Create benchmark.py with:
- make_data(n, seed=42) function for reproducible test data
- run_benchmark() function that tests all sorting algorithms
- Uses @timeit decorator for performance measurement
- Outputs comparison table and saves results to results.json"

**AI Response**: Provided benchmark framework with proper timing and data generation.

**Changes Made**:
- Created benchmark.py with timing framework
- Added baseline (sorted()) and accelerated versions
- Generated comprehensive performance data

### Stage 3: Algorithm Optimization

**Prompt**: "Create optimized versions of sorting algorithms (Cython or algorithm optimization):
- At least one acceleration method
- Must pass all Stage 2 tests
- Add to results.json with acceleration ratios"

**AI Response**: Provided algorithm optimizations since Cython compilation was not feasible in this environment.

**Changes Made**:
- Created sorts_fast.py with optimized implementations:
  - bubble_sort with early termination
  - quick_sort with median-of-three pivot selection
  - merge_sort with insertion sort for small arrays
- Created test_sorts_fast.py to verify correctness

### Stage 4: Visualization

**Prompt**: "Create plot.py with:
- load_results(path) function to read results.json
- plot_results(results, out_path) function to generate log-scale line chart
- Save output as assets/benchmark.png
- Add matplotlib.use('Agg') for headless operation"

**AI Response**: Provided visualization code with proper matplotlib configuration.

**Changes Made**:
- Created plot.py with data loading and plotting functions
- Created test_plot.py to verify visualization
- Generated benchmark.png chart

### Stage 5: Security Self-Scan

**Prompt**: "Perform security self-scan using OpenSSF guidelines:
- Test against 4 chapters: Coding Standards, Exception Handling, Numbers, Neutralization
- Find at least 3 applicable issues
- Write tests for each issue
- Document findings and fixes"

**AI Response**: Provided security testing framework with comprehensive test coverage.

**Changes Made**:
- Created test_security.py with security tests
- Covered all 4 OpenSSF chapters
- Fixed identified security issues

## Summary

The AI collaboration was highly effective throughout all stages of the project. The AI provided correct implementations and suggestions, while I verified the correctness and made necessary adjustments. All tests pass, and the project meets all requirements specified in the assignment.

## Verification

All stages were completed and verified:
- ✅ Stage 1: @timeit decorator with tests
- ✅ Stage 2: Sorting algorithms with tests
- ✅ Stage 2: Benchmark framework
- ✅ Stage 3: Algorithm optimizations
- ✅ Stage 4: Visualization
- ✅ Stage 5: Security self-scan
- ✅ All tests pass
- ✅ Documentation complete