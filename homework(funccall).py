def single_root_word(root_word, *otherwords):
    othr = list(otherwords)
    same_words = []
    for i in othr:
        if root_word in i or i in root_word:
            same_words.append(i)
    return same_words

print(single_root_word('корь','орь', 'якорь', 'море', 'сора'))