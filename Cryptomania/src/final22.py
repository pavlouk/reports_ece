# -*- coding: utf-8 -*-
from Tkinter import *
import tkMessageBox
from random import randint


def home_page():
    global root, frame1, frame2, frame3, panelx, back_image1
    panex = Label(frame2, image=back_image1).place(x=0, y=0, relwidth=1, relheight=1)


def beforekeys():
    global entry1, entry2, frame2, root, frame1, frame3, panel1, back_image2, p1, p2
    back_image2 = PhotoImage(file='Lock2.gif')
    panel1 = Label(frame2, image=back_image2).place(x=0, y=0, relwidth=1, relheight=1)
    p1 = StringVar()
    p1.set("")
    entry1 = Entry(frame2, textvariable=p1, font=("Helvetica", "10"))
    entry1.place(x=120, y=195)
    p2 = StringVar()
    p2.set("")
    entry2 = Entry(frame2, textvariable=p2, font=("Helvetica", "10"))
    entry2.place(x=120, y=276)
    button1 = Button(frame2, text="  Generate  ", command=keys, bg="black", fg="white").place(x=241, y=233)


def keys():
    global entry1, entry2, frame2, root, frame1, frame3, panel1, back_image2, public, private, p1, p2
    m = entry1.get()
    s = entry2.get()
    prwtoi = (13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
              71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139,
              149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
              227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
              307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383,
              389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
              467, 479, 487, 491, 499)
    if m.isdigit() and s.isdigit():
        p = int(m)
        q = int(s)
        if (p not in prwtoi) or (q not in prwtoi):
            tkMessageBox.showerror("Error", "Invalid numbers. Please check the list and try again.")
            p1.set("")
            p2.set("")
        else:
            n = p * q
            f = (p - 1) * (q - 1)
            g = []
            for i in prwtoi:
                if f % i != 0 and i < f:
                    g.append(i)
            k = randint(0, len(g) - 1)
            e = g[k]
            i = 1
            k = "False"
            while k == "False":
                if i * e % f == 1 and i < f:
                    k = "True"
                else:
                    i = i + 1
            d = i
            a = [[e, n], [d, n]]
            v = StringVar()
            v.set(str(e) + "," + str(n))
            public = str(e) + "," + str(n)
            g = StringVar()
            g.set(str(d) + "," + str(n))
            private = str(d) + "," + str(n)
            Entry(frame3, textvariable=v, font=("Helvetica", "10")).place(x=10, y=100)
            Entry(frame3, textvariable=g, font=("Helvetica", "10")).place(x=10, y=230)
    else:
        tkMessageBox.showerror("Error", "Input must be numbers. Please check the list and try again.")
        p1.set("")
        p2.set("")


def beforecoding():
    global root, panel2, back_image3, frame2, the_plain, publ_key, plaintext
    back_image3 = PhotoImage(file='Lock3.gif')
    panel2 = Label(frame2, image=back_image3).place(x=0, y=0, relwidth=1, relheight=1)
    scroll = Scrollbar(frame2)
    scroll.place(x=420, y=40, width=20, height=140)
    the_plain = Text(frame2, font=("Helvetica", "10"))
    the_plain.place(x=20, y=40, width=400, height=140)
    scroll.configure(command=the_plain.yview)
    the_plain.configure(yscrollcommand=scroll.set)
    publ_key = Entry(frame2, font=("Helvetica", "10"))
    publ_key.place(x=120, y=276)
    go = Button(frame2, text="Encrypt", command=coding, bg="black", fg="white")
    go.place(x=155, y=300)


def coding():
    global the_plain, publ_key, frame2, root, panel2, back_image3, plaintext
    pubkey = publ_key.get()
    plaintext = the_plain.get("1.0", END)
    messag = plaintext
    ind = pubkey.split(',')
    x = int(ind[0])
    z = int(ind[1])
    r = []
    r.append(x)
    r.append(z)
    mes = ""
    for j in messag:
        ASCII = ord(j)
        ASCII = realcoding(r, ASCII)
        mes = mes + ASCII
    S = Scrollbar(frame2)
    T = Text(frame2, height=10, width=15, font=("Helvetica", "10"))
    T.place(x=470, y=150)
    S.place(x=573, y=150, height=160)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    T.insert(END, mes)


def realcoding(r, ASCII):
    crypto = (ASCII ** r[0]) % r[1]
    if crypto < 10:
        crypto = "00000" + str(crypto)
    elif crypto < 100:
        crypto = "0000" + str(crypto)
    elif crypto < 1000:
        crypto = "000" + str(crypto)
    elif crypto < 10000:
        crypto = "00" + str(crypto)
    elif crypto < 100000:
        crypto = "0" + str(crypto)
    else:
        crypto = str(crypto)
    return crypto


def beforedecoding():
    global the_cyph, priv_key, frame2, panel3, back_image4
    back_image4 = PhotoImage(file='Lock4.gif')
    panel3 = Label(frame2, image=back_image4).place(x=0, y=0, relwidth=1, relheight=1)
    scroll1 = Scrollbar(frame2)
    scroll1.place(x=400, y=50, width=20, height=80)
    the_cyph = Text(frame2, font=("Helvetica", "10"))
    the_cyph.place(x=50, y=50, width=350, height=80)
    scroll1.configure(command=the_cyph.yview)
    the_cyph.configure(yscrollcommand=scroll1.set)
    priv_key = Entry(frame2, font=("Helvetica", "10"))
    priv_key.place(x=135, y=223)
    Button(frame2, text="Decrypt", command=decoding, bg="black", fg="white").place(x=170, y=250)


def fastmodpower(a, n, p):
    res = 1
    while (n > 0):
        if (n % 2 == 1):
            res = res * a % p
        # print (n,a,res)
        n = n // 2
        a = a * a % p
    return res


def decoding():
    global the_cyph, priv_key, root, frame2, panel3, back_image4
    privkey = priv_key.get()
    cyphertext = the_cyph.get("1.0", END)
    cryptmes = cyphertext
    privkey1 = privkey.split(",")
    c1 = ""
    i1 = 0
    while i1 < len(cryptmes) - 6:
        a = int(cryptmes[i1:i1 + 6])
        # a=a**int(privkey1[0]) % int(privkey1[1])
        a = fastmodpower(a, int(privkey1[0]), int(privkey1[1]))
        b = chr(a)
        c1 = c1 + b
        i1 = i1 + 6

    S1 = Scrollbar(frame2)
    T1 = Text(frame2, height=10, width=15, font=("Helvetica", "10"))
    T1.place(x=470, y=150)
    S1.place(x=594, y=150, height=165)
    S1.config(command=T1.yview)
    T1.config(yscrollcommand=S1.set)
    T1.insert(END, c1)


def showhelp():
    global root, back_image5, top1
    top1 = Toplevel(root)
    top1.wm_geometry("970x375+100+10")
    back_image5 = PhotoImage(file="help.gif")
    panel = Label(top1, image=back_image5).place(x=0, y=0, relwidth=1, relheight=1)
    ex_button = Button(top1, text="Exit", command=top1.destroy).place(x=450, y=330, width=50, height=30)


def About():
    global root, back_image6, top2
    top2 = Toplevel(root)
    top2.wm_geometry("614x728+200+10")
    back_image6 = PhotoImage(file="lock22.gif")
    panel = Label(top2, image=back_image6).place(x=0, y=0, relwidth=1, relheight=1)
    ex_button = Button(top2, text="Ok", command=top2.destroy).place(x=350, y=690, width=50, height=30)


def save_list():
    global root, contents, friend_list, frame3, mm
    contents = mm.get("1.0", END)
    friend_list = open("key_list.txt", "w")
    friend_list.write(contents)
    friend_list.close()


root = Tk()
menu = Menu(root)
root.config(menu=menu)
subMenu1 = Menu(menu)
menu.add_cascade(label="Options", menu=subMenu1)
subMenu1.add_command(label="Help", command=showhelp)
subMenu1.add_command(label="About Cryptomania", command=About)
subMenu1.add_separator()
subMenu1.add_command(label="Exit", command=root.destroy)
#root.iconbitmap(default='lock.ico')
root.title('Cryptomania')
root.wm_geometry("960x495+100+100")
frame1 = Frame(root, relief=SUNKEN)
frame1.place(x=0, y=0, width=150, height=495)
frame1.configure(background="black")
frame2 = Frame(root, relief=SUNKEN)
frame2.place(x=150, y=0, width=660, height=495)
back_image1 = PhotoImage(file="Lock1.gif")
panel = Label(frame2, image=back_image1).place(x=0, y=0, relwidth=1, relheight=1)
frame3 = Frame(root, relief=SUNKEN)
frame3.place(x=810, y=0, width=150, height=495)
frame3.configure(background="black")
Button(frame1, text="           Key Generator              ", command=beforekeys, bg="black", fg="white").place(x=0,
                                                                                                                y=180)
Button(frame1, text="        Message Encryption        ", command=beforecoding, bg="black", fg="white").place(x=0,
                                                                                                              y=290)
Button(frame1, text="        Message Decryption        ", command=beforedecoding, bg="black", fg="white").place(x=0,
                                                                                                                y=400)
Button(frame1, text="                 Home                    ", command=home_page, bg="black", fg="white").place(x=0,
                                                                                                                  y=70)
Button(frame3, text="    Save    ", command=save_list, bg="black", fg="white").place(x=73, y=470)
Label(frame3, text="Your Public Key: ", bg="black", fg="white").place(x=20, y=50)
g = StringVar()
public = ""
g.set(public)
Entry(frame3, textvariable=g, font=("Helvetica", "10")).place(x=20, y=100)
Label(frame3, text="Your Private Key: ", bg="black", fg="white").place(x=20, y=180)
k = StringVar()
private = ""
k.set(private)
Entry(frame3, textvariable=k, font=("Helvetica", "10")).place(x=20, y=230)
Label(frame3, text="Friends' Keylist: ", bg="black", fg="white").place(x=20, y=298)
m = StringVar()
m.set("")
scroller = Scrollbar(frame3)
scroller.place(x=130, y=330, width=20, height=140)
mm = Text(frame3, font=("Helvetica", "10"))
mm.place(x=20, y=330, width=110, height=140)
friend_list = open("key_list.txt", "r+")
friend_list.write("")
contents = friend_list.read()
friend_list.close()
mm.insert(END, contents)
scroller.configure(command=mm.yview)
mm.configure(yscrollcommand=scroller.set)
root.mainloop()
