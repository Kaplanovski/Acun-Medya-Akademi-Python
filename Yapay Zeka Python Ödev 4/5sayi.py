# Kullanıcıdan 5 sayı alma ve listeye ekleme
sayi_listesi = []
for i in range(5):
    sayi = float(input(f"{i+1}. sayıyı girin: "))
    sayi_listesi.append(sayi)

# Liste işlemleri
toplam = sum(sayi_listesi)
ortalama = toplam / len(sayi_listesi)
en_buyuk = max(sayi_listesi)
en_kucuk = min(sayi_listesi)

# Sonuçları ekrana yazdırma
print(f"Liste: {sayi_listesi}")
print(f"Toplam: {toplam}")
print(f"Ortalama: {ortalama}")
print(f"En büyük eleman: {en_buyuk}")
print(f"En küçük eleman: {en_kucuk}")
