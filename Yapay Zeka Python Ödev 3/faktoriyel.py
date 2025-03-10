# Kullanıcıdan sayı alma
sayi = int(input("Lütfen bir sayı girin: "))

# Faktöriyel hesaplama
faktoriyel = 1
for i in range(1, sayi + 1):
    faktoriyel *= i

print(f"{sayi}! = {faktoriyel}")
