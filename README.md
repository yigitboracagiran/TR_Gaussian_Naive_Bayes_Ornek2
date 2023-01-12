Not: Excel dosyası ile Python kodunun aynı dizinde olması gerekmektedir.

1- Veri seti okunarak Data Frame’e başarıyla aktarılmıştır.

2- Veriler, %30-%70 oranında olacak şekilde test ve eğitim verisine bölünmüştür.

3- Kategorik veriler, sayısal verilere dönüştürülmüştür.

4- Nan değerlere sahip satırlar silinmiştir.

5- Yapılan araştırmalar sonucunda listede işlemlerin daha hızlı yapılabileceği öğrenilmiştir. Bu nedenle
Data Frame’lerde tutulan test ve eğitim verileri listeye dönüştürülmüştür.

6- Kolaylık olması ve algoritmanın ilerleyişini daha rahat takip edebilmek için öncelikle rastgele 10
veri ile çalışılmıştır.

7- Eğitim verileri sınıflarına göre ayrılmıştır ve her sınıfın hangi indekslerde bulunduğu listelerde
tutulmuştur.

8- Tüm nitelikler sayısal değere sahip olduğu için test verilerinin hangi sınıftan oluğu hesaplanırken
sayısal verilerde hesaplama yapılması gerekmiştir ve aşağıdaki formül kullanılmıştır:

( 1 / ( Sınıfın Standart Sapması * ( 2 * e ^ [ ( -0.5 ) * ( [ Test Verisi – Sınıfın Ortalaması ] / Sınıfın
Standart Sapması ] ^ 2 ) ) ) * ( Sınıf Kaç Adet Bulunduğu / Toplam Sınıf Sayısı )

9- Bu formülü kullanılabilmesi için sınıfların standart sapması ve ortalaması hsaplanmıştır.

10- Her test verisinin her sınıf için olasıkları hesaplanmıştır.

11- Olasılıklar arasında en yükseği seçilmiştir ve tahmin edilen sınıf bulunmuştur.

12- Tahmin edilen sınıf ile, test verisinin gerçek sınıfı karşılaştırılmış, doğru veya yanlış tahmin olarak
kullanıcıya döndürülmüştür.

13- Tahminlerin yapılırken karmaşıklık matrisinin hesaplanması sağlanmıştır.

14- Karmaşıklık matrisinin indekslerindeki verileri kullanarak True Positive, True Negative, False
Positive ve False Negative değerleri hesaplanmıştır.

15- True Positive, True Negative, False Positive ve False Negative değerleri ile Doğruluk (Accuracy),
Kesinlik (Precision), Hassasiyet (Recall) ve F Score hesaplanmış ve ekrana yazdırılmıştır.

16- Algortimanın tamamlanması üzerine tüm veriler üzerinde hazırlanan algoritma
denenmiştir.

17- Yapılan eğitimin sonunda elde edilen doğruluk her nitelik için sırasıyla: %97.02970297029703,
%97.02970297029703 ve %100 olmuştur.
