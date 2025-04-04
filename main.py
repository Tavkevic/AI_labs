import random

def print_board(board):
    print("\n")
    for i in range(0, 9, 3):

        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("-----------")

def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Горизонтали
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Вертикали
        [0, 4, 8], [2, 4, 6]              # Диагонали
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw(board):
    return " " not in board

def player_move(board):
    while True:
        try:
            move = int(input("Ваш ход (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                return move
            print("Некорректный ход! Попробуйте снова.")
        except ValueError:
            print("Введите число от 1 до 9!")

def ai_move(board):
    # Сначала проверяем, может ли AI выиграть сразу
    for i in range(9):
        if board[i] == " ":
            board[i] = "0"
            if check_win(board, "O"):
                return i
            board[i] = " "

    # Затем блокируем победу игрока
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_win(board, "X"):
                board[i] = "0"
                return i
            board[i] = " "

    # Если центр свободен - занимаем его
    if board[4] == " ":
        return 4
    if board [4] == "0":
    # Занимаем любую свободную сторону
        sides = [1, 3, 5, 7]
        random.shuffle(sides)
        for i in sides:
            if board[i] == " ":
                return i

    if board[4] == "X":
    # Занимаем любой свободный угол
        corners = [0, 2, 6, 8]
        random.shuffle(corners)
        for i in corners:
            if board[i] == " ":
                return i


def main():
    risyet = [str(i+1) for i in range(9)]
    board = [" "] * 9
    current_player = "X"

    print("Добро пожаловать в крестики-нолики!")
    print("Вы играете за 'X'. Вводите числа 1-9, как на клавиатуре:")

    while True:
        print_board(risyet)

        if current_player == "X":
            move = player_move(board)
            board[move] = "X"
            risyet[move] = "X"
        else:
            print("Ход компьютера (O):")
            move = ai_move(board)
            board[move] = "0"
            risyet[move] = "0"

        if check_win(board, current_player):
            print_board(board)
            print(f"Победил {current_player}!")
            break

        if check_draw(board):
            print_board(board)
            print("Ничья!")
            break

        current_player = "0" if current_player == "X" else "X"

    play_again = input("Хотите сыграть еще раз? (Y/N): ").upper()
    if play_again == "Y":
        main()
    else:
        print("Спасибо за игру!")

if __name__ == "__main__":
    main()