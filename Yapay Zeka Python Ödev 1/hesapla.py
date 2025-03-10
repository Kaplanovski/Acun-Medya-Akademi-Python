# Kullanıcıdan iki sayı alma
sayi1 = float(input("Lütfen birinci sayıyı girin: "))
sayi2 = float(input("Lütfen ikinci sayıyı girin: "))

# Matematiksel işlemler
toplam = sayi1 + sayi2
fark = sayi1 - sayi2
carpim = sayi1 * sayi2
if sayi2 != 0:
    bolum = sayi1 / sayi2
else:
    bolum = "Tanımsız (0'a bölme)"

# Sonuçları ekrana yazdırma
print(f"Toplam: {toplam}")
print(f"Fark: {fark}")
print(f"Çarpım: {carpim}")
print(f"Bölüm: {bolum}")
