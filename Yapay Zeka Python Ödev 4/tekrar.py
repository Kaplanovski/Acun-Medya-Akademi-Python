# Kullanıcıdan liste elemanları alma
giris_listesi = input("Liste elemanlarını aralarında boşluk bırakarak girin: ").split()

# Tekrar eden elemanları kaldırma
benzersiz_liste = list(set(giris_listesi))

# Sonuçları ekrana yazdırma
print(f"Orijinal Liste: {giris_listesi}")
print(f"Benzersiz Liste: {benzersiz_liste}")
