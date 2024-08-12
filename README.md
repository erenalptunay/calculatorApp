**Hesap Makinesi Uygulaması**

Bu Python programı, temel matematiksel işlemleri gerçekleştiren bir hesap makinesi uygulamasıdır. Kullanıcıya çeşitli matematiksel işlemler sunar ve kullanıcıdan giriş alarak sonuçları ekrana yazdırır.

**Özellikler**

_Toplama_

_Çıkarma_

_Çarpma_

_Bölme_

_Kare Alma_

_Kök Alma_

_Üs Alma_

_10 Tabanında Logaritma Alma_

**Kullanım**
Uygulamayı Başlatma:
Uygulama, bir terminal veya komut istemcisi aracılığıyla çalıştırılır. Dosya adı calculator.py olarak varsayılmıştır. 
Terminalde aşağıdaki komutu çalıştırarak uygulamayı başlatabilirsiniz:

_python calculator.py_

**Menü Seçenekleri:**
Uygulama, aşağıdaki işlemler için bir menü sunar:

1: Toplama

2: Çıkarma

3: Çarpma

4: Bölme

5: Kare Alma

6: Kök Alma

7: Üs Alma

8: 10 Tabanında Logaritma Alma

q: Çıkış

**İşlem Seçimi:**
Kullanıcı, menüden bir işlem seçmek için belirtilen numarayı girer. İşlem tamamlandığında sonuç ekranda görüntülenir ve kullanıcıya yeni bir işlem yapma veya çıkış yapma seçeneği sunulur.

**Giriş Bilgisi:**
Tam sayılar için giriş yapılır.
Herhangi bir işlem sırasında çıkmak için q tuşuna basabilirsiniz.

**Hata Yönetimi:**
Hatalı girişler kontrol edilir ve kullanıcıya geçerli bir giriş yapması için uyarı verilir.
Bölme işlemi için sıfıra bölme kontrol edilir.
Negatif sayılar için kök alma ve logaritma hesaplamaları sırasında uyarılar verilir.

**Kod Yapısı:**

_addition(a, b): İki sayının toplamını döndürür._

_subtraction(a, b): İki sayı arasındaki farkı döndürür._

_multiplication(a, b): İki sayının çarpımını döndürür._

_division(a, b): İki sayının bölümünü döndürür. Sıfıra bölme kontrolü içerir._

_square(a): Bir sayının karesini döndürür._

_squareroot(a): Bir sayının karekökünü döndürür. Negatif sayılar için uyarı içerir._

_power(a, b): Bir sayının üssünü döndürür. Sıfır üssü ile ilgili uyarılar içerir._

_math.log10(x): 10 tabanında logaritmayı hesaplar. Pozitif değerler için geçerlidir._