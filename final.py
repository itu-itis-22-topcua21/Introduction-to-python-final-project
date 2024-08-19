import random

def tas_kagit_makas_ahmet_enes_topcu():
    print("OYUN TANITIMI\n"
          "Oyunumuzun temel kuralları çok basit.\n"
          "Taş makası yener, makas kağıdı yener, kağıt da taşı yener.\n"
          "İlk 2 turu kazanan oyuncu galip gelir.\n"
          "Oyuncu tekrar oynamak isterse oyunu baştan başlatabilir.\n"
          "Oyundan çıkmak için 'çıkış' yazmanız yeterlidir.\n")
    
    secenekler = {"taş": 0, "kağıt": 1, "makas": 2}

    # Bu değerleri buraya yazdık çünkü her oyun bittiğinde sıfırlanmasını istemiyoruz. Oyundan tamamen çıkınca sıfırlanıyorlar.
    toplam_oyun_sayisi = 0
    oyuncu_oyun_galibiyeti = 0
    bilgisayar_oyun_galibiyeti = 0

    while True:
        
        # Bu değerler her oyun sonrası sıfırlanıyor.
        oyuncu_galibiyeti = 0
        bilgisayar_galibiyeti = 0
        tur_sayisi = 0
        
        # ikiye ulaşanın kazanması için bir while düngüsü kurduk. 
        while oyuncu_galibiyeti < 2 and bilgisayar_galibiyeti < 2:
             
            tur_sayisi += 1
            
            oyuncu_secim = input("3 seçenekten birini seçin: taş - kağıt - makas (Çıkmak için 'çıkış' yazın): ").lower()
            
            if oyuncu_secim == "çıkış":
                print("\nOyundan çıkılıyor. Teşekkürler!\n")
                return  # Oyundan tamamen çıkmak için fonksiyondan çıkıyoruz.

            if oyuncu_secim not in secenekler:
                print("\nGeçersiz seçim, lütfen geçerli bir seçenek girin.\n")
                continue

            # Oyuncunun taş-kağıt-makas seçim sonucu onun disctionaryden sayı karşılığını almak için yapıldı.
            oyuncu_sayi = secenekler[oyuncu_secim]
            bilgisayar_sayi = random.randint(0, 2)  # Bilgisayar için rastgele seçim

            # Bilgisayarın sayı seçiminin yazı karşılığını dictionary den almak için yapıldı. 
            bilgisayar_secim = [key for key, value in secenekler.items() if value == bilgisayar_sayi][0]

            # Oyuncu ve bilgisayarın seçimlerini ekrana yazdırma
            print(f"\nOyuncunun seçimi: {oyuncu_secim}")
            print(f"Bilgisayarın seçimi: {bilgisayar_secim}\n")

            # Turun galibini belirleme
            if oyuncu_sayi == bilgisayar_sayi:
                print("Berabere!\n")
            elif oyuncu_sayi == 0 and bilgisayar_sayi == 2:
                print("Bu turu kazandınız! Taş makası kırdı.\n")
                oyuncu_galibiyeti += 1
            elif oyuncu_sayi == 1 and bilgisayar_sayi == 0:
                print("Bu turu kazandınız! Kağıt taşı sardı.\n")
                oyuncu_galibiyeti += 1
            elif oyuncu_sayi == 2 and bilgisayar_sayi == 1:
                print("Bu turu kazandınız! Makas kağıdı kesti.\n")
                oyuncu_galibiyeti += 1
            else:
                if bilgisayar_sayi == 0 and oyuncu_sayi == 2:
                    print("Bu turu bilgisayar kazandı! Taş makası kırdı.\n")
                elif bilgisayar_sayi == 1 and oyuncu_sayi == 0:
                    print("Bu turu bilgisayar kazandı! Kağıt taşı sardı.\n")
                elif bilgisayar_sayi == 2 and oyuncu_sayi == 1:
                    print("Bu turu bilgisayar kazandı! Makas kağıdı kesti.\n")
                bilgisayar_galibiyeti += 1

            print(f"Durum: Oyuncu {oyuncu_galibiyeti} - Bilgisayar {bilgisayar_galibiyeti}\n")

        # Oynanan oyunun galibiyetini belirleme
        if oyuncu_galibiyeti == 2:
            print("Tebrikler, oyunu kazandınız!\n")
            oyuncu_oyun_galibiyeti += 1
        else:
            print("Bilgisayar oyunu kazandı!\n")
            bilgisayar_oyun_galibiyeti += 1

        toplam_oyun_sayisi += 1

        print(f"Oynanan toplam oyun sayısı: {toplam_oyun_sayisi}")
        print(f"Oynanan tur sayısı: {tur_sayisi}") # Her oyun ayrı ayrı oynanan tur sayısı (oyun bitince sıfırlanır.)
        print(f"Oyuncu galibiyet sayısı: {oyuncu_oyun_galibiyeti}")
        print(f"Bilgisayar galibiyet sayısı: {bilgisayar_oyun_galibiyeti}\n")
        
        # Oyuncunun devam edip etmiyeceğini sorma
        devam = input("Başka bir oyun oynamak ister misiniz? (Evet/Hayır): ").lower()
        print()  # Satır boşluğu için boş bir print 
        if devam != "evet":
            print("Oyun sona erdi. Teşekkürler!\n")
            break
        
        # Bilgisayarın devam edip etmiyeceğini sorma
        bilgisayar_devam = random.choice(["evet", "hayır"])
        print(f"Bilgisayarın isteği: {bilgisayar_devam}\n")
        if bilgisayar_devam != "evet":
            print("Bilgisayar devam etmek istemediği için oyun sona erdi. Teşekkürler!\n")
            break

# Oyunu başlatmak için fonksiyonu çağırıyoruz
tas_kagit_makas_ahmet_enes_topcu()
