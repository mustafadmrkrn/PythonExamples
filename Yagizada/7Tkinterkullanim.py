import tkinter as tk
window = tk.Tk()
window.title("Yağız Ada Selamlaşma Programı")
window.geometry("300x250")

def selamla():
    isim = isim_kutusu.get()
    selam_mesaji = f"Merhaba, {isim}!"
    selam_butonu.config(text=selam_mesaji)

isim_kutusu = tk.Entry(window, font="Arial 12")
isim_kutusu.pack(pady=10)

selam_butonu = tk.Button(window, text="Selamla")
selam_butonu.pack(pady=10)
selam_butonu.config(command=selamla)

window.mainloop()

