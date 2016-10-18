import re
#Считает только положительные числа
def umnoj(string):
    result = string
    pat = r'\d+|[\-\+\/\*]'
    list = re.findall(pat,string)
    #list = string.split()
    for i in range(len(list)):
        if (list[i] == '*'):
            list[i-1] = str(float(list[i-1]) * float(list[i+1]))
            list.pop(i+1)
            list.pop(i)
            result = umnoj(' '.join(list))
            break
        if (list[i] == '/'):
            list[i-1] = str(float(list[i-1]) / float(list[i+1]))
            list.pop(i+1)
            list.pop(i)
            result = umnoj(' '.join(list))
            break
    return result

def summa(string):
    result = string
    pat = r'\d+|[\-\+\/\*]'
    list = re.findall(pat,string)
    #list = string.split()
    for i in range(len(list)):
        if (list[i] == '+'):
            list[i-1] = str(float(list[i-1]) + float(list[i+1]))
            list.pop(i+1)
            list.pop(i)
            result = summa(' '.join(list))
            break
        if (list[i] == '-'):
            list[i-1] = str(float(list[i-1]) - float(list[i+1]))
            list.pop(i+1)
            list.pop(i)
            result = summa(' '.join(list))
            break

    return result

def calc1(string):
    return summa(umnoj(string))





def main():
    string = "3 * 2, 4 + 1,6-3, 8 * 2 * 2"
    list = string.split(',')
    for i in list:
        print (i , " = " , calc1(i))
    #print(calc1('10 * -20 / 5 / 2 + 10 / 5'))

if (__name__ == '__main__'):
    main()

