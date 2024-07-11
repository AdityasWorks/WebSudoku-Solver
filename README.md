# WebSudoku Solver

This Python script automates solving Sudoku puzzles from [WebSudoku](https://www.websudoku.com/) using browser automation with Selenium and data extraction with BeautifulSoup.

## Demo

[![Solver](https://github.com/AdityasWorks/WebSudoku-Solver/blob/main/demo/Websudoku%20Demo.mp4)](https://github.com/AdityasWorks/WebSudoku-Solver/assets/111555593/30bca1a3-5304-46af-9957-167d77b8d5bc
)

## Features

- **Automated Sudoku Solving:** Solves Sudoku puzzles from WebSudoku based on user-provided difficulty level and puzzle ID.
- **Browser Automation:** Utilizes Selenium to interact with WebSudoku, selecting difficulty levels, inputting puzzle IDs, and extracting puzzle grid values.
- **Backtracking Algorithm:** Implements a backtracking algorithm to solve the Sudoku puzzles retrieved from WebSudoku.
- **Numpy Integration:** Uses Numpy for efficient matrix operations, handling the puzzle grid as a 2D array.

## Requirements

Ensure you have Python 3.x installed along with the following Python libraries (installable via `pip`):

- numpy
- beautifulsoup4
- selenium

You can install these dependencies using the provided `requirements.txt` file:

```bash

pip install -r requirements.txt

```
## Usage

1. **Clone the Repository:**

   ```bash
   
   git clone https://github.com/your-username/websudoku-solver.git
   cd websudoku-solver
   
   
2. **Install Dependencies:**

   ```bash
   
   pip install -r requirements.txt

3. **Run the Script:**

   ```bash
   
   python solver.py
   
    ```
   1. Follow the on-screen prompts to enter the difficulty level (`Easy`, `Medium`, `Hard`, `Evil`) and the Sudoku puzzle number.

5. **View Results:**

   After running the script go back to your sudoku and select the first cell. 
