MIL_STD_DOCUMENT = """
RKT-MIL-STD-001
ELEKTRONİK KONTROL BİRİMLERİ ÇEVRESEL DAYANIM STANDARDI

Doküman Sürümü: 1.0
Doküman Sınıfı: Eğitim Amaçlı Teknik Doküman

1. AMAÇ

Bu doküman, elektronik kontrol birimlerinin çevresel koşullar altında
çalışma gereksinimlerini tanımlamak amacıyla hazırlanmıştır.

Standart; çalışma sıcaklığı, depolama sıcaklığı, nem, titreşim,
mekanik şok, rakım ve güç gereksinimlerini kapsamaktadır.

Bu dokümanda verilen değerler yalnızca workshop kapsamında kullanılmak
üzere oluşturulmuş kurgusal teknik gereksinimlerdir.


2. ÇALIŞMA SICAKLIĞI

Elektronik kontrol birimi -40 °C ile +85 °C arasındaki ortam
sıcaklıklarında normal şekilde çalışabilmelidir.

Sistem -40 °C sıcaklıkta en az 2 saat çalıştırılmalıdır.

Sistem +85 °C sıcaklıkta en az 4 saat çalıştırılmalıdır.

Sıcaklık testi sırasında sistemin temel fonksiyonlarında herhangi
bir performans kaybı meydana gelmemelidir.


3. DEPOLAMA SICAKLIĞI

Elektronik kontrol birimi çalışmadığı durumda -55 °C ile +125 °C
arasındaki sıcaklıklarda depolanabilmelidir.

Depolama testi sonrasında sistem oda sıcaklığına getirilmeli ve
minimum 30 dakika bekletildikten sonra fonksiyonel test uygulanmalıdır.

Depolama testi sonrasında fiziksel deformasyon veya elektronik
fonksiyon kaybı kabul edilmez.


4. NEM DAYANIMI

Sistem yüzde 95 bağıl nem seviyesine kadar çalışabilmelidir.

Nem testi +40 °C ortam sıcaklığında gerçekleştirilmelidir.

Test süresi 48 saat olmalıdır.

Test sonunda sistem içerisinde elektriksel kısa devreye veya
fonksiyon kaybına neden olacak seviyede yoğunlaşma oluşmamalıdır.


5. TİTREŞİM TESTİ

Sistem 10 Hz ile 2000 Hz arasındaki titreşimlere karşı dayanıklı olmalıdır.

Titreşim testi X, Y ve Z eksenlerinde ayrı ayrı uygulanmalıdır.

Her eksende test süresi 30 dakika olmalıdır.

Test sırasında elektronik kontrol birimi aktif durumda çalıştırılmalıdır.

Titreşim testi sırasında bağlantı elemanlarında gevşeme, mekanik hasar
veya sistem fonksiyonlarında kesinti meydana gelmemelidir.


6. MEKANİK ŞOK TESTİ

Elektronik kontrol birimi maksimum 40 g mekanik şok seviyesine
dayanabilmelidir.

Şok darbesinin süresi 11 milisaniye olmalıdır.

Test pozitif ve negatif yönlerde X, Y ve Z eksenlerinde uygulanmalıdır.

Her yönde üç adet şok darbesi uygulanmalıdır.

Test sonrasında sistem normal fonksiyonlarını yerine getirebilmelidir.


7. RAKIM GEREKSİNİMLERİ

Elektronik kontrol birimi deniz seviyesinden 5000 metre yüksekliğe
kadar çalışabilmelidir.

Düşük basınç testi sırasında sistem aktif durumda tutulmalıdır.

Test süresi minimum 60 dakika olmalıdır.

Test boyunca haberleşme ve kontrol fonksiyonlarında kesinti
meydana gelmemelidir.


8. GÜÇ GEREKSİNİMLERİ

Elektronik kontrol biriminin nominal çalışma gerilimi 28 V DC'dir.

Sistem 22 V DC ile 32 V DC arasındaki giriş gerilimlerinde
normal şekilde çalışabilmelidir.

Nominal güç tüketimi 60 W değerini geçmemelidir.

Sistem başlangıç anında maksimum 90 W güç tüketebilir.

Ters polarite durumunda sistem kalıcı hasar görmemelidir.


9. TEST SONRASI KABUL KRİTERLERİ

Çevresel testlerin tamamlanmasından sonra elektronik kontrol birimine
fonksiyonel test uygulanmalıdır.

Aşağıdaki durumların tamamı sağlanmalıdır:

- Sistem açılabilmelidir.
- Haberleşme fonksiyonları çalışmalıdır.
- Sensör girişleri doğru şekilde okunmalıdır.
- Kontrol çıkışları çalışmalıdır.
- Kalıcı mekanik deformasyon bulunmamalıdır.
- Elektronik bileşenlerde fiziksel hasar bulunmamalıdır.

Bu gereksinimlerden herhangi birinin sağlanmaması durumunda sistem
çevresel dayanım testinden başarısız kabul edilir.


10. ÖZET

Elektronik kontrol birimi;

-40 °C ile +85 °C arasında çalışabilmeli,
-55 °C ile +125 °C arasında depolanabilmeli,
yüzde 95 bağıl neme dayanabilmeli,
10 Hz ile 2000 Hz titreşim ortamında çalışabilmeli,
40 g mekanik şoka dayanabilmeli,
5000 metre rakıma kadar çalışabilmeli
ve 22 V DC ile 32 V DC giriş gerilimi arasında görev yapabilmelidir.
"""