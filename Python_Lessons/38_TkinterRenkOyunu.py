from tkinter import *
import random

# 10 renk seçeneği
colors = ["red", "blue", "green", "yellow", "orange", "purple", "cyan", "pink", "brown", "gray"]
selected_color = ""
score = 0
lives = 5  # Can sayısı

def select_color():
    global selected_color
    selected_color = random.choice(colors)
    color_label.config(text=selected_color.capitalize(), fg=selected_color)

def check_guess(color):
    global score, lives
    if color == selected_color:
        score += 1
        score_label.config(text="Puan: " + str(score))
        select_color()
    else:
        lives -= 1
        lives_label.config(text="Can: " + str(lives))
        if lives == 0:
            end_game()
        else:
            select_color()

def end_game():
    color_label.config(text="Oyun Bitti!", fg="black")
    for widget in color_frame.winfo_children():
        widget.config(state=DISABLED)
    lives_label.config(text="Can: 0")

root = Tk()
root.title("Renk Tahmini Oyunu")

instruction_label = Label(root, text="Lütfen aşağıdaki rengi doğru bir şekilde seçin:", font=("Arial", 12))
instruction_label.pack(pady=10)

color_label = Label(root, text="", font=("Arial", 20))
color_label.pack()

color_frame = Frame(root)
color_frame.pack(pady=10)

# 10 renk düğmeleri
for color in colors:
    button = Button(color_frame, bg=color, width=5, height=2, command=lambda c=color: check_guess(c))
    button.pack(side=LEFT, padx=5)

score_label = Label(root, text="Puan: 0", font=("Arial", 12))
score_label.pack()

lives_label = Label(root, text="Can: 5", font=("Arial", 12))
lives_label.pack()

select_color()

root.mainloop()
