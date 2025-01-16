def hitung_segitiga():
    alas = float(input("Masukkan alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    luas = 0.5 * alas * tinggi
    print(f"Luas segitiga adalah: {luas}")

def hitung_persegi():
    sisi = float(input("Masukkan sisi persegi: "))
    luas = sisi * sisi
    print(f"Luas persegi adalah: {luas}")

def main():
    print("Pilih rumus bangun ruang yang ingin dihitung:")
    print("1. Segitiga")
    print("2. Persegi")
    pilihan = input("Masukkan pilihan (1/2): ")

    if pilihan == '1':
        hitung_segitiga()
    elif pilihan == '2':
        hitung_persegi()
    else:
        print("Masukan Inputan Yang Benar")

main()