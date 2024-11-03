import tkinter as tk
from tkinter import messagebox
import os

# Yapılan görevlerin kaydolacağı yer
FILE_NAME = "gorevler.txt"

# Ana pencere oluşturma
kok = tk.Tk()
kok.title("Yapılacaklar Listesi")
kok.geometry("500x500")

# Görevlerin oluşumu ve liste
to_do_list = []

listbox = tk.Listbox(kok, width=50, selectmode=tk.SINGLE)
listbox.pack(pady=20)

# Görev girişi (entry_task burada sadece bir kez tanımlandı)
entry_task = tk.Entry(kok, width=50)
entry_task.pack(pady=10)

def add_task():
    task = entry_task.get()
    if task:
        to_do_list.append(task)
        listbox.insert(tk.END, task)
        entry_task.delete(0, tk.END)
        messagebox.showinfo("Başarılı", "Görev başarı ile eklendi.")
    else:
        messagebox.showwarning("Uyarı", "Lütfen bir görev girin.")

def delete_task():
    selected_index = listbox.curselection()
    if selected_index:
        task = listbox.get(selected_index)
        confirm = messagebox.askyesno("Onay", f"'{task}' görevini silmek istediğinize emin misiniz?")
        if confirm:
            listbox.delete(selected_index)
            to_do_list.remove(task)
            messagebox.showinfo("Başarılı", "Görev başarıyla silindi.")
    else:
        messagebox.showwarning("Uyarı", "Lütfen silmek istediğiniz görevi seçin.")

def show_tasks():
    listbox.delete(0, tk.END)
    for task in to_do_list:
        listbox.insert(tk.END, task)

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            tasks = file.readlines()
            for task in tasks:
                task = task.strip()
                if task:
                    to_do_list.append(task)
                    listbox.insert(tk.END, task)

def save_tasks():
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for task in to_do_list:
            file.write(task + "\n")

def exit_app():
    confirm = messagebox.askyesno("Çıkış", "Uygulamadan çıkmak istediğinize emin misiniz?")
    if confirm:
        save_tasks()  # Uygulama kapanmadan önce görevleri kaydet
        kok.destroy()

# Butonlar için bir çerçeve
frame_buttons = tk.Frame(kok)
frame_buttons.pack(pady=10)

# Görev ekle butonu
btn_add = tk.Button(frame_buttons, text="Görev Ekle", width=12, command=add_task)
btn_add.grid(row=0, column=0, padx=5)

# Görev sil butonu
btn_delete = tk.Button(frame_buttons, text="Görev Sil", width=12, command=delete_task)
btn_delete.grid(row=0, column=1, padx=5)

# Görevleri göster butonu
btn_show = tk.Button(frame_buttons, text="Görevleri Göster", width=12, command=show_tasks)
btn_show.grid(row=0, column=2, padx=5)

# Uygulamadan çıkış butonu
btn_exit = tk.Button(kok, text="Çıkış", width=50, command=exit_app)
btn_exit.pack(pady=10)

# Görevleri yükleme
load_tasks()

# Ana döngüyü başlatma
kok.mainloop()
