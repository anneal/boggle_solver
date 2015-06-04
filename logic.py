def trie():
    wordlist = [ words.strip() for words in open('wordlist.txt','r') ]

    result = {}
    for word in wordlist:
        current_dict = result
        for letter in word:
            current_dict = current_dict.setdefault(letter,{})
        current_dict = current_dict.setdefault('END','END')

    return result        

def check_real_word(word):
    current_dict = trie()
    
    for letter in word:
        if letter in current_dict:
            current_dict = current_dict[letter]
        else:
            return False
    if 'END' in current_dict:
        return word
    else:
        return True
