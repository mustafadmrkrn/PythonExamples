import tkinter as tk
from tkinter import messagebox
def gorev_ekle():
    yeni_gorev = gorev_kutusu.get()
    if yeni_gorev != "":
        gorev_listesi.insert(tk.END, yeni_gorev)
        gorev_kutusu.delete(0, tk.END)
    else:
        messagebox.showwarning("Uyarı", "Lütfen bir görev girin!")
def gorev_sil():
    try:
        secili_indeks = gorev_listesi.curselection()[0]
        gorev_listesi.delete(secili_indeks)
    except IndexError:
        messagebox.showwarning("Uyarı", "Lütfen silinecek bir görev seçin!")

#ana pencere oluşturma
pencere = tk.Tk()
pencere.title("Görev Listesi")
pencere.geometry("400x300")

tk.Label(pencere, text="Yeni Görev:", fg="black").pack(pady=5)
gorev_kutusu = tk.Entry(pencere, fg="black", bg="white", insertbackground="black", width=25)
gorev_kutusu.pack(pady=5)

gorev_ekle_butonu = tk.Button(pencere, text="Görev Ekle", command=gorev_ekle, fg="white", bg="blue")
gorev_ekle_butonu.pack(pady=5)

gorev_sil_butonu = tk.Button(pencere, text="Görev Sil", command=gorev_sil, fg="white", bg="red")
gorev_sil_butonu.pack(pady=5)

tk.Label(pencere, text="Görev Listesi:", fg="black").pack(pady=5)
gorev_listesi = tk.Listbox(pencere, fg="black", bg="white", width=25)
gorev_listesi.pack(pady=5)

pencere.mainloop()