#Adedeji Akingbola
#Psid:1793979
x1 = int(input())
y1 = int(input())
c1 = int(input())
x2 = int(input())
y2 = int(input())
c2 = int(input())

for x in range(-10, 10):
    for y in range(-10, 10):
        if x1*x + y1*y == c1 and x2*x + y2*y == c2:
            print(str(x) + " " + str(y))
