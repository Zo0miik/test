import pymorphy2

from app import app
from flask import render_template
from flask import request

@app.route('/index', methods=["GET","POST"])

def index():
    
    count, data = analyz(words=all_words())

    return render_template('index.html',the_result=data, count=count)


morph = pymorphy2.MorphAnalyzer()
@app.route('/', methods= ["GET","POST"])
def all_words():
    words = request.form.get('word')
    return words

def analyz(words):   
    new_list = []
    word = all_words()
    parse = morph.parse(word)[0]
    lexeme_word = parse.lexeme
        
    for word in lexeme_word:
        one_word = word[0]
        if one_word not in new_list:
            new_list.append(one_word)
    count = len(new_list)
    print('Результат: ', count)
    return count, new_list


