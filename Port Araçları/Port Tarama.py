#! /usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet PORT TARAMA")
print("""
Port Tarama Aracina Hos Geldiniz 

1) Hizli Tarama
2) Servis ve Versiyon Bilgisi
3) İsletim Sistemi Bilgisi


""")

islemno = input("İslem Numarasini Girin: ")

if(islemno=="1"):
        hedefip = input("Hedef İp Girin: ")
        os.system("nmap " + hedefip)
elif(islemno=="2"):
          hedefip: input("Hedef İp Girin: ")
          os.system("nmap -sS -sV " + hedefip)
elif(islemno=="3"):
          hedefip = input("Hedef İp Girin: ")
          os.system(nmap -0 + hedefip)
else:
      print("Hatali Secim Yaptiniz Lutfen Tekrar Deneyiniz")