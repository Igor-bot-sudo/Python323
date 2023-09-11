from random import randint
from subprocess import call
from time import sleep
import sqlite3


def play_rps():
    sleep(1)

    options = {1: 'Камень', 2: 'Ножницы', 3: 'Бумага'}    
    user_choice = None

    while user_choice not in options:
        print('1. Камень')
        print('2. Ножницы')
        print('3. Бумага')

        try:
            user_choice = int(input("Ваш ход: "))

            if user_choice not in options:
                raise ValueError
        except ValueError: #Invalid input
            print("ОШИБКА: Число должно быть от 1 до 3.")
            sleep(1)

    # determine computer's choice
    robot_choice = randint(1, 3)
    sleep(1)

    print('Ход компьютера: ', options[robot_choice])

    # determine winner of current game
    if user_choice == robot_choice:
        winner = None
    elif user_choice == 1:
        if robot_choice == 2:
            winner =  'Игрок'
        else:
            winner = 'Компьютер'
    elif user_choice == 2:
        if robot_choice == 3:
            winner =  'Игрок'
        else:
            winner = 'Компьютер'
    else:
        if robot_choice == 1:
            winner =  'Игрок'
        else:
            winner = 'Компьютер'

    # update score of winner if applicable
    if winner:
        print(winner, ' победил!')
    else:
        print('Ничья, повтор')

    sleep(0.5)
    return winner


def game():
    call(['cls'], shell=True)

    print('Камень, Бумага, Ножницы v.1')

    score = {'Игрок':0,'Компьютер':0}
    winner = None
    sleep(1)

    # play current game until there is a winner
    while not winner:
        sleep(1)
        call(['cls'], shell=True)
        print('Компьютер:', score['Компьютер'], 'Игрок: ', score['Игрок'])
        winner = play_rps()

    # update score after game
    score[winner] += 1

    print('Счёт игры:')
    print('Компьютер:', score['Компьютер'], 'Игрок: ', score['Игрок'])
    if score['Игрок'] > score['Компьютер']:
        print('Победил Игрок!\n')
    elif score['Игрок'] == score['Компьютер']:
        print('Ничья.\n')
    else:
        print('Победил компьютер!\n')

    if winner == 'Игрок':
        p_name = input('Введите свое имя\n')
        with sqlite3.connect("game.db") as con:
            cur = con.cursor()
            res = cur.execute("SELECT DISTINCT `player_name` FROM `players`;").\
                fetchall()
            if (p_name,) in res:
                # Increment player's score
                cur.execute(
                    "UPDATE players SET score = score + 1 WHERE player_name = ?;"\
                    , (p_name,))
                cur.execute(
                    "UPDATE games SET score = score + 1 WHERE player_name = ?;"\
                    , (p_name,))
            else:
                # Append new player
                cur.execute(
                    "INSERT INTO players (player_name, score) VALUES (?, 1);"\
                    , (p_name,))
                cur.execute(
                    "INSERT INTO games (player_name, score) VALUES (?, 1);"\
                    , (p_name,))
    # reset winner        
    winner = None


if __name__ == '__main__':
    game()
