def dosya_yaz(dosya_adi, metin, satirlar):
    try:
        with open(dosya_adi, 'w', encoding='utf-8') as dosya:
            dosya.write(metin + '\n')
            for satir in satirlar:
                dosya.write(satir + '\n')
        print(f"{dosya_adi} dosyası başarıyla oluşturuldu ve yazıldı.")
    except Exception as e:
        print(f"Dosya yazılırken bir hata oluştu: {e}")

def dosya_oku(dosya_adi):
    try:
        with open(dosya_adi, 'r', encoding='utf-8') as dosya:
            satirlar = dosya.readlines()
        return satirlar
    except Exception as e:
        print(f"Dosya okunurken bir hata oluştu: {e}")
        return []

# Kullanıcıdan metin alma ve dosyaya yazma
metin = input("Bir metin girin: ")
satirlar = []
for i in range(5):
    satir = input(f"{i+1}. satırı girin: ")
    satirlar.append(satir)

dosya_adi = "deneme.txt"
dosya_yaz(dosya_adi, metin, satirlar)

# Dosyayı okuma ve ekrana yazdırma
print("Dosya içeriği:")
okunan_satirlar = dosya_oku(dosya_adi)
for satir in okunan_satirlar:
    print(satir.strip())
