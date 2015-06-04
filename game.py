from random import shuffle
from die import die
from logic import check_real_word

class game():

    def __init__(self, size):
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
        
        self.size = size
        self.board = [ die(dice_values[j]) for j in range(self.size**2) ]
        shuffle(self.board)
        self.create_connections()
        self.__repr__()


    def create_connections(self):
        for pos in range(len(self.board)):
            print(pos)
            print(self.board[pos].value + ' has:')
            conns = []
            try: conns.append(self.board[pos - 5]); print('-5')
            except: pass
            try: conns.append(self.board[pos - 4]); print('-4')
            except: pass
            try: conns.append(self.board[pos - 3]); print('-3')
            except: pass
            try: conns.append(self.board[pos - 1]); print('-1')
            except: pass
            try: conns.append(self.board[pos + 1]); print('1')
            except: pass
            try: conns.append(self.board[pos + 3]); print('3')
            except: pass
            try: conns.append(self.board[pos + 4]); print('4')
            except: pass
            try: conns.append(self.board[pos + 5]); print('5')
            except: pass

            for j in conns:
                print(j.value)
            self.board[pos].connections = conns


    def __repr__(self):
        print_list = [ letter.value for letter in self.board ]
        printable = ('-' * 17 + '\n')
        for rows in range(self.size):
            for cols in range(self.size):
                printable += ('| %s ' % print_list.pop(0))
            printable += ('|\n' + '-' * 17 + '\n')
        return printable

    def generate_words(self):
        self.solutions = []
        for letter in self.board:
            self.DFS(letter)
            letter.used = False
        print(self.solutions)

    def DFS(self, letter, word = ''):
        letter.used = True
        for j in letter.connections:
            print('Connection: ' + j.value)
        word += letter.value.lower()
        print("word is:" + word)
        test = check_real_word(word)
        print("test result is:" + str(test))
        
        if test:
            print(1)
            if len(word) >= 3 and test == word:
                print(2)
                self.solutions.append([word])
            for connection in letter.connections:
                print(3)
                if not connection.used:
                    self.DFS(connection, word)
            print(4)
            letter.used = False
            word = word[:-1]
        else:
            print(5)
            letter.used = False
            word = word[:-1]
