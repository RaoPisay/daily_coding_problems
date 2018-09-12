import time
#Recursive approach

#Solution function, We have to convert 
def word_break(words:set, input:str, words_so_far:set = set(), min_word_len = 3):
    if len(input) < 3:
        return
    if words.__contains__(input):
        words_so_far.add(input)
    word_break(words,input[:-1])
    word_break(words,input[1:])
    return words_so_far


#Data preparation
currnt_time = time.time()
words = set(['samsung','sam','sung'])
input = 'samsung'

r_words = word_break(words, input)
print(r_words)
r_words.clear()

words = set(['bed', 'bath', 'bedbath', 'and', 'beyond'])
input = 'bedbathandbeyond'

r_words = word_break(words, input)
print(r_words)
r_words.clear()

words = set(['quick', 'brown', 'the', 'fox'])
input = 'thequickbrownfox'

r_words = word_break(words, input)
print(r_words)
r_words.clear()

print(time.time() - currnt_time)