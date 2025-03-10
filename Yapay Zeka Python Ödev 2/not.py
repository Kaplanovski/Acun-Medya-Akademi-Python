# Kullanıcıdan not alma
not_degeri = int(input("Lütfen notunuzu girin (0-100 arası): "))

# Harf notu belirleme
if 90 <= not_degeri <= 100:
    harf_notu = "A"
elif 80 <= not_degeri <= 89:
    harf_notu = "B"
elif 70 <= not_degeri <= 79:
    harf_notu = "C"
elif 60 <= not_degeri <= 69:
    harf_notu = "D"
elif 0 <= not_degeri < 60:
    harf_notu = "F"
else:
    harf_notu = "Geçersiz not. Lütfen 0-100 arasında bir değer girin."

# Sonucu ekrana yazdırma
print(f"Girdiğiniz nota karşılık gelen harf notu: {harf_notu}")
