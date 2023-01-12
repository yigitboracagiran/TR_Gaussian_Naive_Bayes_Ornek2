import pandas #DataFrame icin...
import numpy #Kucukten buyuge yazdirmak icin...
from sklearn.model_selection import train_test_split #test ve egitim verilerini ayirmak icin...
import statistics #ortalama almak icin...
from tabulate import tabulate #karmasiklik matrisini yazdirmak icin...
import math #pi ve euler sayisi icin...

def hesaplama(x): #Burada siniflardan olma olasiliklari hesaplaniyor.
    global birOrtalama, ikiOrtalama, ucOrtalama, birStandartSapma, ikiStandartSapma, ucStandartSapma, birOlasiligi, ikiOlasiligi, ucOlasiligi
    toplamCarpim1=1
    toplamCarpim2=1
    toplamCarpim3=1
    for i in range(6):
        if birStandartSapma[i]!=0:
            carpim1=(1/(birStandartSapma[i]*((2*math.pi)**0.5)))*(math.e**(((-1)/2)*(((x[i]-birOrtalama[i])/birStandartSapma[i])**2))) #Gaussian Naive Bayes Formul...
            toplamCarpim1*=carpim1
        if ikiStandartSapma[i]!=0:
            carpim2=(1/(ikiStandartSapma[i]*((2*math.pi)**0.5)))*(math.e**(((-1)/2)*(((x[i]-ikiOrtalama[i])/ikiStandartSapma[i])**2)))
            toplamCarpim2*=carpim2
        if ucStandartSapma[i]!=0:
            carpim3=(1/(ucStandartSapma[i]*((2*math.pi)**0.5)))*(math.e**(((-1)/2)*(((x[i]-ucOrtalama[i])/ucStandartSapma[i])**2)))
            toplamCarpim3*=carpim3
    return ((toplamCarpim1*birOlasiligi),(toplamCarpim2*ikiOlasiligi),(toplamCarpim3*ucOlasiligi))
    #Siniflardan olma olasiliklari donduruluyor.

csvVerileri=pandas.read_csv('penguins_size.csv') #Excel dosyasi okunuyor.

csvVerileri=csvVerileri.dropna(axis=0)

csvVerileri['species'].replace(['Adelie', 'Chinstrap', 'Gentoo'], [1, 2, 3], inplace=True)
csvVerileri['island'].replace(['Torgersen', 'Biscoe', 'Dream'], [1, 2, 3], inplace=True)
csvVerileri['sex'].replace(['MALE', 'FEMALE', '.'], [1, 2, 3], inplace=True)

y=csvVerileri["species"] #y olusturuluyor.
x=csvVerileri.drop(columns="species") #y sutunu siliniyor ve x olusturuluyor.

(xEgitimVerisi, xTestVerisi, yEgitimVerisi, yTestVerisi)=train_test_split(x, y, random_state=0, test_size=0.3) #Test ve egitim verileri ayriliyor.

yEgitimVerisiListesi=yEgitimVerisi.tolist() #Test ve egitim verileri liste formuna donusturuluyor.
yTestVerisiListesi=yTestVerisi.tolist()
xEgitimVerisiListesi=xEgitimVerisi.values.tolist()
xTestVerisiListesi=xTestVerisi.values.tolist()

birIndeksler=[] #siniflarin hangi indesklerde olduklarini tutacaklar.
ikiIndeksler=[]
ucIndeksler=[]

for i in range(len(yEgitimVerisiListesi)): #Egitim verilerinin siniflarinin indeksleri bulunuyor.
    if yEgitimVerisiListesi[i]==1:
        birIndeksler.append(i)
    elif yEgitimVerisiListesi[i]==2:
        ikiIndeksler.append(i)
    elif yEgitimVerisiListesi[i]==3:
        ucIndeksler.append(i)

birStandartSapma=[]
ikiStandartSapma=[]
ucStandartSapma=[]

birOrtalama=[]
ikiOrtalama=[]
ucOrtalama=[]

for j in range(6):
    birStandartSapma.append(statistics.stdev([xEgitimVerisiListesi[i][j] for i in birIndeksler])) #Degiskenler hesaplaniyor.
    ikiStandartSapma.append(statistics.stdev([xEgitimVerisiListesi[i][j] for i in ikiIndeksler]))
    ucStandartSapma.append(statistics.stdev([xEgitimVerisiListesi[i][j] for i in ucIndeksler]))

    birOrtalama.append(statistics.mean([xEgitimVerisiListesi[i][j] for i in birIndeksler]))
    ikiOrtalama.append(statistics.mean([xEgitimVerisiListesi[i][j] for i in ikiIndeksler]))
    ucOrtalama.append(statistics.mean([xEgitimVerisiListesi[i][j] for i in ucIndeksler]))

birOlasiligi=(len(birIndeksler)/len(xEgitimVerisi)) #Siniflarin, toplam siniflara orani bulunuyor.
ikiOlasiligi=(len(ikiIndeksler)/len(xEgitimVerisi))
ucOlasiligi=(len(ucIndeksler)/len(xEgitimVerisi))

karmasiklikMatrisi=[[1, 0, 0, 0], [2, 0, 0, 0], [3, 0, 0, 0]] #Karmasiklik Matrisimiz
def KarmasiklikMatrisi(sayi1, sayi2): #Karmasikilik Matrisini Guncelleme
    global karmasiklikMatrisi
    karmasiklikMatrisi[sayi1][sayi2]+=1

dogru=0
yanlis=0
dict={0: 1, 1: 2, 2: 3}
for i in range(len(xTestVerisiListesi)):
    carpimlar=hesaplama(xTestVerisiListesi[i]) #Test verisinin, siniflara gore olasilik verisi donuyor.
    indeksler=numpy.argsort(carpimlar) #Kucukten buyuge siralandiginda hangi indekse hangi indeskteki sayilarin donecegi bulunuyor. (Bize sonuncu indeksteki sayi gerekiyor.)
    tahminEdilenSinif=dict[indeksler[2]] #En yuksek olasiliga sahip sinif bulunuyor.
    if yTestVerisiListesi[i]==tahminEdilenSinif:
        print("Sinif dogru tahmin edildi!")
        KarmasiklikMatrisi(tahminEdilenSinif-1, tahminEdilenSinif)
        dogru+=1
    else:
        print("Sinif yanlis tahmin edildi!")
        KarmasiklikMatrisi(tahminEdilenSinif-1, yTestVerisiListesi[i])
        yanlis+=1
    print("Dogru: ", dogru, "Yanlis: ", yanlis)

print("Karmasiklik Matrisi") 
sutunBasliklari=["Kume", "1", "2", "3"]
print(tabulate(karmasiklikMatrisi, sutunBasliklari)) #Karmasiklik Matrisi Yazdiriliyor.

birTP=karmasiklikMatrisi[0][1] #TP, TN, FN ve FP degerleri her nitelik icin hesaplaniyor.
birTN=karmasiklikMatrisi[1][2]+karmasiklikMatrisi[1][3]+karmasiklikMatrisi[2][2]+karmasiklikMatrisi[2][3]
birFN=karmasiklikMatrisi[0][2]+karmasiklikMatrisi[0][3]
birFP=karmasiklikMatrisi[1][1]+karmasiklikMatrisi[2][1]

ikiTP=karmasiklikMatrisi[1][2]
ikiTN=karmasiklikMatrisi[0][1]+karmasiklikMatrisi[0][3]+karmasiklikMatrisi[2][1]+karmasiklikMatrisi[2][3]
ikiFN=karmasiklikMatrisi[1][1]+karmasiklikMatrisi[1][3]
ikiFP=karmasiklikMatrisi[0][2]+karmasiklikMatrisi[2][2]

ucTP=karmasiklikMatrisi[2][3]
ucTN=karmasiklikMatrisi[0][1]+karmasiklikMatrisi[0][2]+karmasiklikMatrisi[1][1]+karmasiklikMatrisi[1][2]
ucFN=karmasiklikMatrisi[2][1]+karmasiklikMatrisi[2][2]
ucFP=karmasiklikMatrisi[0][3]+karmasiklikMatrisi[1][3]

birDogruluk=(birTP+birTN)/(birTP+birFN+birFP+birTN) #Dogruluk, Kesinlik, Duyarlilik ve F1-Score degerleri 3 nitelik icin de hesaplaniyor ve yazdiriliyor.
birKesinlik=birTP/(birTP+birFP)
birDuyarlilik=birTP/(birTP+birFN)
if (birKesinlik+birDuyarlilik)!=0:
    birFScore=2*((birKesinlik*birDuyarlilik)/(birKesinlik+birDuyarlilik))
else:
    birFScore="tanimsiz"
ikiDogruluk=(ikiTP+ikiTN)/(ikiTP+ikiFN+ikiFP+ikiTN)
ikiKesinlik=ikiTP/(ikiTP+ikiFP)
ikiDuyarlilik=ikiTP/(ikiTP+ikiFN)
if (ikiKesinlik+ikiDuyarlilik)!=0:
    ikiFScore=2*((ikiKesinlik*ikiDuyarlilik)/(ikiKesinlik+ikiDuyarlilik))
else:
    ikiFScore="tanimsiz"
ucDogruluk=(ucTP+ucTN)/(ucTP+ucFN+ucFP+ucTN)
ucKesinlik=ucTP/(ucTP+ucFP)
ucDuyarlilik=ucTP/(ucTP+ucFN)
if (ucKesinlik+ucDuyarlilik)!=0:
    ucFScore=2*((ucKesinlik*ucDuyarlilik)/(ucKesinlik+ucDuyarlilik))
else:
    ucFScore="tanimsiz"

print("Dogruluk: ", birDogruluk, "Kesinlik: ", birKesinlik, "Duyarlilik:", birDuyarlilik, "F1 Score:", birFScore)
print("Dogruluk: ", ikiDogruluk, "Kesinlik: ", ikiKesinlik, "Duyarlilik:", ikiDuyarlilik, "F1 Score:", ikiFScore)
print("Dogruluk: ", ucDogruluk, "Kesinlik: ", ucKesinlik, "Duyarlilik:", ucDuyarlilik, "F1 Score:", ucFScore)