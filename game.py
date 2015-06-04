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
            conns = []
            try: conns.append(self.board[pos - 5])
            except: pass
            try: conns.append(self.board[pos - 4])
            except: pass
            try: conns.append(self.board[pos - 3])
            except: pass
            try: conns.append(self.board[pos - 1])
            except: pass
            try: conns.append(self.board[pos + 1])
            except: pass
            try: conns.append(self.board[pos + 3])
            except: pass
            try: conns.append(self.board[pos + 4])
            except: pass
            try: conns.append(self.board[pos + 5])
            except: pass
            
            """ If adding some logic makes it faster....?
            if pos > self.size:
                conns.append(self.board[pos - 4])
                if pos % self.size != 1:
                    conns.append(self.board[pos - 5])
                if not (pos % self.size):
                    conns.append(self.board[pos -3])
            if pos < (self.size * (self.size - 1)):
                conns.append(self.board[pos + 4])
                if pos % self.size != 1:
                    conns.append(self.board[pos + 5])
                if not (pos % self.size):
                    conns.append(self.board[pos + 3])
            if pos % self.size != 1:
                conns.append(self.board[pos - 1])
            if not (pos % self.size):
                conns.append(self.board[pos + 1])
            """
                
            self.board[pos].connections = conns


    def __repr__(self):
        print_list = [ letter.value for letter in self.board ]
        printable = ('-' * 17 + '\n')
        for rows in range(self.size):
            for cols in range(self.size):
                printable += ('| %s ' % print_list.pop())
            printable += ('|\n' + '-' * 17 + '\n')
        return printable

    def generate_words(self):
        for letter in self.board:
            DFS
        
        pass

    def check_dictionary(self):
        pass
   
