import tkinter as tk
import random

def restart_game(event):
    global segments, x_direction, y_direction, IN_GAME
    segments = [(100, 100), (80, 100), (60, 100)]
    x_direction, y_direction = 20, 0
    IN_GAME = True
    initialize()

# Oyun alanı boyutları
WIDTH, HEIGHT = 400, 400
SEG_SIZE = 20  # Yılan parçası boyutu
IN_GAME = True

# Yılanın başlangıç konumu ve hareket yönü
segments = [(100, 100), (80, 100), (60, 100)]
x_direction, y_direction = 20, 0  # Yılanın başlangıç hareketi sağa doğru

# Yeni yiyecek konumu oluşturma
def create_food():
    pos_x = random.randint(0, (WIDTH-SEG_SIZE) // SEG_SIZE) * SEG_SIZE
    pos_y = random.randint(0, (HEIGHT-SEG_SIZE) // SEG_SIZE) * SEG_SIZE
    return pos_x, pos_y

food_position = create_food()

score = 0

def initialize():
    global food_position, score
    food_position = create_food()
    score = 0
    move()

def move():
    global IN_GAME, score
    if IN_GAME:
        new_head = (segments[0][0] + x_direction, segments[0][1] + y_direction)
        if (
            new_head in segments[1:]
            or not 0 <= new_head[0] < WIDTH
            or not 0 <= new_head[1] < HEIGHT
        ):
            IN_GAME = False
        else:
            segments.insert(0, new_head)
            if new_head == food_position:
                initialize_food()
                score += 1  # Skoru arttır
            else:
                segments.pop()
        draw_canvas()
        window.after(100, move)
    else:
        game_over()

def draw_canvas():
    canvas.delete(tk.ALL)
    canvas.create_text(
        WIDTH - 50,
        10,
        text=f"Skor: {score}",
        fill="white",
        font=("Arial", 12),
        anchor=tk.NE  # Sağ üst köşe hizalaması
    )

def initialize():
    global food_position
    food_position = create_food()
    move()

def move():
    global IN_GAME
    if IN_GAME:
        new_head = (segments[0][0] + x_direction, segments[0][1] + y_direction)
        if (
            new_head in segments[1:]
            or not 0 <= new_head[0] < WIDTH
            or not 0 <= new_head[1] < HEIGHT
        ):
            IN_GAME = False
        else:
            segments.insert(0, new_head)
            if new_head == food_position:
                initialize_food()
            else:
                segments.pop()
        draw_canvas()
        window.after(100, move)
    else:
        game_over()

def initialize_food():
    global food_position
    food_position = create_food()

def change_direction(new_direction):
    global x_direction, y_direction
    if new_direction == 'Left' and x_direction != SEG_SIZE:
        x_direction = -SEG_SIZE
        y_direction = 0
    elif new_direction == 'Right' and x_direction != -SEG_SIZE:
        x_direction = SEG_SIZE
        y_direction = 0
    elif new_direction == 'Up' and y_direction != SEG_SIZE:
        x_direction = 0
        y_direction = -SEG_SIZE
    elif new_direction == 'Down' and y_direction != -SEG_SIZE:
        x_direction = 0
        y_direction = SEG_SIZE

def draw_canvas():
    canvas.delete(tk.ALL)
    canvas.create_rectangle(
        food_position[0],
        food_position[1],
        food_position[0] + SEG_SIZE,
        food_position[1] + SEG_SIZE,
        fill="red"
    )
    for segment in segments:
        canvas.create_rectangle(
            segment[0],
            segment[1],
            segment[0] + SEG_SIZE,
            segment[1] + SEG_SIZE,
            fill="black"
        )

def game_over():
    canvas.delete(tk.ALL)
    canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2,
        text="Oyun Bitti!",
        fill="red",
        font=("Arial", 30)
    )

window = tk.Tk()
window.title("Yılan Oyunu")
window.resizable(False, False)

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="green")
canvas.pack()

window.bind('<Left>', lambda event: change_direction('Left'))
window.bind('<Right>', lambda event: change_direction('Right'))
window.bind('<Up>', lambda event: change_direction('Up'))
window.bind('<Down>', lambda event: change_direction('Down'))

window.bind('<r>', restart_game)

initialize()  # Oyunu başlat
window.mainloop()
