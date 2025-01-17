# Mengambil input dari pengguna
jumlah_pinjaman = float(input("Masukkan jumlah pokok pinjaman : ")) 
persentase_bunga = float(input("Masukkan persentase bunga tahunan: "))

# Menghitung dan menampilkan tabel perhitungan bunga tahunan
print("\nTahun\tBunga Tahunan\tTotal Pembayaran")
print("========================================")
total_bunga = 0

for tahun in range(1, 11):
    bunga_tahunan = jumlah_pinjaman * (persentase_bunga / 100)
    total_pembayaran = jumlah_pinjaman + bunga_tahunan
    total_bunga += bunga_tahunan
    
    print(f"{tahun}\t{bunga_tahunan:,.2f}\t{total_pembayaran:,.2f}")
    
    jumlah_pinjaman = total_pembayaran

print(f"\nTotal bunga yang harus dibayar setelah 10 tahun: {total_bunga:,.2f}")