import tkinter as tk
from tkinter import messagebox
from nltk.tokenize import sent_tokenize, word_tokenize

import nltk
nltk.download('punkt')

def summarize_text():
    text = input_text.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Uyarı", "Lütfen özetlenecek bir metin girin.")
        return

    sentences = sent_tokenize(text)
    summary = []
    word_count = 0

    for sentence in sentences:
        words = word_tokenize(sentence)
        if word_count + len(words) <= 50:
            summary.append(sentence)
            word_count += len(words)
        else:
            break

    result = " ".join(summary)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result)

# Arayüz
root = tk.Tk()
root.title("50 Kelimelik Özetleyici")
root.geometry("700x500")

label = tk.Label(root, text="Metninizi girin:", font=("Arial", 12))
label.pack(pady=5)

input_text = tk.Text(root, wrap=tk.WORD, height=10, font=("Arial", 12))
input_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

summarize_button = tk.Button(root, text="Özetle (50 kelime)", command=summarize_text, font=("Arial", 12))
summarize_button.pack(pady=10)

output_label = tk.Label(root, text="Özet:", font=("Arial", 12))
output_label.pack(pady=5)

output_text = tk.Text(root, wrap=tk.WORD, height=6, font=("Arial", 12))
output_text.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

root.mainloop()
