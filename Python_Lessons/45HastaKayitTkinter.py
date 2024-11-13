import tkinter as tk
from tkinter import messagebox

class HospitalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hasta İşlem Sistemi")

        # Hasta kayıt ve sağlık kontrolleri durumu için değişkenler
        self.hasta_kayitli = False
        self.hemsire_musait = True
        self.doktor_musait = True
        self.hasta_listesi = []  # Kayıtlı hastaları saklayacak liste

        # Kullanıcı arayüzünü oluştur
        self.create_widgets()

    def create_widgets(self):
        # Hasta ismi için giriş alanı
        self.name_label = tk.Label(self.root, text="Hasta İsmi:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=5)
        
        # Hasta ekleme butonu
        self.add_patient_button = tk.Button(self.root, text="Hasta Ekle", command=self.register_patient)
        self.add_patient_button.pack(pady=10)
        
        # Kayıtlı hastaları gösterecek metin kutusu
        self.hasta_list_textbox = tk.Text(self.root, width=40, height=10, state='disabled')
        self.hasta_list_textbox.pack(pady=10)

        # Sil ve Güncelle butonları
        self.delete_button = tk.Button(self.root, text="Hasta Sil", command=self.delete_patient)
        self.delete_button.pack(side=tk.LEFT, padx=10)

        self.update_button = tk.Button(self.root, text="Hasta Güncelle", command=self.update_patient)
        self.update_button.pack(side=tk.LEFT, padx=10)

    def register_patient(self):
        # Hastayı kaydetme işlemi
        patient_name = self.name_entry.get()
        
        if not patient_name:  # Hasta ismi boş ise
            messagebox.showwarning("Uyarı", "Lütfen hasta ismini girin.")
            return
        
        if patient_name in self.hasta_listesi:  # Hasta zaten kayıtlıysa
            messagebox.showerror("Hata", f"{patient_name} zaten sistemde kayıtlı.")
        else:
            # Yeni hasta kaydetme
            self.hasta_kayitli = True
            self.hasta_listesi.append(patient_name)
            messagebox.showinfo("Bilgi", f"{patient_name} kaydedildi.")
            self.update_hasta_list_textbox()
            self.name_entry.delete(0, tk.END)  # Hasta ismi girişini temizle
            self.check_nurse_availability()

    def update_hasta_list_textbox(self):
        # Metin kutusunu güncelle
        self.hasta_list_textbox.config(state='normal')
        self.hasta_list_textbox.delete(1.0, tk.END)  # Eski içerikleri temizle
        self.hasta_list_textbox.insert(tk.END, "Kayıtlı Hastalar:\n")
        for hasta in self.hasta_listesi:
            self.hasta_list_textbox.insert(tk.END, hasta + "\n")
        self.hasta_list_textbox.config(state='disabled')  # Düzenlenmesini engelle

    def delete_patient(self):
        # Hasta silme işlemi
        patient_name = self.name_entry.get()
        if patient_name in self.hasta_listesi:
            self.hasta_listesi.remove(patient_name)
            messagebox.showinfo("Bilgi", f"{patient_name} silindi.")
            self.update_hasta_list_textbox()
            self.name_entry.delete(0, tk.END)  # Hasta ismi girişini temizle
        else:
            messagebox.showerror("Hata", f"{patient_name} sistemde bulunamadı.")

    def update_patient(self):
        # Hasta güncelleme işlemi
        patient_name = self.name_entry.get()
        if patient_name in self.hasta_listesi:
            new_name = tk.simpledialog.askstring("Güncelleme", f"{patient_name} isimli hastayı yeni bir isimle değiştirin:")
            if new_name:
                index = self.hasta_listesi.index(patient_name)
                self.hasta_listesi[index] = new_name
                messagebox.showinfo("Bilgi", f"{patient_name}, {new_name} olarak güncellendi.")
                self.update_hasta_list_textbox()
                self.name_entry.delete(0, tk.END)  # Hasta ismi girişini temizle
        else:
            messagebox.showerror("Hata", f"{patient_name} sistemde bulunamadı.")

    def check_nurse_availability(self):
        # Hemşire müsaitlik kontrolü
        if self.hemsire_musait:
            self.check_health_status()
        else:
            messagebox.showinfo("Bilgi", "Müsait hemşire için bekle.")

    def check_health_status(self):
        # Sağlık durumu kontrolü
        messagebox.showinfo("Bilgi", "Sağlık durumu kontrolü yapılıyor.")
        self.check_doctor_availability()

    def check_doctor_availability(self):
        # Doktor müsaitlik kontrolü
        if self.doktor_musait:
            self.assign_doctor()
        else:
            messagebox.showinfo("Bilgi", "Müsait doktor için bekle.")

    def assign_doctor(self):
        # Hastayı doktora atama
        messagebox.showinfo("Bilgi", "Hasta doktora atandı.")
        self.perform_examination()

    def perform_examination(self):
        # Muayene işlemi
        messagebox.showinfo("Bilgi", "Muayene yapılıyor.")
        self.reset_system()

    def reset_system(self):
        # Sistem sıfırlama (yeni hasta için)
        self.hasta_kayitli = False
        messagebox.showinfo("Bilgi", "İşlem tamamlandı, yeni hasta için hazır.")

# Tkinter uygulamasını başlat
root = tk.Tk()
app = HospitalApp(root)
root.mainloop()
