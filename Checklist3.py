#!/usr/bin/env python3

import os
from tkinter import *
import webbrowser

#Masterfully crafted by Cameron Lewis

root = Tk()
root.title('NOC Night Shift Checlist & Links')

menu = Menu(root)
root.config(menu=menu)

def displayme():
    labelResult3 = Label(root, text="This script was masterfully crafted by Cameron Lewis.", bg="green", fg="white")
    labelResult3.grid(row=24, columnspan=2)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Who made this?", command=displayme)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=exit)

def checklisttemplate():
    webbrowser.open_new(r"https://confluence1.daicompanies.com/display/ODSPROD/Checklist+Template")
buttontest = Button(text="Open the Checklist Template", command=checklisttemplate)
buttontest.grid(row=0, columnspan=2)
theLabelseparate = Label(root, text="Checklist:")
theLabelseparate.grid(row=0, column=0, sticky=E)

theLabelseparator = Label(root, text="--------------------------------------------------------")
theLabelseparator.grid(row=1, columnspan=2)

def sysmon():
    webbrowser.open_new(r"http://sysmonweb/SuperMon/#dashboard")
buttonsysmon = Button(text="Open Sysmon", command=sysmon)
buttonsysmon.grid(row=2, columnspan=2)
theLabelsysmon = Label(root, text="WON Sysmon:")
theLabelsysmon.grid(row=2, column=0, sticky=E)

def odssysmon():
    webbrowser.open_new(r"http://odssysmonweb.odsdai.netdai.com/SuperMon/#dashboard")
buttonodssysmon = Button(text="Open ODS Sysmon", command=odssysmon)
buttonodssysmon.grid(row=3, columnspan=2)
theLabelodssysmon = Label(root, text="ODS Sysmon:")
theLabelodssysmon.grid(row=3, column=0, sticky=E)

def hpsdashboard():
    webbrowser.open_new(r"http://odslarss1/Reports/Pages/Report.aspx?ItemPath=%2fHPS%2fHPSDashBoard")
buttonhpsdashboard = Button(text="Open HPS Dashboard", command=hpsdashboard)
buttonhpsdashboard.grid(row=4, columnspan=2)
theLabelhpsdashboard = Label(root, text="ODS Sysmon:")
theLabelhpsdashboard.grid(row=4, column=0, sticky=E)

theLabelseparatorsys = Label(root, text="--------------------------------------------------------")
theLabelseparatorsys.grid(row=5, columnspan=2)

def twelvethirtycheck():
    path1 = r"\\ods\storage\Humana\WelcomeKit\To_ODS"
    os.startfile(path1)
    os.path.join(path1)
button1 = Button(text="Check Humana CID 243 directory", command=twelvethirtycheck)
button1.grid(row=6, column=1, sticky=W)
label1230 = Label(root, text="12:30 AM")
label1230.grid(row=6, column=0)

def oneamcheck():
    path2 = r"\\ODSEFTFS\Usr_Temp"
    os.startfile(path2)
    os.path.join(path2)
button3 = Button(text="Check ODSEFTFS Directory", command=oneamcheck)
button3.grid(row=7, column=1, sticky=W)
label100 = Label(root, text="1:00 AM")
label100.grid(row=7, column=0)

def onethirtycheck():
    path3 = r"\\odsla\Storage\WellCare\To_ODS\VDP_LETTERS\SAMEDAY_LETTER"
    os.startfile(path3)
    os.path.join(path3)
button4 = Button(text="Check WellCare CID 192", command=onethirtycheck)
button4.grid(row=8, column=1, sticky=W)
label200 = Label(root, text="1:00 AM")
label200.grid(row=8, column=0)

def cvstwocheck():
    path4 = r"\\ODSCSStorage\s\Storage\root\CareSource\To_ODS"
    os.startfile(path4)
    os.path.join(path4)
button5 = Button(text="Check Caresource Jobs", command=cvstwocheck)
button5.grid(row=9, column=1, sticky=W)
label2002 = Label(root, text="2:00 AM")
label2002.grid(row=9, column=0)

def cvsreportcheck():
    path5 = r"\\odsla\Storage\CVS_Caremark\Processed\Reports"
    os.startfile(path5)
    os.path.join(path5)
button6 = Button(text="Check CVS Response File", command=cvsreportcheck)
button6.grid(row=10, column=1, sticky=W)
label100 = Label(root, text="2:00 AM")
label100.grid(row=10, column=0)

def uhcresponsecheck():
    path6 = r"\\odsunitedstorage\s\storage\root\UnitedHealthCare\Reponse_Files"
    os.startfile(path6)
    os.path.join(path6)
button7 = Button(text="UHC Response File", command=uhcresponsecheck)
button7.grid(row=11, column=1, sticky=W)
label215 = Label(root, text="2:15 AM")
label215.grid(row=11, column=0)

def cid221check():
    path7 = r"\\odsstorage\s\storage\root\BCBSLA_LargeGroup\To_ODS"
    os.startfile(path7)
    os.path.join(path7)
button8 = Button(text="Check BCBS CID 221", command=cid221check)
button8.grid(row=12, column=1, sticky=W)
label300 = Label(root, text="3:00 AM")
label300.grid(row=12, column=0)

def cvspartedcheck():
    webbrowser.open_new(r"http://odssysmonweb.odsdai.netdai.com/SuperMon/#dashboard")
button81 = Button(text="Check CVS PARTD Error", command=cvspartedcheck)
button81.grid(row=13, column=1, sticky=W)
label3002 = Label(root, text="3:00 AM")
label3002.grid(row=13, column=0)

def wellcarecheck():
    path8 = r"\\ods\STORAGE\WellCare\To_ODS\PAPYRUS\1-SameDay"
    os.startfile(path8)
    os.path.join(path8)
button9 = Button(text="Check Wellcare CID 780", command=wellcarecheck)
button9.grid(row=14, column=1, sticky=W)
label315 = Label(root, text="3:15 AM")
label315.grid(row=14, column=0)

def gmccheck():
    webbrowser.open_new(r"http://odssysmonweb.odsdai.netdai.com/SuperMon/#batchless/v2")
button400 = Button(text="Check CVS PARTD Error", command=gmccheck)
button400.grid(row=15, column=1, sticky=W)
label400 = Label(root, text="4:30 AM")
label400.grid(row=15, column=0)

theLabelseparate1 = Label(root, text="-----------------------------------------------------------")
theLabelseparate1.grid(row=16, columnspan=2)

theLabel = Label(root, text="The following directories are for weekend checks:")
theLabel.grid(row=17, column=1, sticky=W)

def fridayfirstlogiccheck():
    path9 = r"\\Odslafirstlogic\usps_download\NCOALink18MTHHASH"
    os.startfile(path9)
    os.path.join(path9)
button10 = Button(text="Verify you have a .tar file here with a date from Monday", command=fridayfirstlogiccheck)
button10.grid(row=18, column=1, sticky=W)
labelfridayfirstlogic = Label(root, text="FRI, 10:00 PM")
labelfridayfirstlogic.grid(row=18, column=0)

def firstlogiccheck():
    path10 = r"\\ODSLAFIRSTLOGIC\pw\dirs\ncoa"
    os.startfile(path10)
    os.path.join(path10)
button10 = Button(text="Verify files have been extracted from the link above to here", command=firstlogiccheck)
button10.grid(row=19, column=1, sticky=W)
labelfirstlogiccheck = Label(root, text="SAT, 3:30 AM")
labelfirstlogiccheck.grid(row=19, column=0)

theLabelseparator1 = Label(root, text="------------------------------------------------------------")
theLabelseparator1.grid(row=20, columnspan=2)

button2 = Button(text="Press this button to exit.", command=exit)
button2.grid(row=21, columnspan=2)

root.mainloop()
