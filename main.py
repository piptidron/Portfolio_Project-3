import pandas as pd
import random

df = pd.DataFrame({ 0 : ["_", "_", "_"],
                    1 : ["_", "_", "_"],
                    2 : ["_", "_", "_"]})

def check_empty_cell():
    for i in range(3):
        for j in range(3):
            if df.at[i,j] == '_':
                return True

def choice_user():
    choice_user_row = int(input("Enter the row number: "))
    choice_user_column = int(input("Enter the column number: "))
    if df.at[choice_user_row, choice_user_column] == "_":
        df.at[choice_user_row, choice_user_column] = "x"
    else:
        print("This cell is full. Make a choice again.")
        choice_user()

def choice_comp():
    random_row = random.randint(0, 2)
    random_column = random.randint(0, 2)

    if df.at[random_row, random_column] == "_":
        df.at[random_row, random_column] = "o"
    else:
        choice_comp()


def check_win(x):
    for i in range(3):
        if df.at[0,i] == f"{x}" and df.at[1,i] == f"{x}" and df.at[2,i] == f"{x}":
            print(f"{x} WINNER")
            return True
        elif df.at[i,0] == f"{x}" and df.at[i,1] == f"{x}" and df.at[i,2] == f"{x}":
            print(f"{x} WINNER")
            return True
        elif df.at[0,0] == f"{x}" and df.at[1,1] == f"{x}" and df.at[2,2] == f"{x}":
            print(f"{x} WINNER")
            return True
        elif df.at[2,0] == f"{x}" and df.at[1,1] == f"{x}" and df.at[0,2] == f"{x}":
            print(f"{x} WINNER")
            return True
    else:
        return False



while True:
        print(df)

        choice_user()
        if check_win("x"):
            print(df)
            break

        if check_empty_cell():
            choice_comp()
            if check_win('o'):
                print(df)
                break
        else:
            print(df)
            print("Draw")
            break










