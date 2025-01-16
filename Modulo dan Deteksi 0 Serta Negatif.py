def modulo(n):
    if n == 0:
        print("0 bukanlah angka ganjil atau genap.")
    elif n < 0:
        print("inputan yang benar adalah angka bulat positif.")
    elif n % 2 == 0: 
        print("angka", n, "adalah angka genap.") 
    else: 
        print("angka", n, "adalah angka ganjil.")

def main():
    n = int(input("Masukkan angka: "))
    modulo(n)

main()