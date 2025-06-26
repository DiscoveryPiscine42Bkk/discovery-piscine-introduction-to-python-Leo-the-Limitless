# from checkmate import checkmate

# if __name__ == "__main__":
#     # King in check by Rook
#     print("Test 1 (Rook check):", checkmate("""\
# RK
# ..\
# """))

#     # King in check by Bishop
#     print("Test 2 (Bishop check):", checkmate("""\
# B..
# ...
# ..K\
# """))

#     # King in check by Queen (diagonal)
#     print("Test 3 (Queen diagonal check):", checkmate("""\
# Q...
# ....
# ....
# ...K\
# """))

#     # King in check by Knight
#     print("Test 4 (Knight check):", checkmate("""\
# .....
# ..K..
# .....
# .N...
# .....\
# """))

#     # King in check by Pawn
#     print("Test 5 (Pawn check):", checkmate("""\
# ...
# .K.
# P..\
# """))

#     # King is NOT in check
#     print("Test 6 (No check):", checkmate("""\
# ....
# .K..
# ....
# ...R\
# """))

#     # King is blocked from being attacked
#     print("Test 7 (Blocked Queen):", checkmate("""\
# Q..
# .P.
# ..K\
# """))

#     # Invalid character treated as empty square
#     print("Test 8 (Invalid piece blocking):", checkmate("""\
# B..
# .A.
# ..K\
# """))

#     # Error: No King on the board
#     print("Test 9 (Error - no King):", checkmate("""\
# R..
# .P.
# ..Q\
# """))

#     # Error: Multiple Kings
#     print("Test 10 (Error - multiple Kings):", checkmate("""\
# K..
# ...
# ..K\
# """))

# File Check
import sys
from checkmate import checkmate

def main():
    if len(sys.argv) < 2:
        print("Error: No input files provided")
        return

    for filename in sys.argv[1:]:
        try:
            with open(filename, 'r') as f:
                board_str = f.read()
                result = checkmate(board_str)
                print(result)
        except FileNotFoundError:
            print("Error: File not found")
        except Exception:
            print("Error")

if __name__ == "__main__":
    main()
