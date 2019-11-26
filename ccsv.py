from csv import DictWriter
import os


# dosyamızı oluşturuyoruz ve dosyamızda olacak tablo adlarını belirliyoruz.
csv_writer = DictWriter(open('final.csv','w'),fieldnames=['id','name','sku','cat','uzanti'])
csv_writer.writeheader()

# chdir ile resimlerimin (veya dosyalarımın) bulunduğu klasörü belirtiyorum. Yani hangi klasörün içine gireceğimi belirtiyorum.
os.chdir("/home/enes/PycharmProjects/csv/images")
# Bu girdiğimiz klasördeki dosyaları çekmemizi sağlıyor. Print ile çağırırsak dosyalarımızın adlarını görebiliriz.
a = os.listdir()
sayı = len(a)
id=2333232
for i in a:
    id += 1
    # benim dosyalarım veri tabanında 3 kategoriye sahip olacağı için böyle basit bir kontrol yaptım. Kategori artarsa kod değişebilir.
    cat1= i.count('_AYKA')
    cat2= i.count('_NORM')
    # dosyalarımın adında KAPILAR_0026_NORM-157.png gibi isimler bulunmakta ve bu isim
    # kategorisi NORM olan NORM-157 adındaki kapı modelini belirtiyor
    # bu yüzden "_" olan bölümlerden ayırarak bir diziye yazıyorum ve bu dizeden sonuncusunu yani NORM-157.png' yi alıyorum.
    # ve sonrasında .png gördüm yere boşluk yazarak uzantısını kaldırıyorum.
    namee = i.split("_")
    name = namee[-1]
    name = name.replace(".png","")

    # burada ise KAPILAR_0026_NORM-157 kısmı lazım olduğu için sadece uzantıyı kaldırıyorum.
    sku = i.replace(".png","")
    #burada da resmin yolu veriliyor.
    uzanti = "erenodoor.com/wp-content/upload/images/"+i

    # yukarıda içinde bulunan kelimeleri kontrol etmiştik ve saydırmıştık.
    # burada ise o değerler eğer arttıysa kategorisi belli oluyor.
    if cat1 > 0 :
        categori= "AYKA"

    elif cat2 > 0 :
        categori = "NORM"

    else:
        categori = "YOF"


# writerow , writerows ikisinden biri kullanılabilir burada
    # Burada bir sözlük oluşturup içindekileri dosyaya yazıyoruz
    csv_writer.writerow({'id':id,'name':name,'sku':sku, 'cat':categori, 'uzanti': uzanti})
