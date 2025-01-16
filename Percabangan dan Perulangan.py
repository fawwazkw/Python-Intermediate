# Nested while Loops

age = 64
gender = 'M'

if age < 18:
    if gender == 'M':
        print('son')
    else:
        print('daughter')
elif age >= 18 and age < 65:
    if gender == 'M':
        print('father')
    else:
        print('mother')
else:
    if gender == 'M':
        print('grandfather')
    else:
        print('grandmother')


# One-Line while Loops

n = 5
while n > 0: n -= 1; print(n)

# The range() Function

for n in (0, 1, 2, 3, 4):
    print(n)

# The break and continue Statements
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        continue
    print(i)

# The else Clause
temp = input("Ketikan temperatur yang ingin dikonversi, eg. 45F, 120C: ")
degree = int(temp[:-1])
i_convertion = temp[-1]

if i_convertion == "C":
    result = int(round((9 * degree) / 5 + 32))
elif i_convertion == "F":
    result = int(round((degree - 32) * 5 / 9))
else:
    print("Masukan input yang benar")

print("Temperaturnya adalah", result, "derajat")

