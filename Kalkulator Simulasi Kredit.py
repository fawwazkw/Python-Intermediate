def validate_input(prompt, input_type=float, condition=lambda x: x > 0):
    while True:
        try:
            value = input_type(input(prompt))
            if condition(value):
                return value
            else:
                print("Input harus berupa angka positif.")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

def main():
    print("=== Kalkulator Simulasi Kredit ===")
    
    plafon_kredit = validate_input("Masukkan Plafon Kredit (dalam Rupiah): ", float)
    bunga_tahunan = validate_input("Masukkan Bunga Tahunan (%): ", float)
    tenor = validate_input("Masukkan Tenor (dalam tahun): ", int, lambda x: x > 0)
    
    tenor_bulan = tenor * 12
    bunga_bulanan = bunga_tahunan / 12 / 100
    cicilan_bulanan = plafon_kredit / tenor_bulan + (plafon_kredit * bunga_bulanan)
    total_bunga = plafon_kredit * bunga_bulanan * tenor_bulan
    total_pembayaran = plafon_kredit + total_bunga
    
    print("=== Hasil Perhitungan ===")
    print(f"Cicilan Bulanan: Rp {cicilan_bulanan:.2f}")
    print(f"Total Bunga: Rp {total_bunga:.2f}")
    print(f"Total Pembayaran: Rp {total_pembayaran:.2f}")
    
main()