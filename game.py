from random import shuffle
from die import die

class game():

    def __init__(self):
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
        
        self.size = 4
        self.board = [ die(dice_values[j]) for j in range(self.size**2) ]
        shuffle(self.board)
        self.create_connections()
        self.trie()
        print(self)


    def create_connections(self):
        for pos in range(len(self.board)):
            conns = []
            if (pos + 1) > self.size:
                conns.append(self.board[pos - 4])
                if (pos + 1) % self.size != 1:
                    conns.append(self.board[pos - 5])
                if ((pos + 1) % self.size):
                    conns.append(self.board[pos -3])
            if (pos + 1) <= (self.size * (self.size - 1)):
                conns.append(self.board[pos + 4])
                if (pos + 1) % self.size != 1:
                    conns.append(self.board[pos + 3])
                if ((pos + 1) % self.size):
                    conns.append(self.board[pos + 5])
            if (pos + 1) % self.size != 1:
                conns.append(self.board[pos - 1])
            if ((pos + 1) % self.size):
                conns.append(self.board[pos + 1])
            self.board[pos].connections = conns


    def __repr__(self):
        print_list = [ letter.value for letter in self.board ]
        printable = ('-' * 17 + '\n')
        for rows in range(self.size):
            for cols in range(self.size):
                printable += ('| %s ' % print_list.pop(0))
            printable += ('|\n' + '-' * 17 + '\n')
        return printable


    def solve(self):
        self.solutions = []
        print('Solution search in progress......')
        for letter in self.board:
            print('Searching for words starting with %s' % letter.value)
            self.DFS(letter)
            letter.used = False

        print('Compiling the solutions.......')
        printable = [ ''.join(j) for j in self.solutions]
        ## Alternate method instead of .join()
        ## printable = sum(self.solutions, [])
        printable = list(set(printable))
        printable = sorted(printable)
        print('\nThe %s possible solutions are:' % len(printable))
        for k in printable:
            print('\t' + str(k))


    def DFS(self, letter, word = ''):
        letter.used = True
        word += letter.value.lower()
        test = self.check_real_word(word)
        
        if test:
            if len(word) >= 3 and test == word and word not in self.solutions:
                self.solutions.append([word])
            for connection in letter.connections:
                if not connection.used:
                    self.DFS(connection, word)
            letter.used = False
            word = word[:-1]
        else:
            letter.used = False
            word = word[:-1]


    def trie(self):
        wordlist = [ words.strip() for words in open('wordlist.txt','r') ]

        self.valid_words = {}
        for word in wordlist:
            current_dict = self.valid_words
            for letter in word:
                current_dict = current_dict.setdefault(letter,{})
            current_dict = current_dict.setdefault('END','END')

    
    def check_real_word(self, word):
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
