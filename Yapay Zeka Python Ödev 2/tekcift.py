# Kullanıcıdan sayı alma
sayi = int(input("Lütfen bir sayı girin: "))

# Tek mi çift mi kontrolü
if sayi % 2 == 0:
    print(f"{sayi} çift bir sayıdır.")
else:
    print(f"{sayi} tek bir sayıdır.")
