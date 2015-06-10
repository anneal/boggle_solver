""" A trie based on a most significant digit radix tree.
"""

import os.path
from pprint import pprint

class Trie():
    """ A trie can consist of numbers and words.

    The trie has the following attributes:
        nodes: trie (embedded dictionaries) of the items
        count: number of items in the trie
        item_list: list of items in the trie
    """
    
    def __init__(self, items = [], separator = None):
        self.nodes = {}
        self.count = 0
        self.item_list = []

        # If an argument is included when the trie is created, add those items
        if items:
            self.add_item(items, separator)
       

    def __repr__(self):
        printable = 'The trie contains the following: \n'
        for item in sorted(set(self.item_list)):
            printable += str(item) + '\n'
        return printable
   

    def __contains__(self, item):
        return self.has_item(item)


    def _from_file(self, filename):
        """ Reads each line of the file as a separate trie entry."""
        return [line.strip().lower() for line in filename]
    
        
    def _from_string(self, my_str, separator = []):
        """ Reads in and splits strings. """
        if separator:
            return my_str.lower().replace(' ','').split(separator)
        else:
            return my_str.lower().split()
        

    def _format_items(self, unformatted):
        """ The items are formatted as follows:
                 -- leading 0s (zeroes) are added to numbers
                 -- punctuation and non-alphanum char are removed
        """
        formatted = []
        uniform_len = self.max_len(unformatted)
        for each in unformatted:
            if each.isnumeric() and len(each) < uniform_len:
                formatted.append('0' * (uniform_len - len(each)) + each)
            elif each.isnumeric():
                formatted.append(each)
            else:
                alpha_only = ''.join([char for char in each if char.isalpha()])
                formatted.append(alpha_only)
        return formatted


    def add_item(self, item, separator):
        """ Items may be read from a file, input as a string,
        or input as a list.
        """
        if isinstance(item, str) and os.path.isfile(item):
            input_list = self._from_file(item)
        elif isinstance(item, str):
            input_list = self._from_string(item, separator)
        else:
            input_list = item
            
        # If not already in the trie, the formatted items are added to the trie.
        # The lowest level of the trie has the format 'END':'END'
        for each in self._format_items(input_list):
            if each in self.nodes:
                continue
            else:
                current_dict = self.nodes
                for char in each:
                    current_dict = current_dict.setdefault(char,{})
                current_dict = current_dict.setdefault('END','END')
                self.count += 1
                self.item_list.append(each)


    def has_item(self, item):
        """ This method returns True if the item is in the trie """
        current_dict = self.nodes

        for char in item:
            if char in current_dict:
                current_dict = current_dict[char]
            else:
                return False
        if 'END' in current_dict:
            return True
        else:
            return False
    

    def has_prefix(self, prefix):
        """ This method returns True if the prefix is in the trie """
        current_dict = self.nodes

        for char in prefix:
            if char in current_dict:
                current_dict = current_dict[char]
            else:
                return False
        return True
    

    def count_items(self):
        return self.count
    

    def max_len(self, a_list):
        return max([ len(item) for item in a_list ])


if __name__ == '__main__':
    # Run tests if the module is run directly

    import unittest

    class TrieTests(unittest.TestCase):
        def test_empty_Trie(self):
            self.assertEqual(
                {},
                Trie([]).nodes
            )

        def test_filename(self):
            x = Trie('wordlist.txt')
            self.assertNotEqual(
                {},
                x.nodes
            )
            self.assertEqual(
                len(x.item_list),
                x.count_items()
            )

        def test_str1(self):
            x = Trie('THIs is A string.')
            self.assertNotEqual(
                {},
                x.nodes
            )
            self.assertEqual(
                ['this','is','a','string'],
                x.item_list
            )

        def test_str2(self):
            x = Trie('THIs, is, Another string.',',')
            self.assertNotEqual(
                {},
                x.nodes
            )
            self.assertEqual(
                ['this','is','anotherstring'],
                x.item_list
            )

        def test_str3(self):
            x = Trie('THIs , 9is  , A , string.',',')
            self.assertNotEqual(
                {},
                x.nodes
            )
            self.assertEqual(
                ['this','is','a','string'],
                x.item_list
            )

        def test_num1(self):
            y = ['0','5','10']
            x = Trie(y)
            self.assertNotEqual(
                {},
                x.nodes
            )
            self.assertEqual(
                ['00','05','10'],
                x.item_list
            )

        def test_num2(self):
            y = ['11','12','130','14']
            x = Trie(y)
            self.assertNotEqual(
                {},
                x.nodes
            )
            self.assertEqual(
                ['011','012','130','014'],
                x.item_list
            ) 

        def test_in1(self):
            x = Trie('hello there dear')
            self.assertTrue(
                x.has_item('there')
            )
            self.assertTrue(
                x.has_prefix('hell')
            )

        def test_in2(self):
            x = Trie('hello there dear')
            self.assertTrue(
                x.__contains__('there')
            )
            self.assertTrue(
                'hello' in x
            )


    unittest.main()
