import tkinter as tk
window = tk.Tk()
window.title("İlk Deneme")
window.geometry("200x400")

mesaj = tk.Label(window, text="Yağız Ada Tkinter# Kullanıyor",font="Arial 12 bold", fg="blue")
mesaj.pack(pady=20)    
window.mainloop()