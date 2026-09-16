#!/usr/bin/env python3
"""
Main script to run all Project Euler solutions.
"""

import sys
import importlib.util

def run_problem(problem_number):
    """
    Run a specific problem solution.
    """
    try:
        module_name = f"problem_{problem_number}"
        spec = importlib.util.spec_from_file_location(module_name, f"{module_name}.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        print(f"\n{'='*60}")
        print(f"PROBLEM {problem_number}")
        print(f"{'='*60}")
        
        # Run the main function if it exists
        if hasattr(module, '__main__'):
            module.__main__()
        
    except Exception as e:
        print(f"Error running problem {problem_number}: {e}")

def main():
    """
    Run all solved problems.
    """
    print("Project Euler Solutions")
    print("="*60)
    
    # Run problems 1 through 5
    for problem_num in range(1, 6):
        run_problem(problem_num)

if __name__ == "__main__":
    main()