# Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

N=int(input('Введите число: '))

def Summery(N):
    sum=0
    for i in range(N+1):
        sum+=i
    return sum
print(Summery(N))

# решение от Дениса
# n = int(input())
# print(int(((n + 1) / 2) * n))
