import turtle
import time
import random

# Configuration de l'écran
wn = turtle.Screen()
wn.title("Jeu du Serpent")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Désactive les mises à jour de l'écran
# Tête du serpent
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"
# Nourriture du serpent
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)
segments = []
# Stylo pour afficher le score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 Meilleur Score: 0", align="center", font=("Courier", 24, "normal"))


# Fonctions de déplacement
def go_up():


    if head.direction != "down":
        head.direction = "up"


def go_down():


    if head.direction != "up":
        head.direction = "down"


def go_left():


    if head.direction != "right":
        head.direction = "left"


def go_right():


    if head.direction != "left":
        head.direction = "right"


def move():


    if head.direction == "up":
        y = head.ycor()
    head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
    head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
    head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
    head.setx(x + 20)
# Liaisons clavier
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
# Boucle principale du jeu
while True:
 wn.update()
# Vérification des collisions avec les bords
if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
    time.sleep(1)
head.goto(0, 0)
head.direction = "stop"
# Cacher les segments
for segment in segments:
    segment.goto(1000, 1000)
# Réinitialiser le score
score = 0
pen.clear()
pen.write("Score: {} Meilleur Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
# Manger la nourriture
if head.distance(food) < 20:
    x = random.randint(-290, 290)
y = random.randint(-290, 290)
food.goto(x, y)
# Ajouter un segment
new_segment = turtle.Turtle()
new_segment.speed(0)
new_segment.shape("square")
new_segment.color("grey")
new_segment.penup()
segments.append(new_segment)
# Augmenter le score
score += 10
if score > high_score:
    high_score = score
pen.clear()
pen.write("Score: {} Meilleur Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
# Déplacer les segments du serpent
for index in range(len(segments) - 1, 0, -1):
    x = segments[index - 1].xcor()
y = segments[index - 1].ycor()
segments[index].goto(x, y)
if len(segments) > 0:
    x = head.xcor()
y = head.ycor()
segments[0].goto(x, y)
move()
# Fin du jeu
wn.mainloop()
