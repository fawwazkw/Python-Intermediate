
def compare_credit_scores(score_a, score_b):
    if score_a > score_b:
        return "Peminjam A memiliki risiko lebih rendah."
    elif score_b > score_a:
        return "Peminjam B memiliki risiko lebih rendah."
    else:
        return "Risiko kedua peminjam sama."

# Menerima input skor kredit
try:
    score_a = float(input("Masukkan skor kredit Peminjam A: "))
    score_b = float(input("Masukkan skor kredit Peminjam B: "))
    
    # Membandingkan skor kredit dan mencetak hasil
    result = compare_credit_scores(score_a, score_b)
    print(result)
except ValueError:
    print("Input tidak valid. Harap masukkan angka.")