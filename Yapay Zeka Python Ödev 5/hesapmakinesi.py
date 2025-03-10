def hesap_makinesi(sayi1, sayi2):
    toplam = sayi1 + sayi2
    fark = sayi1 - sayi2
    carpim = sayi1 * sayi2
    if sayi2 != 0:
        bolum = sayi1 / sayi2
    else:
        bolum = "Tanımsız (0'a bölme)"
    return toplam, fark, carpim, bolum

# Kullanıcıdan iki sayı alma
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
sonuclar = hesap_makinesi(sayi1, sayi2)

# Sonuçları ekrana yazdırma
print(f"Toplam: {sonuclar[0]}, Fark: {sonuclar[1]}, Çarpım: {sonuclar[2]}, Bölüm: {sonuclar[3]}")
