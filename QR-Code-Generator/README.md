

Python kullanılarak geliştirilmiş basit ve kullanıcı dostu bir QR Kod oluşturucu ve okuma uygulamasıdır. Metin veya URL girerek QR kod oluşturabilir, PNG ve PDF formatında kaydedebilir; ayrıca bilgisayar kamerası ile QR kodları okuyabilirsiniz.

---

Gereksinimler
Uygulamayı çalıştırmak için aşağıdaki yazılımların sisteminizde kurulu olması gerekir:
- Python 3.7 veya üzeri
- qrcode kütüphanesi
- tkinter kütüphanesi (Python ile beraber gelir)
- Pillow (PIL)
- fpdf
- opencv-python

Kurulum için:

pip install qrcode pillow fpdf opencv-python

---

Kullanım

1. Depoyu klonlayın veya kodu indirin.

2. Terminal/komut istemcisinde projenin bulunduğu dizine gidin.

3. Aşağıdaki komutla uygulamayı çalıştırın:

python Main.py

4. Açılan arayüzde QR kod oluşturabilir veya kameradan QR kod okuyabilirsiniz.

---

Uygulama Özellikleri

QR Kod Oluşturma
- Enter the text/URL: QR koda dönüştürmek istediğiniz metin veya URL'yi girin.
- Enter the location to save the QR Code: QR kod görüntüsünün kaydedileceği klasör yolunu yazın.
- Enter the name of the QR Code: Kaydedilecek dosyanın adını yazın (uzantı yazmayın).
- Enter the size: QR kod boyutunu 1-40 arasında seçin (1 = 21x21 modül).

QR Kod Kaydetme
- "Generate Code" butonuna tıklayarak PNG ve PDF formatında QR kod oluşturulur ve belirtilen klasöre kaydedilir.
- İşlem tamamlandığında başarılı olduğuna dair bilgilendirme mesajı gösterilir.

Kameradan QR Kod Okuma
- "Kameradan Oku" butonuna tıklayın.
- Bilgisayar kamerası açılır ve QR kod algılanana kadar çalışır.
- QR kod algılandığında içeriği mesaj kutusunda gösterir.
- Kamera penceresini ESC tuşu ile kapatabilirsiniz.

---

Notlar
- QR kod boyutunun doğru girildiğinden emin olun; çok küçük veya çok büyük değerler hata verebilir.
- Kayıt yolu sisteminizde var olan ve yazma izinlerine sahip bir klasör olmalıdır.
- QR kod okuma modunda kameranızın düzgün çalıştığından emin olun.

---

Geliştirmeler / Katkılar
Projeyi ihtiyaçlarınıza göre özgürce değiştirebilir, yeni özellikler ekleyebilirsiniz. Sorun ya da önerileriniz için GitHub üzerinden issue açabilir veya pull request gönderebilirsiniz.

---

İyi Kodlamalar!
"""