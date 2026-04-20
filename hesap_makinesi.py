# Profesyonel Hesap Makinesi Projesi

def toplama(s1, s2):
    return s1 + s2

def cikarma(s1, s2):
    return s1 - s2

def carpma(s1, s2):
    return s1 * s2

def bolme(s1, s2):
    if s2 == 0:
        return "Hata! Bir sayı 0'a bölünemez."
    return s1 / s2

print("--- HESAP MAKİNESİNE HOŞ GELDİNİZ ---")
print("İşlemler: 1-Topla, 2-Çıkar, 3-Çarp, 4-Böl")

secim = input("Yapmak istediğiniz işlemin numarasını girin (1/2/3/4): ")

sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

if secim == '1':
    print(f"Sonuç: {toplama(sayi1, sayi2)}")
elif secim == '2':
    print(f"Sonuç: {cikarma(sayi1, sayi2)}")
elif secim == '3':
    print(f"Sonuç: {carpma(sayi1, sayi2)}")
elif secim == '4':
    print(f"Sonuç: {bolme(sayi1, sayi2)}")
else:
    print("Geçersiz seçim yaptınız!")
