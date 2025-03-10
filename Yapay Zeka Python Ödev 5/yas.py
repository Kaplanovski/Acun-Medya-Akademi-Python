def yil_kaldi_100_yas(yas):
    return 100 - yas

# Kullanıcıdan yaş alma
yas = int(input("Lütfen yaşınızı girin: "))
yil_kaldi = yil_kaldi_100_yas(yas)

if yil_kaldi > 0:
    print(f"100 yaşına ulaşmanıza {yil_kaldi} yıl kaldı.")
elif yil_kaldi == 0:
    print("Tebrikler! Bu yıl 100 yaşına ulaştınız!")
else:
    print(f"100 yaşı {abs(yil_kaldi)} yıl önce geçmişsiniz.")
