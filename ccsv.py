from csv import DictWriter
import os


csv_writer = DictWriter(open('final.csv','w'),fieldnames=['id','name','sku','cat','uzanti'])
csv_writer.writeheader()


os.chdir("/home/enes/PycharmProjects/csv/images")
a = os.listdir()
sayı = len(a)
id=2333232
for i in a:
    id += 1
    cat1= i.count('_AYKA')
    cat2= i.count('_NORM')
    namee = i.split("_")
    name = namee[-1]
    name = name.replace(".png","")

    sku = i.replace(".png","")

    uzanti = "erenodoor.com/wp-content/upload/images/"+i



    if cat1 > 0 :
        categori= "AYKA"

    elif cat2 > 0 :
        categori = "NORM"

    else:
        categori = "YOF"


# writerow , writerows ikisinden biri kullanılabilir burada
    # Burada bir sözlük oluşturup içindekileri dosyaya yazıyoruz
    csv_writer.writerow({'id':id,'name':name,'sku':sku, 'cat':categori, 'uzanti': uzanti})


"""
id,name,sku,cat,uzanti
erenodoor.com/wp-content/upload/images/dosyaadi
"""



