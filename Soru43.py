market=[
    {"urun":"ekmek","fiyat":10,"stok":20},
    {"urun":"sut","fiyat":30,"stok":15},
    {"urun":"cikolata","fiyat":25,"stok":10}
]
def reyonu_goster():
    for i in market:
        print( {i["urun"],i["fiyat"],i["stok"]}) 

def yeniurun_ekle():
    urun=input("Bir urun giriniz.")
    fiyat=int(input("Bir fiyat giriniz."))
    stok=int(input("Bir stok giriniz."))
    market.append({"urun":urun,"fiyat":fiyat,"stok":stok})
    print(urun,"Reyonlara eklendi")
def urun_sat():
    reyonu_goster()
    secim = int(input("\nSatılacak ürünün numarasını seçin: ")) - 1
    
    if 0 <= secim < len(market):
        secilen = market[secim]
        print("Seçilen ürün:", secilen["urun"])
        adet = int(input("Kaç adet satılacak?: "))
        if adet<=int(secilen["stok"]):
           secilen["stok"]=secilen["stok"]-adet
           print(adet,"satildi")
           toplam=adet*secilen["fiyat"]
           print(toplam,secilen["stok"])
        else :
          print(adet,"satilamadi")
    else :
        print("Ürün seçilemedi.")


while True:
    print("\n=== SÜPERMARKET KASA SİSTEMİ ===")
    print("1 - Reyonu Göster")
    print("2 - Yeni Ürün Ekle")
    print("3 - Kasadan Satış Yap")
    print("4 - Çıkış")
    
    secim = input("İşlem seçin (1-4): ")
    
    if secim == "1":
        reyonu_goster()
    elif secim == "2":
        yeniurun_ekle()
    elif secim == "3":
        urun_sat()
    elif secim =="4":
        print("Kasa kapatılıyor")
        break 
    else : 
        print("Geçersiz işlem")


