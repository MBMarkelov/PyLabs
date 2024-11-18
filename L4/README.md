# Python Lab Tasks App

## Description
This application allows you to run and visualize results for three Python tasks. The tasks involve generating random strings, creating an arithmetic sequence, and filtering city names based on their length.

## Instructions to Run
1. Install PySide6 using pip:
    ```bash
    pip install pyside6
    ```
2. Run the application:
    ```bash
    python app.py
    ```

## Usage
- **Task 1**: Generates random strings of length 10 from lowercase Latin letters.
- **Task 2**: Generates 50 values from an arithmetic sequence.
- **Task 3**: Filters a list of city names based on length and replaces shorter names with "-".

## Test Instructions
Use pytest to test the core functionality of the app:
```bash
pytest tests/
