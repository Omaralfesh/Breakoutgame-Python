from turtle import Turtle
import random

colors = ['green', 'orange', 'yellow', 'pink', 'purple', 'gold', 'gray', 'brown', 'white']
POSITIONS = [(-330, 260), (-165,  260), (0,  260), (165,  260), (330,  260),
             (-330, 240), (-165,  240), (0,  240), (165,  240), (330,  240),
             (-330, 220), (-165,  220), (0,  220), (165,  220), (330,  220)]


class Plates:

    def __init__(self):
        self.all_plates = []
        for position in POSITIONS:
            new_plate = Turtle("square")
            new_plate.shapesize(stretch_wid=1, stretch_len=8)
            new_plate.penup()
            new_plate.color(random.choice(colors))
            self.all_plates.append(new_plate)
            new_plate.goto(position)




