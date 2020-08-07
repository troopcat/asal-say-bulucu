from time import sleep

def asal_sayı_mı(x:int):
    flag = True
    if x == 2:
        return flag
    elif x % 2 == 0:
        flag = False
    if flag:
        for i in range(3,int(x/2)):
            if x % i == 0:
                flag = False
                break
    return flag

sayac = 2
run = True
asal_sayılar = list()

print("""
Bu program asal sayıları bastıracaktır
aynı zamanda CTRL+C hotkey'i ile asal sayıları
bir txt dosyasına kaydetecektir.
Program 7 saniye sonra başlayacaktır.
""")
sleep(7)

while run:
    try:
        kontrol = asal_sayı_mı(sayac)
        if kontrol:
            print(sayac)
            asal_sayılar.append(sayac)
        sayac += 1
    except KeyboardInterrupt:
        f = open("asal_sayilar.txt","w")
        for i in asal_sayılar:
            f.write(f"{i}\n")
        f.close()
        print("\nOK")
        run = False

