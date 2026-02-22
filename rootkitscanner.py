#!/usr/bin/env python
import os
os.system("apt-get install figlet")
os.system("clear")

os.system("figlet ROOTKIT SCANNER")
print(""" 
ROOTKIT SCANNER			
""")
os.system("sudo chkrootkit | grep -E 'WARNING|INFECTED'")

