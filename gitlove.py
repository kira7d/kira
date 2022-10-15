# a = [1, 34, 66, 83, 0]
# print(a[-3::])

# a = [1, 2, 3, 4, 5, 6]
# c = 1
# for b in a:
#     c *= 3
#     print(c)
#
# a = [1, 2, 3, 4, 5, 6]
# c = 1
# for b in a:
#     c *= b
#     print(c)

# for i in range (1,11):
#     print(i)
#
# for i in range(11):
#     print(i,end = " ")

# for i in range(10,-1, -1):
#     print(i,end = " ")

# for i in range(-10,-1, 2):
#     print(i, end = " ")

# for i in range(1, 22, 3):
#     print(i, end = " ")

# a = map(int, input().split())
# b = 0
# for i in a:
#     if i % 2 != 0:
#         b += i
# print(b)

# a = list(map(str,input().split()))
# for i in range(len(a)):
#    a[i] = len(a[i])
# print(*a)

# a = ["киев" , "Одесса"]
# for i in range(len(a)):
#     print(i, end = " ")

# a = 0
# for i in range(12):
#     print(i, end = " ")
#     if i % 2 == 0:
#      a += i
# print(a)

# n = int(input())
# for i in range(2,n):
#      if n % i == 0:
#          print("да")
#          break
# else:
#     print("нет")

# n = int(input())
# a = 0
# for i in range(1,n):
#     if i % 3 == 0 or i % 5 == 0:
#         a += i
# print(a)

n,m = map(int, input().split())
b = []
while n <= m:
    b.append(n**2)
    n = n+1
print(*b)









