def analisa_pelanggan(nama, usia, saldo, pekerjaan):
    #Konsistensi Tipe Data
    if not isinstance(nama, str):
        print("Error: Data untuk parameter 'nama' harus berupa string.")
        return
    if not isinstance(usia, int):
        print("Error: Data untuk parameter 'usia' harus berupa integer.")
        return
    if not isinstance(saldo, float):
        print("Error: Data untuk parameter 'saldo' harus berupa float.")
        return
    if not isinstance(pekerjaan, str):
        print("Error: Data untuk parameter 'pekerjaan' harus berupa string.")
        return

    # Penentuan kategori usia
    if usia < 18:
        kategori = "Pelanggan Anak"
    elif 18 <= usia <= 60:
        kategori = "Pelanggan Dewasa"
    else:
        kategori = "Pelanggan Lansia"
    # Penentuan rekomendasi produk bank
    if saldo < 1000000:
        rekomendasi = "Tabungan Reguler"
    elif 1000000 <= saldo <= 10000000:
        rekomendasi = "Tabungan Premium"
    else:
        rekomendasi = "Investasi Deposito"

    # Output
    print(f"\nNama: {nama}")
    print(f"Usia: {usia} tahun ({kategori})")
    print(f"Saldo: Rp {saldo}")
    print(f"Pekerjaan: {pekerjaan}")
    print(f"Rekomendasi Produk Bank: {rekomendasi}")


# Pemanggilan Fungsi
analisa_pelanggan("Fawwaz Kumudani Widyadhana", 24, 50000000.0, "BUMN")