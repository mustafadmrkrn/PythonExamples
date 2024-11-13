import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

# Araba kiralama sistemi
class CarRental:
    def __init__(self, root):
        self.root = root
        self.root.title("Araba Kiralama Sistemi")
        
        # Koyu modda arka plan ve yazı renklerini ayarlıyoruz
        self.root.configure(bg="#2e2e2e")
        
        # Kiralama verilerini tutacak liste
        self.rentals = []

        # Başlık
        self.header_label = tk.Label(self.root, text="Araba Kiralama Sistemi", font=("Arial", 16), fg="white", bg="#2e2e2e")
        self.header_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Marka giriş etiketi ve kutusu
        self.brand_label = tk.Label(self.root, text="Araba Markası:", fg="white", bg="#2e2e2e")
        self.brand_label.grid(row=1, column=0, padx=10, pady=5)
        self.brand_entry = tk.Entry(self.root, bg="#444", fg="white")
        self.brand_entry.grid(row=1, column=1, padx=10, pady=5)

        # Model giriş etiketi ve kutusu
        self.model_label = tk.Label(self.root, text="Araba Modeli:", fg="white", bg="#2e2e2e")
        self.model_label.grid(row=2, column=0, padx=10, pady=5)
        self.model_entry = tk.Entry(self.root, bg="#444", fg="white")
        self.model_entry.grid(row=2, column=1, padx=10, pady=5)

        # Kiralayan kişi giriş etiketi ve kutusu
        self.renter_label = tk.Label(self.root, text="Kiralayan Kişi:", fg="white", bg="#2e2e2e")
        self.renter_label.grid(row=3, column=0, padx=10, pady=5)
        self.renter_entry = tk.Entry(self.root, bg="#444", fg="white")
        self.renter_entry.grid(row=3, column=1, padx=10, pady=5)

        # Başlangıç tarihi etiketi ve kutusu
        self.start_date_label = tk.Label(self.root, text="Başlangıç Tarihi (YYYY-MM-DD):", fg="white", bg="#2e2e2e")
        self.start_date_label.grid(row=4, column=0, padx=10, pady=5)
        self.start_date_entry = tk.Entry(self.root, bg="#444", fg="white")
        self.start_date_entry.grid(row=4, column=1, padx=10, pady=5)

        # Bitiş tarihi etiketi ve kutusu
        self.end_date_label = tk.Label(self.root, text="Bitiş Tarihi (YYYY-MM-DD):", fg="white", bg="#2e2e2e")
        self.end_date_label.grid(row=5, column=0, padx=10, pady=5)
        self.end_date_entry = tk.Entry(self.root, bg="#444", fg="white")
        self.end_date_entry.grid(row=5, column=1, padx=10, pady=5)

        # Araba kiralama butonu
        self.rent_button = tk.Button(self.root, text="Araba Kirala", command=self.rent_car, bg="#444", fg="white")
        self.rent_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Kiralanan araçları listele butonu
        self.list_button = tk.Button(self.root, text="Kiralanan Araçları Listele", command=self.list_rentals, bg="#444", fg="white")
        self.list_button.grid(row=7, column=0, columnspan=2, pady=10)

        # Kiralanan araçların listeleneceği alan
        self.rentals_label = tk.Label(self.root, text="Kiralanan Araçlar:", font=("Arial", 14), fg="white", bg="#2e2e2e")
        self.rentals_label.grid(row=8, column=0, columnspan=2, pady=10)
        
        self.rentals_listbox = tk.Listbox(self.root, height=10, width=50, bg="#444", fg="white")
        self.rentals_listbox.grid(row=9, column=0, columnspan=2, pady=10)

    def rent_car(self):
        # Kullanıcıdan araç bilgileri ve tarih aralığını al
        brand = self.brand_entry.get()
        model = self.model_entry.get()
        renter = self.renter_entry.get()
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()

        # Tarih formatı kontrolü
        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Hata", "Geçersiz tarih formatı! Lütfen YYYY-MM-DD formatında girin.")
            return

        # Araç bilgileri ve tarihlerin eksik olup olmadığını kontrol et
        if not brand or not model or not renter or not start_date or not end_date:
            messagebox.showerror("Hata", "Lütfen tüm alanları doldurun.")
            return

        # Kiralanan araçları kaydet
        self.rentals.append({
            "brand": brand,
            "model": model,
            "renter": renter,
            "start_date": start_date,
            "end_date": end_date
        })

        messagebox.showinfo("Başarılı", f"{brand} {model} modeli, {renter} tarafından {start_date.strftime('%Y-%m-%d')} ile {end_date.strftime('%Y-%m-%d')} arasında kiralandı.")

    def list_rentals(self):
        # Listeyi temizle
        self.rentals_listbox.delete(0, tk.END)

        # Bugünün tarihi
        today = datetime.today()

        # Kiralanan araçları listele
        for rental in self.rentals:
            # Kira süresi bitişi 1 gün kalan araçlar kırmızı renkte olacak
            days_left = (rental['end_date'] - today).days
            rental_info = f"{rental['brand']} {rental['model']} | Kiralayan: {rental['renter']} | {rental['start_date'].strftime('%Y-%m-%d')} - {rental['end_date'].strftime('%Y-%m-%d')}"
            
            # Eğer kira süresi bitişine 1 gün kaldıysa, kırmızı renkte yazdır
            if days_left <= 1:
                self.rentals_listbox.insert(tk.END, rental_info)
                self.rentals_listbox.itemconfig(tk.END, {'fg': 'red'})
            else:
                self.rentals_listbox.insert(tk.END, rental_info)

if __name__ == "__main__":
    root = tk.Tk()
    car_rental_system = CarRental(root)
    root.mainloop()
