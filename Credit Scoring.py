def calculate_credit_score(umur, pemasukan, history_kredit, pinjaman):
    # Validate input types
    if not (isinstance(umur, int) and isinstance(pemasukan, int) and isinstance(history_kredit, int) and isinstance(pinjaman, int)):
        raise ValueError("Inputan harus Integer")
    
    # Check umur and credit history conditions
    if umur < 21 or umur > 65 or history_kredit < 3:
        return (0, "Berisiko Tinggi")
    
    # Calculate credit score
    credit_score = (history_kredit * 10) + (pemasukan - pinjaman) / 10000
    
    # Determine risk level
    if credit_score < 100:
        risk_level = "Berisiko Tinggi"
    elif 100 <= credit_score <= 200:
        risk_level = "Berisiko Sedang"
    else:
        risk_level = "Berisiko Rendah"
    
    return (credit_score, risk_level)

# Example usumur
print(calculate_credit_score(30, 5000000, 7, 1000000))  