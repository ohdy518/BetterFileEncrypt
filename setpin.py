import tkinter as tk
import bcrypt
typestat = ""
cptypestat = ""
salt = b'$2b$12$rgCYFuE.etnPBnQdd3fiSO'
ava = True
yesnext = False
safe = True
root2 = tk.Tk()
root2.title("Set PIN")
root2.attributes("-toolwindow", True)
root2.attributes("-topmost", True)
root2.geometry("600x120")
mainlbl = tk.Label(text="Enter PIN: ......", font=("Consolas", 24))
mainlbl.pack()
mainlbl.place(x=12, y=12)
def update():
    global typestat, cptypestat
    if len(typestat) == 6:
        if typestat == cptypestat:
            mainlbl.config(text="Encypting PIN...")
            root2.update()
            hashed = bcrypt.hashpw(typestat.encode(), salt)
            mainlbl.config(text="Encrypting PIN [Success]")
            mainlbl.config(text="Checking encryption...")
            root2.update()
            _hashed = bcrypt.hashpw(typestat.encode(), salt)
            if hashed == _hashed:
                mainlbl.config(text="Checking encryption [Success]")
                root2.update()
            else:
                mainlbl.config(text="Checking encryption [Failure]")
                root2.update()
                root2.destroy()
            mainlbl.config(text="Saving PIN...")
            root2.update()
            with open("pin.data", "w") as f:
                f.write(hashed.decode())
            mainlbl.config(text="Saving PIN [Success]")
            root2.update()
            mainlbl.config(text="Done setting PIN. ")
            root2.update()
            root2.destroy()
        else:
            mainlbl.config(text="Re-enter PIN: ......")
            typestat = ""
def kpress(_):
    global typestat, ava, yesnext
    char = _.char
    if len(typestat) == 6:
        ava = False
    if ava: 
        typestat += char
    if not yesnext:
        mainlbl.config(text="Enter PIN: " + "-" * (len(typestat) - 1) + typestat[-1:] + "." * (6-len(typestat)))
    else:
        mainlbl.config(text="Re-enter PIN: " + "-" * (len(typestat) - 1) + typestat[-1:] + "." * (6-len(typestat)))
        update()
    root2.update()
    ava = True
def rmkey(_=any):
    global typestat, yesnext
    typestat = typestat[:-1]
    if not yesnext:
        mainlbl.config(text="Enter PIN: " + "-" * (len(typestat) - 1) + typestat[-1:] + "." * (6-len(typestat)))
    else:
        mainlbl.config(text="Re-enter PIN: " + "-" * (len(typestat) - 1) + typestat[-1:] + "." * (6-len(typestat)))
        update()
    root2.update()
def next(_=any):
    global typestat, cptypestat, yesnext, safe
    if len(typestat) == 6:
        safe = True
    else:
        safe = False
        for i in range(4):
            root2.configure(background="black")
            mainlbl.configure(background="black")
            mainlbl.configure(foreground="#f0f0ed")
            root2.after(80)
            root2.update()
            root2.configure(background="#f0f0ed")
            mainlbl.configure(background="#f0f0ed")
            mainlbl.configure(foreground="black")
            root2.after(80)
            root2.update()
    if safe:
        yesnext = True
        cptypestat = typestat
        typestat = ""
        for i in range(6):
            mainlbl.config(text="Enter PIN: " + "." * (i + 1) + "-" * (5 - i))
            root2.update()
            root2.after(50)
            mainlbl.config(text="enter PIN: " + "." * 6)
        mainlbl.config(text="Renter PIN: " + "." * 6)
        root2.after(50)
        root2.update()
        mainlbl.config(text="Reenter PIN: " + "." * 6)
        root2.after(50)
        root2.update()
        mainlbl.config(text="Re-enter PIN: " + "." * 6)
        root2.after(50)
        root2.unbind("<Return>")
        root2.update()
for i in range(10):
    root2.bind(str(i), kpress)
root2.bind("<BackSpace>", rmkey)
root2.bind("<Return>", next)
root2.mainloop()