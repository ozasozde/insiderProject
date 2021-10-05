def tam_bölünenler(min, max, bolen):

    sayac=0
    for i in range(min, max + 1):
        if(i % bolen == 0):
            sayac += 1

    return(sayac)


min = int(input("min pozitif sayi:"))
max = int(input("max pozitif sayi:"))
bolen_sayi = int(input("bölünecek sayiyi:"))

print("Toplam {} sayı bölünür.".format(tam_bölünenler(min,max,bolen_sayi)))