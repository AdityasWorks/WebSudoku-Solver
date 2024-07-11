import time
import sys
import numpy as np
import pyautogui as pg
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

url = "https://www.websudoku.com/?select=1&level=1"

chrome_options = Options()
chrome_options.add_argument("--headless")

class SudokuSolver:
    def __init__(self, grid_values) -> None:
        self.grid = np.array(grid_values)

    def _fill(self, matrix):
        print("Filling the grid")
        final = [i for i in matrix.flatten()]

        counter = []

        for num in final:
            pg.typewrite(str(int(num)))
            pg.hotkey("right")
            counter.append(num)
            if len(counter) % 9 == 0:
                pg.hotkey("down")
                for _ in range(9):
                    pg.hotkey("left")

    def _possible(self, x, y, n):
        # check row
        for i in range(0, 9):
            if self.grid[i][x] == n and i != y:
                return False

        # check column
        for i in range(0, 9):
            if self.grid[y][i] == n and i != x:
                return False

        # check 3x3 square
        x0 = (x // 3) * 3
        y0 = (y // 3) * 3
        for X in range(x0, x0 + 3):
            for Y in range(y0, y0 + 3):
                if self.grid[Y][X] == n:
                    return False

        return True

    def solve(self):
        for y in range(9):
            for x in range(9):
                if self.grid[y][x] == 0:
                    for n in range(1, 10):
                        if self._possible(x, y, n):
                            self.grid[y][x] = n
                            self.solve()
                            self.grid[y][x] = 0
                    return
                    
        self._fill(self.grid)
        print("Solved!")
        sys.exit()

if __name__ == "__main__":
    difficulty = input("Enter the difficulty (Easy, Medium, Hard, Evil): ")
    sudoku_id = input("Enter Sudoku Number: ")
    print("\nSelect the First Grid of the Sudoku \n")
    with Chrome(options=chrome_options) as browser:
        browser.get(url)
        WebDriverWait(browser, 1).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//frame[@src]")))

        select = Select(WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.NAME, "level"))))
        select.select_by_visible_text(difficulty)

        input_field = WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.NAME, "set_id")))
        input_field.clear()
        input_field.send_keys(sudoku_id)

        submit_button = WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'][value=' Go to this puzzle ']")))
        submit_button.click()

        WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.ID, "puzzle_grid")))

        puzzle_table = browser.find_element(By.ID, "puzzle_grid")
        puzzle_table_html = puzzle_table.get_attribute('outerHTML')

        if puzzle_table_html:
            page_soup = BeautifulSoup(puzzle_table_html, 'html.parser')
            inputs = page_soup.find_all('input')
            grid_values = [int(input_tag.get('value', '0')) for input_tag in inputs]
            grid = [grid_values[i:i + 9] for i in range(0, len(grid_values), 9)]

    # Initialize SudokuSolver with fetched grid values
    solver = SudokuSolver(grid)
    print("Solving...")
    solver.solve()

