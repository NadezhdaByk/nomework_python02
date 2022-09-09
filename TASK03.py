# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

N=int(input('Введите число: '))

def Divider(N):
    div=0
    for i in range(2,N+1):
        if N%i==0:
            div=i
            break
    return div

print(Divider(N))


# Решение от преподавателя

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0:
#         print(i)
#         flag = False
#     i += 1

