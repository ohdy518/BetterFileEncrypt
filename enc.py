import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as tkfd
import pyAesCrypt as pcrypt
import time, os

filelist = []

root = tk.Tk()
root.title("File Encryption")
root.iconbitmap("app.ico")
root.attributes("-toolwindow", True)
root.attributes("-topmost", True)
root.geometry("600x400")
pcg = 0
est = 0
eta = 0
frun = True


def fopen(_=any):
    files = tkfd.askopenfilenames(parent=root, title="Select files to encrypt", filetypes=[("All Files", "*.*")])
    for i in files:
        filelist.append(i)
    deslbl.config(text=f"{str(len(filelist))} file(s) selected: {time.time()}")
def spin(_=any):
    deslbl.config(text=f"New window will open: {time.time()}")
    os.system("python .\\setpin.py")
def enc(_=any):
    global pcg, frun, est, eta
    deslbl.config(text=f"Encrypting: {time.time()}")
    pwf = open("pin.data", "r")
    pw = pwf.read()
    pwf.close()
    pwf = open("pin.data", "w")
    pwf.write("")
    pwf.close()
    for i in filelist:
        if frun:
            st = time.time()
        pcrypt.encryptFile(i, i + ".enc", pw)
        pgbar["value"] += 100 / (len(filelist) * 2)
        pcg += 100 / (len(filelist) * 2)
        pgdes.config(text=f"{round(pcg, 2)}%")
        root.update()
        if frun:
            et = time.time()
            est = et - st
            eta = (et - st) * len(filelist)
            frun = False
        eta -= est
        etalbl.config(text=f"ETA: {round(eta, 2)}s")
    deslbl.config(text=f"Encrypted: {time.time()}")
    deslbl.config(text=f"Replacing: {time.time()}")
    for i in filelist:
        os.replace(i + ".enc", i)
        pgbar["value"] += 100 / (len(filelist) * 2)
        pcg += 100 / (len(filelist) * 2)
        pgdes.config(text=f"{round(pcg, 2)}%")
        root.update()
    deslbl.config(text=f"Replaced: {time.time()}")
    etalbl.config(text=f"ETA: 0s")
openbtn = tk.Button(root, text="Open", font=("Consolas", 12), command=fopen)
openbtn.pack()
openbtn.place(x=12, y=12)
pwbtn = tk.Button(root, text="Set PIN", font=("Consolas", 12), command=spin)
pwbtn.pack()
pwbtn.place(x=12, y=60)
encbtn = tk.Button(root, text="Encrypt", font=("Consolas", 12), command=enc)
encbtn.pack()
encbtn.place(x=12, y=108)
pgbar = ttk.Progressbar(root, orient="horizontal", length=500, mode="determinate")
pgbar.pack()
pgbar.place(x=12, y=156)
pgdes = tk.Label(root, text="0%", font=("Consolas", 12))
pgdes.pack()
pgdes.place(x=520, y=156)
deslbl = tk.Label(root, text="", font=("Consolas", 12))
deslbl.pack()
deslbl.place(x=12, y=204)
etalbl = tk.Label(root, text="ETA: [Not running]", font=("Consolas", 12))
etalbl.pack()
etalbl.place(x=12, y=240)
root.mainloop()