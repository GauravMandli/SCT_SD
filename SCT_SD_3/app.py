from flask import Flask, render_template, request
import copy

app = Flask(__name__)

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        input_data = []
        for i in range(9):
            row = []
            for j in range(9):
                val = request.form.get(f'cell_{i}_{j}')
                row.append(int(val) if val else 0)
            input_data.append(row)

        solved_board = copy.deepcopy(input_data)
        if solve_sudoku(solved_board):
            result = solved_board
        else:
            result = "No solution found."

        return render_template("index.html", board=input_data, result=result)

    return render_template("index.html", board=[[0]*9 for _ in range(9)], result=None)

if __name__ == "__main__":
    app.run(debug=True)
