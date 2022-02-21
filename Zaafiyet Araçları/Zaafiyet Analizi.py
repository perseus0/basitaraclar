#! /usr/bin/env python

import os
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Zaafiyet Analizi")
print("""
Zaafiyet Analizi Aracina Hos Geldiniz

""")

hedefip = input("Hedef İp Girin: ")
os.system("nikto -h " +hedefip)