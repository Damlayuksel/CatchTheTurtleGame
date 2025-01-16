import turtle
import random

# Ekran ve temel ayarlar
screen = turtle.Screen()
screen.bgcolor("pink")
screen.title("Turtle Game")
FONT = ('Arial', 30, 'normal')

# Zorluk seviyesi ayarları
difficulty_settings = {
    "Easy": {"show_time": 1000, "game_time": 20},
    "Medium": {"show_time": 500, "game_time": 15},
    "Hard": {"show_time": 200, "game_time": 10}
}

difficulty = "Easy"  # Varsayılan zorluk seviyesi
score = 0
game_over = False

# Kaplumbağalar
turtle_list = []

# Skor ve geri sayım göstergesi
score_display = turtle.Turtle()
countdown_turtle = turtle.Turtle()


def setup_score_turtle():
    """Skor göstergesi için kaplumbağayı hazırlar."""
    score_display.hideturtle()
    score_display.color("black")
    score_display.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    score_display.setpos(0, y)
    score_display.write(arg="Score=0", move=False, align="center", font=FONT)


grid_size = 50  # Daha büyük bir grid boyutu belirlendi.


def make_turtle(x, y):
    """Belirtilen (x, y) koordinatlarında bir kaplumbağa oluşturur."""
    t = turtle.Turtle()

    def click(x, y):
        """Kaplumbağa tıklandığında skor artırır."""
        global score
        if t.isvisible():  # Yalnızca görünen kaplumbağalar tıklanabilir
            score += 1
            score_display.clear()
            score_display.write(arg="Score= {}".format(score), move=False, align="center", font=FONT)
            t.hideturtle()  # Tıklandıktan sonra kaplumbağa kaybolur

    t.onclick(click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("violet")
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)


x_coordinates = [-4, -2, 0, 2, 4]  # Daha geniş bir alanda kaplumbağalar konumlandırıldı.
y_coordinates = [4, 2, 0, -2, -4]


def set_turtles():
    """Tüm kaplumbağaları başlatır."""
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)
    


def hide_turtles():
    """Tüm kaplumbağaları gizler."""
    for t in turtle_list:
        t.hideturtle()


def show_randomly():
    """Rastgele bir kaplumbağayı gösterir."""
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        show_time = difficulty_settings[difficulty]["show_time"]
        screen.ontimer(show_randomly, show_time)


def countdown(time):
    """Geri sayım yapar."""
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.color("red")
    countdown_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.9 - 30
    countdown_turtle.setpos(0, y)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.write(arg=f"Time={time}", move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over", move=False, align="center", font=FONT)


def select_difficulty():
    """Zorluk seviyesini seçtirir."""
    global difficulty
    difficulty = screen.textinput("Difficulty", "Choose difficulty: Easy, Medium, Hard")
    if difficulty not in difficulty_settings:
        print("Invalid difficulty level! Closing game...")
        screen.bye()  # Geçerli bir seviye seçilmezse oyunu kapat



def start_game():
    """Oyunu başlatır."""
    
    hide_turtles()
    set_turtles()
    setup_score_turtle()
    show_randomly()
    game_time = difficulty_settings[difficulty]["game_time"]
    countdown(game_time)


# Ana işleyici
select_difficulty()  # Zorluk seviyesi seçimi
if difficulty in difficulty_settings:
    
    start_game()

turtle.mainloop()
