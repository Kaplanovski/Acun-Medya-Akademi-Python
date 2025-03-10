def palindrom_mu(kelime):
    return kelime == kelime[::-1]

# Kullanıcıdan kelime alma
kelime = input("Bir kelime girin: ")
if palindrom_mu(kelime):
    print(f"'{kelime}' bir palindromdur.")
else:
    print(f"'{kelime}' bir palindrom değildir.")
