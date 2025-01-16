def main():
    sentence = input("Masukkan sebuah kalimat: ")
    
    if not sentence:
        print("Silakan masukkan sebuah kalimat.")
    elif len(sentence) < 50:
        print(f"JUmlah kalimat ideal, Berikut ini ada kalimatnya: {sentence}")
    else:
        print("Kalimat terlalu panjang, harus kurang dari 50 karakter.")

main()