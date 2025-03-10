# Kullanıcıdan kelimeler alma
kelime_listesi = []
kelime_sayisi = int(input("Kaç kelime girmek istersiniz? "))
for i in range(kelime_sayisi):
    kelime = input(f"{i+1}. kelimeyi girin: ")
    kelime_listesi.append(kelime)

# Listeyi ters sıralama
ters_sirali_liste = list(reversed(kelime_listesi))

# Sonuçları ekrana yazdırma
print(f"Orijinal Liste: {kelime_listesi}")
print(f"Ters Sıralı Liste: {ters_sirali_liste}")
