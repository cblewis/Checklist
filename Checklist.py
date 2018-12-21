#!/usr/bin/env python3

import os
import time
import webbrowser
from tkinter import *

#Masterfully crafted by Cameron Lewis

root = Tk()

menu = Menu(root)
root.config(menu=menu)

def displayme():
    labelResult3 = Label(root, text="This script was masterfully crafted by Cameron Lewis.", bg="green", fg="white")
    labelResult3.pack(side=BOTTOM, fill=X)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Who made this?", command=displayme)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=exit)

topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

def checklisttemplate():
    webbrowser.open_new(r"https://confluence1.daicompanies.com/display/ODSPROD/Checklist+Template")
buttontest = Button(text="Open the Checklist Template", command=checklisttemplate)
buttontest.pack()

theLabelseparate = Label(root)
theLabelseparate.pack()

def twelvethirtycheck():
    path1 = r"\\ods\storage\Humana\WelcomeKit\To_ODS"
    os.startfile(path1)
    os.path.join(path1)

button1 = Button(text="Check Humana CID 243 directory", command=twelvethirtycheck)
button1.pack()

def oneamcheck():
    path2 = r"\\ODSEFTFS\Usr_Temp"
    os.startfile(path2)
    os.path.join(path2)

button3 = Button(text="Check ODSEFTFS Directory", command=oneamcheck)
button3.pack()

def onethirtycheck():
    path3 = r"\\odsla\Storage\WellCare\To_ODS\VDP_LETTERS\SAMEDAY_LETTER"
    os.startfile(path3)
    os.path.join(path3)

button4 = Button(text="Check WellCare CID 192", command=onethirtycheck)
button4.pack()

def cvstwocheck():
    path4 = r"\\ODSCSStorage\s\Storage\root\CareSource\To_ODS"
    os.startfile(path4)
    os.path.join(path4)

button5 = Button(text="Check Caresource Jobs", command=cvstwocheck)
button5.pack()

def cvsreportcheck():
    path5 = r"\\odsla\Storage\CVS_Caremark\Processed\Reports"
    os.startfile(path5)
    os.path.join(path5)

button6 = Button(text="Check CVS Response File", command=cvsreportcheck)
button6.pack()

def uhcresponsecheck():
    path6 = r"\\odsunitedstorage\s\storage\root\UnitedHealthCare\Reponse_Files"
    os.startfile(path6)
    os.path.join(path6)

button7 = Button(text="UHC Response File", command=uhcresponsecheck)
button7.pack()

def cid221check():
    path7 = r"\\odsstorage\s\storage\root\BCBSLA_LargeGroup\To_ODS"
    os.startfile(path7)
    os.path.join(path7)

button8 = Button(text="Check BCBS CID 221", command=cid221check)
button8.pack()

def wellcarecheck():
    path8 = r"\\ods\STORAGE\WellCare\To_ODS\PAPYRUS\1-SameDay"
    os.startfile(path8)
    os.path.join(path8)

button9 = Button(text="Check Wellcare CID 780", command=wellcarecheck)
button9.pack()


theLabel = Label(root, text="The following directories are for weekend checks:")
theLabel.pack(fill=X)

def fridayfirstlogiccheck():
    path9 = r"\\Odslafirstlogic\usps_download\NCOALink18MTHHASH"
    os.startfile(path9)
    os.path.join(path9)

button10 = Button(text="Verify you have a .tar file here with a date from Monday", command=fridayfirstlogiccheck)
button10.pack()

def firstlogiccheck():
    path10 = r"\\ODSLAFIRSTLOGIC\pw\dirs\ncoa"
    os.startfile(path10)
    os.path.join(path10)

button10 = Button(text="Verify files have been extracted from the link above to here", command=firstlogiccheck)
button10.pack()


button2 = Button(text="Press this button to exit.", command=exit)
button2.pack(side=BOTTOM)

root.geometry("500x500")
root.mainloop()