#8 düşmanın bulunduğu tunuvada kazananı belirleyen program

import random


class Dusman:
    def __init__(self, isim, kalan_can, saldiri_gucu, mermi_sayisi = 50):
        self.isim = isim
        self.kalan_can = kalan_can
        self.saldiri_gucu = saldiri_gucu
        self.mermi_sayisi = mermi_sayisi
    
    def saldir(self):
        print(self.isim + " Saldiriyor")
        harcanan_mermi = 5
        #print(str(harcanan_mermi) + " kadar mermi harcandi.")
        self.mermi_sayisi -= harcanan_mermi
        
        return (harcanan_mermi,self.saldiri_gucu)
    
    def saldiriyaugra(self,harcanan_mermi,saldiri_gucu):
        print(self.isim + " Savunuyor.")
        self.kalan_can -= (harcanan_mermi * saldiri_gucu)
        print(self.isim  + " 'nin Kalan Cani = " + str(self.kalan_can))
        return self.kalan_can
        
    def mermi_bitti_mi(self):
        if(self.mermi_sayisi <= 0):
            print(self.isim +": Mermim bitti.Oyundan cıkıyorum.")
            return True
        return False
    
    def can(self):
        can = self.kalan_can
        return can
       
    def hayatta_mi(self):
        if(self.kalan_can <= 0):           
            #print("Oluyorum......")
            return 0
        else:
            #print("Yikilmadim ayaktayim!")
            return 1
    
        
    def print(self):
        #print("Basiliyor.......")
        print("Isim:",self.isim,"Kalan Can:",self.kalan_can,"Saldiri Gucu:",self.saldiri_gucu,"Mermi Sayisi:",self.mermi_sayisi)
        
               
def savastir(a,b):
    i = 0
      
    dusmanlar[a].print()
    dusmanlar[b].print()
    print("Round Basliyor....")
    while(i < 9): 
                  
        donendeger = dusmanlar[a].saldir()   
        dusmanlar[b].saldiriyaugra(donendeger[0],donendeger[1])
        dusmanlar[b].hayatta_mi()
        
        
        donendeger = dusmanlar[b].saldir()   
        dusmanlar[a].saldiriyaugra(donendeger[0],donendeger[1])
        dusmanlar[a].hayatta_mi()
        
        can1 = dusmanlar[a].can()
        can2 = dusmanlar[b].can()
        if(dusmanlar[a].hayatta_mi() == 0 and dusmanlar[b].hayatta_mi() == 0):
            if(can1 > can2):
                print("Dusman " + str(a+1) + " Kazandi....")
                return a 
            else:
                print("Dusman " + str(b+1)  +" Kazandi....")
                return b
                      
        elif(dusmanlar[b].hayatta_mi() == 0):               
            print("Dusman " + str(a+1) + " Kazandi....") 
            return a
            break               
        
        elif(dusmanlar[a].hayatta_mi() == 0):               
            print("Dusman " + str(b+1)  +" Kazandi....")
            return b 
            break                
        i+= 1

            
                           
dusmanlar = []

i = 0

while(i < 8):
    rastgelecan = random.randrange(200,400)
    rastgelesaldirigucu = random.randrange(20,30)
    yenidusman = Dusman("Dusman " + str(i+1),rastgelecan,rastgelesaldirigucu)
    dusmanlar.append(yenidusman)
    

    i+= 1

c = savastir(0,7)
d = savastir(1,6)
e = savastir(2,5)
f = savastir(3,4)
g = savastir(c,d)
h = savastir(e,f)
w = savastir(g,h)

print("Turnuvanin kazanani : Dusman ", str(w+1) + "\nTebrikler.................")