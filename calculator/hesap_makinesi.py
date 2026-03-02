from colorama import Fore, Style, init
init(autoreset=True)

def baslik():
    print(Fore.CYAN + "=" * 35)
    print(Fore.CYAN + "         HESAP MAKİNESİ")
    print(Fore.CYAN + "=" * 35)

def hesapla():
    baslik()

    try:
        sayi1 = float(input(Fore.YELLOW + "\n Birinci sayı: "))
        sayi2 = float(input(Fore.YELLOW + " İkinci sayı : "))
        islem = input(Fore.YELLOW + " İşlem (+, -, *, /): ")

        if islem == "+":
            sonuc = sayi1 + sayi2
        elif islem == "-":
            sonuc = sayi1 - sayi2
        elif islem == "*":
            sonuc = sayi1 * sayi2
        elif islem == "/":
            if sayi2 == 0:
                print(Fore.RED + "\n  Sıfıra bölme hatası!")
                return
            sonuc = sayi1 / sayi2
        else:
            print(Fore.RED + "\n  Geçersiz işlem!")
            return

        print(Fore.GREEN + f"\n  Sonuç: {sonuc}")

    except ValueError:
        print(Fore.RED + "\n  Lütfen geçerli bir sayı gir!")

    print(Fore.CYAN + "\n" + "=" * 35)

hesapla()

