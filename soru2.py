birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]
onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]


def okunus(sayı_okuma):
    birler_basamagi = sayı % 10
    onlar_basamagi = sayı // 10

    return onlar[onlar_basamagi] + " " + birler[birler_basamagi]

def sayı_atama(sayı):

    basamak = 0
    while (sayı > 0):
        basamak += 1
        sayı //= 10
    if(basamak == 2):
        print(okunus(sayı))
    else:
        print("İki basamaklı sayı giriniz.")

sayı = int(input("Sayı:"))
sayı_atama(sayı)