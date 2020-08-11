import tkinter
import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox

t_cases = ""
t_deaths = ""
t_recovered = ""
url = ''
t_active = ''
i = 0
ac_or_cl = 'OTHER CASES'


def action(*args):
    global variable, url, top
    inp = e1.get()
    if inp == 'World' or inp == 'Earth' or inp == 'earth' or inp == 'world':
        url = "https://www.worldometers.info/coronavirus/"
    else:
        url = "https://www.worldometers.info/coronavirus/country/" + inp

    display()


def display():
    global top, var1, t_cases, t_deaths, t_recovered, t_active, i, ac_or_cl
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    try:
        data = soup.find_all("div", class_="maincounter-number")
        t_cases = data[0].text.strip()
        t_deaths = data[1].text.strip()
        t_recovered = data[2].text.strip()
        var1.set(t_deaths)
        var2.set(t_cases)
        var3.set(t_recovered)
    except:
        messagebox.showinfo("Error", "Enter correct country")
        v.set('')
        return
    active = soup.find_all("div", class_='number-table-main')
    t_active = active[0].text.strip()
    var8.set(t_active)
    print('\nClosed: ', t_active)
    data1 = soup.find_all("div", class_="panel-heading")
    ac_or_cl = data1[0].text.strip()
    var7.set(ac_or_cl)
    v.set('')  # clear after search


# main
top = tkinter.Tk()
top.geometry("670x500")
top.configure(bg="#0A3D62")

# Heading
var = tkinter.StringVar()
lab = tkinter.Label(
    top,
    textvariable=var,
    width=20,
    bg='#0A3D62',
    fg='#67E6DC',
    justify='left',
    pady=10
)
lab.config(font="Verdana 24 underline")
var.set("Covid-19 Tracker")
lab.grid(row=0, column=0, columnspan=10, pady=(2, 12))

# text message
txt = 'Coronavirus disease (COVID-19) is an infectious disease caused by\na newly discovered coronavirus. Most people ' \
      'who fall sick with\n COVID-19 will experience mild to moderate symptoms and recover\n without special ' \
      'treatment. '
panel1 = tkinter.Label(top, text=txt, bg='#0A3D62', fg='White', justify=LEFT)
panel1.grid(sticky=W, row=3, column=3, columnspan=4, rowspan=2, padx=10, pady=10)


# User entry

v = StringVar()
e1 = tkinter.Entry(
    top,
    textvariable=v,
    bg='#0A3D62',
    fg='White',
    relief=SUNKEN,

)
e1.bind('<Return>', action)
e1.grid(row=2, column=0, padx=5)
v.set('Entry Country')


# Submit Button

submit = tkinter.Button(
    top,
    text='Search',
    bg='#0A3D62',
    fg='White',
    command=lambda: action()
)
submit.grid(row=2, column=1, padx=5)


# Cases Label
var4 = StringVar()
var4.set("CASES")
lab1 = tkinter.Label(
    top,
    textvariable=var4,
    fg='#B83227',
    bg='#2C3335'
)
lab1.grid(row=3, column=0, sticky=E)

# Cases value
var2 = StringVar()
lab_total = tkinter.Label(
    top,
    width=15,
    textvariable=var2,
    fg='#B83227',
    bg='#2C3335',
    relief=SUNKEN

)
lab_total.grid(row=3, column=1, pady=5)

# Death Label
var5 = StringVar()
var5.set("DEATHS")
lab2 = tkinter.Label(
    top,
    textvariable=var5,
    fg='#B83227',
    bg='#2C3335'
)
lab2.grid(row=4, column=0, sticky=E)

# Death Value
var1 = StringVar()
lab_death = tkinter.Label(
    top,
    width=15,
    textvariable=var1,
    fg='#B83227',
    bg='#2C3335',
    relief=SUNKEN
)
lab_death.grid(row=4, column=1)

# Recovered Label
var6 = StringVar()
var6.set("RECOVERED")
lab3 = tkinter.Label(
    top,
    textvariable=var6,
    fg='#B83227',
    bg='#2C3335'
)
lab3.grid(row=5, column=0, sticky=E)

# Recovered Value
var3 = StringVar()
lab_reco = tkinter.Label(
    top,
    width=15,
    textvariable=var3,
    fg='#B83227',
    bg='#2C3335',
    relief=SUNKEN
)
lab_reco.grid(row=5, column=1, pady=5, padx=5)

# Active Label
var7 = StringVar()
lab_ac = tkinter.Label(
    top,
    textvariable=var7,
    fg='#B83227',
    bg='#2C3335',
)
var7.set('OTHER CASES')
lab_ac.grid(row=6, column=0, sticky=E)

# Active value
var8 = StringVar()
lab_acv = tkinter.Label(
    top,
    width=15,
    textvariable=var8,
    fg='#B83227',
    bg='#2C3335',
    relief=SUNKEN
)
lab_acv.grid(row=6, column=1, pady=5, padx=5)

# bottom text

txt = StringVar()
dos_head = tkinter.Label(
    top,
    textvariable=txt,
    bg='#0A3D62',
    fg='White'
)
txt.set('Do\' during this Pandemic:')
dos_head.config(font=("Courier", 11))
dos_head.grid(row=7, column=0, columnspan=2, padx=5, pady=(30, 2))

txt1 = StringVar()
dos = tkinter.Label(
    top,
    textvariable=txt1,
    bg='#0A3D62',
    fg='White',
    justify=LEFT
)
txt1.set('1. Wash Hands Regularly\n2. Maintain Social Distancing\n3. Avoid going outside\n4. Wear Mask')
dos.config(font=("Courier", 11))
dos.grid(row=8, column=0, columnspan=2, padx=5, pady=2, sticky=W)

# image

img1 = tkinter.PhotoImage(file=r'bg1.png')
# img2 = img1.subsample(2, 2)
img = tkinter.Label(
    top,
    image=img1
)
img.grid(row=8, column=3, columnspan=3, rowspan=2)

top.mainloop()
