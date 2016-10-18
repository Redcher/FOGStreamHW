class point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

def distance(point1, point2):
    return ((point1.x - point2.x)**2 + (point1.y - point2.y)**2)**(1/2)

# Передаётся список точек, возвращает список с расстоянием между каждой из них
def calc(listPoints):
    listDist = []
    for i in range(len(listPoints)):
        for j in range(len(listPoints)):
            if (i != j):
                listDist.append(distance(listPoints[i],listPoints[j]))
    return listDist

def main():
    file = open('hw4.txt', mode = 'r')
    max = None
    min = None
    listPoints = []
    for i in file:
        i = i.split()
        i = [int(j) for j in i]
        listPoints.append(point(i[0],i[1]))
    listDist = calc(listPoints)
    for i in listDist:
        if (max == None):
            max = i
        elif(i>max):
            max = i
        if (min == None):
            min = i
        elif (i < max):
            min = i
    print("Наибольшее расстояние: " + str(max))
    print("Наименьшее расстояние: " + str(min))

if (__name__ == "__main__"):
    main()