import tkinter as tk
pencere = tk.Tk()
pencere.title("To-Do List Uygulaması")
gorev_ekle_etiketi = tk.Label(pencere, text="Yapılacak görevi girin:")
gorev_ekle_girdi = tk.Entry(pencere)
gorev_ekle_buton = tk.Button(pencere, text="Görev Ekle")

gorevler_goster_liste = tk.Listbox(pencere)

gorev_sil_etiketi = tk.Label(pencere, text="Silmek istediğiniz görevi girin:")
gorev_sil_girdi = tk.Entry(pencere)
gorev_sil_buton = tk.Button(pencere, text="Görev Sil")

cikis_buton = tk.Button(pencere, text="Çıkış")
gorev_ekle_etiketi.pack()
gorev_ekle_girdi.pack()
gorev_ekle_buton.pack()

gorevler_goster_liste.pack()

gorev_sil_etiketi.pack()
gorev_sil_girdi.pack()
gorev_sil_buton.pack()

cikis_buton.pack()
def gorev_ekle():
    task = gorev_ekle_girdi.get()
    to_do_list.append(task)
    gorevler_goster_liste.insert(tk.END, task)
    gorev_ekle_girdi.delete(0, tk.END)

def gorev_sil():
    task = gorev_sil_girdi.get()
    if task in to_do_list:
        to_do_list.remove(task)
        index = gorevler_goster_liste.get(0, tk.END).index(task)
        gorevler_goster_liste.delete(index)
        gorev_sil_girdi.delete(0, tk.END)

def cikis():
    pencere.destroy()

gorev_ekle_buton.config(command=gorev_ekle)
gorev_sil_buton.config(command=gorev_sil)
cikis_buton.config(command=cikis)
pencere.mainloop()
