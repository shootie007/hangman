# coding:utf-8

import random

def hangman(word):
    wrong = 0
    stages = ['',
              '________        ',
              '|               ',
              '|       |       ',
              '|       o       ',
              '|      /|\      ',
              '|      / \      ',
              '|               ',
              ]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False
    print('Welcome to Hangman.')
    name = input('READY PLAYER 1 NAME : ')

    while wrong < len(stages) - 1 :
        print('\n')
        msg = 'Guess A Letter.'
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1

        print(''.join(board))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('You Win!')
            print(''.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong + 1]))
        print('You Lose! The Answer Is {}.'.format(word))

hangman_list = ['cat', 'dog', 'hand', 'door', 'phone']
hangman(random.choice(hangman_list))
