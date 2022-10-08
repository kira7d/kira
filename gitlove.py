# a = [1, 34, 66, 83, 0]
# print(a[-3::])

a = input().lower()
if a[::] == a[::-1]:
    print("yes")
else:
    print("no")
