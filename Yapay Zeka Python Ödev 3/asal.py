# Asallık kontrolü
print("1’den 100’e kadar olan asal sayılar:")
for sayi in range(2, 101):  # 1 asal değildir, 2’den başlar
    asal = True  # Asal olduğunu varsayalım
    for i in range(2, int(sayi ** 0.5) + 1):  # 2’den kareköküne kadar kontrol
        if sayi % i == 0:
            asal = False
            break
    if asal:
        print(sayi)
