# Функция перебирает все символы
# Когда натыкается на Открывающую скобку, ищет Закрывающую и удаляет обе
# Конструкция со срезами нужна на случай, если Закрывающая скобка будет ДО Открывающей
# Потом он снова проходится по всем символам в поисках любой скобки, если их нет, возвращает 'YES'
def BraceChecker2(string):
    index = -1
    for i in string:
        index += 1
        if i == '(':
            if (')' in string[index:]):
                string = string[:index] + string[index:].replace(')', '-', 1)
                string = string[:index] + string[index:].replace(i, '-', 1)
        if i == '{':
            if ('}' in string[index:]):
                string = string[:index] + string[index:].replace('}', '-', 1)
                string = string[:index] + string[index:].replace(i, '-', 1)
        if i == '[':
            if (']' in string[index:]):
                string = string[:index] + string[index:].replace(']', '-', 1)
                string = string[:index] + string[index:].replace(i, '-', 1)
    index = -1
    for i in string:
        index += 1
        if (i in '([{'):
            return -1
        elif (i in ')]}'):
            return index
    return 'YES'

def main():
    string = input('Введите строку:')
    #string = '))'
    print (BraceChecker2(string))#Она не проверяет случай, когда (-[-)-]

if (__name__ == "__main__"):
    main()