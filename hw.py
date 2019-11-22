print('hello world')
a = int(input("Введите число а"))
b = int(input("Введите число b"))

sum = a + b
if a > b:
    max = a
elif b > a:
    max = b
else:
    max = "Числа равны"

s = a * b

print("a =", a)
print("b =", b)
print("max =", max)
print("sum =", sum)
print("a * b =", s)
