print("""
vize1 %30
vize2 %30
final %40 
""")

vize1 = int(input("vize 1 notu: "))
vize2 = int(input("vize 2 notu: "))
final = int(input("final notu: "))

if((vize1 >= 0 and vize1 <=100) and (vize2 >= 0 and vize2 <=100) and (final >= 0 and final <=100)):
 vize1 = ((30*vize1)/100)
 vize2 = ((30*vize2)/100)
 final = ((40*final)/100)

 toplam = vize1 + vize2 + final

 if (toplam >= 90):
  print("Harf notu: AA")
 elif (toplam >= 85):
  print("Harf notu: BA")
 elif (toplam >= 80):
  print("Harf notu: BB")
 elif (toplam >= 75):
  print("Harf notu: BB")
 elif (toplam >= 70):
  print("Harf notu: CC")
 elif (toplam >= 65):
  print("Harf notu: DC")
 elif (toplam >= 60):
  print("Harf notu: DD")
 elif (toplam >= 55):
  print("Harf notu: FD")
 else:
  print("Harf notu: FF")


else:
 print("Geçersiz değer girdiniz (0-100 arası değer olmalı.) Program sonlandırılıyor..")


