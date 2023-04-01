"""
Dieses Modul enthält das Snake-Spiel mit tkinter.
"""
import tkinter as tk
import random

# Fenster erstellen
root = tk.Tk()
root.title("Snake")
root.geometry("600x600")
# Canvas erstellen
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# pylint: disable=too-few-public-methods
class Snake:
    """
    Eine Klasse, die die Schlange im Spiel repräsentiert.
    """

    def __init__(self):
        """
        body : list
            Eine Liste von Tupeln, die die Positionen jedes Segments des Schlangenkörpers darstellt.
        direction : str
            Ein String, der die Richtung der Bewegung der Schlange repräsentiert.
        """
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = "Right"

    def move(self):
        """
        Bewegt die Schlange um einen Schritt in ihre aktuelle Richtung.
        """
        # Neue Kopfposition berechnen
        if self.direction == "Up":
            new_head = (self.body[0][0], self.body[0][1] - 10)
        elif self.direction == "Down":
            new_head = (self.body[0][0], self.body[0][1] + 10)
        elif self.direction == "Left":
            new_head = (self.body[0][0] - 10, self.body[0][1])
        elif self.direction == "Right":
            new_head = (self.body[0][0] + 10, self.body[0][1])

        # Neue Kopfposition der Schlange hinzufügen
        self.body.insert(0, new_head)

        # Schwanz der Schlange entfernen
        self.body.pop()


class Food:
    """
    Eine Klasse, die das Essen im Spiel repräsentiert.
    """
    def __init__(self):
        """
        Konstruktor-Methode. Erstellt das Essen an einer zufälligen Position.
        """
        self.position = (random.randint(0, 39) * 10, random.randint(0, 39) * 10)

    def get_position(self):
        """
        Gibt die aktuelle Position des Essens zurück.
        """
        return self.position

    def update_position(self):
        """
        Aktualisiert die Position des Essens, falls es von der Schlange gefressen wurde.
        """
        self.position = (random.randint(0, 39) * 10, random.randint(0, 39) * 10)

def handle_key(event):
    """
    Event-Handler für Tastatureingaben. Ändert die Richtung der Schlange
    entsprechend der gedrückten Pfeiltaste.
    """
    if event.keysym == "Up" and snake.direction != "Down":
        snake.direction = "Up"
    elif event.keysym == "Down" and snake.direction != "Up":
        snake.direction = "Down"
    elif event.keysym == "Left" and snake.direction != "Right":
        snake.direction = "Left"
    elif event.keysym == "Right" and snake.direction != "Left":
        snake.direction = "Right"


def game_loop():
    """
    Spiel-Loop. Wird in jeder Runde des Spiels ausgeführt.
    """
    # pylint: disable=W0603
    # pylint: disable=C0103
    global food

    # Schlange bewegen
    snake.move()

    # Prüfen, ob die Schlange das Essen gefressen hat
    if snake.body[0] == food.position:
        food = Food()
        # Schwanz der Schlange verlängern
        snake.body.append(snake.body[-1])

    # Prüfen, ob die Schlange mit dem Rand kollidiert ist
    # pylint: disable=C0301
    if snake.body[0][0] < 0 or snake.body[0][0] > 600 or snake.body[0][1] < 0 or snake.body[0][1] > 600:
        # Spiel verloren
        print("Rand Getroffen")
        root.destroy()

    # Kollision mit dem Körper der Schlange prüfen
    for i in range(1, len(snake.body)):
        if snake.body[0] == snake.body[i]:
            # Spiel verloren
            print("Game Over")
            root.destroy()
            break

        # Spiel-Fenster löschen und neu zeichnen
        canvas.delete("all")

    # Schlange zeichnen
    for segment in snake.body:
        canvas.create_rectangle(
            segment[0], segment[1], segment[0] + 10, segment[1] + 10, fill="green")

    # Essen zeichnen
    canvas.create_oval(food.position[0], food.position[1],
        food.position[0] + 10, food.position[1] + 10, fill="red")

    # Spiel-Loop in 100ms erneut ausführen
    root.after(100, game_loop)

# Event-Handler für Tastatureingaben registrieren
root.bind("<Up>", handle_key)
root.bind("<Down>", handle_key)
root.bind("<Left>", handle_key)
root.bind("<Right>", handle_key)

# Spielobjekte erstellen
snake = Snake()
food = Food()

# Spiel-Loop starten
game_loop()

# Fenster anzeigen
root.mainloop()
