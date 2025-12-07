import curses
from curses import wrapper
from colorama import Fore, Style

# Calculator button layout
buttons = [
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C", "exit", "", ""]
]

# Map operators to Python operators
operator_map = {"×": "*", "÷": "/"}

def run_calculator(stdscr):
    curses.curs_set(0)
    current_expr = ""
    row, col = 0, 0
    
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "iPhone Calculator (Use arrows to move, Enter to press)")
        stdscr.addstr(1, 0, "Expression: " + current_expr)
        
        # Display buttons
        for r, button_row in enumerate(buttons):
            for c, label in enumerate(button_row):
                x = c * 6
                y = r + 3
                if r == row and c == col:
                    stdscr.addstr(y, x, f"[{label.center(3)}]", curses.A_REVERSE)
                else:
                    stdscr.addstr(y, x, f" {label.center(3)} ")
        
        key = stdscr.getch()
        
        # Arrow navigation
        if key == curses.KEY_UP and row > 0: row -= 1
        elif key == curses.KEY_DOWN and row < len(buttons) - 1: row += 1
        elif key == curses.KEY_LEFT and col > 0: col -= 1
        elif key == curses.KEY_RIGHT and col < 3: col += 1
        # Enter key to press button
        elif key in [10, 13]:
            label = buttons[row][col]
            if label in ["", None]: continue
            if label == "=":
                try:
                    expr = current_expr
                    for op, py_op in operator_map.items():
                        expr = expr.replace(op, py_op)
                    current_expr = str(eval(expr))
                except Exception:
                    current_expr = "Error"
            elif label.upper() == "C":
                current_expr = ""
            elif label.lower() == "exit":
                break
            else:
                current_expr += label
        
        stdscr.refresh()

# Run calculator
if __name__ == "__main__":
    wrapper(run_calculator)
