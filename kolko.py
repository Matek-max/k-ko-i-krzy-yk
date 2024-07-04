# Gra w kółko i krzyżyk (Tic Tac Toe)

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Sprawdzenie wierszy
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Sprawdzenie kolumn
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Sprawdzenie przekątnych
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def main():
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        row = int(input(f"Gracz {current_player}, wybierz wiersz (1-3): ")) - 1
        col = int(input(f"Gracz {current_player}, wybierz kolumnę (1-3): ")) - 1

        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Gratulacje! Gracz {current_player} wygrywa!")
                break
            elif all(all(cell != " " for cell in row) for row in board):
                print_board(board)
                print("Remis!")
                break
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("To pole jest już zajęte. Wybierz inne.")

if __name__ == "__main__":
    main()
