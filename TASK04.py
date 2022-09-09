import random

N=int(input("Введите кол-во учеников в классе: "))
heigth=int(input("Введите рост мальчика: "))

def Enter_Class(N, h):
    class_1=[]
    for i in range(0,N):
        class_1.append(random.randint(160,180))
    class_1.append(h)
    return class_1

class_2=Enter_Class(N, heigth)
print(class_2)
class_new=sorted(class_2)
print(class_new)   
print(class_new.index(heigth)+1)

# решение от преподавателя
# n = int(input())
# arr_rost = list()

# for i in range(n):
#     rost = int(input())
#     arr_rost.append(rost)
    
# # имя_списка.sort()
# # sorted(имя_списка)
# my_rost = int(input())

# j = 1
# for i in arr_rost:
#     if my_rost <= i:
#         j += 1
# print(j)
