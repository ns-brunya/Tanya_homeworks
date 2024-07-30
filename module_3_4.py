def single_root_words(root_word,*other_word):
    same_words=[]
    for i in range(len(other_word)):
        if root_word.lower() in other_word[i].lower() or other_word[i].lower() in root_word.lower():
            same_words.append(other_word[i])
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)