# Adding Machine v01

## Purpose

The `addingMachine_v01.py` script is a simple text-based program designed to function as an adding machine. It allows users to input numerical values, accumulating these inputs to provide a sum of all valid entries. The program serves as an exercise in basic file operations and error handling within Python.

## How It Works

The script performs two main operations: 

1. **Input and Store Data:** 
   - The program prompts the user to enter numerical amounts.
   - Each input is appended to a `tape.txt` file in CSV format.
   - The user can terminate the input session by typing `stop`.

2. **Read and Calculate Sum:**
   - The script reads the `tape.txt` file, parsing the stored numerical values.
   - It calculates and displays the total sum of valid integers found in the file.
   - Invalid entries (non-integer values) are identified and skipped with a notification message.

## Usage

1. **Run the Program:**
   - Execute `addingMachine_v01.py` in your Python environment.

2. **Input Values:**
   - Enter numbers when prompted. 
   - Type `stop` to end the input session.

3. **Output:**
   - The program will read from `tape.txt`, compute the total sum of valid numbers, and display the result.
   - For any invalid input lines, a warning is printed, and those lines are not included in the sum total.

## Dependencies

This script does not require any external libraries beyond Python's standard library.

## Important Notes

- Ensure `tape.txt` exists in the same directory as the script before running the program, or the program will create one for you.
- The script will continue appending to `tape.txt`, maintaining a record of inputs from previous runs unless the file is manually cleared.