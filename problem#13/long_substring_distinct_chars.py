def get_long_substring(word:str, k):
    chars = []
    for c in word:
        if(not chars.__contains__(c) and len(chars) < k):
            chars.append(c)

