#2
def print_name_and_age ():
    Name = input("His name: ")
    Age = int(input("His age: "))
    
    print("Name : ", Name)
    print("Age: ", Age)

#1   
def func1(*args):
    for arg in args:
        print(arg)


#3
def chees(x,y,x1,y1):
    #проверка соседства клеток
    if abs(x-y) <= 1 and abs (x1-y1) <= 1:
        return "Yes"
    else:
        return "Net"
x = int(input("Stolb first cletki:  "))
y = int(input("Stroka first cletki: "))
x1 = int(input("Stolb second cletki:  "))
y1 = int(input("Stroka second cletki: "))

itog = chees(x,y,x1,y1)

#5
def calculation(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction
result = calculation(8, 6)
print("сумма:",result[0])
print("разность:",result[1])

#4
def funcia4(a: list, b:list):
    c = []
    if len(a) > len(b):
        x = len(a)
    else:
        x = len(b)
    for i in range(x):
        print(i)
        try:
            c.append([a[i], b[i]])
            if i > (len(a)-1):
                c.append(b[i])
            if i > (len(b)-1):
                c.append(a[i])
        except:
            if i > (len(a)-1):
                c.append(b[i])
            if i > (len(b)-1):
                c.append(a[i])
        
    print(c)

    

