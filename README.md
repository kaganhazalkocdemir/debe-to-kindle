# debe to kindle
Mini Tool to lovers of debe from eksisozluk (one of the most famous website -reffered as collaborative dictionary like 
reddit- in Turkey) for pushing debe (Most Liked Entries from Tomorrow?) to kindle every day via Github Actions.

# Nasıl Kullanırım ?
1. Projeyi fork'layın. (Github üyeliğiniz yoksa tabi önce üye olun ve sağ üstte yer alan Fork'a tıklayın)
2. `Settings > Secrets`'a girip, sağ üstte yer alan `New Depository Secret` ile aşağıda yer alan üç adet Secret'i oluşturun.
    * KINDLE_MAIL : kindle mail adresiniz. (isim@kindle.com)
    * MAIL_NAME : gönderilecek mail adresiniz (durumsever@gmail.com)
    * MAIL_PASSWORD : mail adresinizin şifresi.
3. Dilerseniz gönderim saatini `.github/workflows/debe-to-kindle.yml` dosyasında yer alan `cron: "1 7 * * *"` kısmından
değiştirebilirsiniz. İkinci sayı saati ilk sayı ise dakikayı belirtiyor. 09:20 için `cron: "20 9 * * *"` gibi.
4. Debe'yi günlük kindle üzerinden okumanın keyfini çıkarın :)
