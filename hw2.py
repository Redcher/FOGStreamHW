import re


def Editor1(string):
    WordsList = string.split(' ')
    for wordID in range(len(WordsList)):
        if (WordsList[wordID].isdigit() and len(WordsList[wordID]) > 3):
            WordsList[wordID] = ''
        if ('@' in WordsList[wordID][1:]):#Хотя бы 1 символ до @
            if ('.' in WordsList[wordID][WordsList[wordID].find('@')+2:-2]):#Хотя бы 1 символ до и 2 после точки
                WordsList[wordID] = '[Контакты запрещены]'
        elif ('.' in WordsList[wordID][1:-2] and not('.') in WordsList[wordID][-2:]):#Хотя бы 1 символ до и 2 после точки с исключением многоточия
            WordsList[wordID] = '[Ссылки запрещены]'
    return ' '.join(WordsList).lstrip().capitalize()

def Editor2(string):
    lookfor1 = r"[\w\.-]+@[\w-]+\.[\w\.]+" #РВ для e-mail
    lookfor2 = r"\w+\.[A-Za-z][A-Za-z\.]*" #РВ для сайтов
    lookfor3 = r"\d{4,}"# РВ для чисел
    result = re.sub(lookfor1, '[Контакты запрещены]',string)
    result = re.sub(lookfor2, '[Ссылки запрещены]', result)
    result = re.sub(lookfor3, '', result)
    result = result.lstrip().capitalize()

    return result

def main():
    print(Editor1('1234 hello qwerty@mail.ru 23432 my site is vk.com bye...'))
    print(Editor2('1234 hello qwerty@mail.ru 23432 my site is vk.com bye...'))

if (__name__ == '__main__'):
    main()