# Calculator Application

# Libraries
import math
import time


# Functions
def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def square(a):
    return a ** 2


def squareroot(a):
    return a ** 0.5


def power(a, b):
    return a ** b


while True:
    print("Hesap Makinesi")
    print("--------------------")
    print("İşlemler:")
    print("1.Toplama")
    print("2.Çıkarma")
    print("3.Çarpma")
    print("4.Bölme")
    print("5.Kare Alma")
    print("6.Kök Alma")
    print("7.Üs Alma")
    print("8.Logaritma")
    print("q.Çıkış")
    print("--------------------")


    selection = input("Yapmak istediğiniz işlemi seçiniz:")

    if selection == "q":

        print("Çıkış yapılıyor...\n")
        time.sleep(1)
        break

    elif selection == "1":
        while True:
            print("1.Toplama İşlemi (Çıkış için 'q' tuşlayınız.)")

            x = input("İlk sayıyı giriniz:")

            if x == "q":
                print("Menüye dönülüyor...\n")
                time.sleep(1)
                break
            elif not x.isdigit():
                print("Hatalı giriş. Lütfen bir tam sayı veya çıkış için 'q' giriniz.\n")
                continue
            else:
                x = int(x)

            y = input("İkinci sayıyı giriniz:")

            if y == "q":
                print("Menüye dönülüyor...\n")
                time.sleep(1)
                break
            elif not y.isdigit():
                print("Hatalı giriş. Lütfen bir tam sayı veya çıkış için 'q' giriniz.\n")
                continue
            else:
                y = int(y)

            print("{} + {} = {}\n".format(x, y, addition(x, y)))
            time.sleep(0.5)


    elif selection == "2":
        while True:
            print("2.Çıkarma İşlemi (Çıkış için 'q' tuşlayınız.)")

            x = input("İlk sayıyı giriniz:")

            if x == "q":
                print("Menüye dönülüyor...\n")
                time.sleep(1)
                break
            elif not x.isdigit():
                print("Hatalı giriş. Lütfen bir tam sayı veya çıkış için 'q' giriniz.\n")
                continue
            else:
                x = int(x)

            y = input("İkinci sayıyı giriniz:")

            if y == "q":
                print("Menüye dönülüyor...\n")
                time.sleep(1)
                break
            elif not y.isdigit():
                print("Hatalı giriş. Lütfen bir tam sayı veya çıkış için 'q' giriniz.\n")
                continue
            else:
                y = int(y)

            print("{} - {} = {}\n".format(x, y, subtraction(x, y)))
            time.sleep(0.5)


    elif selection == "3":
        while True:
            print("3.Çarpma İşlemi (Çıkış için 'q' tuşlayınız.)")

            x = input("İlk sayıyı giriniz:")

            if x == "q":
                print("Menüye dönülüyor...\n")
                time.sleep(1)
                break
            elif not x.isdigit():
                print("Hatalı giriş. Lütfen bir tam sayı veya çıkış için 'q' giriniz.\n")
                continue
            else:
                x = int(x)

            y = input("İkinci sayıyı giriniz:")

            if y == "q":
                print("Menüye dönülüyor...\n")
                time.sleep(1)
                break
            elif not y.isdigit():
                print("Hatalı giriş. Lütfen bir tam sayı veya çıkış için 'q' giriniz.\n")
                continue
            else:
                y = int(y)

            print("{} x {} = {}\n".format(x, y, multiplication(x, y)))
            time.sleep(0.5)

    elif selection == "4":
        while True:
            print("3.Bölme İşlemi (Çıkış için 'q' tuşlayınız.)")

            x = input("İlk sayıyı giriniz:")

            if x == "q":
                print("Menüye dönülüyor...\n")
                time.sleep(1)
                break
            elif not x.isdigit():
                print("Hatalı giriş. Lütfen bir tam sayı veya çıkış için 'q' giriniz.\n")
                continue
            else:
                x = int(x)

            y = input("İkinci sayıyı giriniz:")

            if y == "q":
                print("Menüye dönülüyor...\n")
                time.sleep(1)
                break
            elif not y.isdigit():
                print("Hatalı giriş. Lütfen bir tam sayı veya çıkış için 'q' giriniz.\n")
                continue
            else:

                y = int(y)

                if x != 0 and y == 0:
                    print("Bir sayının 0'a bölümü tanımsızdır.\n")
                    time.sleep(0.5)


                elif x == 0 and y == 0:
                    print("0'ın 0'a bölümü tanımsızdır.\n")
                    time.sleep(0.5)


                else:
                    print("{} / {} = {}\n".format(x, y, division(x, y)))
                    time.sleep(0.5)


    elif selection == "5":
        while True:
            print("5.Kare Alma İşlemi (Çıkış için 'q' tuşlayınız.)")

            x = input("İlk sayıyı giriniz:")

            if x == "q":
                print("Menüye dönülüyor...\n")
                time.sleep(1)
                break
            elif not x.isdigit():
                print("Hatalı giriş. Lütfen bir tam sayı veya çıkış için 'q' giriniz.\n")
                continue
            else:
                x = int(x)

                print("{}^2 = {}\n".format(x, square(x)))
                time.sleep(0.5)


    elif selection == "6":
        while True:

            print("6.Kök Alma İşlemi (Çıkış için 'q' tuşlayınız.)")

            x = input("İlk sayıyı giriniz:")

            if x == "q":
                print("Menüye dönülüyor...\n")
                time.sleep(1)
                break
            elif not x.isdigit():
                print("Hatalı giriş. Lütfen bir tam sayı veya çıkış için 'q' giriniz.\n")
                continue
            else:
                x = int(x)

                if x < 0:
                    print("Kökün için negatif bir sayı olamaz.\n")
                    time.sleep(0.5)

                else:
                    print("{}^0.5 = {}\n".format(x, squareroot(x)))
                    time.sleep(0.5)


    elif selection == "7":
        while True:
            print("7.Üs Alma İşlemi (Çıkış için 'q' tuşlayınız.)")

            x = input("Tabanı giriniz:")

            if x == "q":
                print("Menüye dönülüyor...\n")
                time.sleep(1)
                break
            elif not x.isdigit():
                print("Hatalı giriş. Lütfen bir tam sayı veya çıkış için 'q' giriniz.\n")
                continue
            else:
                x = int(x)

            y = input("Kuvvetini giriniz:")

            if y == "q":
                print("Menüye dönülüyor...\n")
                time.sleep(1)
                break
            elif not y.isdigit():
                print("Hatalı giriş. Lütfen bir tam sayı veya çıkış için 'q' giriniz.\n")
                continue
            else:

                y = int(y)

                if x == 0 and y == 0:
                    print("0'ın 0'ıncı üssü belirsiz bir ifadedir.\n")
                    time.sleep(0.5)

                elif x == 0 and y < 0:
                    print("0'ın negatif üsleri tanımsızdır.\n")
                    time.sleep(0.5)

                else:
                    print("{}^{} = {}\n".format(x, y, power(x, y)))
                    time.sleep(0.5)



    elif selection == "8":

        while True:
            print("8.10 Tabanında Logaritma Alma İşlemi (Çıkış için 'q' tuşlayınız.)")

            x = input("Tabanı giriniz:")

            if x == "q":
                print("Menüye dönülüyor...\n")
                time.sleep(1)
                break
            elif not x.isdigit():
                print("Hatalı giriş. Lütfen bir tam sayı veya çıkış için 'q' giriniz.\n")
                continue
            else:
                x = int(x)

                if x <= 0:
                    print("Pozitif bir değer girilmelidir.\n")
                    print("0 ve negatif sayılar için tanımsızdır.\n")
                    time.sleep(0.5)

                else:
                    print("log10({}) = {}\n".format(x, math.log10(x)))
                    time.sleep(0.5)

    elif selection.isdigit():

        print("Hatalı bir seçim yaptınız.")
        print("Lütfen 1-8 arasında seçim yapınız.\n")
        time.sleep(1)
        continue


    else:
        print("Hatalı işlem!")
        print("Çıkış için 'q'. İşlem seçimi için 1-8 numaralarını tuşlayınız.\n")
        time.sleep(1)
        continue