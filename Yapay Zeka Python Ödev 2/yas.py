# Kullanıcıdan yaş alma
yas = int(input("Lütfen yaşınızı girin: "))

# Yaş grubu belirleme
if 0 <= yas <= 12:
    yas_grubu = "Çocuk"
elif 13 <= yas <= 19:
    yas_grubu = "Genç"
elif 20 <= yas <= 59:
    yas_grubu = "Yetişkin"
elif yas >= 60:
    yas_grubu = "Yaşlı"
else:
    yas_grubu = "Geçersiz yaş girdiniz. Lütfen pozitif bir değer girin."

# Sonucu ekrana yazdırma
print(f"Yaş grubunuz: {yas_grubu}")
