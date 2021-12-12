class BingoNum:
    number = None 
    def __init__(self, number):
        self.number = str(number)
    def __str__(self):
        return str(self.number)

class BingoBoard:
    board = None
    def __init__(self, board):
        self.board = board
    def __str__(self):
        return str('\n'.join([" ".join((str(num) for num in line)) for line in self.board]))
    def sum_board(self):
        # only include horizontal lines
        positive_ints = [int(j.number) if int(j.number) >= 0 else 0 for sub in self.board[:5] for j in sub]
        return sum(positive_ints) 

def check_boards(boards):
    bingo_string = "-1" * 5
    for bingo_board in boards:
        for line in bingo_board.board:
            if ("".join(str(num) for num in line) == bingo_string):
                return True, bingo_board
    return False, None

def main():
    in_file = open('input.txt', 'r')
    in_lines = in_file.readlines()
    call_numbers = in_lines[0].strip().split(',')
    board_size = 5
    bingo_boards = []
    nums = {str(num):BingoNum(num) for num in range(100)} 

    for i in range(2, len(in_lines), 6):
        horiz_board = []
        vert_board = []
        for horiz in range(board_size):
            this_line = in_lines[i+horiz].strip().split()
            this_line = [nums[num] for num in this_line]
            horiz_board.append(this_line)
        for vert in range(board_size):
            this_line = []
            for l in range(board_size):
                this_line.append(horiz_board[l][vert])
            vert_board.append(this_line)
        board = horiz_board + vert_board
        bingo_boards.append(BingoBoard(board))
    for num in call_numbers:
    # mark number for all boards
        nums[num].number = -1
        bingo, result_board = check_boards(bingo_boards)
        if bingo:
            board_sum = result_board.sum_board()
            print(int(num) * board_sum)
            return
        
if __name__ == "__main__":
    main()
