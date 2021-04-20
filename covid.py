import urllib.request ,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import re
from tkinter import *

#extract numbers from website
url = "https://covid19.who.int/region/searo/country/in"
html  = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')
tags = soup('span')
for tag in tags:

    if 'confirmed' in str(tag):
        cases = str(tag)
        number = re.findall('[0-9]+.[0-9]+',cases)
        confirmed = number[0]+','+number[1]
        #print(confirmed)
    elif 'deaths' in str(tag):
        deaths = str(tag)
        dnumber = re.findall('[0-9]+.[0-9]+',deaths)
        total_death = dnumber[0]
        #print(total_death)   

root = Tk()
root.title("Covid-cases India")
root.geometry('973x345')

#define image
bg = PhotoImage(file='images/india.png')

#create a label 
my_label = Label(root,image=bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)

#label above bg
my_text1 = Label(root,text='COVID CASES-INDIA',font=('Modern',40),fg='white')
my_text1.pack(pady=40)

#create variable
active_cases = 'TOTAL CASES = '+confirmed
death_count = 'TOTAL DEATHS = '+total_death

my_text2 = Label(root,text=active_cases,font=('Modern',30),fg='green')
my_text2.pack(pady=20)
my_text3 = Label(root,text=death_count,font=('Modern',30),fg='red')
my_text3.pack(pady=20)
   
 

root.mainloop()    
