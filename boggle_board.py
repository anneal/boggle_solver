"""
This file creates the Boggle board.
"""
from random import shuffle, randint

def roll(sides):
    return sides[randint(0,5)]

def main():
    dice = ['VITEGN',    # 1976 version dice
            'ACESLR',
            'VAZEDN',
            'ICATAO',
            'NODUKT',
            'ENIPHS',
            'ORIFBX',
            'KULEGY',
            'EYIEHF',
            'ESUTLP',
            'EWOSDN',
            'PECADM',
            'ALIBTY',
            'SAHOMR',
            'JABOMQ',
            'URIGLW']
    shuffle(dice)
    board = list(map(roll,dice))

    print('-'*17)
    for rows in range(4):
        for cols in range(4):
            print('| %s ' % board.pop(), end='')
        print('|\n'+'-'*17)

main()
