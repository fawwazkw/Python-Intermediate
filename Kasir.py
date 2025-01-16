stock = {
    'Apel': 10,
    'Jeruk': 7,
    'Anggur': 6
}


harga = {
    'Apel': 10000,
    'Jeruk': 15000,
    'Anggur': 20000
}

jumlah_buah = {}
for buah in stock:
    while True:
        jumlah = int(input(f"\nMasukkan Jumlah {buah}: "))
        if jumlah <= stock[buah]:
            jumlah_buah[buah] = jumlah
            stock[buah] -= jumlah
            break
        else:
            print(f"Jumlah yang dimasukkan terlalu banyak. Stock {buah} tinggal: {stock[buah]}")


print("\nDetail Belanja")
total = 0
for buah, jumlah in jumlah_buah.items():
    subtotal = jumlah * harga[buah]
    total += subtotal
    print(f"{buah}: {jumlah} x {harga[buah]} = {subtotal}")

print(f"Total: {total}")


while True:
    jumlah_uang = int(input("\nMasukkan jumlah uang: "))
    if jumlah_uang >= total:
        kembalian = jumlah_uang - total
        print("\nTerima kasih")
        print(f"Uang kembali anda: {kembalian}")
        break
    else:
        kekurangan = total - jumlah_uang
        print(f"Uang anda kurang sebesar {kekurangan}")