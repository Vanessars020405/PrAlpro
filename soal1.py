def beratbadan(BMI, tinggi_harapan):
    return BMI * (tinggi_harapan**2)

tinggi = float(input("Masukkan tinggi badan anda (dalam meter): "))
BMI = float(input("Masukkan nilai BMI yang diharapkan: "))

hitung_berat= beratbadan(BMI, tinggi)

print(f"berat badan yang diperlukan {hitung_berat:.2f} kilogram.")

