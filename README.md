# debe to kindle [![Scheduled](https://github.com/angelsdemos/debe-to-kindle/actions/workflows/debe-to-kindle.yml/badge.svg?branch=main&event=schedule)](https://github.com/angelsdemos/debe-to-kindle/actions/workflows/debe-to-kindle.yml) [![Push](https://github.com/angelsdemos/debe-to-kindle/actions/workflows/debe-to-kindle-push.yml/badge.svg)](https://github.com/angelsdemos/debe-to-kindle/actions/workflows/debe-to-kindle-push.yml)

<img src="img\dtk1.jpg" width="900">
Mini Tool to lovers of debe from eksisozluk (one of the most famous website -refered as collaborative dictionary like 
reddit- in Turkey) for pushing debe (Most Liked Entries of Yesterday) to kindle every day via Github Actions.

[Screenshot 1](https://github.com/angelsdemos/debe-to-kindle/blob/main/img/dtk2.jpg), [Screenshot 2](https://github.com/angelsdemos/debe-to-kindle/blob/main/img/dtk3.jpg).

# Nasıl Kullanırım ?
1. Öncelikle mail yapacağınız mail adresinizin SMTP ayarlarlarının açık olması, Gmail ve Yahoo için uygulama şifresi oluşturmanız 
   ve Github'a üye olmanız gerekmektedir. Mail ayarlarınızın nasıl yapılacağına **Detaylı Mail Ayarları** kısmından
   bakabilirsiniz.
2. Uygulamayı fork'layın. (Github üyeliğiniz yoksa tabi önce üye olun ve sağ üstte yer alan Fork'a tıklayın)
3. `Settings > Secrets`'a girip, sağ üstte yer alan `New Depository Secret` ile aşağıda yer alan üç adet Secret'i oluşturun.
    * `KINDLE_MAIL` : kindle mail adresiniz. (isim@kindle.com)
    * `MAIL_NAME` : gönderilecek mail adresiniz (durumsever@gmail.com)
    * `MAIL_PASSWORD` : mail adresinizin şifresi.
   
<img src="img/github4.png" width=1000>

4. Dilerseniz gönderim saatini `.github/workflows/debe-to-kindle.yml` dosyasında yer alan `cron: "1 4 * * *"` kısmından
değiştirebilirsiniz. İkinci sayı saati ilk sayı ise dakikayı belirtiyor. 09:20 için `cron: "20 9 * * *"` gibi. 
(Saatler UTC üzerinden)
5. `debe-to-kindle-push.yml` ve `debe-to-kindle.yml` adında iki adet action var. Push değişiklik yapıldığında ve fork'ladığınızda
, diğeri ise günlük olarak mail gönderir. Actions'a tıklayın ve çıkan uyarıyı onaylayın. Mail ayarlarınızı ve Secret'ları
eklediyseniz uygulamanın çalıştığını görmek ve o gün için DEBE'nizi almak için `Actions > debe-to-kindle-push`'u seçerek
`Run Workflow`'u tıklayın.

![debe to kindle](img/github3.png)

6. Yeni oluşan ve sarı görünen Action'nın tamamlanmasını bekleyin (Bu işlem biraz uzun sürebilir). Kırmızı işaret çıkarsa
ve Action tamamlanamaz ise mail gönderim aşamasında hata olmuş demektir. Genellikle ilk girişlerde mail gönderiminde hata
   olabilir. Mail adresinize gelen Güvenlik Uyarısı'ndan "Bu Benim" seçeneğine tıklayarak yeniden 'Run Workflow'u tıklayarak
işlemi tekrarlayabilirsiniz (_bkz: Detaylı Mail Ayarları_). Hala hata alıyorsanız mail SMTP ayarlarında hata veya eksik
bir işlem gerçekleştirmişsiniz ve muhtemelen giriş yapılamıyordur. **Detaylı Mail Ayarları** kısmına göz atın.
7. O günlük DEBE'nizi aldıysanız Actions sekmesinden `debe-to-kindle`'ı tıklayarak "Enable Workflow"'u tıklayın.
![debe to kindle](img/github2.png)
8. Gönderim yaptığınız mail adresinize amazon üzerinden "Verify your Kindle document" mail'i alabilirsiniz. Dilerseniz bu adımı
mail gönderdiğiniz mail adresinizi amazon'a ekleyerek geçebilirsiniz (ayrıntılı bilgi gelen mailin altında yer alıyor) veya
sadece istediğiniz günler bu onaylamayı yaparak debe'yi kindle'a gönderebilirsiniz.
9. Günlük DEBE'yi kindle üzerinden okunmanın keyfini çıkarın :)
   
# Detaylı Mail Ayarları
## Gmail
Gmail SMTP ayarlarına [buradan](https://support.google.com/mail/answer/7126229) ulaşabilirsiniz.
Uygulama ayarları Gmail için ayarlandığı için YML dosyaları üzerinde bir değişiklik yapmanıza gerek yoktur.
1. Mail adresinizin sağ üstte yer alan ayarlar kısmından "Tüm Ayarları Görüntüleyin"e tıklayın.
2. "Yönlendirme ve POP/IMAP" başlığından "IMAP erişimi" bölümünden "IMAP'ı etkinleştir"i seçin.
![Gmail IMAP](img/gmail1.png)
3. [Bu](https://myaccount.google.com/security) adresten Google > Güvenlik bölümüne girin. "Google'da oturum açma" kısmından
"Uygulama Şifreleri"ne tıklayın. Eğer "Uygulama Şifreleri" görünmüyor ise iki adımlı uygulama kullanmıyorsunuz demektir.
İki adımlı uygulama açık olmadan Google SMTP'ye izin verse de sürekli olarak SMTP üzerinden giriş sorunu yaşayabilirsiniz.
İki adımlı uygulama kapalı olacak ise [bu](https://myaccount.google.com/lesssecureapps) sayfadan "Daha az güvenli uygulama erişimi"
ne izin verin.
<img src="img/gmail2.png" width=900>

4. Uygulama Şifreleri kısmında "Uygulama seçin"e ve ardından Diğer'e tıklayarak oluşturulacak şifre için bir isim verin.
ve oluşturulan şifreyi kopyalayın. Bu şifre sizin SMTP giriş şifreniz olacak.

<img src="img/gmail3.png" width=350> <img src="img/gmail4.png" width=400>

5. Kalan adımları **Nasıl Kullanırım** kısmından tamamlayın. Eğer ilk mail gönderiminde (uygulama kurulumunu yaparken)
hata çıkar ve Güvenlik Uyarısı mail'i gelirse Etlinliği Kontrol Et'e tıklayın ve açılan pencereden "Evet, bendim" seçeneğini
seçin ve mail gönderimini anlatılan şekilde başlatın.

<img src="img/gmail5.png" width=305> <img src="img/gmail6.png" width=450>

## Outlook
Outlook SMTP ayarlarına [buradan](https://support.microsoft.com/tr-tr/office/outlook-com-i%C3%A7in-pop-imap-ve-smtp-ayarlar%C4%B1-d088b986-291d-42b8-9564-9c414e2aa040)
ulaşabilirsiniz.
1. Outlook mail adresinize giriş yapıp sağ üstte yer alan Ayarlar bölümünden "Tüm Outlook ayarlarını görüntüle" seçeneğini
seçin. Açılan pencereden `POP ve IMAP` bölümünden `Cihazların ve uygulamaların POP kullanmasına izin ver` seçeneğini onaylayın.

<img src="img/outlook1.png" height=255> <img src="img/outlook2.png" width=600>
2. Kendi uygulama sayfanızdan `.github/workflows/debe-to-kindle.yml` ve `.github/workflows/debe-to-kindle-push.yml` isimli
dosyalarından SMTP ayarlarını yapmanız gerekmektedir. Verilen dosya adresine gidip sağ üstte yer alan `Edit this file`ı tıklayın
   
![debe to kindle](img/github1.png)
3. Aşağıda yer alan satırları belirtilen şekilde değiştirin. İki dosyada da değişiklik yapmayı unutmayın.
   * `server_address` : smtp-mail.outlook.com
   * `server_port` : 587
   * `secure` :  false
4. Kalan adımları **Nasıl Kullanırım** kısmından tamamlayın. Eğer ilk mail gönderiminde (uygulama kurulumunu yaparken)
hata çıkar ve Güvenlik Uyarısı mail'i gelirse En son etkinliği inceleyin'e tıklayın ve açılan sayfada Bu bendim'i seçin ve
mail gönderimini anlatılan şekilde başlatın.
   
<img src="img/outlook3.png" width=400>

## Yahoo

Yahoo için SMTP ayarlarına [buradan](https://help.yahoo.com/kb/SLN4724.html) ulaşabilirsiniz.

1. Kendi uygulama sayfanızdan `.github/workflows/debe-to-kindle.yml` ve `.github/workflows/debe-to-kindle-push.yml` isimli
dosyalarından SMTP ayarlarını yapmanız gerekmektedir. Verilen dosya adresine gidip sağ üstte yer alan `Edit this file`ı tıklayın
   
![debe to kindle](img/github1.png)
2. Aşağıda yer alan satırları belirtilen şekilde değiştirin. İki dosyada da değişiklik yapmayı unutmayın.
   * `server_address` : smtp.mail.yahoo.com
   * `server_port` : 587
   * `secure` :  true
   
3. [Yahoo > Güvenlik](https://login.yahoo.com/myaccount/security/?.scrumb=ak.SZbEsSMW) bölümününden `Uygulama Parolası` kısmından
`Uygulama parolaları oluştur ve yönet`i tıklayın. Uygulama adını girin ve verilen şifreyi kopyalayın.
Bu şifre sizin SMTP giriş şifreniz olacak.
4. Kalan adımları **Nasıl Kullanırım** kısmından tamamlayın.

<img src="img/yahoo1.png" width=400> <img src="img/yahoo2.png" width=260>

## Diğer Mail Servisleri
Diğer mail adreslerinin SMTP ayarlarına göre Outlook ve Yahoo'da anlatıldığı şekilde 
`.github/workflows/debe-to-kindle.yml` ve `.github/workflows/debe-to-kindle-push.yml` dosyalarını değiştirin. Eğer hata
ile karşılaşırsanız mail servisi SMTP üzerinden giriş yapmanıza izin vermemiştir. Kullandığınız servisin SMTP ve güvenlik
ayarlarını kullanım için kontrol edin.


# Oluşabilecek Hatalar
Eğer giriş hatası ile karşılaşıyorsanız kullandığınız mail servisine SMTP ile giriş yapamamış olabilirsiniz. Giriş yaptığınız
kişinin siz olduğunu onaylama, uygulama şifresi alma gibi adımlara bakabilirsiniz. İptal etmek istediğinizde Actions 
üzerinden `debe-to-kindle`'ı tıklayarak `Disable Workflow` seçeneğini seçebilir veya Settings bölümünden
`Delete this repository` ile uygulamayı silebilirsiniz. 

# Geri Bildirim
Bir hata bulduysanız (o sizin kullanıcı hatanızdır, gayet çalışıyor işte), veya (daha ne eklenebilir emin değilim ama) 
yeni bir özellik eklenmesini dilerseniz mail atmaktan (angelsdemos@gmail.com), pull requests göndermekten, sözlük üzerinden mesaj atmaktan ve dua
etmekten geri durmayın.
