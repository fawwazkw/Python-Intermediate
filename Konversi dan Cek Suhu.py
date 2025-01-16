def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))

celsius = fahrenheit_to_celsius(fahrenheit)

if 36.5 <= celsius <= 37.2:
    print(f"{celsius} Suhu Badan Normal")
elif celsius < 36.5:
    print(f"{celsius} Hipotermia")
else:
    print(f"{celsius} Hipertermia")