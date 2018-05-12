#coding:utf-8

import pymorphy2

morph = pymorphy2.MorphAnalyzer()

def all_words():
    words = []
    print('Ввод списка слов построчно: ')
    while True:
        
        one_input = input()
        if one_input == '':
            break
        else:
            words.append(one_input)
    return words

def analyz(words):   
    new_list = []
    print(words)
    for word in words:
        parse = morph.parse(word)[0]
        lexeme_word = parse.lexeme
        
        for word in lexeme_word:
            one_word = word[0]
            if one_word not in new_list:
                new_list.append(one_word)
    
    print('Результат: ', len(new_list))
    # for word in new_list:
    #     print(word)
    return new_list

data = analyz(words=all_words())
print(data)



