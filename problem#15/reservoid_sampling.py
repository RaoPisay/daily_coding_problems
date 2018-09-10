import random as random
def select_random():
    stream_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    idx = 0    
    while idx < len(stream_chars):
        print('Random char from the first',(idx+1),'char is ', gen_random(stream_chars, idx))
        idx+=1

def gen_random(stream:str, idx:int):
    r_idx = random.randint(0, idx)
    return stream[r_idx]

select_random()