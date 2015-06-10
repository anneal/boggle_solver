""" This module generates a Boggle board and produces the solutions """

from random import shuffle
from pprint import pprint
from die import Die
import sys
import time

class Game():
    """ A Game may be initialized with a size from 2x2 to 4x4. The default 
        board size is 4x4. (Additional dice must be added to increase the
        board size for Big Boggle.)

        Attributes of the Game include:
            size: int value from 2 to 4, inclusive
            board: list of lists (matrix) of Die objects
    """

    def __init__(self, size = 4):
        "This game uses the 1976 dice"
        dice_values = ['VITEGN',
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
                ['J','A','B','O','M','Qu'],
                'URIGLW']

        # Set the size of the game board to be between 2x2 and 4x4
        if 2 <= size <= 4:
            self.size = size
        else:
            self.size = 4

        # Assign a die to each board position
        self.board = [[Die(dice_values.pop()) for j in range(self.size)]
                      for k in range(self.size)]

        # Cover your ears! We're shaking the board up!
        shuffle(self.board)

        # Create the connections of all dice touched by a die
        self.create_connections()

        # Create the trie of valid words
        self.trie()
        
        # Display the board
        print(self)


    def create_connections(self):
        """ For each row and column in the board, the adjacent die are
        added as connections to the current die.
        """
        for r in range(self.size):
            for c in range(self.size):
                conns = []
                if r != 0:
                    conns.append(self.board[r-1][c])
                    if c != 0:
                        conns.append(self.board[r-1][c-1])
                    if c != self.size - 1:
                        conns.append(self.board[r-1][c+1])
                if r != self.size - 1:
                    conns.append(self.board[r+1][c])
                    if c != 0:
                        conns.append(self.board[r+1][c-1])
                    if c != self.size - 1:
                        conns.append(self.board[r+1][c+1])
                if c != 0:
                    conns.append(self.board[r][c-1])
                if c != self.size - 1:
                    conns.append(self.board[r][c+1])
                self.board[r][c].connections = conns
                    

    def __repr__(self):
        num_dash = 1 + self.size * 4
        printable = ('-' * num_dash + '\n')
        for rows in range(self.size):
            for cols in range(self.size):
                printable += ('| %s ' % self.board[rows][cols].value)
            printable += ('|\n' + '-' * num_dash + '\n')
        return printable


    def solve(self):
        """ The solutions are found via a recursive depth-first search.
        The minimum word length is 3 characters.
        """
        self.solutions = []
        for row in self.board:
            for letter in row:
                self.dfs(letter)
                letter.used = False     # Set the die as unused and continue


        printable = sorted({ ''.join(j) for j in self.solutions})
        print('\nThe %s possible solutions are:' % len(printable))
        for k in printable:
            print('\t' + str(k))


    def dfs(self, letter, word = ''):
        """ This is the recursive depth first search."""
        letter.used = True
        word += letter.value.lower()
        test = self.check_real_word(word)
        
        if test:
            if len(word) >= 3 and test == word and word not in self.solutions:
                self.solutions.append([word])
            for connection in letter.connections:
                if not connection.used:
                    self.dfs(connection, word)
            letter.used = False
        else:
            letter.used = False


    def trie(self):
        """ The MSD trie is created from a file."""
        wordlist = [ words.strip() for words in open('wordlist.txt','r') ]

        self.valid_words = {}
        for word in wordlist:
            current_dict = self.valid_words
            for letter in word:
                current_dict = current_dict.setdefault(letter,{})
            current_dict = current_dict.setdefault('END','END')

        pprint(self.valid_words)

    
    def check_real_word(self, word):
        """ This function returns
        -- the word if it is a valid word
        -- True if the word is part of a larger word
        -- False if the word is not in the trie
        """
        current_dict = self.valid_words
        
        for letter in word:
            if letter in current_dict:
                current_dict = current_dict[letter]
            else:
                return False
        if 'END' in current_dict:
            return word
        else:
            return True

def main():
    """ The user can input two arguments after running the game
        python3 game.py [size] [time]

    If the user does not enter a size, it defaults to a 4x4 board
    with a 3 minute time limit.
    """

    if len(sys.argv) > 0:
        new_game = Game(int(sys.argv[1]))
    else:
        new_game = Game(4)

    try:
        time.sleep(int(sys.argv[2]))
    except:
        print('The solutions will be displayed in 3 minutes...')
        time.sleep(60)
        print('... 2 minutes...')
        time.sleep(60)
        print('... 1 minutes...')
        time.sleep(50)
        for t in range(10,0,-1):
            print('... %s ...' % t)
            time.sleep(1)
    new_game.solve()
    print('\n')

main()
