def hitung_detail_hari(total_hari):
    tahun = total_hari // 365
    sisa_hari = total_hari % 365

    bulan = sisa_hari // 30
    sisa_hari = sisa_hari % 30

    minggu = sisa_hari // 7
    hari = sisa_hari % 7

    return tahun, bulan, minggu, hari


total_hari = int(input("Masukkan total jumlah hari: "))

tahun, bulan, minggu, hari = hitung_detail_hari(total_hari)

print(f"{total_hari} hari adalah {tahun} tahun, {bulan} bulan, {minggu} minggu, dan {hari} hari.")