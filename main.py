from multiprocessing.sharedctypes import Value
from re import A
import os
import tkinter as tk
from  tkinter import  *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from turtle import color
import random

from matplotlib.pyplot import table
from numpy import insert, integer

conn=sqlite3.connect("E:\\restaurant\\database1.db")
cur=conn.cursor()
win=Tk()
win.geometry("1350x850")
win.title('deer restaurant')

def add_fatora():       
    
    not_repeated_num=cur.execute("select recipt_number from recipts")
    results=cur.fetchall()
    if len(results)==0:
        print('yes')
        cur.execute("insert into recipts(recipt_number) values(?)",(32857,))
        conn.commit()
    else:
        dd=cur.execute("SELECT recipt_number FROM recipts WHERE num=(SELECT MAX(num) FROM recipts)")
        results2=cur.fetchall()
        x=results2[0]
        y=x[0]+7
        cur.execute("insert into recipts(recipt_number) values(?)",(y,))
        conn.commit()

def showAssaer():
    def save_assaer():
        # mango
        mango=mango_text.get()
        if(mango !=""):
                    # 
            mango_num=int(mango_text.get())
            mango_price=20
            total1=mango_num*mango_price
            print(total1)
        # guava
        guava=guava_text.get()
        if(guava !=""):
            # 
            guava_num=int(guava_text.get())
            guava_price=17
            total2=guava_num*guava_price
            print(total2)

             # farawela
        farawela=farawella_text.get()
        if(farawela !=""):
     # 
            farawela_num=int(farawella_text.get())
            farawela_price=18
            total3=farawela_num*farawela_price
            print(total3)

        
             # kewy
        kewy=kewy_text.get()
        if(kewy !=""):
     
            kewy_num=int(kewy_text.get())
            kewy_price=20
            total4=kewy_num*kewy_price
            print(total4)

        khokh=khokh_text.get()
        if(khokh!=""):
            khokh_num=int(khokh_text.get())
            khokh_price=17
            total5=khokh_num*khokh_price
            print(total5)

        ananas=ananas_text.get()
        if(ananas!=""):
            ananas_num=int(ananas_text.get())
            ananas_price=17
            total6=ananas_num*ananas_price
            print(total6)

        romman=romman_text.get()
        if(romman !=""):
            romman_num=int(romman_text.get())
            romman_price=18
            total7=romman_num*romman_price
            print(total7)

        batteekh=batteekh_text.get()
        if(batteekh !=""):
            batteekh_num=int(batteekh_text.get())
            batteekh_price=17
            total8=batteekh_num*batteekh_price
            print(total8)
        
        lemon=lemon_text.get()
        if(lemon !=""):
           lemon_num=int(lemon_text.get())
           lemon_price=15
           total9=lemon_num*lemon_price
           print(total9)

                
        apple=apple_text.get()
        if(apple !=""):
            apple_num=int(apple_text.get())
            apple_price=18
            total10=apple_num*apple_price
            print(total10)

                 
        banana_with_milk=banana_with_milk_text.get()
        if(banana_with_milk !=""):
            banana_with_milk_num=int(banana_with_milk_text.get())
            banana_with_milk_price=18
            total11=banana_with_milk_num*banana_with_milk_price
            print(total11)


                 
        guava_with_milk=guava_with_milk_text.get()
        if(guava_with_milk !=""):
            guava_with_milk_num=int(guava_with_milk_text.get())
            guava_with_milk_price=20
            total12=guava_with_milk_num*guava_with_milk_price
            print(total12)
                 
        farawela_with_milk=farawela_with_milk_text.get()
        if(farawela_with_milk !=""):
            farawela_with_milk_num=int(farawela_with_milk_text.get())
            farawela_with_milk_price=22
            total13=farawela_with_milk_num*farawela_with_milk_price
            print(total13)

        kewy_with_milk=kewy_with_milk_text.get()
        if(kewy_with_milk !=""):
            kewy_with_milk_num=int(kewy_with_milk_text.get())
            kewy_with_milk_price=24
            total14=kewy_with_milk_num*kewy_with_milk_price
            print(total14)
        
                
        orange=orange_text.get()
        if(orange !=""):
            orange_num=int(orange_text.get())
            orange_price=18
            total15=orange_num*orange_price
            print(total15)
                 
        teen=teen_text.get()
        if(teen !=""):
            teen_num=int(teen_text.get())
            teen_price=20
            total16=teen_num*teen_price
            print(total16)


        neanaa_lemon=neanaa_lemon_text.get()
        if(neanaa_lemon !=""):
            neanaa_lemon_num=int(neanaa_lemon_text.get())
            neanaa_lemon_price=17
            total17=neanaa_lemon_num*neanaa_lemon_price
            print(total17)
        
        lebnan_lemon=lebnan_lemon_text.get()
        if(lebnan_lemon !=""):
            lebnan_lemon_num=int(lebnan_lemon_text.get())
            lebnan_lemon_price=18
            total18=lebnan_lemon_num*lebnan_lemon_price
            print(total18)
        
        balah=balah_text.get()
        if(balah !=""):
            balah_num=int(balah_text.get())
            balah_price=18
            total19=balah_num*balah_price
            print(total19)
         
        cantalop=cantalop_text.get()
        if(cantalop !=""):
            cantalop_num=int(cantalop_text.get())
            cantalop_price=17
            total20=cantalop_num*cantalop_price
            print(total20)
 



    assaer_window=Toplevel(win)
    assaer_window.geometry("450x560")
    assaer_window.geometry("+550+50")
    assaer_label=Label(assaer_window,font=('courier 30 bold'), fg='blue',text="عصائر")
    assaer_label.place(x=200,y=10)
    # مانجو
    mango_Label=Label(assaer_window,text="مانجا",font=('courier 15 bold'))
    mango_Label.place(x=360,y=70)
    mango_text=Entry(assaer_window,width=8,font=('courier 15 bold'),justify="center")
    mango_text.place(x=260,y=70)

    # جوافة
    guava_Label=Label(assaer_window,text="جوافة",font=('courier 15 bold'))
    guava_Label.place(x=365,y=115)
    guava_text=Entry(assaer_window,width=8,font=('courier 15 bold'),justify="center")
    guava_text.place(x=260,y=115)
    # فراولة
    farawela_Label=Label(assaer_window,text="فراولة",font=('courier 15 bold'))
    farawela_Label.place(x=360,y=160)
    farawella_text=Entry(assaer_window,width=8,font=('courier 15 bold'),justify="center")
    farawella_text.place(x=260,y=160)

    # كيوي
    kewy_Label=Label(assaer_window,text="  كيوي",font=('courier 15 bold'))
    kewy_Label.place(x=360,y=205)
    kewy_text=Entry(assaer_window,width=8,font=('courier 15 bold'),justify="center")
    kewy_text.place(x=260,y=205)
    
    # خوخ
    khokh_Label=Label(assaer_window,text="  خوخ",font=('courier 15 bold'))
    khokh_Label.place(x=360,y=250)
    khokh_text=Entry(assaer_window,width=8,font=('courier 15 bold'),justify="center")
    khokh_text.place(x=260,y=250)
    # أناناس
    ananas_Label=Label(assaer_window,text="  أناناس",font=('courier 15 bold'))
    ananas_Label.place(x=350,y=295)
    ananas_text=Entry(assaer_window,width=8,font=('courier 15 bold'),justify="center")
    ananas_text.place(x=260,y=295)
    # رمان
    romman_Label=Label(assaer_window,text="  رمان",font=('courier 15 bold'))
    romman_Label.place(x=350,y=340)
    romman_text=Entry(assaer_window,width=8,font=('courier 15 bold'),justify="center")
    romman_text.place(x=260,y=340)
    # بطيخ
    batteekh_Label=Label(assaer_window,text="  بطيخ",font=('courier 15 bold'))
    batteekh_Label.place(x=350,y=385)
    batteekh_text=Entry(assaer_window,width=8,font=('courier 15 bold'),justify="center")
    batteekh_text.place(x=260,y=385)
    # ليمون
    lemon_Label=Label(assaer_window,text="  ليمون",font=('courier 15 bold'))
    lemon_Label.place(x=350,y=430)
    lemon_text=Entry(assaer_window,width=8,font=('courier 15 bold'),justify="center")
    lemon_text.place(x=260,y=430)
     # نعناع
    apple_Label=Label(assaer_window,text="  تفاح",font=('courier 15 bold'))
    apple_Label.place(x=350,y=475)
    apple_text=Entry(assaer_window,width=8,font=('courier 15 bold'),justify="center")
    apple_text.place(x=260,y=475)
        
    
     
 # موز باللبن
    banana_with_milk_Label=Label(assaer_window,text="  موز باللبن",font=('courier 12 bold'))
    banana_with_milk_Label.place(x=105,y=70)
    banana_with_milk_text=Entry(assaer_window,width=8,font=('courier 15 bold'),justify="center")
    banana_with_milk_text.place(x=20,y=70)
    
    # جوافة باللبن
    guava_with_milk_Label=Label(assaer_window,text="  جوافة باللبن",font=('courier 12 bold'))
    guava_with_milk_Label.place(x=95,y=115)
    guava_with_milk_text=Entry(assaer_window,width=8,font=('courier 15 bold'),justify="center")
    guava_with_milk_text.place(x=20,y=115)

    #  فراولة باللبن 
    farawela_with_milk_Label=Label(assaer_window,text="  فراولة باللبن",font=('courier 12 bold'))
    farawela_with_milk_Label.place(x=95,y=160)
    farawela_with_milk_text=Entry(assaer_window,width=8,font=('courier 15 bold'),justify="center")
    farawela_with_milk_text.place(x=20,y=160)
    #  كيوي باللبن 
    kewy_with_milk_Label=Label(assaer_window,text="  كيوي باللبن",font=('courier 12 bold'))
    kewy_with_milk_Label.place(x=95,y=205)
    kewy_with_milk_text=Entry(assaer_window,width=8,font=('courier 15 bold'),justify="center")
    kewy_with_milk_text.place(x=20,y=205)
    #   برتقال فريش 
    orange_Label=Label(assaer_window,text="   برتقال فريش",font=('courier 12 bold'))
    orange_Label.place(x=95,y=250)
    orange_text=Entry(assaer_window,width=8,font=('courier 15 bold'),justify="center")
    orange_text.place(x=20,y=250)
    #   تين شوكي 
    teen_Label=Label(assaer_window,text="   تين شوكي",font=('courier 12 bold'))
    teen_Label.place(x=95,y=295)
    teen_text=Entry(assaer_window,width=8,font=('courier 15 bold'),justify="center")
    teen_text.place(x=20,y=295)
    #   ليمون نعناع 
    neanaa_lemon_Label=Label(assaer_window,text="   ليمون نعناع",font=('courier 12 bold'))
    neanaa_lemon_Label.place(x=95,y=340)
    neanaa_lemon_text=Entry(assaer_window,width=8,font=('courier 15 bold'),justify="center")
    neanaa_lemon_text.place(x=20,y=340)
    #   ليمون لبناني 
    lebnan_lemon_Label=Label(assaer_window,text="   ليمون لبناني",font=('courier 12 bold'))
    lebnan_lemon_Label.place(x=95,y=385)
    lebnan_lemon_text=Entry(assaer_window,width=8,font=('courier 15 bold'),justify="center")
    lebnan_lemon_text.place(x=20,y=385)
    #    بلح ياللبن 
    balah_Label=Label(assaer_window,text="    بلح باللبن",font=('courier 12 bold'))
    balah_Label.place(x=95,y=430)
    balah_text=Entry(assaer_window,width=8,font=('courier 15 bold'),justify="center")
    balah_text.place(x=20,y=430)
    # كانتالوب
    cantalop_Label=Label(assaer_window,text="    كانتالوب ",font=('courier 12 bold'))
    cantalop_Label.place(x=95,y=475)
    cantalop_text=Entry(assaer_window,width=8,font=('courier 15 bold'),justify="center")
    cantalop_text.place(x=20,y=475)
    # button to save

    save_button = Button(assaer_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_assaer)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=200, y=515)
def showcrippes():
    
    def save_crippes():
             # sogok
        sogok=sogok_text.get()
        if(sogok !=""):
                    # 
            sogok_num=int(sogok_text.get())
            sogok_price=38
            total1=sogok_num*sogok_price
            print(total1)

             # crispy
        crispy=crispy_text.get()
        if(crispy !=""):
                    # 
            crispy_num=int(crispy_text.get())
            crispy_price=40
            total1=crispy_num*crispy_price
            print(total1)

                 # gambary
        gambary=gambary_text.get()
        if(gambary !=""):
                    # 
            gambary_num=int(gambary_text.get())
            gambary_price=50
            total1=gambary_num*gambary_price
            print(total1)

                 # shawrma
        shawrma=shawrma_text.get()
        if(shawrma !=""):
                    # 
            shawrma_num=int(shawrma_text.get())
            shawrma_price=32
            total1=shawrma_num*shawrma_price
            print(total1)

                 # batatess
        batatess=batatess_text.get()
        if(batatess !=""):
                    # 
            batatess_num=int(batatess_text.get())
            batatess_price=20
            total1=batatess_num*batatess_price
            print(total1)

                 # kofta
        kofta=kofta_text.get()
        if(kofta !=""):
                    # 
            kofta_num=int(kofta_text.get())
            kofta_price=35
            total1=kofta_num*kofta_price
            print(total1)

                 # sheesh
        sheesh=sheesh_text.get()
        if(sheesh !=""):
                    # 
            sheesh_num=int(sheesh_text.get())
            sheesh_price=35
            total1=sheesh_num*sheesh_price
            print(total1)

                 # basterma
        basterma=basterma_text.get()
        if(basterma !=""):
                    # 
            basterma_num=int(basterma_text.get())
            basterma_price=21
            total1=basterma_num*basterma_price
            print(total1)

                 # cfood
        cfood=cfood_text.get()
        if(cfood !=""):
                    # 
            cfood_num=int(cfood_text.get())
            cfood_price=55
            total1=cfood_num*cfood_price
            print(total1)

                 # hotdog
        hotdog=hotdog_text.get()
        if(hotdog !=""):
                    # 
            hotdog_num=int(hotdog_text.get())
            hotdog_price=32
            total1=hotdog_num*hotdog_price
            print(total1)

                 # hockery
        hockery=hockery_text.get()
        if(hockery !=""):
                    # 
            hockery_num=int(hockery_text.get())
            hockery_price=48
            total1=hockery_num*hockery_price
            print(total1)

                 # ffrakh
        ffrakh=ffrakh_text.get()
        if(ffrakh !=""):
                    # 
            ffrakh_num=int(ffrakh_text.get())
            ffrakh_price=35
            total1=ffrakh_num*ffrakh_price
            print(total1)

                 # fmeat
        fmeat=fmeat_text.get()
        if(fmeat !=""):
                    # 
            fmeat_num=int(fmeat_text.get())
            fmeat_price=38
            total1=fmeat_num*fmeat_price
            print(total1)

                 # checken
        checken=checken_text.get()
        if(checken !=""):
                    # 
            checken_num=int(checken_text.get())
            checken_price=40
            total1=checken_num*checken_price
            print(total1)

                 # cheese
        cheese=cheese_text.get()
        if(cheese !=""):
                    # 
            cheese_num=int(cheese_text.get())
            cheese_price=30
            total1=cheese_num*cheese_price
            print(total1)

                 # burger
        burger=burger_text.get()
        if(burger !=""):
                    # 
            burger_num=int(burger_text.get())
            burger_price=42
            total1=burger_num*burger_price
            print(total1)

                 # kebda
        kebda=kebda_text.get()
        if(kebda !=""):
                    # 
            kebda_num=int(kebda_text.get())
            kebda_price=34
            total1=kebda_num*kebda_price
            print(total1)

                 # pbatates
        pbatates=pbatates_text.get()
        if(pbatates !=""):
                    # 
            pbatates_num=int(pbatates_text.get())
            pbatates_price=21
            total1=pbatates_num*pbatates_price
            print(total1)

                 # mmeat
        mmeat=mmeat_text.get()
        if(mmeat !=""):
                    # 
            mmeat_num=int(mmeat_text.get())
            mmeat_price=35
            total1=mmeat_num*mmeat_price
            print(total1)

                 # mfrakh
        mfrakh=mfrakh_text.get()
        if(mfrakh !=""):
                    # 
            mfrakh_num=int(mfrakh_text.get())
            mfrakh_price=36
            total1=mfrakh_num*mfrakh_price
            print(total1)

  
    crippes_window=Toplevel(win)
    crippes_window.geometry("500x560")
    crippes_window.geometry("+550+50")
    crippes_label=Label(crippes_window,font=('courier 30 bold'), fg='blue',text="كريبات")
    crippes_label.place(x=200,y=10)
    # سجق
    sogok_Label=Label(crippes_window,text="سجق",font=('courier 15 bold'))
    sogok_Label.place(x=420,y=70)
    sogok_text=Entry(crippes_window,width=8,font=('courier 15 bold'),justify="center")
    sogok_text.place(x=295,y=70)

    # كريسبي
    crispy_Label=Label(crippes_window,text="كريسبي",font=('courier 15 bold'))
    crispy_Label.place(x=405,y=115)
    crispy_text=Entry(crippes_window,width=8,font=('courier 15 bold'),justify="center")
    crispy_text.place(x=295,y=115)
    # جمبري
    gambary_Label=Label(crippes_window,text="جمبري",font=('courier 15 bold'))
    gambary_Label.place(x=405,y=160)
    gambary_text=Entry(crippes_window,width=8,font=('courier 15 bold'),justify="center")
    gambary_text.place(x=295,y=160)

    # شاورما
    shawrma_Label=Label(crippes_window,text="  شاورما",font=('courier 15 bold'))
    shawrma_Label.place(x=385,y=205)
    shawrma_text=Entry(crippes_window,width=8,font=('courier 15 bold'),justify="center")
    shawrma_text.place(x=295,y=205)
    
    # بطاطس
    batatess_Label=Label(crippes_window,text="  بطاطس",font=('courier 15 bold'))
    batatess_Label.place(x=390,y=250)
    batatess_text=Entry(crippes_window,width=8,font=('courier 15 bold'),justify="center")
    batatess_text.place(x=295,y=250)
    # كفتة
    kofta_Label=Label(crippes_window,text="  كفتة",font=('courier 15 bold'))
    kofta_Label.place(x=400,y=295)
    kofta_text=Entry(crippes_window,width=8,font=('courier 15 bold'),justify="center")
    kofta_text.place(x=295,y=295)
    # شيش
    sheesh_Label=Label(crippes_window,text="  شيش",font=('courier 15 bold'))
    sheesh_Label.place(x=410,y=340)
    sheesh_text=Entry(crippes_window,width=8,font=('courier 15 bold'),justify="center")
    sheesh_text.place(x=295,y=340)
    # بسطرمة
    basterma_Label=Label(crippes_window,text="  بسطرمة",font=('courier 15 bold'))
    basterma_Label.place(x=390,y=385)
    basterma_text=Entry(crippes_window,width=8,font=('courier 15 bold'),justify="center")
    basterma_text.place(x=295,y=385)
    # سي فود
    cfood_Label=Label(crippes_window,text="  سي فود",font=('courier 15 bold'))
    cfood_Label.place(x=390,y=430)
    cfood_text=Entry(crippes_window,width=8,font=('courier 15 bold'),justify="center")
    cfood_text.place(x=295,y=430)
     # هوت دوج
    hotdog_Label=Label(crippes_window,text="  هوت دوج",font=('courier 15 bold'))
    hotdog_Label.place(x=390,y=475)
    hotdog_text=Entry(crippes_window,width=8,font=('courier 15 bold'),justify="center")
    hotdog_text.place(x=295,y=475)
        
    
     
 #  هوكري بورجر
    hockery_Label=Label(crippes_window,text=" هوكري بورجر",font=('courier 12 bold'))
    hockery_Label.place(x=120,y=70)
    hockery_text=Entry(crippes_window,width=8,font=('courier 15 bold'),justify="center")
    hockery_text.place(x=20,y=70)
    
    #  فاهيتا فراخ
    ffrakh_Label=Label(crippes_window,text="    فاهيتا فراخ",font=('courier 12 bold'))
    ffrakh_Label.place(x=95,y=115)
    ffrakh_text=Entry(crippes_window,width=8,font=('courier 15 bold'),justify="center")
    ffrakh_text.place(x=20,y=115)

    #    فاهيتا لحم 
    fmeat_Label=Label(crippes_window,text="    فاهيتا لحم",font=('courier 12 bold'))
    fmeat_Label.place(x=105,y=160)
    fmeat_text=Entry(crippes_window,width=8,font=('courier 15 bold'),justify="center")
    fmeat_text.place(x=20,y=160)
    #   تشيكن رول 
    checken_Label=Label(crippes_window,text="   تشيكن رول",font=('courier 12 bold'))
    checken_Label.place(x=115,y=205)
    checken_text=Entry(crippes_window,width=8,font=('courier 15 bold'),justify="center")
    checken_text.place(x=20,y=205)
    #    ميكس جبن 
    cheese_Label=Label(crippes_window,text="    ميكس جبن",font=('courier 12 bold'))
    cheese_Label.place(x=115,y=250)
    cheese_text=Entry(crippes_window,width=8,font=('courier 15 bold'),justify="center")
    cheese_text.place(x=20,y=250)
    #    بورجر ديبر 
    burger_Label=Label(crippes_window,text="    بورجر ديبر",font=('courier 12 bold'))
    burger_Label.place(x=115,y=295)
    burger_text=Entry(crippes_window,width=8,font=('courier 15 bold'),justify="center")
    burger_text.place(x=20,y=295)
    #    كبدة اسكندراني 
    kebda_Label=Label(crippes_window,text="    كبدة اسكندراني",font=('courier 12 bold'))
    kebda_Label.place(x=95,y=340)
    kebda_text=Entry(crippes_window,width=8,font=('courier 15 bold'),justify="center")
    kebda_text.place(x=20,y=340)
    #    بطاطس بالبسطرمة 
    pbatates_Label=Label(crippes_window,text="    بطاطس بالبسطرمة",font=('courier 12 bold'))
    pbatates_Label.place(x=95,y=385)
    pbatates_text=Entry(crippes_window,width=8,font=('courier 15 bold'),justify="center")
    pbatates_text.place(x=20,y=385)
    #     ميكس لحوم 
    mmeat_Label=Label(crippes_window,text="    ميكس لحوم ",font=('courier 12 bold'))
    mmeat_Label.place(x=115,y=430)
    mmeat_text=Entry(crippes_window,width=8,font=('courier 15 bold'),justify="center")
    mmeat_text.place(x=20,y=430)
    # ميكس فراخ
    mfrakh_Label=Label(crippes_window,text="    ميكس فراخ ",font=('courier 12 bold'))
    mfrakh_Label.place(x=115,y=475)
    mfrakh_text=Entry(crippes_window,width=8,font=('courier 15 bold'),justify="center")
    mfrakh_text.place(x=20,y=475)
    # button to save

    save_button = Button(crippes_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_crippes)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=200, y=515)
def showmeals():
    
    def save_meals():
              # mango
        mango=mango_text.get()
        if(mango !=""):
                    # 
            mango_num=int(mango_text.get())
            mango_price=20
            total1=mango_num*mango_price
            print(total1)

                  # mango
        mango=mango_text.get()
        if(mango !=""):
                    # 
            mango_num=int(mango_text.get())
            mango_price=20
            total1=mango_num*mango_price
            print(total1)

                  # mango
        mango=mango_text.get()
        if(mango !=""):
                    # 
            mango_num=int(mango_text.get())
            mango_price=20
            total1=mango_num*mango_price
            print(total1)

                  # mango
        mango=mango_text.get()
        if(mango !=""):
                    # 
            mango_num=int(mango_text.get())
            mango_price=20
            total1=mango_num*mango_price
            print(total1)

                  # mango
        mango=mango_text.get()
        if(mango !=""):
                    # 
            mango_num=int(mango_text.get())
            mango_price=20
            total1=mango_num*mango_price
            print(total1)

                  # mango
        mango=mango_text.get()
        if(mango !=""):
                    # 
            mango_num=int(mango_text.get())
            mango_price=20
            total1=mango_num*mango_price
            print(total1)

                  # mango
        mango=mango_text.get()
        if(mango !=""):
                    # 
            mango_num=int(mango_text.get())
            mango_price=20
            total1=mango_num*mango_price
            print(total1)

                  # mango
        mango=mango_text.get()
        if(mango !=""):
                    # 
            mango_num=int(mango_text.get())
            mango_price=20
            total1=mango_num*mango_price
            print(total1)

                  # mango
        mango=mango_text.get()
        if(mango !=""):
                    # 
            mango_num=int(mango_text.get())
            mango_price=20
            total1=mango_num*mango_price
            print(total1)

                  # mango
        mango=mango_text.get()
        if(mango !=""):
                    # 
            mango_num=int(mango_text.get())
            mango_price=20
            total1=mango_num*mango_price
            print(total1)

                  # mango
        mango=mango_text.get()
        if(mango !=""):
                    # 
            mango_num=int(mango_text.get())
            mango_price=20
            total1=mango_num*mango_price
            print(total1)
                  # mango
        mango=mango_text.get()
        if(mango !=""):
                    # 
            mango_num=int(mango_text.get())
            mango_price=20
            total1=mango_num*mango_price
            print(total1)

                  # mango
        mango=mango_text.get()
        if(mango !=""):
                    # 
            mango_num=int(mango_text.get())
            mango_price=20
            total1=mango_num*mango_price
            print(total1)

                  # mango
        mango=mango_text.get()
        if(mango !=""):
                    # 
            mango_num=int(mango_text.get())
            mango_price=20
            total1=mango_num*mango_price
            print(total1)

                  # mango
        mango=mango_text.get()
        if(mango !=""):
                    # 
            mango_num=int(mango_text.get())
            mango_price=20
            total1=mango_num*mango_price
            print(total1)
        

    meals_window=Toplevel(win)
    meals_window.geometry("560x450")
    meals_window.geometry("+250+50")
    meals_label=Label(meals_window,font=('courier 30 bold'), fg='blue',text="وجبات")
    meals_label.place(x=230,y=10)
    # سجق
    korden_Label=Label(meals_window,text="كوردن بلو",font=('courier 15 bold'))
    korden_Label.place(x=420,y=70)
    korden_text=Entry(meals_window,width=8,font=('courier 15 bold'),justify="center")
    korden_text.place(x=310,y=70)

    # كريسبي
    stripes_Label=Label(meals_window,text="استريبس",font=('courier 15 bold'))
    stripes_Label.place(x=420,y=115)
    stripes_text=Entry(meals_window,width=8,font=('courier 15 bold'),justify="center")
    stripes_text.place(x=310,y=115)
    # جمبري
    butterfly_Label=Label(meals_window,text="بترفلاي",font=('courier 15 bold'))
    butterfly_Label.place(x=420,y=160)
    butterfly_text=Entry(meals_window,width=8,font=('courier 15 bold'),justify="center")
    butterfly_text.place(x=310,y=160)

    # شاورما
    barmagana_Label=Label(meals_window,text="  برمجانة",font=('courier 15 bold'))
    barmagana_Label.place(x=420,y=205)
    barmagana_text=Entry(meals_window,width=8,font=('courier 15 bold'),justify="center")
    barmagana_text.place(x=310,y=205)
    
    # بطاطس
    pmeat_Label=Label(meals_window,text="  بيكانا لحمة",font=('courier 15 bold'))
    pmeat_Label.place(x=380,y=250)
    pmeat_text=Entry(meals_window,width=8,font=('courier 15 bold'),justify="center")
    pmeat_text.place(x=310,y=250)
    # كفتة
    pfrakh_Label=Label(meals_window,text="  بيكانا فراخ",font=('courier 15 bold'))
    pfrakh_Label.place(x=380,y=295)
    pfrakh_text=Entry(meals_window,width=8,font=('courier 15 bold'),justify="center")
    pfrakh_text.place(x=310,y=295)
    # شيش
    ffrakh_Label=Label(meals_window,text="   فاهيتا فراخ",font=('courier 15 bold'))
    ffrakh_Label.place(x=380,y=340)
    ffrakh_text=Entry(meals_window,width=8,font=('courier 15 bold'),justify="center")
    ffrakh_text.place(x=310,y=340)
    # بسطرمة
    fmeat_Label=Label(meals_window,text="   فاهيتا لحمة",font=('courier 15 bold'))
    fmeat_Label.place(x=380,y=385)
    fmeat_text=Entry(meals_window,width=8,font=('courier 15 bold'),justify="center")
    fmeat_text.place(x=310,y=385)

 #  هوكري بورجر
    baneeh_Label=Label(meals_window,text="  وجبة بانيه ",font=('courier 12 bold'))
    baneeh_Label.place(x=120,y=70)
    baneeh_text=Entry(meals_window,width=8,font=('courier 15 bold'),justify="center")
    baneeh_text.place(x=20,y=70)
    
    #  فاهيتا فراخ
    torly_Label=Label(meals_window,text=" تورلي باللحمة ",font=('courier 12 bold'))
    torly_Label.place(x=110,y=115)
    torly_text=Entry(meals_window,width=8,font=('courier 15 bold'),justify="center")
    torly_text.place(x=20,y=115)

    #    فاهيتا لحم 
    achecken_Label=Label(meals_window,text=" تشيكن أمريكاني",font=('courier 12 bold'))
    achecken_Label.place(x=105,y=160)
    achecken_text=Entry(meals_window,width=8,font=('courier 15 bold'),justify="center")
    achecken_text.place(x=20,y=160)
    #   تشيكن رول 
    rchecken_Label=Label(meals_window,text="   تشيكن رول",font=('courier 12 bold'))
    rchecken_Label.place(x=115,y=205)
    rchecken_text=Entry(meals_window,width=8,font=('courier 15 bold'),justify="center")
    rchecken_text.place(x=20,y=205)
    #    ميكس جبن 
    tagen_Label=Label(meals_window,text=" طواجن بامية باللحمة ",font=('courier 10 bold'))
    tagen_Label.place(x=115,y=250)
    tagen_text=Entry(meals_window,width=8,font=('courier 15 bold'),justify="center")
    tagen_text.place(x=20,y=250)
    #    بورجر ديبر 
    dawood_Label=Label(meals_window,text=" داود باشا بالبطاطس ",font=('courier 10 bold'))
    dawood_Label.place(x=115,y=295)
    dawood_text=Entry(meals_window,width=8,font=('courier 15 bold'),justify="center")
    dawood_text.place(x=20,y=295)
   
    #    بورجر ديبر 
    mixgril_Label=Label(meals_window,text=" وجبة مكس جريل ",font=('courier 12 bold'))
    mixgril_Label.place(x=115,y=340)
    mixgril_text=Entry(meals_window,width=8,font=('courier 15 bold'),justify="center")
    mixgril_text.place(x=20,y=340)
   
    # button to save

    save_button = Button(meals_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_meals)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=110, y=400)
def showhot_drinks():
    hot_drinks_window=Toplevel(win)
    hot_drinks_window.geometry("500x500")
    hot_drinks_window.geometry("+550+50")
    hot_drinks_label=Label(hot_drinks_window,font=('courier 30 bold'), fg='blue',text="مشروبات ساخنة")
    hot_drinks_label.place(x=100,y=10)
    # سجق
    hot_drinks_Label1=Label(hot_drinks_window,text="شاي",font=('courier 15 bold'))
    hot_drinks_Label1.place(x=390,y=70)
    hot_drinks_text1=Entry(hot_drinks_window,width=8,font=('courier 15 bold'),justify="center")
    hot_drinks_text1.place(x=260,y=70)

    # كريسبي
    hot_drinks_Label2=Label(hot_drinks_window,text="شاي أخضر",font=('courier 15 bold'))
    hot_drinks_Label2.place(x=360,y=115)
    hot_drinks_text2=Entry(hot_drinks_window,width=8,font=('courier 15 bold'),justify="center")
    hot_drinks_text2.place(x=260,y=115)
    # جمبري
    hot_drinks_Label3=Label(hot_drinks_window,text="شاي فواكه",font=('courier 15 bold'))
    hot_drinks_Label3.place(x=360,y=160)
    hot_drinks_text3=Entry(hot_drinks_window,width=8,font=('courier 15 bold'),justify="center")
    hot_drinks_text3.place(x=260,y=160)

    # شاورما
    hot_drinks_Label4=Label(hot_drinks_window,text="  شاي بالحليب",font=('courier 15 bold'))
    hot_drinks_Label4.place(x=340,y=205)
    hot_drinks_text4=Entry(hot_drinks_window,width=8,font=('courier 15 bold'),justify="center")
    hot_drinks_text4.place(x=260,y=205)
    
    # بطاطس
    hot_drinks_Label5=Label(hot_drinks_window,text="  سحلب مكسرات",font=('courier 15 bold'))
    hot_drinks_Label5.place(x=340,y=250)
    hot_drinks_text5=Entry(hot_drinks_window,width=8,font=('courier 15 bold'),justify="center")
    hot_drinks_text5.place(x=260,y=250)
    # كفتة
    hot_drinks_Label6=Label(hot_drinks_window,text="  سحلب نوتيلا",font=('courier 15 bold'))
    hot_drinks_Label6.place(x=340,y=295)
    hot_drinks_text6=Entry(hot_drinks_window,width=8,font=('courier 15 bold'),justify="center")
    hot_drinks_text6.place(x=260,y=295)
    # شيش
    hot_drinks_Label7=Label(hot_drinks_window,text="  سحلب أوريو",font=('courier 15 bold'))
    hot_drinks_Label7.place(x=340,y=340)
    hot_drinks_text7=Entry(hot_drinks_window,width=8,font=('courier 15 bold'),justify="center")
    hot_drinks_text7.place(x=260,y=340)
    # بسطرمة
    hot_drinks_Label8=Label(hot_drinks_window,text="  سحلب فواكه",font=('courier 15 bold'))
    hot_drinks_Label8.place(x=340,y=385)
    hot_drinks_text8=Entry(hot_drinks_window,width=8,font=('courier 15 bold'),justify="center")
    hot_drinks_text8.place(x=260,y=385)
   
   
 #  هوكري بورجر
    hot_drinks_Label11=Label(hot_drinks_window,text="  سحلب لوتس",font=('courier 12 bold'))
    hot_drinks_Label11.place(x=120,y=70)
    hot_drinks_text11=Entry(hot_drinks_window,width=8,font=('courier 15 bold'),justify="center")
    hot_drinks_text11.place(x=20,y=70)
    
    #  فاهيتا فراخ
    hot_drinks_Label12=Label(hot_drinks_window,text=" قهوة تركي",font=('courier 12 bold'))
    hot_drinks_Label12.place(x=120,y=115)
    hot_drinks_text12=Entry(hot_drinks_window,width=8,font=('courier 15 bold'),justify="center")
    hot_drinks_text12.place(x=20,y=115)

    #    فاهيتا لحم 
    hot_drinks_Label13=Label(hot_drinks_window,text=" قهوة تركي دابل  ",font=('courier 12 bold'))
    hot_drinks_Label13.place(x=105,y=160)
    hot_drinks_text13=Entry(hot_drinks_window,width=8,font=('courier 15 bold'),justify="center")
    hot_drinks_text13.place(x=20,y=160)
    #   تشيكن رول 
    hot_drinks_Label14=Label(hot_drinks_window,text="    قهوة كراميل",font=('courier 12 bold'))
    hot_drinks_Label14.place(x=95,y=205)
    hot_drinks_text14=Entry(hot_drinks_window,width=8,font=('courier 15 bold'),justify="center")
    hot_drinks_text14.place(x=20,y=205)
    #    ميكس جبن 
    hot_drinks_Label15=Label(hot_drinks_window,text=" قهوة شوكليت   ",font=('courier 12 bold'))
    hot_drinks_Label15.place(x=115,y=250)
    hot_drinks_text15=Entry(hot_drinks_window,width=8,font=('courier 15 bold'),justify="center")
    hot_drinks_text15.place(x=20,y=250)
    #    بورجر ديبر 
    hot_drinks_Label16=Label(hot_drinks_window,text="  قهوة فرنساوي  ",font=('courier 12 bold'))
    hot_drinks_Label16.place(x=115,y=295)
    hot_drinks_text16=Entry(hot_drinks_window,width=8,font=('courier 15 bold'),justify="center")
    hot_drinks_text16.place(x=20,y=295)

    hot_drinks_Label16=Label(hot_drinks_window,text="  قهوة بندق  ",font=('courier 12 bold'))
    hot_drinks_Label16.place(x=115,y=340)
    hot_drinks_text16=Entry(hot_drinks_window,width=8,font=('courier 15 bold'),justify="center")
    hot_drinks_text16.place(x=20,y=340)
   
   
   
    # button to save

    save_button = Button(hot_drinks_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_hot_drinks)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=120, y=430)
def showcapachino():
    
    def save_capachino():
        pass
    capachino_window=Toplevel(win)
    capachino_window.geometry("540x500")
    capachino_window.geometry("+400+50")
    capachino_label=Label(capachino_window,font=('courier 30 bold'), fg='blue',text=" كابتشينو")
    capachino_label.place(x=200,y=10)
    # سجق
    capachino_Label1=Label(capachino_window,text="لاتيه",font=('courier 15 bold'))
    capachino_Label1.place(x=420,y=70)
    capachino_text1=Entry(capachino_window,width=8,font=('courier 15 bold'),justify="center")
    capachino_text1.place(x=280,y=70)

    # كريسبي
    capachino_Label2=Label(capachino_window,text=" بنانا لاتيه",font=('courier 15 bold'))
    capachino_Label2.place(x=400,y=115)
    capachino_text2=Entry(capachino_window,width=8,font=('courier 15 bold'),justify="center")
    capachino_text2.place(x=280,y=115)
    # جمبري
    capachino_Label3=Label(capachino_window,text=" موكا",font=('courier 15 bold'))
    capachino_Label3.place(x=415,y=160)
    capachino_text3=Entry(capachino_window,width=8,font=('courier 15 bold'),justify="center")
    capachino_text3.place(x=280,y=160)

    # شاورما
    capachino_Label4=Label(capachino_window,text=" موكا بندق",font=('courier 15 bold'))
    capachino_Label4.place(x=400,y=205)
    capachino_text4=Entry(capachino_window,width=8,font=('courier 15 bold'),justify="center")
    capachino_text4.place(x=280,y=205)
    
    # بطاطس
    capachino_Label5=Label(capachino_window,text=" موكا كاراميل ",font=('courier 15 bold'))
    capachino_Label5.place(x=375,y=250)
    capachino_text5=Entry(capachino_window,width=8,font=('courier 15 bold'),justify="center")
    capachino_text5.place(x=280,y=250)
    # كفتة
    capachino_Label6=Label(capachino_window,text="  موكا فانيليا",font=('courier 15 bold'))
    capachino_Label6.place(x=360,y=295)
    capachino_text6=Entry(capachino_window,width=8,font=('courier 15 bold'),justify="center")
    capachino_text6.place(x=280,y=295)
    # شيش
    capachino_Label7=Label(capachino_window,text="موكا شوكولاتة ",font=('courier 15 bold'))
    capachino_Label7.place(x=380,y=340)
    capachino_text7=Entry(capachino_window,width=8,font=('courier 15 bold'),justify="center")
    capachino_text7.place(x=280,y=340)
    # بسطرمة
    capachino_Label8=Label(capachino_window,text="   أمريكان كوفيه",font=('courier 15 bold'))
    capachino_Label8.place(x=340,y=385)
    capachino_text8=Entry(capachino_window,width=8,font=('courier 15 bold'),justify="center")
    capachino_text8.place(x=280,y=385)
   
   
 #  هوكري بورجر
    capachino_Label11=Label(capachino_window,text="   نسكافيه بلاك",font=('courier 12 bold'))
    capachino_Label11.place(x=100,y=70)
    capachino_text11=Entry(capachino_window,width=8,font=('courier 15 bold'),justify="center")
    capachino_text11.place(x=20,y=70)
    
    #  فاهيتا فراخ
    capachino_Label12=Label(capachino_window,text="  نسكافيه باللبن",font=('courier 12 bold'))
    capachino_Label12.place(x=100,y=115)
    capachino_text12=Entry(capachino_window,width=8,font=('courier 15 bold'),justify="center")
    capachino_text12.place(x=20,y=115)

    #    فاهيتا لحم
    capachino_Label13=Label(capachino_window,text=" كابتشينو  ",font=('courier 12 bold'))
    capachino_Label13.place(x=120,y=160)
    capachino_text13=Entry(capachino_window,width=8,font=('courier 15 bold'),justify="center")
    capachino_text13.place(x=20,y=160)
    #   تشيكن رول 
    capachino_Label14=Label(capachino_window,text="    كابتشينو بندق ",font=('courier 12 bold'))
    capachino_Label14.place(x=95,y=205)
    capachino_text14=Entry(capachino_window,width=8,font=('courier 15 bold'),justify="center")
    capachino_text14.place(x=20,y=205)
    #    ميكس جبن 
    capachino_Label15=Label(capachino_window,text="كابتشينو كاراميل ",font=('courier 12 bold'))
    capachino_Label15.place(x=115,y=250)
    capachino_text15=Entry(capachino_window,width=8,font=('courier 15 bold'),justify="center")
    capachino_text15.place(x=20,y=250)
    #    بورجر ديبر 
    capachino_Label16=Label(capachino_window,text="كابتشينو فانيليا",font=('courier 12 bold'))
    capachino_Label16.place(x=115,y=295)
    capachino_text16=Entry(capachino_window,width=8,font=('courier 15 bold'),justify="center")
    capachino_text16.place(x=20,y=295)

    capachino_Label16=Label(capachino_window,text="كابتشينو شوكولاتة ",font=('courier 12 bold'))
    capachino_Label16.place(x=115,y=340)
    capachino_text16=Entry(capachino_window,width=8,font=('courier 15 bold'),justify="center")
    capachino_text16.place(x=20,y=340)
   
   
   
    # button to save

    save_button = Button(capachino_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_capachino)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=120, y=430)
def showmoqablat():
    def save_moqablat():
                # batates
        batates=batates_text.get()
        if(batates !=""):
                    # 
            batates_num=int(batates_text.get())
            batates_price=15
            total1=batates_num*batates_price
            print(total1)

                      # soteeh
        soteeh=soteeh_text.get()
        if(soteeh !=""):
                  # 
          soteeh_num=int(soteeh_text.get())
          soteeh_price=15
          total1=soteeh_num*soteeh_price
          print(total1)

                      # basal
        basal=basal_text.get()
        if(basal !=""):
                  # 
          basal_num=int(basal_text.get())
          basal_price=10
          total1=basal_num*basal_price
          print(total1)

                      # cheese_batates
        cheese_batates=cheese_batates_text.get()
        if(cheese_batates !=""):
                  # 
          cheese_batates_num=int(cheese_batates_text.get())
          cheese_batates_price=20
          total1=cheese_batates_num*cheese_batates_price
          print(total1)

                      # frakh
        frakh=frakh_text.get()
        if(frakh !=""):
                  # 
          frakh_num=int(frakh_text.get())
          frakh_price=35
          total1=frakh_num*frakh_price
          print(total1)

                      # basmate
        basmaty=basmaty_text.get()
        if(basmaty !=""):
                  # 
          basmaty_num=int(basmaty_text.get())
          basmaty_price=10
          total1=basmaty_num*basmaty_price
          print(total1)

                      # shearia
        shearia=shearia_text.get()
        if(shearia !=""):
                  # 
          shearia_num=int(shearia_text.get())
          shearia_price=10
          total1=shearia_num*shearia_price
          print(total1)
        
                      # mahshy
        mahshy=mahshy_text.get()
        if(mahshy !=""):
                  # 
          mahshy_num=int(mahshy_text.get())
          mahshy_price=25
          total1=mahshy_num*mahshy_price
          print(total1)


                      # meat
        meat=meat_text.get()
        if(meat !=""):
                  # 
          meat_num=int(meat_text.get())
          meat_price=20
          total1=meat_num*meat_price
          print(total1)


                      # cheese
        cheese=cheese_text.get()
        if(cheese !=""):
                  # 
          cheese_num=int(cheese_text.get())
          cheese_price=15
          total1=cheese_num*cheese_price
          print(total1)


      
    moqablat_window=Toplevel(win)
    moqablat_window.geometry("540x340")
    moqablat_window.geometry("+100+50")
    moqablat_label=Label(moqablat_window,font=('courier 30 bold'), fg='blue',text=" مقبلات")
    moqablat_label.place(x=200,y=10)
    # سجق
    batates_Label=Label(moqablat_window,text="بطاطس",font=('courier 15 bold'))
    batates_Label.place(x=420,y=70)
    batates_text=Entry(moqablat_window,width=8,font=('courier 15 bold'),justify="center")
    batates_text.place(x=280,y=70)

    # كريسبي
    soteeh_Label=Label(moqablat_window,text="  سوتيه",font=('courier 15 bold'))
    soteeh_Label.place(x=400,y=115)
    soteeh_text=Entry(moqablat_window,width=8,font=('courier 15 bold'),justify="center")
    soteeh_text.place(x=280,y=115)
    # جمبري
    basal_Label=Label(moqablat_window,text=" حلقات بصل",font=('courier 15 bold'))
    basal_Label.place(x=380,y=160)
    basal_text=Entry(moqablat_window,width=8,font=('courier 15 bold'),justify="center")
    basal_text.place(x=280,y=160)

    # شاورما
    cheese_batates_Label=Label(moqablat_window,text="  تشيز بطاطس",font=('courier 15 bold'))
    cheese_batates_Label.place(x=370,y=205)
    cheese_batates_text=Entry(moqablat_window,width=8,font=('courier 15 bold'),justify="center")
    cheese_batates_text.place(x=280,y=205)
    
    # بطاطس
    frakh_Label=Label(moqablat_window,text="   ناجتس فراخ ",font=('courier 15 bold'))
    frakh_Label.place(x=350,y=250)
    frakh_text=Entry(moqablat_window,width=8,font=('courier 15 bold'),justify="center")
    frakh_text.place(x=280,y=250)
    

 #  هوكري بورجر
    basmaty_Label=Label(moqablat_window,text="  أرز بسمتي  ",font=('courier 12 bold'))
    basmaty_Label.place(x=100,y=70)
    basmaty_text=Entry(moqablat_window,width=8,font=('courier 15 bold'),justify="center")
    basmaty_text.place(x=20,y=70)
    
    #  فاهيتا فراخ
    shearia_Label=Label(moqablat_window,text="   أرز شعرية",font=('courier 12 bold'))
    shearia_Label.place(x=100,y=115)
    shearia_text=Entry(moqablat_window,width=8,font=('courier 15 bold'),justify="center")
    shearia_text.place(x=20,y=115)

    #    فاهيتا لحم
    mahshy_Label=Label(moqablat_window,text=" محشي ورق عنب  ",font=('courier 12 bold'))
    mahshy_Label.place(x=120,y=160)
    mahshy_text=Entry(moqablat_window,width=8,font=('courier 15 bold'),justify="center")
    mahshy_text.place(x=20,y=160)
    #   تشيكن رول 
    meat_Label=Label(moqablat_window,text="  سامبوسة لحمة   ",font=('courier 12 bold'))
    meat_Label.place(x=95,y=205)
    meat_text=Entry(moqablat_window,width=8,font=('courier 15 bold'),justify="center")
    meat_text.place(x=20,y=205)
    #    ميكس جبن 
    cheese_Label=Label(moqablat_window,text=" سامبوسة جبنة ",font=('courier 12 bold'))
    cheese_Label.place(x=115,y=250)
    cheese_text=Entry(moqablat_window,width=8,font=('courier 15 bold'),justify="center")
    cheese_text.place(x=20,y=250)
   
   
    # button to save

    save_button = Button(moqablat_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_moqablat)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=220, y=300)
def showicecofee():
    
    def save_ice_coffee():
        pass
    icecofee_window=Toplevel(win)
    icecofee_window.geometry("540x280")
    icecofee_window.geometry("+450+50")
    icecofee_label=Label(icecofee_window,font=('courier 30 bold'), fg='blue',text=" آيس كوفي")
    icecofee_label.place(x=200,y=10)
    # سجق
    icecofee_Label1=Label(icecofee_window,text="آيس موكا",font=('courier 15 bold'))
    icecofee_Label1.place(x=420,y=70)
    icecofee_text1=Entry(icecofee_window,width=8,font=('courier 15 bold'),justify="center")
    icecofee_text1.place(x=280,y=70)

    # كريسبي
    icecofee_Label2=Label(icecofee_window,text="  آيس نوتيلا",font=('courier 15 bold'))
    icecofee_Label2.place(x=390,y=115)
    icecofee_text2=Entry(icecofee_window,width=8,font=('courier 15 bold'),justify="center")
    icecofee_text2.place(x=280,y=115)
    # جمبري
    icecofee_Label3=Label(icecofee_window,text="  كابتشينو",font=('courier 15 bold'))
    icecofee_Label3.place(x=400,y=160)
    icecofee_text3=Entry(icecofee_window,width=8,font=('courier 15 bold'),justify="center")
    icecofee_text3.place(x=280,y=160)

   

 #  هوكري بورجر
    icecofee_Label11=Label(icecofee_window,text=" شوكولاتة  ",font=('courier 12 bold'))
    icecofee_Label11.place(x=130,y=70)
    icecofee_text11=Entry(icecofee_window,width=8,font=('courier 15 bold'),justify="center")
    icecofee_text11.place(x=20,y=70)
    
    #  فاهيتا فراخ
    icecofee_Label12=Label(icecofee_window,text="  اسبريسو ",font=('courier 12 bold'))
    icecofee_Label12.place(x=130,y=115)
    icecofee_text12=Entry(icecofee_window,width=8,font=('courier 15 bold'),justify="center")
    icecofee_text12.place(x=20,y=115)

    #    فاهيتا لحم
    icecofee_Label13=Label(icecofee_window,text="   آيس لاتيه  ",font=('courier 12 bold'))
    icecofee_Label13.place(x=120,y=160)
    icecofee_text13=Entry(icecofee_window,width=8,font=('courier 15 bold'),justify="center")
    icecofee_text13.place(x=20,y=160)
    #   تشيكن رول 
    icecofee_Label14=Label(icecofee_window,text="  آيس فرابتشينو   ",font=('courier 12 bold'))
    icecofee_Label14.place(x=95,y=205)
    icecofee_text14=Entry(icecofee_window,width=8,font=('courier 15 bold'),justify="center")
    icecofee_text14.place(x=20,y=205)
   

   
    # button to save

    save_button = Button(icecofee_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_ice_coffee)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=260, y=230)
def showsoda_cooctail():
    
    def save_soda_cooctail():
        pass
    soda_cooctail_window=Toplevel(win)
    soda_cooctail_window.geometry("570x340")
    soda_cooctail_window.geometry("+250+50")
    soda_cooctail_label=Label(soda_cooctail_window,font=('courier 30 bold'), fg='blue',text=" كوكتيل صودا")
    soda_cooctail_label.place(x=170,y=10)
    # سجق
    soda_cooctail_Label1=Label(soda_cooctail_window,text="شري كولا",font=('courier 15 bold'))
    soda_cooctail_Label1.place(x=460,y=70)
    soda_cooctail_text1=Entry(soda_cooctail_window,width=8,font=('courier 15 bold'),justify="center")
    soda_cooctail_text1.place(x=350,y=70)

    # كريسبي
    soda_cooctail_Label2=Label(soda_cooctail_window,text="  سترومي",font=('courier 15 bold'))
    soda_cooctail_Label2.place(x=450,y=115)
    soda_cooctail_text2=Entry(soda_cooctail_window,width=8,font=('courier 15 bold'),justify="center")
    soda_cooctail_text2.place(x=350,y=115)
    # جمبري
    soda_cooctail_Label3=Label(soda_cooctail_window,text=" موخيتو ",font=('courier 15 bold'))
    soda_cooctail_Label3.place(x=455,y=160)
    soda_cooctail_text3=Entry(soda_cooctail_window,width=8,font=('courier 15 bold'),justify="center")
    soda_cooctail_text3.place(x=350,y=160)

    # شاورما
    soda_cooctail_Label4=Label(soda_cooctail_window,text="  بلورايز ",font=('courier 15 bold'))
    soda_cooctail_Label4.place(x=440,y=205)
    soda_cooctail_text4=Entry(soda_cooctail_window,width=8,font=('courier 15 bold'),justify="center")
    soda_cooctail_text4.place(x=350,y=205)
    
    # بطاطس
    soda_cooctail_Label5=Label(soda_cooctail_window,text=" ابل صودا ",font=('courier 15 bold'))
    soda_cooctail_Label5.place(x=440,y=250)
    soda_cooctail_text5=Entry(soda_cooctail_window,width=8,font=('courier 15 bold'),justify="center")
    soda_cooctail_text5.place(x=350,y=250)
    

 #  هوكري بورجر
    soda_cooctail_Label11=Label(soda_cooctail_window,text=" ريدبول فراولة  ",font=('courier 12 bold'))
    soda_cooctail_Label11.place(x=130,y=70)
    soda_cooctail_text11=Entry(soda_cooctail_window,width=8,font=('courier 15 bold'),justify="center")
    soda_cooctail_text11.place(x=20,y=70)
    
    #  فاهيتا فراخ
    soda_cooctail_Label12=Label(soda_cooctail_window,text="   ريدبول بلو كرواسون ",font=('courier 12 bold'))
    soda_cooctail_Label12.place(x=110,y=115)
    soda_cooctail_text12=Entry(soda_cooctail_window,width=8,font=('courier 15 bold'),justify="center")
    soda_cooctail_text12.place(x=20,y=115)

    #    فاهيتا لحم
    soda_cooctail_Label13=Label(soda_cooctail_window,text="   سبرايت مينت  ",font=('courier 12 bold'))
    soda_cooctail_Label13.place(x=140,y=160)
    soda_cooctail_text13=Entry(soda_cooctail_window,width=8,font=('courier 15 bold'),justify="center")
    soda_cooctail_text13.place(x=20,y=160)
    #   تشيكن رول 
    soda_cooctail_Label14=Label(soda_cooctail_window,text=" صن شاين  ",font=('courier 12 bold'))
    soda_cooctail_Label14.place(x=160,y=205)
    soda_cooctail_text14=Entry(soda_cooctail_window,width=8,font=('courier 15 bold'),justify="center")
    soda_cooctail_text14.place(x=20,y=205)
    #    ميكس جبن 
    soda_cooctail_Label15=Label(soda_cooctail_window,text="   الكتريك بلو ",font=('courier 12 bold'))
    soda_cooctail_Label15.place(x=135,y=250)
    soda_cooctail_text15=Entry(soda_cooctail_window,width=8,font=('courier 15 bold'),justify="center")
    soda_cooctail_text15.place(x=20,y=250)
   
   
    # button to save

    save_button = Button(soda_cooctail_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_soda_cooctail)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=220, y=300)
def show_child_meals():
    def save_child_meals():
          # nagtess
        nagtess=nagtess_text.get()
        if(nagtess !=""):
              # 
            nagtess_num=int(nagtess_text.get())
            nagtess_price=30
            total1=nagtess_num*nagtess_price
            print(total1)


        strips=strips_text.get()
        if(strips !=""):
              # 
            strips_num=int(strips_text.get())
            strips_price=30
            total1=strips_num*strips_price
            print(total1)

    child_meals_window=Toplevel(win)
    child_meals_window.geometry("420x290")
    child_meals_window.geometry("+150+50")
    child_label=Label(child_meals_window,font=('courier 30 bold'), fg='blue',text="  وجبات أطفال")
    child_label.place(x=80,y=10)
    
    nagtess_label=Label(child_meals_window,text="ناجنس الدجاج مع البطاطس ",font=('courier 15 bold'))
    nagtess_label.place(x=130,y=90)
    nagtess_text=Entry(child_meals_window,width=8,font=('courier 15 bold'),justify="center")
    nagtess_text.place(x=20,y=90)

    strips_label=Label(child_meals_window,text="استريبس الدجاج مع البطاطس ",font=('courier 15 bold'))
    strips_label.place(x=120,y=140)
    strips_text=Entry(child_meals_window,width=8,font=('courier 15 bold'),justify="center")
    strips_text.place(x=20,y=140)

     
    save_button = Button(child_meals_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_child_meals)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=120, y=200)
def show_breakfast():

    def save_breakfast():
          # foul
        foul=foul_text.get()
        if(foul !=""):
              # 
            foul_num=int(foul_text.get())
            foul_price=30
            total1=foul_num*foul_price
            print(total1)

                  # cheese
        cheese=cheese_text.get()
        if(cheese !=""):
              # 
            cheese_num=int(cheese_text.get())
            cheese_price=15
            total1=cheese_num*cheese_price
            print(total1)


                  # fataer
        fataer=fataer_text.get()
        if(fataer !=""):
              # 
            fataer_num=int(fataer_text.get())
            fataer_price=18
            total1=fataer_num*fataer_price
            print(total1)


                  # basterma
        basterma=basterma_text.get()
        if(basterma !=""):
              # 
            basterma_num=int(basterma_text.get())
            basterma_price=20
            total1=basterma_num*basterma_price
            print(total1)

                  # frakh
        frakh=frakh_text.get()
        if(frakh !=""):
              # 
            frakh_num=int(frakh_text.get())
            frakh_price=25
            total1=frakh_num*frakh_price
            print(total1)


    breakfast_window=Toplevel(win)
    breakfast_window.geometry("420x400")
    breakfast_window.geometry("+150+50")
    breakfast_label=Label(breakfast_window,font=('courier 30 bold'), fg='blue',text="  وجبات افطار")
    breakfast_label.place(x=80,y=10)

    foul_label=Label(breakfast_window,text="   فول وفلافل وجبنة مشكل ",font=('courier 15 bold'))
    foul_label.place(x=110,y=90)
    foul_text=Entry(breakfast_window,width=8,font=('courier 15 bold'),justify="center")
    foul_text.place(x=20,y=90)

    cheese_label=Label(breakfast_window,text="  توست جبنة مشكل  ",font=('courier 15 bold'))
    cheese_label.place(x=120,y=140)
    cheese_text=Entry(breakfast_window,width=8,font=('courier 15 bold'),justify="center")
    cheese_text.place(x=20,y=140)

          
    fataer_label=Label(breakfast_window,text="    2فطيرة+ عسل +جبنة +شاي  ",font=('courier 15 bold'))
    fataer_label.place(x=100,y=185)
    fataer_text=Entry(breakfast_window,width=8,font=('courier 15 bold'),justify="center")
    fataer_text.place(x=20,y=185)
 
     
    basterma_label=Label(breakfast_window,text="  توست  بسطرمة  ",font=('courier 15 bold'))
    basterma_label.place(x=150,y=230)
    basterma_text=Entry(breakfast_window,width=8,font=('courier 15 bold'),justify="center")
    basterma_text.place(x=20,y=230)

        
    frakh_label=Label(breakfast_window,text="  توست  فراخ  ",font=('courier 15 bold'))
    frakh_label.place(x=150,y=275)
    frakh_text=Entry(breakfast_window,width=8,font=('courier 15 bold'),justify="center")
    frakh_text.place(x=20,y=275)
    
    save_button = Button(breakfast_window, text=" حفظ", width=7, font=(
    'arial 12 bold'), fg="white", bg="blue", command=save_breakfast)
    save_button.config(height=1,
                    width=10)
    save_button.place(x=120, y=340)
def show_rizo():
    
    def save_rizo():
        pass
    rizo_window=Toplevel(win)
    rizo_window.geometry("340x420")
    rizo_window.geometry("+150+50")
    rizo_label=Label(rizo_window,font=('courier 30 bold'), fg='blue',text="  ريزو ")
    rizo_label.place(x=70,y=10)
    rizo_label1=Label(rizo_window,text=" استربس ",font=('courier 15 bold'))
    rizo_label1.place(x=140,y=90)
    rizo_label1=Entry(rizo_window,width=8,font=('courier 15 bold'),justify="center")
    rizo_label2=Label(rizo_window,text=" شاورما  ",font=('courier 15 bold'))
    rizo_label2.place(x=150,y=140)
    rizo_label2=Entry(rizo_window,width=8,font=('courier 15 bold'),justify="center")
    rizo_label2.place(x=20,y=140)
      
    rizo_label3=Label(rizo_window,text=" كبده اسكندراني  ",font=('courier 15 bold'))
    rizo_label3.place(x=120,y=185)
    rizo_label3=Entry(rizo_window,width=8,font=('courier 15 bold'),justify="center")
    rizo_label3.place(x=20,y=185)
 
    rizo_label4=Label(rizo_window,text=" شيش ",font=('courier 15 bold'))
    rizo_label4.place(x=170,y=230)
    rizo_label4=Entry(rizo_window,width=8,font=('courier 15 bold'),justify="center")
    rizo_label4.place(x=20,y=230)
    
    rizo_label5=Label(rizo_window,text="  سجق ",font=('courier 15 bold'))
    rizo_label5.place(x=170,y=275)
    rizo_label5=Entry(rizo_window,width=8,font=('courier 15 bold'),justify="center")
    rizo_label5.place(x=20,y=275)
          
    rizo_label6=Label(rizo_window,text="  كفتة ",font=('courier 15 bold'))
    rizo_label6.place(x=170,y=320)
    rizo_label6=Entry(rizo_window,width=8,font=('courier 15 bold'),justify="center")
    rizo_label6.place(x=20,y=320)
    
    
    save_button = Button(rizo_window, text=" حفظ", width=7, font=(
'arial 12 bold'), fg="white", bg="blue", command=save_rizo)
    save_button.config(height=1,
                width=10)
    save_button.place(x=120, y=370)   
def showcooctails():
    
    def save_cooctails():
        pass
    cooctails_window=Toplevel(win)
    cooctails_window.geometry("500x450")
    cooctails_window.geometry("+550+50")
    cooctails_label=Label(cooctails_window,font=('courier 30 bold'), fg='blue',text=" كوكتيل")
    cooctails_label.place(x=200,y=10)
    # سجق
    cooctails_Label1=Label(cooctails_window,text="فلوريدا",font=('courier 15 bold'))
    cooctails_Label1.place(x=390,y=70)
    cooctails_text1=Entry(cooctails_window,width=8,font=('courier 15 bold'),justify="center")
    cooctails_text1.place(x=260,y=70)

    # كريسبي
    cooctails_Label2=Label(cooctails_window,text="تروبيكال ",font=('courier 15 bold'))
    cooctails_Label2.place(x=390,y=115)
    cooctails_text2=Entry(cooctails_window,width=8,font=('courier 15 bold'),justify="center")
    cooctails_text2.place(x=260,y=115)
    # جمبري
    cooctails_Label3=Label(cooctails_window,text=" ميرفانا",font=('courier 15 bold'))
    cooctails_Label3.place(x=390,y=160)
    cooctails_text3=Entry(cooctails_window,width=8,font=('courier 15 bold'),justify="center")
    cooctails_text3.place(x=260,y=160)

    # شاورما
    cooctails_Label4=Label(cooctails_window,text="  براديس ",font=('courier 15 bold'))
    cooctails_Label4.place(x=390,y=205)
    cooctails_text4=Entry(cooctails_window,width=8,font=('courier 15 bold'),justify="center")
    cooctails_text4.place(x=260,y=205)
    
    # بطاطس
    cooctails_Label5=Label(cooctails_window,text="  ريد جوس ",font=('courier 15 bold'))
    cooctails_Label5.place(x=385,y=250)
    cooctails_text5=Entry(cooctails_window,width=8,font=('courier 15 bold'),justify="center")
    cooctails_text5.place(x=260,y=250)
    # كفتة
    cooctails_Label6=Label(cooctails_window,text="  كريزي  ",font=('courier 15 bold'))
    cooctails_Label6.place(x=390,y=295)
    cooctails_text6=Entry(cooctails_window,width=8,font=('courier 15 bold'),justify="center")
    cooctails_text6.place(x=260,y=295)
    # شيش
    cooctails_Label7=Label(cooctails_window,text="  هاواي ",font=('courier 15 bold'))
    cooctails_Label7.place(x=390,y=340)
    cooctails_text7=Entry(cooctails_window,width=8,font=('courier 15 bold'),justify="center")
    cooctails_text7.place(x=260,y=340)
    # بسطرمة

   
 #  هوكري بورجر
    cooctails_Label11=Label(cooctails_window,text="  باثون فروت ",font=('courier 12 bold'))
    cooctails_Label11.place(x=120,y=70)
    cooctails_text11=Entry(cooctails_window,width=8,font=('courier 15 bold'),justify="center")
    cooctails_text11.place(x=20,y=70)
    
    #  فاهيتا فراخ
    cooctails_Label12=Label(cooctails_window,text=" جرين جوس ",font=('courier 12 bold'))
    cooctails_Label12.place(x=135,y=115)
    cooctails_text12=Entry(cooctails_window,width=8,font=('courier 15 bold'),justify="center")
    cooctails_text12.place(x=20,y=115)

    #    فاهيتا لحم 
    cooctails_Label13=Label(cooctails_window,text=" الاسكا",font=('courier 12 bold'))
    cooctails_Label13.place(x=150,y=160)
    cooctails_text13=Entry(cooctails_window,width=8,font=('courier 15 bold'),justify="center")
    cooctails_text13.place(x=20,y=160)
    #   تشيكن رول 
    cooctails_Label14=Label(cooctails_window,text="تانجو",font=('courier 12 bold'))
    cooctails_Label14.place(x=160,y=205)
    cooctails_text14=Entry(cooctails_window,width=8,font=('courier 15 bold'),justify="center")
    cooctails_text14.place(x=20,y=205)
    #    ميكس جبن 
    cooctails_Label15=Label(cooctails_window,text=" سبيشيال",font=('courier 12 bold'))
    cooctails_Label15.place(x=140,y=250)
    cooctails_text15=Entry(cooctails_window,width=8,font=('courier 15 bold'),justify="center")
    cooctails_text15.place(x=20,y=250)
    #    بورجر ديبر 
    cooctails_Label16=Label(cooctails_window,text="كوكتيل دير",font=('courier 12 bold'))
    cooctails_Label16.place(x=135,y=295)
    cooctails_text16=Entry(cooctails_window,width=8,font=('courier 15 bold'),justify="center")
    cooctails_text16.place(x=20,y=295)

    cooctails_Label8=Label(cooctails_window,text="   فيتامين سي",font=('courier 15 bold'))
    cooctails_Label8.place(x=100,y=340)
    cooctails_text8=Entry(cooctails_window,width=8,font=('courier 15 bold'),justify="center")
    cooctails_text8.place(x=20,y=340)





   
   
    # button to save

    save_button = Button(cooctails_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_cooctails)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=200, y=400)
def show_soupes():
    def save_soupes():
        pass

    soupes_window=Toplevel(win)
    soupes_window.geometry("350x320")
    soupes_window.geometry("+350+50")
    soupes_label=Label(soupes_window,font=('courier 30 bold'), fg='blue',text="  شربة ")
    soupes_label.place(x=80,y=10)
 # سجق
    soupes_label=Label(soupes_window,text="شوربة لسان عصفور ",font=('courier 15 bold'))
    soupes_label.place(x=130,y=90)
    soupes_label=Entry(soupes_window,width=8,font=('courier 15 bold'),justify="center")
    soupes_label.place(x=20,y=90)

    soupes_label=Label(soupes_window,text="شوربة فراخ ",font=('courier 15 bold'))
    soupes_label.place(x=140,y=140)
    soupes_label=Entry(soupes_window,width=8,font=('courier 15 bold'),justify="center")
    soupes_label.place(x=20,y=140)
    soupes_label=Label(soupes_window,text="شوربة سي فوود  ",font=('courier 15 bold'))
    soupes_label.place(x=140,y=185)
    soupes_label=Entry(soupes_window,width=8,font=('courier 15 bold'),justify="center")
    soupes_label.place(x=20,y=185)

     
    save_button = Button(soupes_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_soupes)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=120, y=250)
def show_salades():
    def save_salades():
        pass
    salades_window=Toplevel(win)
    salades_window.geometry("540x340")
    salades_window.geometry("+100+50")
    salades_label=Label(salades_window,font=('courier 30 bold'), fg='blue',text=" سلطات")
    salades_label.place(x=200,y=10)
    # سجق
    salades_Label1=Label(salades_window,text="سلاط",font=('courier 15 bold'))
    salades_Label1.place(x=440,y=70)
    salades_text1=Entry(salades_window,width=8,font=('courier 15 bold'),justify="center")
    salades_text1.place(x=280,y=70)

    # كريسبي
    salades_Label2=Label(salades_window,text="  طحينه",font=('courier 15 bold'))
    salades_Label2.place(x=400,y=115)
    salades_text2=Entry(salades_window,width=8,font=('courier 15 bold'),justify="center")
    salades_text2.place(x=280,y=115)
    # جمبري
    salades_Label3=Label(salades_window,text=" بابا غنوج ",font=('courier 15 bold'))
    salades_Label3.place(x=380,y=160)
    salades_text3=Entry(salades_window,width=8,font=('courier 15 bold'),justify="center")
    salades_text3.place(x=280,y=160)

    # شاورما
    salades_Label4=Label(salades_window,text="كلوسلو",font=('courier 15 bold'))
    salades_Label4.place(x=430,y=205)
    salades_text4=Entry(salades_window,width=8,font=('courier 15 bold'),justify="center")
    salades_text4.place(x=280,y=205)
    
    # بطاطس
    salades_Label5=Label(salades_window,text="ثوميه",font=('courier 15 bold'))
    salades_Label5.place(x=430,y=250)
    salades_text5=Entry(salades_window,width=8,font=('courier 15 bold'),justify="center")
    salades_text5.place(x=280,y=250)
    

 #  هوكري بورجر
    salades_Label11=Label(salades_window,text="بنجر بالفواكه",font=('courier 12 bold'))
    salades_Label11.place(x=130,y=70)
    salades_text11=Entry(salades_window,width=8,font=('courier 15 bold'),justify="center")
    salades_text11.place(x=20,y=70)
    
    #  فاهيتا فراخ
    salades_Label12=Label(salades_window,text="مكسيكي حار",font=('courier 12 bold'))
    salades_Label12.place(x=130,y=115)
    salades_text12=Entry(salades_window,width=8,font=('courier 15 bold'),justify="center")
    salades_text12.place(x=20,y=115)

    #    فاهيتا لحم
    salades_Label13=Label(salades_window,text="سيزار سلاط",font=('courier 12 bold'))
    salades_Label13.place(x=150,y=160)
    salades_text13=Entry(salades_window,width=8,font=('courier 15 bold'),justify="center")
    salades_text13.place(x=20,y=160)
    #   تشيكن رول 
    salades_Label14=Label(salades_window,text="زبادي ",font=('courier 12 bold'))
    salades_Label14.place(x=150,y=205)
    salades_text14=Entry(salades_window,width=8,font=('courier 15 bold'),justify="center")
    salades_text14.place(x=20,y=205)
    #    ميكس جبن 
    salades_Label15=Label(salades_window,text=" سلاطه خضره",font=('courier 12 bold'))
    salades_Label15.place(x=145,y=250)
    salades_text15=Entry(salades_window,width=8,font=('courier 15 bold'),justify="center")
    salades_text15.place(x=20,y=250)
   
   
    # button to save

    save_button = Button(salades_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_salades)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=220, y=300)
def showgazzy_drinks():
    def save_gazzy_drinks():
                 # sogok
        pepsi=pepsi_text.get()
        if(pepsi !=""):
                    # 
            pepsi_num=int(pepsi_text.get())
            pepsi_price=10
            total1=pepsi_num*pepsi_price
            print(total1)

                # seven
        seven=seven_text.get()
        if(seven !=""):
                    # 
            seven_num=int(seven_text.get())
            seven_price=10
            total1=seven_num*seven_price
            print(total1)


                    # marinda
        marinda=marinda_text.get()
        if(marinda !=""):
                    # 
            marinda_num=int(marinda_text.get())
            marinda_price=10
            total1=marinda_num*marinda_price
            print(total1)

                # redball
        redball=redball_text.get()
        if(redball !=""):
                    # 
            redball_num=int(redball_text.get())
            redball_price=35
            total1=redball_num*redball_price
            print(total1)

                # shweps
        shweps=shweps_text.get()
        if(shweps !=""):
                    # 
            shweps_num=int(shweps_text.get())
            shweps_price=13
            total1=shweps_num*shweps_price
            print(total1)

                # pril
        pril=pril_text.get()
        if(pril !=""):
                    # 
            pril_num=int(pril_text.get())
            pril_price=15
            total1=pril_num*pril_price
            print(total1)

                # water
        water=water_text.get()
        if(water !=""):
                    # 
            water_num=int(water_text.get())
            water_price=5
            total1=water_num*water_price
            print(total1)

      
    gazzy_drinks_window=Toplevel(win)
    gazzy_drinks_window.geometry("540x280")
    gazzy_drinks_window.geometry("+550+50")
    gazzy_drinks_label=Label(gazzy_drinks_window,font=('courier 30 bold'), fg='blue',text="  مشروبات غازية")
    gazzy_drinks_label.place(x=90,y=10)
    # سجق
    pepsi_Label=Label(gazzy_drinks_window,text=" بيبسي",font=('courier 15 bold'))
    pepsi_Label.place(x=420,y=70)
    pepsi_text=Entry(gazzy_drinks_window,width=8,font=('courier 15 bold'),justify="center")
    pepsi_text.place(x=280,y=70)

    # كريسبي
    seven_Label=Label(gazzy_drinks_window,text="سفن",font=('courier 15 bold'))
    seven_Label.place(x=450,y=115)
    seven_text=Entry(gazzy_drinks_window,width=8,font=('courier 15 bold'),justify="center")
    seven_text.place(x=280,y=115)
    # جمبري
    marinda_Label=Label(gazzy_drinks_window,text="  مريندا",font=('courier 15 bold'))
    marinda_Label.place(x=400,y=160)
    marinda_text=Entry(gazzy_drinks_window,width=8,font=('courier 15 bold'),justify="center")
    marinda_text.place(x=280,y=160)

   

 #  هوكري بورجر
    redball_Label=Label(gazzy_drinks_window,text=" ريدبول  ",font=('courier 12 bold'))
    redball_Label.place(x=130,y=70)
    redball_text=Entry(gazzy_drinks_window,width=8,font=('courier 15 bold'),justify="center")
    redball_text.place(x=20,y=70)
    
    #  فاهيتا فراخ
    shweps_Label=Label(gazzy_drinks_window,text="  شويبس ",font=('courier 12 bold'))
    shweps_Label.place(x=130,y=115)
    shweps_text=Entry(gazzy_drinks_window,width=8,font=('courier 15 bold'),justify="center")
    shweps_text.place(x=20,y=115)

    #    فاهيتا لحم
    pril_Label=Label(gazzy_drinks_window,text="بريل",font=('courier 12 bold'))
    pril_Label.place(x=150,y=160)
    pril_text=Entry(gazzy_drinks_window,width=8,font=('courier 15 bold'),justify="center")
    pril_text.place(x=20,y=160)
    #   تشيكن رول 
    water_Label=Label(gazzy_drinks_window,text="مياه",font=('courier 12 bold'))
    water_Label.place(x=140,y=205)
    water_text=Entry(gazzy_drinks_window,width=8,font=('courier 15 bold'),justify="center")
    water_text.place(x=20,y=205)
   

   
    # button to save

    save_button = Button(gazzy_drinks_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_gazzy_drinks)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=260, y=230)
def showzabbady():
    def save_zabbady():
         # mango
        sada=sada_text.get()
        if(sada !=""):
             # 
            sada_num=int(sada_text.get())
            sada_price=18
            total1=sada_num*sada_price
            print(total1)
                # notella
        notella=notella_text.get()
        if(notella !=""):
            # 
           notella_num=int(notella_text.get())
           notella_price=22
           total1=notella_num*notella_price
           print(total1)

                # asal
        asal=asal_text.get()
        if(asal !=""):
            # 
           asal_num=int(asal_text.get())
           asal_price=20
           total1=asal_num*asal_price
           print(total1)

                # deel
        deer=deer_text.get()
        if(deer !=""):
            # 
           deer_num=int(deer_text.get())
           deer_price=28
           total1=deer_num*deer_price
           print(total1)

                # fruit
        fruit=fruit_text.get()
        if(fruit !=""):
            # 
           fruit_num=int(fruit_text.get())
           fruit_price=22
           total1=fruit_num*fruit_price
           print(total1)

                # special
        special=special_text.get()
        if(special !=""):
            # 
           special_num=int(special_text.get())
           special_price=25
           total1=special_num*special_price
           print(total1)

    zabbady_window=Toplevel(win)
    zabbady_window.geometry("540x250")
    zabbady_window.geometry("+250+150")
    zabbady_label=Label(zabbady_window,font=('courier 30 bold'), fg='blue',text=" زبادي")
    zabbady_label.place(x=200,y=10)
    # سجق
    sada_Label=Label(zabbady_window,text="زبادي سادة",font=('courier 15 bold'))
    sada_Label.place(x=400,y=70)
    sada_text=Entry(zabbady_window,width=8,font=('courier 15 bold'),justify="center")
    sada_text.place(x=280,y=70)

    # كريسبي
    notella_Label=Label(zabbady_window,text="  زبادي نوتيلا",font=('courier 15 bold'))
    notella_Label.place(x=370,y=115)
    notella_text=Entry(zabbady_window,width=8,font=('courier 15 bold'),justify="center")
    notella_text.place(x=280,y=115)
    # جمبري
    asal_Label=Label(zabbady_window,text="  زبادي بالعسل",font=('courier 15 bold'))
    asal_Label.place(x=370,y=160)
    asal_text=Entry(zabbady_window,width=8,font=('courier 15 bold'),justify="center")
    asal_text.place(x=280,y=160)

    deer_Label=Label(zabbady_window,text="زبادي دير",font=('courier 12 bold'))
    deer_Label.place(x=140,y=70)
    deer_text=Entry(zabbady_window,width=8,font=('courier 15 bold'),justify="center")
    deer_text.place(x=20,y=70)
    
    #  فاهيتا فراخ
    fruit_Label=Label(zabbady_window,text="زبادي فواكه ",font=('courier 12 bold'))
    fruit_Label.place(x=130,y=115)
    fruit_text=Entry(zabbady_window,width=8,font=('courier 15 bold'),justify="center")
    fruit_text.place(x=20,y=115)

    #    فاهيتا لحم
    special_Label=Label(zabbady_window,text=" زبادي اسبشيل ",font=('courier 12 bold'))
    special_Label.place(x=120,y=160)
    special_text=Entry(zabbady_window,width=8,font=('courier 15 bold'),justify="center")
    special_text.place(x=20,y=160)
   
   
    save_button = Button(zabbady_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_zabbady)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=220, y=220)   
def showextra():
    
    def save_extra():
        pass
    extra_window=Toplevel(win)
    extra_window.geometry("540x250")
    extra_window.geometry("+100+50")
    extra_label=Label(extra_window,font=('courier 30 bold'), fg='blue',text=" اكسترا")
    extra_label.place(x=200,y=10)
    # سجق
    extra_Label1=Label(extra_window,text=" صوص",font=('courier 15 bold'))
    extra_Label1.place(x=400,y=70)
    extra_text1=Entry(extra_window,width=8,font=('courier 15 bold'),justify="center")
    extra_text1.place(x=280,y=70)

    # كريسبي
    extra_Label2=Label(extra_window,text="فلفل",font=('courier 15 bold'))
    extra_Label2.place(x=400,y=115)
    extra_text2=Entry(extra_window,width=8,font=('courier 15 bold'),justify="center")
    extra_text2.place(x=280,y=115)
    # جمبري
    extra_Label3=Label(extra_window,text="آيس كريم",font=('courier 15 bold'))
    extra_Label3.place(x=400,y=160)
    extra_text3=Entry(extra_window,width=8,font=('courier 15 bold'),justify="center")
    extra_text3.place(x=280,y=160)

    extra_Label11=Label(extra_window,text=" فواكه",font=('courier 12 bold'))
    extra_Label11.place(x=140,y=70)
    extra_text11=Entry(extra_window,width=8,font=('courier 15 bold'),justify="center")
    extra_text11.place(x=20,y=70)
    
    #  فاهيتا فراخ
    extra_Label12=Label(extra_window,text="لبن",font=('courier 12 bold'))
    extra_Label12.place(x=180,y=115)
    extra_text12=Entry(extra_window,width=8,font=('courier 15 bold'),justify="center")
    extra_text12.place(x=20,y=115)

    #    فاهيتا لحم
    extra_Label13=Label(extra_window,text=" مكسرات  ",font=('courier 12 bold'))
    extra_Label13.place(x=140,y=160)
    extra_text13=Entry(extra_window,width=8,font=('courier 15 bold'),justify="center")
    extra_text13.place(x=20,y=160)
   
   
    save_button = Button(extra_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_extra)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=220, y=220)   
def showsandwishes():
    def save_sandwishes():
              # zenger
      zenger=zenger_text.get()
      if(zenger !=""):
                  # 
          zenger_num=int(zenger_text.get())
          zenger_price=34
          total1=zenger_num*zenger_price
          print(total1)

              # kofta
      kofta=kofta_text.get()
      if(kofta !=""):
                  # 
          kofta_num=int(kofta_text.get())
          kofta_price=35
          total1=kofta_num*kofta_price
          print(total1)

              # steek
      steek=steek_text.get()
      if(steek !=""):
                  # 
          steek_num=int(steek_text.get())
          steek_price=45
          total1=steek_num*steek_price
          print(total1)

              # crispy
      crispy=crispy_text.get()
      if(crispy !=""):
                  # 
          crispy_num=int(crispy_text.get())
          crispy_price=35
          total1=crispy_num*crispy_price
          print(total1)

              # milano
      milano=milano_text.get()
      if(milano !=""):
                  # 
          milano_num=int(milano_text.get())
          milano_price=35
          total1=milano_num*milano_price
          print(total1)


              # hockery
      hockery=hockery_text.get()
      if(hockery !=""):
                  # 
          hockery_num=int(hockery_text.get())
          hockery_price=45
          total1=hockery_num*hockery_price
          print(total1)

              # cranshy
      cranshy=cranchy_text.get()
      if(cranshy !=""):
                  # 
          cranshy_num=int(cranchy_text.get())
          cranshy_price=35
          total1=cranshy_num*cranshy_price
          print(total1)
              # meat
      meat=meat_text.get()
      if(meat !=""):
                  # 
          meat_num=int(meat_text.get())
          meat_price=40
          total1=meat_num*meat_price
          print(total1)


                # frakh
      frakh=frakh_text.get()
      if(frakh !=""):
                  # 
          frakh_num=int(frakh_text.get())
          frakh_price=36
          total1=frakh_num*frakh_price
          print(total1)

              # gambary
      gambary=gambary_text.get()
      if(gambary !=""):
                  # 
          gambary_num=int(gambary_text.get())
          gambary_price=45
          total1=gambary_num*gambary_price
          print(total1)

                # baneeh
      baneeh=baneeh_text.get()
      if(baneeh !=""):
                  # 
          baneeh_num=int(baneeh_text.get())
          baneeh_price=44
          total1=baneeh_num*baneeh_price
          print(total1)

                # sheesh
      sheesh=sheesh_text.get()
      if(sheesh !=""):
                  # 
          sheesh_num=int(sheesh_text.get())
          sheesh_price=33
          total1=sheesh_num*sheesh_price
          print(total1)
                # kebda
      kebda=kebda_text.get()
      if(kebda !=""):
                  # 
          kebda_num=int(kebda_text.get())
          kebda_price=30
          total1=kebda_num*kebda_price
          print(total1)

                # serian_batates
      serian_batates=serian_batates_text.get()
      if(serian_batates !=""):
                  # 
          serian_batates_num=int(serian_batates_text.get())
          serian_batates_price=10
          total1=serian_batates_num*serian_batates_price
          print(total1)

                # cheese_batates
      cheese_batates=cheese_batates_text.get()
      if(cheese_batates !=""):
                  # 
          cheese_batates_num=int(cheese_batates_text.get())
          cheese_batates_price=15
          total1=cheese_batates_num*cheese_batates_price
          print(total1)

                # cheese_burger
      cheese_burger=cheese_burger_text.get()
      if(cheese_burger !=""):
                  # 
          cheese_burger_num=int(cheese_burger_text.get())
          cheese_burger_price=40
          total1=cheese_burger_num*cheese_burger_price
          print(total1)

                # classic_burger
      classic_burger=classic_burger_text.get()
      if(classic_burger !=""):
                  # 
          classic_burger_num=int(classic_burger_text.get())
          classic_burger_price=35
          total1=classic_burger_num*classic_burger_price
          print(total1)

                # sogok
      sogok=sogok_text.get()
      if(sogok !=""):
                  # 
          sogok_num=int(sogok_text.get())
          sogok_price=35
          total1=sogok_num*sogok_price
          print(total1)

                # crispy_gambary
      crispy_gambary=crispy_gambary_text.get()
      if(crispy_gambary !=""):
                  # 
          crispy_gambary_num=int(crispy_gambary_text.get())
          crispy_gambary_price=45
          total1=crispy_gambary_num*crispy_gambary_price
          print(total1)



    
    sandwishes_window=Toplevel(win)
    sandwishes_window.geometry("650x560")
    sandwishes_window.geometry("+150+50")
    sandwishes_labe=Label(sandwishes_window,font=('courier 30 bold'), fg='blue',text="سندوتشات")
    sandwishes_labe.place(x=200,y=10)
    # مانجو
    zenger_Label=Label(sandwishes_window,text="زنجر",font=('courier 15 bold'))
    zenger_Label.place(x=480,y=70)
    zenger_text=Entry(sandwishes_window,width=8,font=('courier 15 bold'),justify="center")
    zenger_text.place(x=360,y=70)

    # جوافة
    kofta_Label=Label(sandwishes_window,text="كفته",font=('courier 15 bold'))
    kofta_Label.place(x=485,y=115)
    kofta_text=Entry(sandwishes_window,width=8,font=('courier 15 bold'),justify="center")
    kofta_text.place(x=360,y=115)
    # فراولة
    steek_Label=Label(sandwishes_window,text="استيك",font=('courier 15 bold'))
    steek_Label.place(x=480,y=160)
    steek_text=Entry(sandwishes_window,width=8,font=('courier 15 bold'),justify="center")
    steek_text.place(x=360,y=160)

    # كيوي
    crispy_Label=Label(sandwishes_window,text="  كريسبي ",font=('courier 15 bold'))
    crispy_Label.place(x=460,y=205)
    crispy_text=Entry(sandwishes_window,width=8,font=('courier 15 bold'),justify="center")
    crispy_text.place(x=360,y=205)
    
    # خوخ
    milano_Label=Label(sandwishes_window,text="  ميلانو",font=('courier 15 bold'))
    milano_Label.place(x=460,y=250)
    milano_text=Entry(sandwishes_window,width=8,font=('courier 15 bold'),justify="center")
    milano_text.place(x=360,y=250)
    # أناناس
    hockery_Label=Label(sandwishes_window,text="  هوكرى بورجر",font=('courier 15 bold'))
    hockery_Label.place(x=450,y=295)
    hockery_text=Entry(sandwishes_window,width=8,font=('courier 15 bold'),justify="center")
    hockery_text.place(x=360,y=295)
    # رمان
    cranchy_Label=Label(sandwishes_window,text="  كرانشي",font=('courier 15 bold'))
    cranchy_Label.place(x=480,y=340)
    cranchy_text=Entry(sandwishes_window,width=8,font=('courier 15 bold'),justify="center")
    cranchy_text.place(x=360,y=340)
    # بطيخ
    meat_Label=Label(sandwishes_window,text="  فاهيتا لحم ",font=('courier 15 bold'))
    meat_Label.place(x=450,y=385)
    meat_text=Entry(sandwishes_window,width=8,font=('courier 15 bold'),justify="center")
    meat_text.place(x=360,y=385)
    # ليمون
    frakh_Label=Label(sandwishes_window,text="  فاهيتا فراخ",font=('courier 15 bold'))
    frakh_Label.place(x=450,y=430)
    frakh_text=Entry(sandwishes_window,width=8,font=('courier 15 bold'),justify="center")
    frakh_text.place(x=360,y=430)
     # نعناع
    gambary_Label=Label(sandwishes_window,text="  فاهيتا جمبرى",font=('courier 15 bold'))
    gambary_Label.place(x=450,y=475)
    gambary_text=Entry(sandwishes_window,width=8,font=('courier 15 bold'),justify="center")
    gambary_text.place(x=360,y=475)
        
    
     
 # موز باللبن
    baneeh_Label=Label(sandwishes_window,text="  ماجنوم بانيه ",font=('courier 12 bold'))
    baneeh_Label.place(x=135,y=70)
    baneeh_text=Entry(sandwishes_window,width=8,font=('courier 15 bold'),justify="center")
    baneeh_text.place(x=20,y=70)
    
    # جوافة باللبن
    sheesh_Label=Label(sandwishes_window,text="شيش طاووق",font=('courier 12 bold'))
    sheesh_Label.place(x=155,y=115)
    sheesh_text=Entry(sandwishes_window,width=8,font=('courier 15 bold'),justify="center")
    sheesh_text.place(x=20,y=115)

    #  فراولة باللبن 
    kebda_Label=Label(sandwishes_window,text="كبده اسكندراني",font=('courier 12 bold'))
    kebda_Label.place(x=135,y=160)
    kebda_text=Entry(sandwishes_window,width=8,font=('courier 15 bold'),justify="center")
    kebda_text.place(x=20,y=160)
    #  كيوي باللبن 
    serian_batates_Label=Label(sandwishes_window,text="بطاطس سورى",font=('courier 12 bold'))
    serian_batates_Label.place(x=155,y=205)
    serian_batates_text=Entry(sandwishes_window,width=8,font=('courier 15 bold'),justify="center")
    serian_batates_text.place(x=20,y=205)
    #   برتقال فريش 
    cheese_batates_Label=Label(sandwishes_window,text="بطاطس بالجبنه",font=('courier 12 bold'))
    cheese_batates_Label.place(x=135,y=250)
    cheese_batates_text=Entry(sandwishes_window,width=8,font=('courier 15 bold'),justify="center")
    cheese_batates_text.place(x=20,y=250)
    #   تين شوكي 
    cheese_burger_Label=Label(sandwishes_window,text="برجر جبنه و مشروم",font=('courier 12 bold'))
    cheese_burger_Label.place(x=135,y=295)
    cheese_burger_text=Entry(sandwishes_window,width=8,font=('courier 15 bold'),justify="center")
    cheese_burger_text.place(x=20,y=295)
   
   
    classic_burger_Label=Label(sandwishes_window,text="   كلاسيك برجر ",font=('courier 12 bold'))
    classic_burger_Label.place(x=135,y=340)
    classic_burger_text=Entry(sandwishes_window,width=8,font=('courier 15 bold'),justify="center")
    classic_burger_text.place(x=20,y=340)
    #    بلح ياللبن 
    sogok_Label=Label(sandwishes_window,text="سجق اسكندراني",font=('courier 12 bold'))
    sogok_Label.place(x=135,y=385)
    sogok_text=Entry(sandwishes_window,width=8,font=('courier 15 bold'),justify="center")
    sogok_text.place(x=20,y=385)
    # كانتالوب
    crispy_gambary_Label=Label(sandwishes_window,text="جمبرى كريسبي",font=('courier 12 bold'))
    crispy_gambary_Label.place(x=135,y=430)
    crispy_gambary_text=Entry(sandwishes_window,width=8,font=('courier 15 bold'),justify="center")
    crispy_gambary_text.place(x=20,y=430)
    # button to save

    save_button = Button(sandwishes_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_sandwishes)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=200, y=480)
def showherbs():
    
    def save_herbs():
               # yanson
       yanson=yanson_text.get()
       if(yanson !=""):
                   # 
           yanson_num=int(yanson_text.get())
           yanson_price=8
           total1=yanson_num*yanson_price
           print(total1)

                  # karkadeeh
       karkadeeh=karkadeeh_text.get()
       if(karkadeeh !=""):
                   # 
           karkadeeh_num=int(karkadeeh_text.get())
           karkadeeh_price=8
           total1=karkadeeh_num*karkadeeh_price
           print(total1)

                  # neanaa
       neanaa=neanaa_text.get()
       if(neanaa !=""):
                   # 
           neanaa_num=int(neanaa_text.get())
           neanaa_price=8
           total1=neanaa_num*neanaa_price
           print(total1)

                  # kerfa
       kerfa=kerfa_text.get()
       if(kerfa !=""):
                   # 
           kerfa_num=int(kerfa_text.get())
           kerfa_price=10
           total1=kerfa_num*kerfa_price
           print(total1)

                  # ganzapil
       ganzapil=ganzapil_text.get()
       if(ganzapil !=""):
                   # 
           ganzapil_num=int(ganzapil_text.get())
           ganzapil_price=10
           total1=ganzapil_num*ganzapil_price
           print(total1)

                  # kerfa_ganzapil
       kerfa_ganzapil=kerfa_ganzapil_text.get()
       if(kerfa_ganzapil !=""):
                   # 
           kerfa_ganzapil_num=int(kerfa_ganzapil_text.get())
           kerfa_ganzapil_price=12
           total1=kerfa_ganzapil_num*kerfa_ganzapil_price
           print(total1)

                  # kerfa_milk
       kerfa_milk=kerfa_milk_text.get()
       if(kerfa_milk !=""):
                   # 
           kerfa_milk_num=int(kerfa_milk_text.get())
           kerfa_milk_price=15
           total1=kerfa_milk_num*kerfa_milk_price
           print(total1)

                  # synayon
       synayon=synayon_text.get()
       if(synayon !=""):
                   # 
           synayon_num=int(synayon_text.get())
           synayon_price=17
           total1=synayon_num*synayon_price
           print(total1)
                  # hotseeder
       hotseeder=hotseeder_text.get()
       if(hotseeder !=""):
                   # 
           hotseeder_num=int(hotseeder_text.get())
           hotseeder_price=15
           total1=hotseeder_num*hotseeder_price
           print(total1)

                  # cooctail
       cooctail=cooctail_text.get()
       if(cooctail !=""):
                   # 
           cooctail_num=int(cooctail_text.get())
           cooctail_price=20
           total1=cooctail_num*cooctail_price
           print(total1)
 

    herbs_window=Toplevel(win)
    herbs_window.geometry("540x340")
    herbs_window.geometry("+500+50")
    herbs_label=Label(herbs_window,font=('courier 30 bold'), fg='blue',text=" أعشاب")
    herbs_label.place(x=200,y=10)
    # سجق
    yanson_Label=Label(herbs_window,text="ينسون",font=('courier 15 bold'))
    yanson_Label.place(x=420,y=70)
    yanson_text=Entry(herbs_window,width=8,font=('courier 15 bold'),justify="center")
    yanson_text.place(x=280,y=70)

    # كريسبي
    karkadeeh_Label=Label(herbs_window,text="  كركديه",font=('courier 15 bold'))
    karkadeeh_Label.place(x=400,y=115)
    karkadeeh_text=Entry(herbs_window,width=8,font=('courier 15 bold'),justify="center")
    karkadeeh_text.place(x=280,y=115)
    # جمبري
    neanaa_Label=Label(herbs_window,text="  نعناع",font=('courier 15 bold'))
    neanaa_Label.place(x=400,y=160)
    neanaa_text=Entry(herbs_window,width=8,font=('courier 15 bold'),justify="center")
    neanaa_text.place(x=280,y=160)

    # شاورما
    kerfa_Label=Label(herbs_window,text="قرفة",font=('courier 15 bold'))
    kerfa_Label.place(x=420,y=205)
    kerfa_text=Entry(herbs_window,width=8,font=('courier 15 bold'),justify="center")
    kerfa_text.place(x=280,y=205)
    
    # بطاطس
    ganzapil_Label=Label(herbs_window,text="جنزبيل",font=('courier 15 bold'))
    ganzapil_Label.place(x=410,y=250)
    ganzapil_text=Entry(herbs_window,width=8,font=('courier 15 bold'),justify="center")
    ganzapil_text.place(x=280,y=250)
    

 #  هوكري بورجر
    kerfa_ganzapil_Label=Label(herbs_window,text="قرفة بالجنزبيل",font=('courier 12 bold'))
    kerfa_ganzapil_Label.place(x=130,y=70)
    kerfa_ganzapil_text=Entry(herbs_window,width=8,font=('courier 15 bold'),justify="center")
    kerfa_ganzapil_text.place(x=20,y=70)
    
    #  فاهيتا فراخ
    kerfa_milk_Label=Label(herbs_window,text="قرفة باللبن",font=('courier 12 bold'))
    kerfa_milk_Label.place(x=130,y=115)
    kerfa_milk_text=Entry(herbs_window,width=8,font=('courier 15 bold'),justify="center")
    kerfa_milk_text.place(x=20,y=115)

    #    فاهيتا لحم
    synayon_Label=Label(herbs_window,text="سينابون",font=('courier 12 bold'))
    synayon_Label.place(x=150,y=160)
    synayon_text=Entry(herbs_window,width=8,font=('courier 15 bold'),justify="center")
    synayon_text.place(x=20,y=160)
    #   تشيكن رول 
    hotseeder_Label=Label(herbs_window,text="هوت سيدر",font=('courier 12 bold'))
    hotseeder_Label.place(x=130,y=205)
    hotseeder_text=Entry(herbs_window,width=8,font=('courier 15 bold'),justify="center")
    hotseeder_text.place(x=20,y=205)
    #    ميكس جبن 
    cooctail_Label=Label(herbs_window,text="كوكتيل أعشاب",font=('courier 12 bold'))
    cooctail_Label.place(x=130,y=250)
    cooctail_text=Entry(herbs_window,width=8,font=('courier 15 bold'),justify="center")
    cooctail_text.place(x=20,y=250)
   
   
    # button to save

    save_button = Button(herbs_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_herbs)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=220, y=300)
def showavocado():
    def save_avocado():
        
        # mekasarat
        mekasarat=mekasarat_text.get()
        if(mekasarat !=""):
            
           mekasarat_num=int(mekasarat_text.get())
           mekasarat_price=27
           total1=mekasarat_num*mekasarat_price
           print(total1)

        # foul
        foul=foul_text.get()
        if(foul !=""):
            # 
           foul_num=int(foul_text.get())
           foul_price=28
           total1=foul_num*foul_price
           print(total1)


        # special
        special=special_text.get()
        if(special !=""):
            # 
           special_num=int(special_text.get())
           special_price=30
           total1=special_num*special_price
           print(total1)

        # asal
        asal=asal_text.get()
        if(asal !=""):
            # 
           asal_num=int(asal_text.get())
           asal_price=25
           total1=asal_num*asal_price
           print(total1)


                # kewy
        kewy=kewy_text.get()
        if(kewy !=""):
            # 
           kewy_num=int(kewy_text.get())
           kewy_price=28
           total1=kewy_num*kewy_price
           print(total1)

                # balah
        balah=balah_text.get()
        if(balah !=""):
            # 
           balah_num=int(balah_text.get())
           balah_price=28
           total1=balah_num*balah_price
           print(total1)

                # mango
        mango=mango_text.get()
        if(mango !=""):
            # 
           mango_num=int(mango_text.get())
           mango_price=28
           total1=mango_num*mango_price
           print(total1)

    avocado_window=Toplevel(win)
    avocado_window.geometry("580x280")
    avocado_window.geometry("+450+50")
    avocado_label=Label(avocado_window,font=('courier 30 bold'), fg='blue',text=" أفوكادو ")
    avocado_label.place(x=200,y=10)
    # سجق
    mekasarat_Label=Label(avocado_window,text=" افوكادو مكسرات",font=('courier 12 bold'))
    mekasarat_Label.place(x=420,y=70)
    mekasarat_text=Entry(avocado_window,width=8,font=('courier 15 bold'),justify="center")
    mekasarat_text.place(x=280,y=70)

    # كريسبي
    foul_Label=Label(avocado_window,text="افوكادو فول سوداني",font=('courier 12 bold'))
    foul_Label.place(x=390,y=115)
    foul_text=Entry(avocado_window,width=8,font=('courier 15 bold'),justify="center")
    foul_text.place(x=280,y=115)
    # جمبري
    special_Label=Label(avocado_window,text="  افوكادو اسبيشيل",font=('courier 12 bold'))
    special_Label.place(x=400,y=160)
    special_text=Entry(avocado_window,width=8,font=('courier 15 bold'),justify="center")
    special_text.place(x=280,y=160)

   

 #  هوكري بورجر
    asal_Label=Label(avocado_window,text=" افوكادو عسل  ",font=('courier 12 bold'))
    asal_Label.place(x=130,y=70)
    asal_text=Entry(avocado_window,width=8,font=('courier 15 bold'),justify="center")
    asal_text.place(x=20,y=70)
    
    #  فاهيتا فراخ
    kewy_Label=Label(avocado_window,text="افوكادو كيوي",font=('courier 12 bold'))
    kewy_Label.place(x=130,y=115)
    kewy_text=Entry(avocado_window,width=8,font=('courier 15 bold'),justify="center")
    kewy_text.place(x=20,y=115)

    #    فاهيتا لحم
    balah_Label=Label(avocado_window,text="افوكادو بلح",font=('courier 12 bold'))
    balah_Label.place(x=135,y=160)
    balah_text=Entry(avocado_window,width=8,font=('courier 15 bold'),justify="center")
    balah_text.place(x=20,y=160)
    #   تشيكن رول 
    mango_Label=Label(avocado_window,text="افوكادو مانجا",font=('courier 12 bold'))
    mango_Label.place(x=120,y=205)
    mango_text=Entry(avocado_window,width=8,font=('courier 15 bold'),justify="center")
    mango_text.place(x=20,y=205)
   

   
    # button to save

    save_button = Button(avocado_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_avocado)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=260, y=230)
def showsmoozy():
    def save_smoozy():
               # mango
       mango=mango_text.get()
       if(mango !=""):
                   # 
           mango_num=int(mango_text.get())
           mango_price=25
           total1=mango_num*mango_price
           print(total1)

                  # guava
       guava=guava_text.get()
       if(guava !=""):
                   # 
           guava_num=int(guava_text.get())
           guava_price=23
           total1=guava_num*guava_price
           print(total1)

                  # farawla
       farawla=farawla_text.get()
       if(farawla !=""):
                   # 
           farawla_num=int(farawla_text.get())
           farawla_price=25
           total1=farawla_num*farawla_price
           print(total1)

                  # kewy
       kewy=kewy_text.get()
       if(kewy !=""):
                   # 
           kewy_num=int(kewy_text.get())
           kewy_price=25
           total1=kewy_num*kewy_price
           print(total1)

                  # ananas
       ananas=ananas_text.get()
       if(ananas !=""):
                   # 
           ananas_num=int(ananas_text.get())
           ananas_price=22
           total1=ananas_num*ananas_price
           print(total1)

                  # khokh
       khokh=khokh_text.get()
       if(khokh !=""):
                   # 
           khokh_num=int(khokh_text.get())
           khokh_price=22
           total1=khokh_num*khokh_price
           print(total1)

                  # batteekh
       batteekh=batteekh_text.get()
       if(batteekh !=""):
                   # 
           batteekh_num=int(batteekh_text.get())
           batteekh_price=25
           total1=batteekh_num*batteekh_price
           print(total1)

                  # blueberry
       blueberry=blueberry_text.get()
       if(blueberry !=""):
                   # 
           blueberry_num=int(blueberry_text.get())
           blueberry_price=25
           total1=blueberry_num*blueberry_price
           print(total1)

                  # roseberry
       roseberry=roseberry_text.get()
       if(roseberry !=""):
                   # 
           roseberry_num=int(roseberry_text.get())
           roseberry_price=25
           total1=roseberry_num*roseberry_price
           print(total1)

                  # maxberry
       maxberry=maxberry_text.get()
       if(maxberry !=""):
                   # 
           maxberry_num=int(maxberry_text.get())
           maxberry_price=28
           total1=maxberry_num*maxberry_price
           print(total1)

                  # bashoz_fruit
       bashoz_fruit=bashoz_fruit_text.get()
       if(bashoz_fruit !=""):
                   # 
           bashoz_fruit_num=int(bashoz_fruit_text.get())
           bashoz_fruit_price=25
           total1=bashoz_fruit_num*bashoz_fruit_price
           print(total1)

                  # lemon_neanaa
       lemon_neanaa=lemon_neanaa_text.get()
       if(lemon_neanaa !=""):
                   # 
           lemon_neanaa_num=int(lemon_neanaa_text.get())
           lemon_neanaa_price=23
           total1=lemon_neanaa_num*lemon_neanaa_price
           print(total1)

                  # lemon
       lemon=lemon_text.get()
       if(lemon !=""):
                   # 
           lemon_num=int(lemon_text.get())
           lemon_price=20
           total1=lemon_num*lemon_price
           print(total1)

    
    smoozy_window=Toplevel(win)
    smoozy_window.geometry("550x450")
    smoozy_window.geometry("+150+50")
    smoozy_label=Label(smoozy_window,font=('courier 30 bold'), fg='blue',text=" سموزي")
    smoozy_label.place(x=200,y=10)
    # سجق
    mango_Label=Label(smoozy_window,text="سموزي مانجا",font=('courier 12 bold'))
    mango_Label.place(x=405,y=70)
    mango_text=Entry(smoozy_window,width=8,font=('courier 15 bold'),justify="center")
    mango_text.place(x=300,y=70)

    # كريسبي
    guava_Label=Label(smoozy_window,text="سموزي جوافة ",font=('courier 12 bold'))
    guava_Label.place(x=405,y=115)
    guava_text=Entry(smoozy_window,width=8,font=('courier 15 bold'),justify="center")
    guava_text.place(x=300,y=115)
    # جمبري
    farawla_Label=Label(smoozy_window,text=" سموزي فراولة",font=('courier 12 bold'))
    farawla_Label.place(x=390,y=160)
    farawla_text=Entry(smoozy_window,width=8,font=('courier 15 bold'),justify="center")
    farawla_text.place(x=300,y=160)

    # شاورما
    kewy_Label=Label(smoozy_window,text="  سموزي كيوي ",font=('courier 12 bold'))
    kewy_Label.place(x=390,y=205)
    kewy_text=Entry(smoozy_window,width=8,font=('courier 15 bold'),justify="center")
    kewy_text.place(x=300,y=205)
    
    # بطاطس
    ananas_Label=Label(smoozy_window,text="  سموزي أناناس  ",font=('courier 12 bold'))
    ananas_Label.place(x=385,y=250)
    ananas_text=Entry(smoozy_window,width=8,font=('courier 15 bold'),justify="center")
    ananas_text.place(x=300,y=250)
    # كفتة
    khokh_Label=Label(smoozy_window,text="  سموزي خوخ  ",font=('courier 12 bold'))
    khokh_Label.place(x=390,y=295)
    khokh_text=Entry(smoozy_window,width=8,font=('courier 15 bold'),justify="center")
    khokh_text.place(x=300,y=295)
    # شيش
    batteekh_Label=Label(smoozy_window,text="  سموزي بطيخ ",font=('courier 12 bold'))
    batteekh_Label.place(x=390,y=340)
    batteekh_text=Entry(smoozy_window,width=8,font=('courier 15 bold'),justify="center")
    batteekh_text.place(x=300,y=340)
    # بسطرمة

   
 #  هوكري بورجر
    blueberry_Label=Label(smoozy_window,text="سموزي بلوبيري",font=('courier 12 bold'))
    blueberry_Label.place(x=120,y=70)
    blueberry_text=Entry(smoozy_window,width=8,font=('courier 15 bold'),justify="center")
    blueberry_text.place(x=20,y=70)
    
    #  فاهيتا فراخ
    roseberry_Label=Label(smoozy_window,text="  سموزي روزبيري ",font=('courier 12 bold'))
    roseberry_Label.place(x=100,y=115)
    roseberry_text=Entry(smoozy_window,width=8,font=('courier 15 bold'),justify="center")
    roseberry_text.place(x=20,y=115)

    #    فاهيتا لحم 
    maxberry_Label=Label(smoozy_window,text=" سموزي مكس بيري",font=('courier 12 bold'))
    maxberry_Label.place(x=115,y=160)
    maxberry_text=Entry(smoozy_window,width=8,font=('courier 15 bold'),justify="center")
    maxberry_text.place(x=20,y=160)
    #   تشيكن رول 
    bashoz_fruit_Label=Label(smoozy_window,text="سموزي باشوز فروت",font=('courier 12 bold'))
    bashoz_fruit_Label.place(x=120,y=205)
    bashoz_fruit_text=Entry(smoozy_window,width=8,font=('courier 15 bold'),justify="center")
    bashoz_fruit_text.place(x=20,y=205)
    #    ميكس جبن 
    lemon_neanaa_Label=Label(smoozy_window,text=" سموزي ليمون نعناع",font=('courier 12 bold'))
    lemon_neanaa_Label.place(x=110,y=250)
    lemon_neanaa_text=Entry(smoozy_window,width=8,font=('courier 15 bold'),justify="center")
    lemon_neanaa_text.place(x=20,y=250)
    #    بورجر ديبر 
    lemon_Label=Label(smoozy_window,text=" سموزي ليمون",font=('courier 12 bold'))
    lemon_Label.place(x=125,y=295)
    lemon_text=Entry(smoozy_window,width=8,font=('courier 15 bold'),justify="center")
    lemon_text.place(x=20,y=295)

    # button to save

    save_button = Button(smoozy_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_smoozy)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=200, y=400)
def showhotchoclate():
    
    def save_hotchoclate():
            # hotchoclate
        hotchoclate=hotchoclate_text.get()
        if(hotchoclate !=""):
                    # 
            hotchoclate_num=int(hotchoclate_text.get())
            hotchoclate_price=18
            total1=hotchoclate_num*hotchoclate_price
            print(total1)

                # galaxy
        galaxy=galaxy_text.get()
        if(galaxy !=""):
                    # 
            galaxy_num=int(galaxy_text.get())
            galaxy_price=22
            total1=galaxy_num*galaxy_price
            print(total1)

                # notella
        notella=notella_text.get()
        if(notella !=""):
                    # 
            notella_num=int(notella_text.get())
            notella_price=22
            total1=notella_num*notella_price
            print(total1)

                # oreo
        oreo=oreo_text.get()
        if(oreo !=""):
                    # 
            oreo_num=int(oreo_text.get())
            oreo_price=22
            total1=oreo_num*oreo_price
            print(total1)

                # deer
        deer=deer_text.get()
        if(deer !=""):
                    # 
            deer_num=int(deer_text.get())
            deer_price=27
            total1=deer_num*deer_price
            print(total1)

                # lotas
        lotas=lotas_text.get()
        if(lotas !=""):
                    # 
            lotas_num=int(lotas_text.get())
            lotas_price=25
            total1=lotas_num*lotas_price
            print(total1)

                # karamel
        karamel=karamel_text.get()
        if(karamel !=""):
                    # 
            karamel_num=int(karamel_text.get())
            karamel_price=22
            total1=karamel_num*karamel_price
            print(total1)


    hotchoclate_window=Toplevel(win)
    hotchoclate_window.geometry("580x280")
    hotchoclate_window.geometry("+650+220")
    hotchoclate_label=Label(hotchoclate_window,font=('courier 30 bold'), fg='blue',text="   هوت شوكليت")
    hotchoclate_label.place(x=90,y=10)
    # سجق
    hotchoclate_Label=Label(hotchoclate_window,text=" هوت شوكلت",font=('courier 12 bold'))
    hotchoclate_Label.place(x=430,y=70)
    hotchoclate_text=Entry(hotchoclate_window,width=8,font=('courier 15 bold'),justify="center")
    hotchoclate_text.place(x=315,y=70)

    # كريسبي
    galaxy_Label=Label(hotchoclate_window,text="هوت شوكلت جلاكسي",font=('courier 12 bold'))
    galaxy_Label.place(x=420,y=115)
    galaxy_text=Entry(hotchoclate_window,width=8,font=('courier 15 bold'),justify="center")
    galaxy_text.place(x=315,y=115)
    # جمبري
    notella_Label=Label(hotchoclate_window,text="  هوت شوكلت نوتيلا",font=('courier 12 bold'))
    notella_Label.place(x=400,y=160)
    notella_text=Entry(hotchoclate_window,width=8,font=('courier 15 bold'),justify="center")
    notella_text.place(x=315,y=160)

   

 #  هوكري بورجر
    oreo_Label=Label(hotchoclate_window,text=" هوت شوكليت أوريو  ",font=('courier 12 bold'))
    oreo_Label.place(x=130,y=70)
    oreo_text=Entry(hotchoclate_window,width=8,font=('courier 15 bold'),justify="center")
    oreo_text.place(x=20,y=70)
    
    #  فاهيتا فراخ
    deer_Label=Label(hotchoclate_window,text="  هوت شوكلت دير  ",font=('courier 12 bold'))
    deer_Label.place(x=130,y=115)
    deer_text=Entry(hotchoclate_window,width=8,font=('courier 15 bold'),justify="center")
    deer_text.place(x=20,y=115)

    #    فاهيتا لحم
    lotas_Label=Label(hotchoclate_window,text="هوت لوتس",font=('courier 12 bold'))
    lotas_Label.place(x=150,y=160)
    lotas_text=Entry(hotchoclate_window,width=8,font=('courier 15 bold'),justify="center")
    lotas_text.place(x=20,y=160)
    #   تشيكن رول 
    karamel_Label=Label(hotchoclate_window,text="هوت كراميل",font=('courier 12 bold'))
    karamel_Label.place(x=140,y=205)
    karamel_text=Entry(hotchoclate_window,width=8,font=('courier 15 bold'),justify="center")
    karamel_text.place(x=20,y=205)
   

   
    # button to save

    save_button = Button(hotchoclate_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_hotchoclate)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=260, y=230)
def show_icecream():
    def save_icecream():
         # toot
        toot=toot_text.get()
        if(toot!=""):
             # 
            toot_num=int(toot_text.get())
            toot_price=20
            total=toot_num*toot_price
            print(total)
        

          # toot
        oreo=oreo_text.get()
        if(oreo !=""):
        # 
            oreo_num=int(oreo_text.get())
            oreo_price=22
            total=oreo_num*oreo_price
            print(total)
           # toot
        notella=notella_text.get()
        if(notella !=""):
 # 
            notella_num=int(notella_text.get())
            notella_price=20
            total=notella_num*notella_price
            print(total)
        
        keetcat=keetcat_text.get()
        if(keetcat !=""):
            keetcat_num=int(keetcat_text.get())
            keetcat_price=22
            total=keetcat_num*keetcat_price
            print(total)

        frost=frost_text.get()
        if(frost !=""):
            frost_num=int(frost_text.get())
            frost_price=27
            total=frost_num*frost_price
            print(total)
        

        monday3=monday_text.get()
        if(monday3 !=""):
            monday_num=int(monday_text.get())
            monday_price=17
            total=monday_num*monday_price
            print(total)
        
        
        banana3=banana_text.get()
        if(banana3 !=""):
            banana_num=int(banana_text.get())
            banana_price=30
            total=banana_num*banana_price
            print(total)
        
        
        
        monday5=monday_text.get()
        if(monday5 !=""):
            monday_num=int(monday_text.get())
            monday_price=30
            total=monday_num*monday_price
            print(total)
        
        
    icecream_window=Toplevel(win)
    icecream_window.geometry("500x310")
    icecream_window.geometry("+300+150")
    icecream_label=Label(icecream_window,font=('courier 30 bold'), fg='blue',text=" آيس كريم")
    icecream_label.place(x=160,y=10)
    # سجق
    toot_Label=Label(icecream_window,text="توت",font=('courier 15 bold'))
    toot_Label.place(x=400,y=70)
    toot_text=Entry(icecream_window,width=8,font=('courier 15 bold'),justify="center")
    toot_text.place(x=280,y=70)

    # كريسبي
    oreo_Label=Label(icecream_window,text="  اوريو",font=('courier 15 bold'))
    oreo_Label.place(x=375,y=115)
    oreo_text=Entry(icecream_window,width=8,font=('courier 15 bold'),justify="center")
    oreo_text.place(x=280,y=115)
    # جمبري
    notella_Label=Label(icecream_window,text="نوتيلا",font=('courier 15 bold'))
    notella_Label.place(x=390,y=160)
    notella_text=Entry(icecream_window,width=8,font=('courier 15 bold'),justify="center")
    notella_text.place(x=280,y=160)

    # شاورما
    frost_Label=Label(icecream_window,text="فروست ",font=('courier 15 bold'))
    frost_Label.place(x=390,y=205)
    frost_text=Entry(icecream_window,width=8,font=('courier 15 bold'),justify="center")
    frost_text.place(x=280,y=205)


 #  هوكري بورجر
    monday_Label=Label(icecream_window,text=" من داي 3بولة",font=('courier 12 bold'))
    monday_Label.place(x=130,y=70)
    monday_text=Entry(icecream_window,width=8,font=('courier 15 bold'),justify="center")
    monday_text.place(x=20,y=70)
    
    #  فاهيتا فراخ
    keetcat_Label=Label(icecream_window,text=" كيت كات",font=('courier 12 bold'))
    keetcat_Label.place(x=130,y=115)
    keetcat_text=Entry(icecream_window,width=8,font=('courier 15 bold'),justify="center")
    keetcat_text.place(x=20,y=115)

    #    فاهيتا لحم
    banana_Label=Label(icecream_window,text=" بنانا سلفيين",font=('courier 12 bold'))
    banana_Label.place(x=130,y=160)
    banana_text=Entry(icecream_window,width=8,font=('courier 15 bold'),justify="center")
    banana_text.place(x=20,y=160)
    #   تشيكن رول 
    monday5_Label=Label(icecream_window,text="من داي 5بولة ",font=('courier 12 bold'))
    monday5_Label.place(x=130,y=205)
    monday5_text=Entry(icecream_window,width=8,font=('courier 15 bold'),justify="center")
    monday5_text.place(x=20,y=205)
   
   
    # button to save

    save_button = Button(icecream_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_icecream)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=220, y=250)
def showshawrma():
    
    def save_shawrma():
        pass
    shawrma_window=Toplevel(win)
    shawrma_window.geometry("540x300")
    shawrma_window.geometry("+50+150")
    shawrma_label=Label(shawrma_window,font=('courier 30 bold'), fg='blue',text=" شاورما")
    shawrma_label.place(x=200,y=10)
    # سجق
    shawrma_Label1=Label(shawrma_window,text="ساندوتش لارج",font=('courier 15 bold'))
    shawrma_Label1.place(x=400,y=70)
    shawrma_text1=Entry(shawrma_window,width=8,font=('courier 15 bold'),justify="center")
    shawrma_text1.place(x=280,y=70)

    # كريسبي
    shawrma_Label2=Label(shawrma_window,text="  ساندوتش اكس لارج",font=('courier 13 bold'))
    shawrma_Label2.place(x=365,y=115)
    shawrma_text2=Entry(shawrma_window,width=8,font=('courier 15 bold'),justify="center")
    shawrma_text2.place(x=280,y=115)
    # جمبري
    shawrma_Label3=Label(shawrma_window,text="  وجبة عربي",font=('courier 15 bold'))
    shawrma_Label3.place(x=380,y=160)
    shawrma_text3=Entry(shawrma_window,width=8,font=('courier 15 bold'),justify="center")
    shawrma_text3.place(x=280,y=160)

    # شاورما
    shawrma_Label4=Label(shawrma_window,text="  فتة شاورما ",font=('courier 15 bold'))
    shawrma_Label4.place(x=370,y=205)
    shawrma_text4=Entry(shawrma_window,width=8,font=('courier 15 bold'),justify="center")
    shawrma_text4.place(x=280,y=205)
    
    
 #  هوكري بورجر
    shawrma_Label11=Label(shawrma_window,text="وجبة عربي عائلي",font=('courier 12 bold'))
    shawrma_Label11.place(x=120,y=70)
    shawrma_text11=Entry(shawrma_window,width=8,font=('courier 15 bold'),justify="center")
    shawrma_text11.place(x=20,y=70)
    
    #  فاهيتا فراخ
    shawrma_Label12=Label(shawrma_window,text="وزن 1ك",font=('courier 12 bold'))
    shawrma_Label12.place(x=150,y=115)
    shawrma_text12=Entry(shawrma_window,width=8,font=('courier 15 bold'),justify="center")
    shawrma_text12.place(x=20,y=115)

    #    فاهيتا لحم
    shawrma_Label13=Label(shawrma_window,text="وزن 1/2 ك",font=('courier 12 bold'))
    shawrma_Label13.place(x=135,y=160)
    shawrma_text13=Entry(shawrma_window,width=8,font=('courier 15 bold'),justify="center")
    shawrma_text13.place(x=20,y=160)
    #   تشيكن رول 
    shawrma_Label14=Label(shawrma_window,text="وزن 1/4 ك",font=('courier 12 bold'))
    shawrma_Label14.place(x=135,y=205)
    shawrma_text14=Entry(shawrma_window,width=8,font=('courier 15 bold'),justify="center")
    shawrma_text14.place(x=20,y=205)
    
    # button to save

    save_button = Button(shawrma_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_shawrma)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=220, y=260)
def showmacarona():
    
    def save_macarona():
        pass

    macarona_window=Toplevel(win)
    macarona_window.geometry("560x340")
    macarona_window.geometry("+100+200")
    macarona_label=Label(macarona_window,font=('courier 30 bold'), fg='blue',text=" مكرونة")
    macarona_label.place(x=200,y=10)
    # سجق
    macarona_Label1=Label(macarona_window,text="نجرسكو",font=('courier 13 bold'))
    macarona_Label1.place(x=470,y=70)
    macarona_text1=Entry(macarona_window,width=8,font=('courier 15 bold'),justify="center")
    macarona_text1.place(x=330,y=70)

    # كريسبي
    macarona_Label2=Label(macarona_window,text="  نجرسكو جمبرى",font=('courier 13 bold'))
    macarona_Label2.place(x=405,y=115)
    macarona_text2=Entry(macarona_window,width=8,font=('courier 15 bold'),justify="center")
    macarona_text2.place(x=330,y=115)
    # جمبري
    macarona_Label3=Label(macarona_window,text=" حم اتشيكن",font=('courier 13 bold'))
    macarona_Label3.place(x=430,y=160)
    macarona_text3=Entry(macarona_window,width=8,font=('courier 15 bold'),justify="center")
    macarona_text3.place(x=330,y=160)

    # شاورما
    macarona_Label4=Label(macarona_window,text="  بلونيز ",font=('courier 13 bold'))
    macarona_Label4.place(x=430,y=205)
    macarona_text4=Entry(macarona_window,width=8,font=('courier 15 bold'),justify="center")
    macarona_text4.place(x=330,y=205)
    
    # بطاطس
    macarona_Label5=Label(macarona_window,text="   اربياتا ",font=('courier 13 bold'))
    macarona_Label5.place(x=430,y=250)
    macarona_text5=Entry(macarona_window,width=8,font=('courier 15 bold'),justify="center")
    macarona_text5.place(x=330,y=250)
    

 #  هوكري بورجر
    macarona_Label11=Label(macarona_window,text="الفريدو",font=('courier 12 bold'))
    macarona_Label11.place(x=150,y=70)
    macarona_text11=Entry(macarona_window,width=8,font=('courier 15 bold'),justify="center")
    macarona_text11.place(x=20,y=70)
    
    #  فاهيتا فراخ
    macarona_Label12=Label(macarona_window,text="اسباجيتي ميت بول",font=('courier 12 bold'))
    macarona_Label12.place(x=120,y=115)
    macarona_text12=Entry(macarona_window,width=8,font=('courier 15 bold'),justify="center")
    macarona_text12.place(x=20,y=115)

    #    فاهيتا لحم
    macarona_Label13=Label(macarona_window,text=" مكرونه بصوص الكارى  ",font=('courier 12 bold'))
    macarona_Label13.place(x=120,y=160)
    macarona_text13=Entry(macarona_window,width=8,font=('courier 15 bold'),justify="center")
    macarona_text13.place(x=20,y=160)
    #   تشيكن رول 
    macarona_Label14=Label(macarona_window,text="باسطا سي فود",font=('courier 12 bold'))
    macarona_Label14.place(x=120,y=205)
    macarona_text14=Entry(macarona_window,width=8,font=('courier 15 bold'),justify="center")
    macarona_text14.place(x=20,y=205)
    #    ميكس جبن 
    macarona_Label15=Label(macarona_window,text=" بشاميل  ",font=('courier 12 bold'))
    macarona_Label15.place(x=140,y=250)
    macarona_text15=Entry(macarona_window,width=8,font=('courier 15 bold'),justify="center")
    macarona_text15.place(x=20,y=250)
   
   
    # button to save

    save_button = Button(macarona_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_macarona)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=220, y=300)
def showspresso():
    def save_spresso():
        pass
    spresso_window=Toplevel(win)
    spresso_window.geometry("560x300")
    spresso_window.geometry("+50+200")
    spresso_label=Label(spresso_window,font=('courier 30 bold'), fg='blue',text=" اسبريسو")
    spresso_label.place(x=200,y=10)
    # سجق
    spresso_Label1=Label(spresso_window,text="كون بانا",font=('courier 13 bold'))
    spresso_Label1.place(x=400,y=70)
    spresso_text1=Entry(spresso_window,width=8,font=('courier 15 bold'),justify="center")
    spresso_text1.place(x=300,y=70)

    # كريسبي
    spresso_Label2=Label(spresso_window,text="  كورتادو ",font=('courier 13 bold'))
    spresso_Label2.place(x=385,y=115)
    spresso_text2=Entry(spresso_window,width=8,font=('courier 15 bold'),justify="center")
    spresso_text2.place(x=300,y=115)
    # جمبري
    spresso_Label3=Label(spresso_window,text=" رومانو ",font=('courier 13 bold'))
    spresso_Label3.place(x=400,y=160)
    spresso_text3=Entry(spresso_window,width=8,font=('courier 15 bold'),justify="center")
    spresso_text3.place(x=300,y=160)

    # شاورما
    spresso_Label4=Label(spresso_window,text="  أفوكاتو  ",font=('courier 13 bold'))
    spresso_Label4.place(x=400,y=205)
    spresso_text4=Entry(spresso_window,width=8,font=('courier 15 bold'),justify="center")
    spresso_text4.place(x=300,y=205)


    spresso_Label11=Label(spresso_window,text="أفوكاتو آيس",font=('courier 12 bold'))
    spresso_Label11.place(x=150,y=70)
    spresso_text11=Entry(spresso_window,width=8,font=('courier 15 bold'),justify="center")
    spresso_text11.place(x=20,y=70)
    
    #  فاهيتا فراخ
    spresso_Label12=Label(spresso_window,text="  ميكاتو",font=('courier 12 bold'))
    spresso_Label12.place(x=120,y=115)
    spresso_text12=Entry(spresso_window,width=8,font=('courier 15 bold'),justify="center")
    spresso_text12.place(x=20,y=115)

    #    فاهيتا لحم
    spresso_Label13=Label(spresso_window,text=" اسبريسو دابل  ",font=('courier 12 bold'))
    spresso_Label13.place(x=120,y=160)
    spresso_text13=Entry(spresso_window,width=8,font=('courier 15 bold'),justify="center")
    spresso_text13.place(x=20,y=160)
    #   تشيكن رول 
    spresso_Label14=Label(spresso_window,text="اسبريسو سنجل",font=('courier 12 bold'))
    spresso_Label14.place(x=120,y=205)
    spresso_text14=Entry(spresso_window,width=8,font=('courier 15 bold'),justify="center")
    spresso_text14.place(x=20,y=205)
    

    save_button = Button(spresso_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_spresso)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=220, y=260)
def showmilkcheck():
    def save_milkcheck():
        pass
    milkcheck_window=Toplevel(win)
    milkcheck_window.geometry("450x590")
    milkcheck_window.geometry("+550+50")
    milkcheck_label=Label(milkcheck_window,font=('courier 30 bold'), fg='blue',text="ميلك تشيك")
    milkcheck_label.place(x=130,y=10)
    # مانجو
    milkcheck_Label1=Label(milkcheck_window,text="لوتس",font=('courier 15 bold'))
    milkcheck_Label1.place(x=360,y=70)
    milkcheck_text1=Entry(milkcheck_window,width=8,font=('courier 15 bold'),justify="center")
    milkcheck_text1.place(x=230,y=70)

    # جوافة
    milkcheck_Label2=Label(milkcheck_window,text="هوهوز",font=('courier 15 bold'))
    milkcheck_Label2.place(x=360,y=115)
    milkcheck_text2=Entry(milkcheck_window,width=8,font=('courier 15 bold'),justify="center")
    milkcheck_text2.place(x=230,y=115)
    # فراولة
    milkcheck_Label3=Label(milkcheck_window,text="توينكز",font=('courier 15 bold'))
    milkcheck_Label3.place(x=360,y=160)
    milkcheck_text3=Entry(milkcheck_window,width=8,font=('courier 15 bold'),justify="center")
    milkcheck_text3.place(x=230,y=160)

    # كيوي
    milkcheck_Label4=Label(milkcheck_window,text="  جلاكسي",font=('courier 15 bold'))
    milkcheck_Label4.place(x=330,y=205)
    milkcheck_text4=Entry(milkcheck_window,width=8,font=('courier 15 bold'),justify="center")
    milkcheck_text4.place(x=230,y=205)
    
    # خوخ
    milkcheck_Label5=Label(milkcheck_window,text="  كيت كات",font=('courier 15 bold'))
    milkcheck_Label5.place(x=330,y=250)
    milkcheck_text5=Entry(milkcheck_window,width=8,font=('courier 15 bold'),justify="center")
    milkcheck_text5.place(x=230,y=250)
    # أناناس
    milkcheck_Label6=Label(milkcheck_window,text="  اسنيكرز",font=('courier 15 bold'))
    milkcheck_Label6.place(x=330,y=295)
    milkcheck_text6=Entry(milkcheck_window,width=8,font=('courier 15 bold'),justify="center")
    milkcheck_text6.place(x=230,y=295)
    # رمان
    milkcheck_Label7=Label(milkcheck_window,text="  شوكلاتة",font=('courier 15 bold'))
    milkcheck_Label7.place(x=330,y=340)
    milkcheck_text7=Entry(milkcheck_window,width=8,font=('courier 15 bold'),justify="center")
    milkcheck_text7.place(x=230,y=340)
    # بطيخ
    milkcheck_Label8=Label(milkcheck_window,text="  فانيليا",font=('courier 15 bold'))
    milkcheck_Label8.place(x=330,y=385)
    milkcheck_text8=Entry(milkcheck_window,width=8,font=('courier 15 bold'),justify="center")
    milkcheck_text8.place(x=230,y=385)
    # ليمون
    milkcheck_Label9=Label(milkcheck_window,text="  مكسرات",font=('courier 15 bold'))
    milkcheck_Label9.place(x=330,y=430)
    milkcheck_text9=Entry(milkcheck_window,width=8,font=('courier 15 bold'),justify="center")
    milkcheck_text9.place(x=230,y=430)
     # نعناع
    milkcheck_Label10=Label(milkcheck_window,text="  بلح",font=('courier 15 bold'))
    milkcheck_Label10.place(x=330,y=475)
    milkcheck_text10=Entry(milkcheck_window,width=8,font=('courier 15 bold'),justify="center")
    milkcheck_text10.place(x=230,y=475)
        
    
     
 # موز باللبن
    milkcheck_Label11=Label(milkcheck_window,text="فراولة",font=('courier 12 bold'))
    milkcheck_Label11.place(x=135,y=70)
    milkcheck_text11=Entry(milkcheck_window,width=8,font=('courier 15 bold'),justify="center")
    milkcheck_text11.place(x=20,y=70)
    
    # جوافة باللبن
    milkcheck_Label12=Label(milkcheck_window,text="مانجا",font=('courier 12 bold'))
    milkcheck_Label12.place(x=135,y=115)
    milkcheck_text12=Entry(milkcheck_window,width=8,font=('courier 15 bold'),justify="center")
    milkcheck_text12.place(x=20,y=115)

    #  فراولة باللبن 
    milkcheck_Label13=Label(milkcheck_window,text="كراميل",font=('courier 12 bold'))
    milkcheck_Label13.place(x=135,y=160)
    milkcheck_text13=Entry(milkcheck_window,width=8,font=('courier 15 bold'),justify="center")
    milkcheck_text13.place(x=20,y=160)
    #  كيوي باللبن 
    milkcheck_Label14=Label(milkcheck_window,text="  توت ",font=('courier 12 bold'))
    milkcheck_Label14.place(x=135,y=205)
    milkcheck_text14=Entry(milkcheck_window,width=8,font=('courier 15 bold'),justify="center")
    milkcheck_text14.place(x=20,y=205)
    #   برتقال فريش 
    milkcheck_Label15=Label(milkcheck_window,text="وايت ابل",font=('courier 12 bold'))
    milkcheck_Label15.place(x=130,y=250)
    milkcheck_text15=Entry(milkcheck_window,width=8,font=('courier 15 bold'),justify="center")
    milkcheck_text15.place(x=20,y=250)
    #   تين شوكي 
    milkcheck_Label16=Label(milkcheck_window,text="تشيز كيك",font=('courier 12 bold'))
    milkcheck_Label16.place(x=130,y=295)
    milkcheck_text16=Entry(milkcheck_window,width=8,font=('courier 15 bold'),justify="center")
    milkcheck_text16.place(x=20,y=295)
    #   ليمون نعناع 
    milkcheck_Label17=Label(milkcheck_window,text="شوكلت كيك",font=('courier 12 bold'))
    milkcheck_Label17.place(x=130,y=340)
    milkcheck_text17=Entry(milkcheck_window,width=8,font=('courier 15 bold'),justify="center")
    milkcheck_text17.place(x=20,y=340)
    #   ليمون لبناني 
    milkcheck_Label18=Label(milkcheck_window,text="اوريو",font=('courier 12 bold'))
    milkcheck_Label18.place(x=130,y=385)
    milkcheck_text18=Entry(milkcheck_window,width=8,font=('courier 15 bold'),justify="center")
    milkcheck_text18.place(x=20,y=385)
    #    بلح ياللبن 
    milkcheck_Label19=Label(milkcheck_window,text="بوريو",font=('courier 12 bold'))
    milkcheck_Label19.place(x=130,y=430)
    milkcheck_text19=Entry(milkcheck_window,width=8,font=('courier 15 bold'),justify="center")
    milkcheck_text19.place(x=20,y=430)
    # كانتالوب
    milkcheck_Label20=Label(milkcheck_window,text="شبه جيد ",font=('courier 12 bold'))
    milkcheck_Label20.place(x=130,y=475)
    milkcheck_text20=Entry(milkcheck_window,width=8,font=('courier 15 bold'),justify="center")
    milkcheck_text20.place(x=20,y=475)

    milkcheck_Label21=Label(milkcheck_window,text="نوتيلا",font=('courier 12 bold'))
    milkcheck_Label21.place(x=130,y=515)
    milkcheck_text21=Entry(milkcheck_window,width=8,font=('courier 15 bold'),justify="center")
    milkcheck_text21.place(x=20,y=515)
    # button to save

    save_button = Button(milkcheck_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_milkcheck)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=200, y=530)
def showdesert():
    desert_window=Toplevel(win)
    desert_window.geometry("600x520")
    desert_window.geometry("+550+50")
    desert_label=Label(desert_window,font=('courier 30 bold'), fg='blue',text=" حلويات")
    desert_label.place(x=200,y=10)
    # مانجو
    desert_Label1=Label(desert_window,text="مولتن كيك",font=('courier 15 bold'))
    desert_Label1.place(x=400,y=70)
    desert_text1=Entry(desert_window,width=8,font=('courier 15 bold'),justify="center")
    desert_text1.place(x=270,y=70)

    # جوافة
    desert_Label2=Label(desert_window,text="اتشيز كيك",font=('courier 15 bold'))
    desert_Label2.place(x=400,y=115)
    desert_text2=Entry(desert_window,width=8,font=('courier 15 bold'),justify="center")
    desert_text2.place(x=270,y=115)
    # فراولة
    desert_Label3=Label(desert_window,text="شوكلت كيك",font=('courier 15 bold'))
    desert_Label3.place(x=400,y=160)
    desert_text3=Entry(desert_window,width=8,font=('courier 15 bold'),justify="center")
    desert_text3.place(x=270,y=160)

    # كيوي
    desert_Label4=Label(desert_window,text="  ريد فل لفيت",font=('courier 15 bold'))
    desert_Label4.place(x=400,y=205)
    desert_text4=Entry(desert_window,width=8,font=('courier 15 bold'),justify="center")
    desert_text4.place(x=270,y=205)
    
    # خوخ
    desert_Label5=Label(desert_window,text="فادج شوكلت",font=('courier 15 bold'))
    desert_Label5.place(x=400,y=250)
    desert_text5=Entry(desert_window,width=8,font=('courier 15 bold'),justify="center")
    desert_text5.place(x=270,y=250)
    # أناناس
    desert_Label6=Label(desert_window,text="كريب نوتيلا",font=('courier 15 bold'))
    desert_Label6.place(x=400,y=295)
    desert_text6=Entry(desert_window,width=8,font=('courier 15 bold'),justify="center")
    desert_text6.place(x=270,y=295)
    # رمان
    desert_Label7=Label(desert_window,text="كريب نوتيلا موز",font=('courier 15 bold'))
    desert_Label7.place(x=400,y=340)
    desert_text7=Entry(desert_window,width=8,font=('courier 15 bold'),justify="center")
    desert_text7.place(x=270,y=340)
    # بطيخ
    desert_Label8=Label(desert_window,text="  أم علي1",font=('courier 15 bold'))
    desert_Label8.place(x=400,y=385)
    desert_text8=Entry(desert_window,width=8,font=('courier 15 bold'),justify="center")
    desert_text8.place(x=270,y=385)
    # ليمون
    desert_Label9=Label(desert_window,text="  أم علي2",font=('courier 15 bold'))
    desert_Label9.place(x=400,y=430)
    desert_text9=Entry(desert_window,width=8,font=('courier 15 bold'),justify="center")
    desert_text9.place(x=270,y=430)
    

    desert_Label11=Label(desert_window,text="أرز باللبن فرن",font=('courier 12 bold'))
    desert_Label11.place(x=135,y=70)
    desert_text11=Entry(desert_window,width=8,font=('courier 15 bold'),justify="center")
    desert_text11.place(x=20,y=70)
    
    # جوافة باللبن
    desert_Label12=Label(desert_window,text="أرز باللبن ",font=('courier 12 bold'))
    desert_Label12.place(x=135,y=115)
    desert_text12=Entry(desert_window,width=8,font=('courier 15 bold'),justify="center")
    desert_text12.place(x=20,y=115)

    #  فراولة باللبن 
    desert_Label13=Label(desert_window,text="جلي",font=('courier 12 bold'))
    desert_Label13.place(x=170,y=160)
    desert_text13=Entry(desert_window,width=8,font=('courier 15 bold'),justify="center")
    desert_text13.place(x=20,y=160)
    #  كيوي باللبن 
    desert_Label14=Label(desert_window,text="  جلي2 ",font=('courier 12 bold'))
    desert_Label14.place(x=160,y=205)
    desert_text14=Entry(desert_window,width=8,font=('courier 15 bold'),justify="center")
    desert_text14.place(x=20,y=205)
    #   برتقال فريش 
    desert_Label15=Label(desert_window,text="فروت سالد ",font=('courier 12 bold'))
    desert_Label15.place(x=130,y=250)
    desert_text15=Entry(desert_window,width=8,font=('courier 15 bold'),justify="center")
    desert_text15.place(x=20,y=250)
    #   تين شوكي 
    desert_Label16=Label(desert_window,text=" طاجن نوتيلا",font=('courier 12 bold'))
    desert_Label16.place(x=130,y=295)
    desert_text16=Entry(desert_window,width=8,font=('courier 15 bold'),justify="center")
    desert_text16.place(x=20,y=295)
    #   ليمون نعناع 
    desert_Label17=Label(desert_window,text=" طاجن 2",font=('courier 12 bold'))
    desert_Label17.place(x=130,y=340)
    desert_text17=Entry(desert_window,width=8,font=('courier 15 bold'),justify="center")
    desert_text17.place(x=20,y=340)
    #   ليمون لبناني 
    desert_Label18=Label(desert_window,text="أب",font=('courier 12 bold'))
    desert_Label18.place(x=160,y=385)
    desert_text18=Entry(desert_window,width=8,font=('courier 15 bold'),justify="center")
    desert_text18.place(x=20,y=385)
    #    بلح ياللبن 
    desert_Label19=Label(desert_window,text="أم علي دير",font=('courier 12 bold'))
    desert_Label19.place(x=130,y=430)
    desert_text19=Entry(desert_window,width=8,font=('courier 15 bold'),justify="center")
    desert_text19.place(x=20,y=430)
   
   
    # button to save

    save_button = Button(desert_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_desert)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=200, y=470)
def showmadness():
    def save_madness():
        pass
    madness_window=Toplevel(win)
    madness_window.geometry("580x280")
    madness_window.geometry("+100+250")
    madness_label=Label(madness_window,font=('courier 30 bold'), fg='blue',text=" مادنس دير ")
    madness_label.place(x=200,y=10)
    # سجق
    madness_Label1=Label(madness_window,text="  تشير مادنس",font=('courier 12 bold'))
    madness_Label1.place(x=390,y=70)
    madness_text1=Entry(madness_window,width=8,font=('courier 15 bold'),justify="center")
    madness_text1.place(x=280,y=70)

    # كريسبي
    madness_Label2=Label(madness_window,text="شوكلت مادنس  ",font=('courier 12 bold'))
    madness_Label2.place(x=390,y=115)
    madness_text2=Entry(madness_window,width=8,font=('courier 15 bold'),justify="center")
    madness_text2.place(x=280,y=115)
    # جمبري
    madness_Label3=Label(madness_window,text="فروت مادنس",font=('courier 12 bold'))
    madness_Label3.place(x=400,y=160)
    madness_text3=Entry(madness_window,width=8,font=('courier 15 bold'),justify="center")
    madness_text3.place(x=280,y=160)

   

 #  هوكري بورجر
    madness_Label11=Label(madness_window,text="اوريو مادنس",font=('courier 12 bold'))
    madness_Label11.place(x=130,y=70)
    madness_text11=Entry(madness_window,width=8,font=('courier 15 bold'),justify="center")
    madness_text11.place(x=20,y=70)
    
    #  فاهيتا فراخ
    madness_Label12=Label(madness_window,text="هوهوز مادنس ",font=('courier 12 bold'))
    madness_Label12.place(x=130,y=115)
    madness_text12=Entry(madness_window,width=8,font=('courier 15 bold'),justify="center")
    madness_text12.place(x=20,y=115)

    #    فاهيتا لحم
    madness_Label13=Label(madness_window,text=" لوتس مادنس",font=('courier 12 bold'))
    madness_Label13.place(x=135,y=160)
    madness_text13=Entry(madness_window,width=8,font=('courier 15 bold'),justify="center")
    madness_text13.place(x=20,y=160)
    #   تشيكن رول 
    madness_Label14=Label(madness_window,text=" مادنس دير",font=('courier 12 bold'))
    madness_Label14.place(x=120,y=205)
    madness_text14=Entry(madness_window,width=8,font=('courier 15 bold'),justify="center")
    madness_text14.place(x=20,y=205)
   

   
    # button to save

    save_button = Button(madness_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_madness)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=260, y=230)
def showwafel():
    def save_wafel():
               # mango
        choclate=choclate_text.get()
        if(choclate !=""):
                    # 
            choclate_num=int(choclate_text.get())
            choclate_price=30
            total1=choclate_num*choclate_price
            print(total1)

                   # farawela
        farawela=farawela_text.get()
        if(farawela !=""):
                    # 
            farawela_num=int(farawela_text.get())
            farawela_price=30
            total1=farawela_num*farawela_price
            print(total1)

                   # karamel
        karamel=karamel_text.get()
        if(karamel !=""):
                    # 
            karamel_num=int(karamel_text.get())
            karamel_price=30
            total1=karamel_num*karamel_price
            print(total1)

                   # asal
        asal=asal_text.get()
        if(asal !=""):
                    # 
            asal_num=int(asal_text.get())
            asal_price=28
            total1=asal_num*asal_price
            print(total1)

                   # notella
        notella=notella_text.get()
        if(notella !=""):
                    # 
            notella_num=int(notella_text.get())
            notella_price=32
            total1=notella_num*notella_price
            print(total1)

                   # notella_banana
        notella_banana=notella_banana_text.get()
        if(notella_banana !=""):
                    # 
            notella_banana_num=int(notella_banana_text.get())
            notella_banana_price=35
            total1=notella_banana_num*notella_banana_price
            print(total1)

                   # notella_farawela
        notella_farawela=notella_farawela_text.get()
        if(notella_farawela !=""):
                    # 
            notella_farawela_num=int(notella_farawela_text.get())
            notella_farawela_price=35
            total1=notella_farawela_num*notella_farawela_price
            print(total1)

                   # fruit
        fruit=fruit_text.get()
        if(fruit !=""):
                    # 
            fruit_num=int(fruit_text.get())
            fruit_price=35
            total1=fruit_num*fruit_price
            print(total1)

                   # deer
        deer=deer_text.get()
        if(deer !=""):
                    # 
            deer_num=int(deer_text.get())
            deer_price=40
            total1=deer_num*deer_price
            print(total1)

    
    wafel_window=Toplevel(win)
    wafel_window.geometry("540x340")
    wafel_window.geometry("+100+250")
    wafel_label=Label(wafel_window,font=('courier 30 bold'), fg='blue',text=" وافل دير")
    wafel_label.place(x=140,y=10)
    # سجق
    choclate_Label=Label(wafel_window,text="وافل شوكلت",font=('courier 12 bold'))
    choclate_Label.place(x=420,y=70)
    choclate_text=Entry(wafel_window,width=8,font=('courier 15 bold'),justify="center")
    choclate_text.place(x=300,y=70)

    # كريسبي
    farawela_Label=Label(wafel_window,text="  وافل فراولة",font=('courier 12 bold'))
    farawela_Label.place(x=400,y=115)
    farawela_text=Entry(wafel_window,width=8,font=('courier 15 bold'),justify="center")
    farawela_text.place(x=300,y=115)
    # جمبري
    karamel_Label=Label(wafel_window,text=" وافل كارميل  ",font=('courier 12 bold'))
    karamel_Label.place(x=400,y=160)
    karamel_text=Entry(wafel_window,width=8,font=('courier 15 bold'),justify="center")
    karamel_text.place(x=300,y=160)

    # شاورما
    asal_Label=Label(wafel_window,text="وافل عسل",font=('courier 12 bold'))
    asal_Label.place(x=430,y=205)
    asal_text=Entry(wafel_window,width=8,font=('courier 15 bold'),justify="center")
    asal_text.place(x=300,y=205)
    
    # بطاطس
    notella_Label=Label(wafel_window,text="وافل نوتيلا",font=('courier 12 bold'))
    notella_Label.place(x=430,y=250)
    notella_text=Entry(wafel_window,width=8,font=('courier 15 bold'),justify="center")
    notella_text.place(x=300,y=250)
    

 #  هوكري بورجر
    notella_banana_Label=Label(wafel_window,text="وافل نوتيلا موز ",font=('courier 12 bold'))
    notella_banana_Label.place(x=130,y=70)
    notella_banana_text=Entry(wafel_window,width=8,font=('courier 15 bold'),justify="center")
    notella_banana_text.place(x=20,y=70)
    
    #  فاهيتا فراخ
    notella_farawela_Label=Label(wafel_window,text=" وافل نوتيلا فراولة",font=('courier 12 bold'))
    notella_farawela_Label.place(x=120,y=115)
    notella_farawela_text=Entry(wafel_window,width=8,font=('courier 15 bold'),justify="center")
    notella_farawela_text.place(x=20,y=115)

    #    فاهيتا لحم
    fruit_Label=Label(wafel_window,text="وافل فواكه ",font=('courier 12 bold'))
    fruit_Label.place(x=150,y=160)
    fruit_text=Entry(wafel_window,width=8,font=('courier 15 bold'),justify="center")
    fruit_text.place(x=20,y=160)

     #    فاهيتا لحم
    deer_Label=Label(wafel_window,text="وافل دير ",font=('courier 12 bold'))
    deer_Label.place(x=150,y=205)
    deer_text=Entry(wafel_window,width=8,font=('courier 15 bold'),justify="center")
    deer_text.place(x=20,y=205)
    
    # button to save

    save_button = Button(wafel_window, text=" حفظ", width=7, font=(
        'arial 12 bold'), fg="white", bg="blue", command=save_wafel)
    save_button.config(height=1,
                        width=10)
    save_button.place(x=220, y=300)
# title:
title = Label(win, font=('courier 30 bold'), fg='blue'

                           , text="مطعم دير  ")

title.place(x=600, y=20)
#---------------------------Buttons -----------------------------------------------


#  region buttons

assaer_button = Button(win, text=" عصائر", width=15, font=(
    'arial 12 bold'), fg="white", bg="green", command=showAssaer)
assaer_button.config(height=2,
                     width=15)
assaer_button.place(x=850, y=100)

#     button2

ice_coffee_button = Button(win, text=" آيس كوفي", width=15, font=(
    'arial 12 bold'), fg="white", bg="green", command=showicecofee)
ice_coffee_button.config(height=2,
                         width=15)
ice_coffee_button.place(x=850, y=170)

#     button3

cooctails_button = Button(win, text=" كوكتيل", width=15, font=(
    'arial 12 bold'), fg="white", bg="green", command=showcooctails)
cooctails_button.config(height=2,
                        width=15)
cooctails_button.place(x=850, y=240)

#     button4

gazzy_drinks_button = Button(win, text=" مشروبات غازية", width=15, font=(
    'arial 12 bold'), fg="white", bg="green", command=showgazzy_drinks)
gazzy_drinks_button.config(height=2,
                           width=15)
gazzy_drinks_button.place(x=850, y=310)

#     button5

herbs_button = Button(win, text=" أعشاب", width=15, font=(
    'arial 12 bold'), fg="white", bg="green", command=showherbs)
herbs_button.config(height=2,
                    width=15)
herbs_button.place(x=850, y=380)

#     button6

hot_chocolate_button = Button(win, text=" هوت شوكليت", width=15, font=(
    'arial 12 bold'), fg="white", bg="green", command=showhotchoclate)
hot_chocolate_button.config(height=2,
                            width=15)
hot_chocolate_button.place(x=850, y=450)

#     button7

hot_drinks_button = Button(win, text=" مشروبات  ساخنة", width=15, font=(
    'arial 12 bold'), fg="white", bg="green", command=showhot_drinks)
hot_drinks_button.config(height=2,
                         width=15)
hot_drinks_button.place(x=850, y=520)

#     button8

milk_check_button = Button(win, text=" ميلك تشيك", width=15, font=(
    'arial 12 bold'), fg="white", bg="green", command=showmilkcheck)
milk_check_button.config(height=2,
                         width=15)
milk_check_button.place(x=850, y=590)

#  center side
#     button9

capachino_button=Button(win,text="  كابتشينو",width=15,font=('arial 12 bold'),fg="white",bg="green",command=showcapachino)
capachino_button.config(height=2, 
			  width=15)
capachino_button.place(x=600,y=100)

#     button10

soda_button=Button(win,text=" كوكتيل صودا",width=15,font=('arial 12 bold'),fg="white",bg="green",command=showsoda_cooctail)
soda_button.config(height=2, 
			  width=15)
soda_button.place(x=600,y=170)



#     button 11


soupes_button=Button(win,text=" شربة",width=15,font=('arial 12 bold'),fg="white",bg="green",command=show_soupes)
soupes_button.config(height=2, 
			  width=15)
soupes_button.place(x=600,y=240)
# Button 12

zabbady_button=Button(win,text=" زبادي",width=15,font=('arial 12 bold'),fg="white",bg="green",command=showzabbady)
zabbady_button.config(height=2, 
			  width=15)
zabbady_button.place(x=600,y=310)
# Button 13

avocado_button=Button(win,text=" أفوكادو",width=15,font=('arial 12 bold'),fg="white",bg="green",command=showavocado)
avocado_button.config(height=2, 
			  width=15)
avocado_button.place(x=600,y=380)

#     button14

icecream_button=Button(win,text=" آيس كريم ",width=15,font=('arial 12 bold'),fg="white",bg="green",command=show_icecream)
icecream_button.config(height=2, 
			  width=15)
icecream_button.place(x=600,y=450)

#     button15

crippes_button=Button(win,text=" كريبات",width=15,font=('arial 12 bold'),fg="white",bg="green",command=showcrippes)
crippes_button.config(height=2, 
			  width=15)
crippes_button.place(x=600,y=520)

#     button16

desert_button=Button(win,text=" حلويات",width=15,font=('arial 12 bold'),fg="white",bg="green",command=showdesert)
desert_button.config(height=2, 
			  width=15)
desert_button.place(x=600,y=590)
# center2

#     button17

meals_button=Button(win,text=" وجبات",width=15,font=('arial 12 bold'),fg="white",bg="green",command=showmeals)
meals_button.config(height=2, 
			  width=15)
meals_button.place(x=350,y=100)

# button 18
breakfast_button=Button(win,text="  وجبات افطار",width=15,font=('arial 12 bold'),fg="white",bg="green",command=show_breakfast)
breakfast_button.config(height=2, 
			  width=15)
breakfast_button.place(x=350,y=170)



#     button19

children_meals_button=Button(win,text=" وجبات أطفال",width=15,font=('arial 12 bold'),fg="white",bg="green",command=show_child_meals)
children_meals_button.config(height=2, 
			  width=15)
children_meals_button.place(x=350,y=240)
#     button 20

extra_button=Button(win,text=" اكسترا",width=15,font=('arial 12 bold'),fg="white",bg="green",command=showextra)
extra_button.config(height=2, 
			  width=15)
extra_button.place(x=350,y=310)

#     button21

zabbady_button=Button(win,text=" زبادي",width=15,font=('arial 12 bold'),fg="white",bg="green",command=showzabbady)
zabbady_button.config(height=2, 
			  width=15)
zabbady_button.place(x=350,y=380)


#     button 22

ice_cream_button=Button(win,text="  ",width=15,font=('arial 12 bold'),fg="white",bg="green")
ice_cream_button.config(height=2, 
			  width=15)
ice_cream_button.place(x=350,y=450)


#     button23

macarona_button=Button(win,text=" مكرونة",width=15,font=('arial 12 bold'),fg="white",bg="green",command=showmacarona)
macarona_button.config(height=2, 
			  width=15)
macarona_button.place(x=350,y=520)


#     button24

madness_button=Button(win,text=" مادنس دير",width=15,font=('arial 12 bold'),fg="white",bg="green",command=showmadness)
madness_button.config(height=2, 
			  width=15)
madness_button.place(x=350,y=590)

# left side

#     button25

moqablat_button=Button(win,text=" مقبلات",width=15,font=('arial 12 bold'),fg="white",bg="green",command=showmoqablat)
moqablat_button.config(height=2, 
			  width=15)
moqablat_button.place(x=100,y=100)

#     button26

rizo_button=Button(win,text=" ريزو",width=15,font=('arial 12 bold'),fg="white",bg="green",command=show_rizo)
rizo_button.config(height=2, 
			  width=15)
rizo_button.place(x=100,y=170)

#     button27

salades_button=Button(win,text=" سلطات",width=15,font=('arial 12 bold'),fg="white",bg="green",command=show_salades)
salades_button.config(height=2, 
			  width=15)
salades_button.place(x=100,y=240)

#     button28

sandwishes_button=Button(win,text=" سندوتشات",width=15,font=('arial 12 bold'),fg="white",bg="green",command=showsandwishes)
sandwishes_button.config(height=2, 
			  width=15)
sandwishes_button.place(x=100,y=310)


#     button29

smoozy_button=Button(win,text=" سموزي",width=15,font=('arial 12 bold'),fg="white",bg="green",command=showsmoozy)
smoozy_button.config(height=2, 
			  width=15)
smoozy_button.place(x=100,y=380)

#     button30

shawrma_button=Button(win,text=" شاورما",width=15,font=('arial 12 bold'),fg="white",bg="green",command=showshawrma)
shawrma_button.config(height=2, 
			  width=15)
shawrma_button.place(x=100,y=450)

#     button31

spresso_button=Button(win,text=" اسبريسو",width=15,font=('arial 12 bold'),fg="white",bg="green",command=showspresso)
spresso_button.config(height=2, 
			  width=15)
spresso_button.place(x=100,y=520)

#     button32ff

wafel_button=Button(win,text=" وافل دير",width=15,font=('arial 12 bold'),fg="white",bg="green",command=showwafel)
wafel_button.config(height=2, 
			  width=15)
wafel_button.place(x=100,y=590)

# endregion buttons

add_recipt_button=Button(win,text=" فاتورة جديدة ",width=15,font=('arial 12 bold'),fg="white",bg="red",command=add_fatora)
add_recipt_button.config(height=2, 
			  width=15)
add_recipt_button.place(x=1100,y=300)

def save_recipt_():
        dd=cur.execute("SELECT recipt_number FROM recipts WHERE num=(SELECT MAX(num) FROM recipts)")
        results2=cur.fetchall()
        rec_num=results2[0]
        rec_num=rec_num[0]
        recipt_info="select * from recipt_contents where recipt_number=?"
        cur.execute(recipt_info,(rec_num,))
        all_recipt_info=cur.fetchall()
        print(all_recipt_info)
        total="select sum(total) from recipt_contents where recipt_number=?"
        cur.execute(total,(rec_num,))
        all_total=cur.fetchall()
        all_total=all_total[0]
        print(all_total)
        file_location='F:/'+str(rec_num)+'.doc'
        file=open(file_location, 'w')

        file.write('\t\tمطعم دير')
        file.write('\n')

        file.write('\t\tطربيزة رقم')
        file.write(table_number_combobox.get())
        file.write('\n\n')

        file.write('مجموع سعر عدد الصنف ')
        file.write('\n\n')
        for i in all_recipt_info:

            file.write(str(i[4]))
            file.write('\t')
            file.write(" ")
            file.write(" ")



            file.write(str(i[3]))
            file.write(" ")
            file.write(" ")



            file.write(str(i[2]))
            file.write(" ")
            file.write(" ")

            

            
            file.write(str(i[1]))
            

            file.write('\n')
        file.write('\t\t الاجمالي')
        file.write(str(all_total[0]))

        
        save_recipt=Button(new_window,width=20,text="حفظ فاتورة",fg="white",bg="blue",command=save_recipt_)
        save_recipt.place(x=20,y=60)

    
    # ------------------------------------classes of restaurant------------------------
    #       1 desert
    #        design
        desert_label= Label(new_window, font=('arial 20 bold'), fg='steelblue',text="حلويات  ")
        desert_label.place(x=90,y=130)
        desert_var = tk.StringVar()
        desert_combobox = ttk.Combobox(new_window, textvariable=desert_var,width=15,font=15,background="steelblue")
        desert_combobox.place(x=50,y=190)
        desert_entry= Entry(new_window, width=10, fg='steelblue',font="arial 15 bold")

        desert_entry.place(x=250,y=190)

def handle_desert():
    quantity=desert_entry.get()
    if quantity=="":
        showerror('خطأ','ادخل رقم')
    quantity2=int(quantity)
    x="select name , price from desert where name= ?"
    xx=(desert_combobox.get(),)
    cur.execute(x,xx)
    results=cur.fetchall()
    results_to_tuple=tuple(results)
    #  tuple of tuple to list
    elements=[element for tupl in results_to_tuple for element in tupl]
    price=int(elements[1])
    name=elements[0]
    elements.append(quantity2)
    total=quantity2*price
    elements.append(total)

    dd=cur.execute("SELECT recipt_number FROM recipts WHERE num=(SELECT MAX(num) FROM recipts)")
    results2=cur.fetchall()
    rec_num=results2[0]
    rec_num=rec_num[0]
    elements.append(rec_num)
    cur.execute("insert into recipt_contents(recipt_number,price,quantity,class,total) values(?,?,?,?,?)",(rec_num,price,quantity2,name,total,))
    conn.commit()
        
    desert_button=Button(new_window,width=15,text="اضافة",fg="white",bg="blue",command=handle_desert)
    desert_button.place(x=370,y=190)


    # database

    cur.execute("select name from desert order by name asc")
    all_desert=cur.fetchall()
    # list of tuple to tuple of tuple
    all_desert=tuple(all_desert)
    #  tuple of tuple to list
    elements=[element for tupl in all_desert for element in tupl]
    # list to tuple
    e=tuple(elements)
    desert_combobox['values']=e


    # ------------------------------------classes of restaurant------------------------
    #       2 wafel_deer
    #        design
    wafel_deer_label= Label(new_window, font=('arial 20 bold'), fg='steelblue',text="وافل دير  ")
    wafel_deer_label.place(x=550,y=130)
    wafel_deer_var = tk.StringVar()
    wafel_deer_combobox = ttk.Combobox(new_window, textvariable=wafel_deer_var,width=15,font=15,background="steelblue")
    wafel_deer_combobox.place(x=500,y=190)
    wafel_deer_entry= Entry(new_window, width=10, fg='steelblue',font="arial 15 bold")

    wafel_deer_entry.place(x=700,y=190)

    def handle_wafel_deer():
         quantity=wafel_deer_entry.get()
         if quantity=="":
             showerror('خطأ','ادخل رقم')
         quantity2=int(quantity)
         x="select name , price from wafel_deer where name= ?"
         xx=(wafel_deer_combobox.get(),)
         cur.execute(x,xx)
         results=cur.fetchall()
         results_to_tuple=tuple(results)
         #  tuple of tuple to list
         elements=[element for tupl in results_to_tuple for element in tupl]
         price=int(elements[1])
         name=elements[0]
         elements.append(quantity2)
         total=quantity2*price
         elements.append(total)

         dd=cur.execute("SELECT recipt_number FROM recipts WHERE num=(SELECT MAX(num) FROM recipts)")
         results2=cur.fetchall()
         rec_num=results2[0]
         rec_num=rec_num[0]
         elements.append(rec_num)
         cur.execute("insert into recipt_contents(recipt_number,price,quantity,class,total) values(?,?,?,?,?)",(rec_num,price,quantity2,name,total,))
         conn.commit()
                
    wafel_deer_button=Button(new_window,width=15,text="اضافة",fg="white",bg="blue",command=handle_wafel_deer)
    wafel_deer_button.place(x=820,y=190)


    # database


    cur.execute("select name from wafel_deer order by name asc")
    all_wafel_deer=cur.fetchall()
    # list of tuple to tuple of tuple
    all_wafel_deer=tuple(all_wafel_deer)
    #  tuple of tuple to list
    elements=[element for tupl in all_wafel_deer for element in tupl]
    # list to tuple
    e=tuple(elements)
    wafel_deer_combobox['values']=e



    # ------------------------------------classes of restaurant------------------------
    #       3 capatchino
    #        design
    capatchino_label= Label(new_window, font=('arial 20 bold'), fg='steelblue',text=" كابتشينو ")
    capatchino_label.place(x=90,y=230)
    capatchino_var = tk.StringVar()
    capatchino_combobox = ttk.Combobox(new_window, textvariable=capatchino_var,width=15,font=15,background="steelblue")
    capatchino_combobox.place(x=50,y=270)
    capatchino_entry= Entry(new_window, width=10, fg='steelblue',font="arial 15 bold")
    capatchino_entry.place(x=250,y=270)

    def handle_capatchino():
         quantity=capatchino_entry.get()
         if quantity=="":
             showerror('خطأ','ادخل رقم')
         quantity2=int(quantity)
         x="select name , price from capatchino where name= ?"
         xx=(capatchino_combobox.get(),)
         cur.execute(x,xx)
         results=cur.fetchall()
         results_to_tuple=tuple(results)
         #  tuple of tuple to list
         elements=[element for tupl in results_to_tuple for element in tupl]
         price=int(elements[1])
         name=elements[0]
         elements.append(quantity2)
         total=quantity2*price
         elements.append(total)

         dd=cur.execute("SELECT recipt_number FROM recipts WHERE num=(SELECT MAX(num) FROM recipts)")
         results2=cur.fetchall()
         rec_num=results2[0]
         rec_num=rec_num[0]
         elements.append(rec_num)
         cur.execute("insert into recipt_contents(recipt_number,price,quantity,class,total) values(?,?,?,?,?)",(rec_num,price,quantity2,name,total,))
         conn.commit()
                
    capatchino_button=Button(new_window,width=15,text="اضافة",fg="white",bg="blue",command=handle_capatchino)
    capatchino_button.place(x=370,y=270)


    # database

    cur.execute("select name from capatchino order by name asc")
    all_capatchino=cur.fetchall()
    # list of tuple to tuple of tuple
    all_capatchino=tuple(all_capatchino)
    #  tuple of tuple to list
    elements=[element for tupl in all_capatchino for element in tupl]
    # list to tuple
    e=tuple(elements)
    capatchino_combobox['values']=e


    # ------------------------------------classes of restaurant------------------------
    #       4 zabbady
    #        design
    zabbady_label= Label(new_window, font=('arial 20 bold'), fg='steelblue',text="زبادي ")
    zabbady_label.place(x=550,y=230)
    zabbady_var = tk.StringVar()
    zabbady_combobox = ttk.Combobox(new_window, textvariable=zabbady_var,width=15,font=15,background="steelblue")
    zabbady_combobox.place(x=500,y=270)
    zabbady_entry= Entry(new_window, width=10, fg='steelblue',font="arial 15 bold")
    zabbady_entry.place(x=700,y=270)
    def handle_zabbady():
         quantity=zabbady_entry.get()
         if quantity=="":
             showerror('خطأ','ادخل رقم')
         quantity2=int(quantity)
         x="select name , price from zabbady where name= ?"
         xx=(zabbady_combobox.get(),)
         cur.execute(x,xx)
         results=cur.fetchall()
         results_to_tuple=tuple(results)
         #  tuple of tuple to list
         elements=[element for tupl in results_to_tuple for element in tupl]
         price=int(elements[1])
         name=elements[0]
         elements.append(quantity2)
         total=quantity2*price
         elements.append(total)

         dd=cur.execute("SELECT recipt_number FROM recipts WHERE num=(SELECT MAX(num) FROM recipts)")
         results2=cur.fetchall()
         rec_num=results2[0]
         rec_num=rec_num[0]
         elements.append(rec_num)
         cur.execute("insert into recipt_contents(recipt_number,price,quantity,class,total) values(?,?,?,?,?)",(rec_num,price,quantity2,name,total,))
         conn.commit()
                
    zabbady_button=Button(new_window,width=15,text="اضافة",fg="white",bg="blue",command=handle_zabbady)
    zabbady_button.place(x=820,y=270)


    # database


    cur.execute("select name from zabbady order by name asc")
    all_zabbady=cur.fetchall()
    # list of tuple to tuple of tuple
    all_zabbady=tuple(all_zabbady)
    #  tuple of tuple to list
    elements=[element for tupl in all_zabbady for element in tupl]
    # list to tuple
    e=tuple(elements)
    zabbady_combobox['values']=e


    # ------------------------------------classes of restaurant------------------------
    #       5 eat_meals_children
    #        design
    eat_meals_children_label= Label(new_window, font=('arial 20 bold'), fg='steelblue',text=" وجبات أطفال ")
    eat_meals_children_label.place(x=90,y=330)
    eat_meals_children_var = tk.StringVar()
    eat_meals_children_combobox = ttk.Combobox(new_window, textvariable=eat_meals_children_var,width=15,font=15,background="steelblue")
    eat_meals_children_combobox.place(x=50,y=370)
    eat_meals_children_entry= Entry(new_window, width=10, fg='steelblue',font="arial 15 bold")
    eat_meals_children_entry.place(x=250,y=370)


    def handle_eat_meals_children():
         quantity=eat_meals_children_entry.get()
         if quantity=="":
             showerror('خطأ','ادخل رقم')
         quantity2=int(quantity)
         x="select name , price from eat_meals_childern where name= ?"
         xx=(eat_meals_children_combobox.get(),)
         cur.execute(x,xx)
         results=cur.fetchall()
         results_to_tuple=tuple(results)
         #  tuple of tuple to list
         elements=[element for tupl in results_to_tuple for element in tupl]
         price=int(elements[1])
         name=elements[0]
         elements.append(quantity2)
         total=quantity2*price
         elements.append(total)

         dd=cur.execute("SELECT recipt_number FROM recipts WHERE num=(SELECT MAX(num) FROM recipts)")
         results2=cur.fetchall()
         rec_num=results2[0]
         rec_num=rec_num[0]
         elements.append(rec_num)
         cur.execute("insert into recipt_contents(recipt_number,price,quantity,class,total) values(?,?,?,?,?)",(rec_num,price,quantity2,name,total,))
         conn.commit()
     
    eat_meals_children_button=Button(new_window,width=15,text="اضافة",fg="white",bg="blue",command=handle_eat_meals_children)
    eat_meals_children_button.place(x=370,y=370)


    # database

    cur.execute("select name from madness_deer order by name asc")
    all_eat_meals_children=cur.fetchall()
    # list of tuple to tuple of tuple
    all_eat_meals_children=tuple(all_eat_meals_children)
    #  tuple of tuple to list
    elements=[element for tupl in all_eat_meals_children for element in tupl]
    # list to tuple
    e=tuple(elements)
    eat_meals_children_combobox['values']=e


    # ------------------------------------classes of restaurant------------------------
    #       6 eat_meals
    #        design
    eat_meals_label= Label(new_window, font=('arial 20 bold'), fg='steelblue',text=" وجبات ")
    eat_meals_label.place(x=550,y=330)
    eat_meals_var = tk.StringVar()
    eat_meals_combobox = ttk.Combobox(new_window, textvariable=eat_meals_var,width=15,font=15,background="steelblue")
    eat_meals_combobox.place(x=500,y=370)
    eat_meals_entry= Entry(new_window, width=10, fg='steelblue',font="arial 15 bold")
    eat_meals_entry.place(x=700,y=370)
    def handle_eat_meals():
         quantity=eat_meals_entry.get()
         if quantity=="":
             showerror('خطأ','ادخل رقم')
         quantity2=int(quantity)
         x="select name , price from eat_meals where name= ?"
         xx=(eat_meals_combobox.get(),)
         cur.execute(x,xx)
         results=cur.fetchall()
         results_to_tuple=tuple(results)
         #  tuple of tuple to list
         elements=[element for tupl in results_to_tuple for element in tupl]
         price=int(elements[1])
         name=elements[0]
         elements.append(quantity2)
         total=quantity2*price
         elements.append(total)

         dd=cur.execute("SELECT recipt_number FROM recipts WHERE num=(SELECT MAX(num) FROM recipts)")
         results2=cur.fetchall()
         rec_num=results2[0]
         rec_num=rec_num[0]
         elements.append(rec_num)
         cur.execute("insert into recipt_contents(recipt_number,price,quantity,class,total) values(?,?,?,?,?)",(rec_num,price,quantity2,name,total,))
         conn.commit()
     
    eat_meals_button=Button(new_window,width=15,text="اضافة",fg="white",bg="blue",command=handle_eat_meals)
    eat_meals_button.place(x=820,y=370)


    # database


    cur.execute("select name from eat_meals order by name asc")
    all_eat_meals=cur.fetchall()
    # list of tuple to tuple of tuple
    all_eat_meals=tuple(all_eat_meals)
    #  tuple of tuple to list
    elements=[element for tupl in all_eat_meals for element in tupl]
    # list to tuple
    e=tuple(elements)
    eat_meals_combobox['values']=e


    # ------------------------------------classes of restaurant------------------------
    #       7 shawrma
    #        design
    shawrma_label= Label(new_window, font=('arial 20 bold'), fg='steelblue',text="شاورما ")
    shawrma_label.place(x=90,y=430)
    shawrma_var = tk.StringVar()
    shawrma_combobox = ttk.Combobox(new_window, textvariable=shawrma_var,width=15,font=15,background="steelblue")
    shawrma_combobox.place(x=50,y=470)
    shawrma_entry= Entry(new_window, width=10, fg='steelblue',font="arial 15 bold")
    shawrma_entry.place(x=250,y=470)
    def handle_shawrma():
         quantity=shawrma_entry.get()
         if quantity=="":
             showerror('خطأ','ادخل رقم')
         quantity2=int(quantity)
         x="select name , price from shawrma where name= ?"
         xx=(shawrma_combobox.get(),)
         cur.execute(x,xx)
         results=cur.fetchall()
         results_to_tuple=tuple(results)
         #  tuple of tuple to list
         elements=[element for tupl in results_to_tuple for element in tupl]
         price=int(elements[1])
         name=elements[0]
         elements.append(quantity2)
         total=quantity2*price
         elements.append(total)

         dd=cur.execute("SELECT recipt_number FROM recipts WHERE num=(SELECT MAX(num) FROM recipts)")
         results2=cur.fetchall()
         rec_num=results2[0]
         rec_num=rec_num[0]
         elements.append(rec_num)
         cur.execute("insert into recipt_contents(recipt_number,price,quantity,class,total) values(?,?,?,?,?)",(rec_num,price,quantity2,name,total,))
         conn.commit()
     
    shawrma_button=Button(new_window,width=15,text="اضافة",fg="white",bg="blue",command=handle_shawrma)
    shawrma_button.place(x=370,y=470)


    # database

    cur.execute("select name from shawrma order by name asc")
    all_shawrma=cur.fetchall()
    # list of tuple to tuple of tuple
    all_shawrma=tuple(all_shawrma)
    #  tuple of tuple to list
    elements=[element for tupl in all_shawrma for element in tupl]
    # list to tuple
    e=tuple(elements)
    shawrma_combobox['values']=e


    # ------------------------------------classes of restaurant------------------------
    #       8 soda_coctails
    #        design
    soda_coctails_label= Label(new_window, font=('arial 20 bold'), fg='steelblue',text=" صودا كوكتيل ")
    soda_coctails_label.place(x=550,y=430)
    soda_coctails_var = tk.StringVar()
    soda_coctails_combobox = ttk.Combobox(new_window, textvariable=soda_coctails_var,width=15,font=15,background="steelblue")
    soda_coctails_combobox.place(x=500,y=470)
    soda_coctails_entry= Entry(new_window, width=10, fg='steelblue',font="arial 15 bold")
    def handle_soda_coctails():
         quantity=soda_coctails_entry.get()
         if quantity=="":
             showerror('خطأ','ادخل رقم')
         quantity2=int(quantity)
         x="select name , price from soda_coctails where name= ?"
         xx=(soda_coctails_combobox.get(),)
         cur.execute(x,xx)
         results=cur.fetchall()
         results_to_tuple=tuple(results)
         #  tuple of tuple to list
         elements=[element for tupl in results_to_tuple for element in tupl]
         price=int(elements[1])
         name=elements[0]
         elements.append(quantity2)
         total=quantity2*price
         elements.append(total)

         dd=cur.execute("SELECT recipt_number FROM recipts WHERE num=(SELECT MAX(num) FROM recipts)")
         results2=cur.fetchall()
         rec_num=results2[0]
         rec_num=rec_num[0]
         elements.append(rec_num)
         cur.execute("insert into recipt_contents(recipt_number,price,quantity,class,total) values(?,?,?,?,?)",(rec_num,price,quantity2,name,total,))
         conn.commit()
     
    soda_coctails_entry.place(x=700,y=470)
    soda_coctails_button=Button(new_window,width=15,text="اضافة",fg="white",bg="blue",command=handle_soda_coctails)
    soda_coctails_button.place(x=820,y=470)


    # database


    cur.execute("select name from soda_coctails order by name asc")
    all_soda_coctails=cur.fetchall()
    # list of tuple to tuple of tuple
    all_soda_coctails=tuple(all_soda_coctails)
    #  tuple of tuple to list
    elements=[element for tupl in all_soda_coctails for element in tupl]
    # list to tuple
    e=tuple(elements)
    soda_coctails_combobox['values']=e


    # ------------------------------------classes of restaurant------------------------
    #       9 soupes
    #        design
    soupes_label= Label(new_window, font=('arial 20 bold'), fg='steelblue',text="شوربة ")
    soupes_label.place(x=90,y=530)
    soupes_var = tk.StringVar()
    soupes_combobox = ttk.Combobox(new_window, textvariable=soupes_var,width=15,font=15,background="steelblue")
    soupes_combobox.place(x=50,y=570)
    soupes_entry= Entry(new_window, width=10, fg='steelblue',font="arial 15 bold")
    soupes_entry.place(x=250,y=570)
    def handle_soupes():
         quantity=soupes_entry.get()
         if quantity=="":
             showerror('خطأ','ادخل رقم')
         quantity2=int(quantity)
         x="select name , price from soupes where name= ?"
         xx=(soupes_combobox.get(),)
         cur.execute(x,xx)
         results=cur.fetchall()
         results_to_tuple=tuple(results)
         #  tuple of tuple to list
         elements=[element for tupl in results_to_tuple for element in tupl]
         price=int(elements[1])
         
         name=elements[0]
         elements.append(quantity2)
         total=quantity2*price
         elements.append(total)

         dd=cur.execute("SELECT recipt_number FROM recipts WHERE num=(SELECT MAX(num) FROM recipts)")
         results2=cur.fetchall()
         rec_num=results2[0]
         rec_num=rec_num[0]
         elements.append(rec_num)
         cur.execute("insert into recipt_contents(recipt_number,price,quantity,class,total) values(?,?,?,?,?)",(rec_num,price,quantity2,name,total,))
         conn.commit()
     
    soupes_button=Button(new_window,width=15,text="اضافة",fg="white",bg="blue",command=handle_soupes)
    soupes_button.place(x=370,y=570)


    # database

    cur.execute("select name from soupes order by name asc")
    all_soupes=cur.fetchall()
    # list of tuple to tuple of tuple
    all_soupes=tuple(all_soupes)
    #  tuple of tuple to list
    elements=[element for tupl in all_soupes for element in tupl]
    # list to tuple
    e=tuple(elements)
    soupes_combobox['values']=e


    # ------------------------------------classes of restaurant------------------------
    #       10 spresso
    #        design
    spresso_label= Label(new_window, font=('arial 20 bold'), fg='steelblue',text="اسبريسو  ")
    spresso_label.place(x=550,y=530)
    spresso_var = tk.StringVar()
    spresso_combobox = ttk.Combobox(new_window, textvariable=spresso_var,width=15,font=15,background="steelblue")
    spresso_combobox.place(x=500,y=570)
    spresso_entry= Entry(new_window, width=10, fg='steelblue',font="arial 15 bold")
    spresso_entry.place(x=700,y=570)
    def handle_spresso():
         quantity=spresso_entry.get()
         if quantity=="":
             showerror('خطأ','ادخل رقم')
         quantity2=int(quantity)
         x="select name , price from spresso where name= ?"
         xx=(spresso_combobox.get(),)
         cur.execute(x,xx)
         results=cur.fetchall()
         results_to_tuple=tuple(results)
         #  tuple of tuple to list
         elements=[element for tupl in results_to_tuple for element in tupl]
         price=int(elements[1])
         name=elements[0]
         elements.append(quantity2)
         total=quantity2*price
         elements.append(total)

         dd=cur.execute("SELECT recipt_number FROM recipts WHERE num=(SELECT MAX(num) FROM recipts)")
         results2=cur.fetchall()
         rec_num=results2[0]
         rec_num=rec_num[0]
         elements.append(rec_num)
         cur.execute("insert into recipt_contents(recipt_number,price,quantity,class,total) values(?,?,?,?,?)",(rec_num,price,quantity2,name,total,))
         conn.commit()
     
    spresso_button=Button(new_window,width=15,text="اضافة",fg="white",bg="blue",command=handle_spresso)
    spresso_button.place(x=820,y=570)


    # database

    cur.execute("select name from spresso order by name asc")
    all_spresso=cur.fetchall()
    # list of tuple to tuple of tuple
    all_spresso=tuple(all_spresso)
    #  tuple of tuple to list
    elements=[element for tupl in all_spresso for element in tupl]
    # list to tuple
    e=tuple(elements)
    spresso_combobox['values']=e
   

        

















    hot_drinks_entry.place(x=250,y=190)
    def handle_hot_drinks():
         quantity=hot_drinks_entry.get()
         if quantity=="":
             showerror('خطأ','ادخل رقم')
         quantity2=int(quantity)
         x="select name , price from hot_drinks where name= ?"
         xx=(hot_drinks_combobox.get(),)
         cur.execute(x,xx)
         results=cur.fetchall()
         results_to_tuple=tuple(results)
         #  tuple of tuple to list
         elements=[element for tupl in results_to_tuple for element in tupl]
         price=int(elements[1])
         name=elements[0]
         elements.append(quantity2)
         total=quantity2*price
         elements.append(total)

         dd=cur.execute("SELECT recipt_number FROM recipts WHERE num=(SELECT MAX(num) FROM recipts)")
         results2=cur.fetchall()
         rec_num=results2[0]
         rec_num=rec_num[0]
         elements.append(rec_num)
         cur.execute("insert into recipt_contents(recipt_number,price,quantity,class,total) values(?,?,?,?,?)",(rec_num,price,quantity2,name,total,))
         conn.commit()
     
    hot_drinks_button=Button(new_window,width=15,text="اضافة",fg="white",bg="blue",command=handle_hot_drinks)
    hot_drinks_button.place(x=370,y=190)


    # database

    cur.execute("select name from hot_drinks order by name asc")
    all_hot_drinks=cur.fetchall()
    # list of tuple to tuple of tuple
    all_hot_drinks=tuple(all_hot_drinks)
    #  tuple of tuple to list
    elements=[element for tupl in all_hot_drinks for element in tupl]
    # list to tuple
    e=tuple(elements)
    hot_drinks_combobox['values']=e


    # ------------------------------------classes of restaurant------------------------
    #       2 ice_coffe
    #        design
    ice_coffe_label= Label(new_window, font=('arial 20 bold'), fg='steelblue',text="آيس كوفي ")
    ice_coffe_label.place(x=550,y=130)
    ice_coffe_var = tk.StringVar()
    ice_coffe_combobox = ttk.Combobox(new_window, textvariable=ice_coffe_var,width=15,font=15,background="steelblue")
    ice_coffe_combobox.place(x=500,y=190)
    ice_coffe_entry= Entry(new_window, width=10, fg='steelblue',font="arial 15 bold")
    ice_coffe_entry.place(x=700,y=190)
    def handle_ice_coffe():
         quantity=ice_coffe_entry.get()
         if quantity=="":
             showerror('خطأ','ادخل رقم')
         quantity2=int(quantity)
         x="select name , price from ice_coffe where name= ?"
         xx=(ice_coffe_combobox.get(),)
         cur.execute(x,xx)
         results=cur.fetchall()
         results_to_tuple=tuple(results)
         #  tuple of tuple to list
         elements=[element for tupl in results_to_tuple for element in tupl]
         price=int(elements[1])
         name=elements[0]
         elements.append(quantity2)
         total=quantity2*price
         elements.append(total)

         dd=cur.execute("SELECT recipt_number FROM recipts WHERE num=(SELECT MAX(num) FROM recipts)")
         results2=cur.fetchall()
         rec_num=results2[0]
         rec_num=rec_num[0]
         elements.append(rec_num)
         cur.execute("insert into recipt_contents(recipt_number,price,quantity,class,total) values(?,?,?,?,?)",(rec_num,price,quantity2,name,total,))
         conn.commit()
     
    ice_coffe_button=Button(new_window,width=15,text="اضافة",fg="white",bg="blue",command=handle_ice_coffe)
    ice_coffe_button.place(x=820,y=190)


    # database


    cur.execute("select name from ice_coffe order by name asc")
    all_ice_coffe=cur.fetchall()
    # list of tuple to tuple of tuple
    all_ice_coffe=tuple(all_ice_coffe)
    #  tuple of tuple to list
    elements=[element for tupl in all_ice_coffe for element in tupl]
    # list to tuple
    e=tuple(elements)
    ice_coffe_combobox['values']=e



    # ------------------------------------classes of restaurant------------------------
    #       3 ice_cream
    #        design
    ice_cream_label= Label(new_window, font=('arial 20 bold'), fg='steelblue',text="آيس كريم ")
    ice_cream_label.place(x=90,y=230)
    ice_cream_var = tk.StringVar()
    ice_cream_combobox = ttk.Combobox(new_window, textvariable=ice_cream_var,width=15,font=15,background="steelblue")
    ice_cream_combobox.place(x=50,y=270)
    ice_cream_entry= Entry(new_window, width=10, fg='steelblue',font="arial 15 bold")
    ice_cream_entry.place(x=250,y=270)
    def handle_ice_cream():
         quantity=ice_cream_entry.get()
         if quantity=="":
             showerror('خطأ','ادخل رقم')
         quantity2=int(quantity)
         x="select name , price from ice_cream where name= ?"
         xx=(ice_cream_combobox.get(),)
         cur.execute(x,xx)
         results=cur.fetchall()
         results_to_tuple=tuple(results)
         #  tuple of tuple to list
         elements=[element for tupl in results_to_tuple for element in tupl]
         price=int(elements[1])
         name=elements[0]
         elements.append(quantity2)
         total=quantity2*price
         elements.append(total)

         dd=cur.execute("SELECT recipt_number FROM recipts WHERE num=(SELECT MAX(num) FROM recipts)")
         results2=cur.fetchall()
         rec_num=results2[0]
         rec_num=rec_num[0]
         elements.append(rec_num)
         cur.execute("insert into recipt_contents(recipt_number,price,quantity,class,total) values(?,?,?,?,?)",(rec_num,price,quantity2,name,total,))
         conn.commit()
     
    ice_cream_button=Button(new_window,width=15,text="اضافة",fg="white",bg="blue",command=handle_ice_cream)
    ice_cream_button.place(x=370,y=270)


    # database

    cur.execute("select name from ice_cream order by name asc")
    all_ice_cream=cur.fetchall()
    # list of tuple to tuple of tuple
    all_ice_cream=tuple(all_ice_cream)
    #  tuple of tuple to list
    elements=[element for tupl in all_ice_cream for element in tupl]
    # list to tuple
    e=tuple(elements)
    ice_cream_combobox['values']=e


    # ------------------------------------classes of restaurant------------------------
    #       4 macarona
    #        design
    macarona_label= Label(new_window, font=('arial 20 bold'), fg='steelblue',text="مكرونة ")
    macarona_label.place(x=550,y=230)
    macarona_var = tk.StringVar()
    macarona_combobox = ttk.Combobox(new_window, textvariable=macarona_var,width=15,font=15,background="steelblue")
    macarona_combobox.place(x=500,y=270)
    macarona_entry= Entry(new_window, width=10, fg='steelblue',font="arial 15 bold")
    macarona_entry.place(x=700,y=270)
    def handle_macarona():
         quantity=macarona_entry.get()
         if quantity=="":
             showerror('خطأ','ادخل رقم')
         quantity2=int(quantity)
         x="select name , price from macarona where name= ?"
         xx=(macarona_combobox.get(),)
         cur.execute(x,xx)
         results=cur.fetchall()
         results_to_tuple=tuple(results)
         #  tuple of tuple to list
         elements=[element for tupl in results_to_tuple for element in tupl]
         price=int(elements[1])
         name=elements[0]
         elements.append(quantity2)
         total=quantity2*price
         elements.append(total)

         dd=cur.execute("SELECT recipt_number FROM recipts WHERE num=(SELECT MAX(num) FROM recipts)")
         results2=cur.fetchall()
         rec_num=results2[0]
         rec_num=rec_num[0]
         elements.append(rec_num)
         cur.execute("insert into recipt_contents(recipt_number,price,quantity,class,total) values(?,?,?,?,?)",(rec_num,price,quantity2,name,total,))
         conn.commit()
     
    macarona_button=Button(new_window,width=15,text="اضافة",fg="white",bg="blue",command=handle_macarona)
    macarona_button.place(x=820,y=270)


    # database


    cur.execute("select name from macarona order by name asc")
    all_macarona=cur.fetchall()
    # list of tuple to tuple of tuple
    all_macarona=tuple(all_macarona)
    #  tuple of tuple to list
    elements=[element for tupl in all_macarona for element in tupl]
    # list to tuple
    e=tuple(elements)
    macarona_combobox['values']=e


    # ------------------------------------classes of restaurant------------------------
    #       5 madness_deer
    #        design
    madness_dear_label= Label(new_window, font=('arial 20 bold'), fg='steelblue',text="مادنس دير ")
    madness_dear_label.place(x=90,y=330)
    madness_dear_var = tk.StringVar()
    madness_dear_combobox = ttk.Combobox(new_window, textvariable=madness_dear_var,width=15,font=15,background="steelblue")
    madness_dear_combobox.place(x=50,y=370)
    madness_dear_entry= Entry(new_window, width=10, fg='steelblue',font="arial 15 bold")
    madness_dear_entry.place(x=250,y=370)
    def handle_madness_dear():
         quantity=madness_dear_entry.get()
         if quantity=="":
             showerror('خطأ','ادخل رقم')
         quantity2=int(quantity)
         x="select name , price from madness_deer where name= ?"
         xx=(madness_dear_combobox.get(),)
         cur.execute(x,xx)
         results=cur.fetchall()
         results_to_tuple=tuple(results)
         #  tuple of tuple to list
         elements=[element for tupl in results_to_tuple for element in tupl]
         price=int(elements[1])
         name=elements[0]
         elements.append(quantity2)
         total=quantity2*price
         elements.append(total)

         dd=cur.execute("SELECT recipt_number FROM recipts WHERE num=(SELECT MAX(num) FROM recipts)")
         results2=cur.fetchall()
         rec_num=results2[0]
         rec_num=rec_num[0]
         elements.append(rec_num)
         cur.execute("insert into recipt_contents(recipt_number,price,quantity,class,total) values(?,?,?,?,?)",(rec_num,price,quantity2,name,total,))
         conn.commit()
    madness_dear_button=Button(new_window,width=15,text="اضافة",fg="white",bg="blue",command=handle_madness_dear)
    madness_dear_button.place(x=370,y=370)


    # database

    cur.execute("select name from madness_deer order by name asc")
    all_madness_dear=cur.fetchall()
    # list of tuple to tuple of tuple
    all_madness_dear=tuple(all_madness_dear)
    #  tuple of tuple to list
    elements=[element for tupl in all_madness_dear for element in tupl]
    # list to tuple
    e=tuple(elements)
    madness_dear_combobox['values']=e


    # ------------------------------------classes of restaurant------------------------
    #       6 milk_check
    #        design
    milk_check_label= Label(new_window, font=('arial 20 bold'), fg='steelblue',text="ميلك تشيك ")
    milk_check_label.place(x=550,y=330)
    milk_check_var = tk.StringVar()
    milk_check_combobox = ttk.Combobox(new_window, textvariable=milk_check_var,width=15,font=15,background="steelblue")
    milk_check_combobox.place(x=500,y=370)
    milk_check_entry= Entry(new_window, width=10, fg='steelblue',font="arial 15 bold")
    milk_check_entry.place(x=700,y=370)
    def handle_milk_check():
         quantity=milk_check_entry.get()
         if quantity=="":
             showerror('خطأ','ادخل رقم')
         quantity2=int(quantity)
         x="select name , price from milk_check where name= ?"
         xx=(milk_check_combobox.get(),)
         cur.execute(x,xx)
         results=cur.fetchall()
         results_to_tuple=tuple(results)
         #  tuple of tuple to list
         elements=[element for tupl in results_to_tuple for element in tupl]
         price=int(elements[1])
         name=elements[0]
         elements.append(quantity2)
         total=quantity2*price
         elements.append(total)

         dd=cur.execute("SELECT recipt_number FROM recipts WHERE num=(SELECT MAX(num) FROM recipts)")
         results2=cur.fetchall()
         rec_num=results2[0]
         rec_num=rec_num[0]
         elements.append(rec_num)
         cur.execute("insert into recipt_contents(recipt_number,price,quantity,class,total) values(?,?,?,?,?)",(rec_num,price,quantity2,name,total,))
         conn.commit()
    milk_check_button=Button(new_window,width=15,text="اضافة",fg="white",bg="blue",command=handle_milk_check)
    milk_check_button.place(x=820,y=370)


    # database


    cur.execute("select name from milk_check order by name asc")
    all_milk_check=cur.fetchall()
    # list of tuple to tuple of tuple
    all_milk_check=tuple(all_milk_check)
    #  tuple of tuple to list
    elements=[element for tupl in all_milk_check for element in tupl]
    # list to tuple
    e=tuple(elements)
    milk_check_combobox['values']=e


    # ------------------------------------classes of restaurant------------------------
    #       7 moqablat
    #        design
    moqablat_label= Label(new_window, font=('arial 20 bold'), fg='steelblue',text="مقبلات ")
    moqablat_label.place(x=90,y=430)
    moqablat_var = tk.StringVar()
    moqablat_combobox = ttk.Combobox(new_window, textvariable=moqablat_var,width=15,font=15,background="steelblue")
    moqablat_combobox.place(x=50,y=470)
    moqablat_entry= Entry(new_window, width=10, fg='steelblue',font="arial 15 bold")
    moqablat_entry.place(x=250,y=470)
    def handle_moqablat():
         quantity=moqablat_entry.get()
         if quantity=="":
             showerror('خطأ','ادخل رقم')
         quantity2=int(quantity)
         x="select name , price from moqablat where name= ?"
         xx=(moqablat_combobox.get(),)
         cur.execute(x,xx)
         results=cur.fetchall()
         results_to_tuple=tuple(results)
         #  tuple of tuple to list
         elements=[element for tupl in results_to_tuple for element in tupl]
         price=int(elements[1])
         name=elements[0]
         elements.append(quantity2)
         total=quantity2*price
         elements.append(total)

         dd=cur.execute("SELECT recipt_number FROM recipts WHERE num=(SELECT MAX(num) FROM recipts)")
         results2=cur.fetchall()
         rec_num=results2[0]
         rec_num=rec_num[0]
         elements.append(rec_num)
         cur.execute("insert into recipt_contents(recipt_number,price,quantity,class,total) values(?,?,?,?,?)",(rec_num,price,quantity2,name,total,))
         conn.commit()
    moqablat_button=Button(new_window,width=15,text="اضافة",fg="white",bg="blue",command=handle_moqablat)
    moqablat_button.place(x=370,y=470)


    # database

    cur.execute("select name from moqablat order by name asc")
    all_moqablat=cur.fetchall()
    # list of tuple to tuple of tuple
    all_moqablat=tuple(all_moqablat)
    #  tuple of tuple to list
    elements=[element for tupl in all_moqablat for element in tupl]
    # list to tuple
    e=tuple(elements)
    moqablat_combobox['values']=e


    # ------------------------------------classes of restaurant------------------------
    #       8 rizo
    #        design
    rizo_label= Label(new_window, font=('arial 20 bold'), fg='steelblue',text=" ريزو ")
    rizo_label.place(x=550,y=430)
    rizo_var = tk.StringVar()
    rizo_combobox = ttk.Combobox(new_window, textvariable=rizo_var,width=15,font=15,background="steelblue")
    rizo_combobox.place(x=500,y=470)
    rizo_entry= Entry(new_window, width=10, fg='steelblue',font="arial 15 bold")
    rizo_entry.place(x=700,y=470)
    def handle_rizo():
         quantity=rizo_entry.get()
         if quantity=="":
             showerror('خطأ','ادخل رقم')
         quantity2=int(quantity)
         x="select name , price from rizo where name= ?"
         xx=(rizo_combobox.get(),)
         cur.execute(x,xx)
         results=cur.fetchall()
         results_to_tuple=tuple(results)
         #  tuple of tuple to list
         elements=[element for tupl in results_to_tuple for element in tupl]
         price=int(elements[1])
         name=elements[0]
         elements.append(quantity2)
         total=quantity2*price
         elements.append(total)

         dd=cur.execute("SELECT recipt_number FROM recipts WHERE num=(SELECT MAX(num) FROM recipts)")
         results2=cur.fetchall()
         rec_num=results2[0]
         rec_num=rec_num[0]
         elements.append(rec_num)
         cur.execute("insert into recipt_contents(recipt_number,price,quantity,class,total) values(?,?,?,?,?)",(rec_num,price,quantity2,name,total,))
         conn.commit()
    rizo_button=Button(new_window,width=15,text="اضافة",fg="white",bg="blue",command=handle_rizo)
    rizo_button.place(x=820,y=470)


    # database


    cur.execute("select name from rizo order by name asc")
    all_rizo=cur.fetchall()
    # list of tuple to tuple of tuple
    all_rizo=tuple(all_rizo)
    #  tuple of tuple to list
    elements=[element for tupl in all_rizo for element in tupl]
    # list to tuple
    e=tuple(elements)
    rizo_combobox['values']=e


    # ------------------------------------classes of restaurant------------------------
    #       9 salades
    #        design
    salades_label= Label(new_window, font=('arial 20 bold'), fg='steelblue',text="سلطات ")
    salades_label.place(x=90,y=530)
    salades_var = tk.StringVar()
    salades_combobox = ttk.Combobox(new_window, textvariable=salades_var,width=15,font=15,background="steelblue")
    salades_combobox.place(x=50,y=570)
    salades_entry= Entry(new_window, width=10, fg='steelblue',font="arial 15 bold")
    salades_entry.place(x=250,y=570)
    def handle_salades():
         quantity=salades_entry.get()
         if quantity=="":
             showerror('خطأ','ادخل رقم')
         quantity2=int(quantity)
         x="select name , price from salades where name= ?"
         xx=(salades_combobox.get(),)
         cur.execute(x,xx)
         results=cur.fetchall()
         results_to_tuple=tuple(results)
         #  tuple of tuple to list
         elements=[element for tupl in results_to_tuple for element in tupl]
         price=int(elements[1])
         name=elements[0]
         elements.append(quantity2)
         total=quantity2*price
         elements.append(total)

         dd=cur.execute("SELECT recipt_number FROM recipts WHERE num=(SELECT MAX(num) FROM recipts)")
         results2=cur.fetchall()
         rec_num=results2[0]
         rec_num=rec_num[0]
         elements.append(rec_num)
         cur.execute("insert into recipt_contents(recipt_number,price,quantity,class,total) values(?,?,?,?,?)",(rec_num,price,quantity2,name,total,))
         conn.commit()
    salades_button=Button(new_window,width=15,text="اضافة",bg="blue",fg="white",command=handle_salades)
    salades_button.place(x=370,y=570)


    # database

    cur.execute("select name from salades order by name asc")
    all_salades=cur.fetchall()
    # list of tuple to tuple of tuple
    all_salades=tuple(all_salades)
    #  tuple of tuple to list
    elements=[element for tupl in all_salades for element in tupl]
    # list to tuple
    e=tuple(elements)
    salades_combobox['values']=e


    # ------------------------------------classes of restaurant------------------------
    #       10 smoozy
    #        design
    smoozy_label= Label(new_window, font=('arial 20 bold'), fg='steelblue',text="سموزي  ")
    smoozy_label.place(x=550,y=530)
    smoozy_var = tk.StringVar()
    smoozy_combobox = ttk.Combobox(new_window, textvariable=smoozy_var,width=15,font=15,background="steelblue")
    smoozy_combobox.place(x=500,y=570)
    smoozy_entry= Entry(new_window, width=10, fg='steelblue',font="arial 15 bold")
    smoozy_entry.place(x=700,y=570)
    def handle_smoozy():
         quantity=smoozy_entry.get()
         if quantity=="":
             showerror('خطأ','ادخل رقم')
         quantity2=int(quantity)
         x="select name , price from smoozy where name= ?"
         xx=(smoozy_combobox.get(),)
         cur.execute(x,xx)
         results=cur.fetchall()
         results_to_tuple=tuple(results)
         #  tuple of tuple to list
         elements=[element for tupl in results_to_tuple for element in tupl]
         price=int(elements[1])
         name=elements[0]
         elements.append(quantity2)
         total=quantity2*price
         elements.append(total)

         dd=cur.execute("SELECT recipt_number FROM recipts WHERE num=(SELECT MAX(num) FROM recipts)")
         results2=cur.fetchall()
         rec_num=results2[0]
         rec_num=rec_num[0]
         elements.append(rec_num)
         cur.execute("insert into recipt_contents(recipt_number,price,quantity,class,total) values(?,?,?,?,?)",(rec_num,price,quantity2,name,total,))
         conn.commit()
    smoozy_button=Button(new_window,width=15,text="اضافة",bg="blue",fg="white",command=handle_smoozy)
    smoozy_button.place(x=820,y=570)


    # database

    cur.execute("select name from smoozy order by name asc")
    all_smoozy=cur.fetchall()
    # list of tuple to tuple of tuple
    all_smoozy=tuple(all_smoozy)
    #  tuple of tuple to list
    elements=[element for tupl in all_smoozy for element in tupl]
    # list to tuple
    e=tuple(elements)
    smoozy_combobox['values']=e
    nxt_btn=Button(new_window,text="التالي",fg="red",width=20,command=third_page)
    nxt_btn.place(x=20,y=60)


win.mainloop()

