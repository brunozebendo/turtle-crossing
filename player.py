from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

'''código para definir o formato, a localização e a posição da tartaruga.
 Reparar que criou a classe, criou o método iniciar __init__ que é um método
  construtor, ele indica que ali vai ser construída uma classe.
Passou o método dentro da função e estabeleceu a velocidade no começo do código,
 o que facilita caso se queira alterar'''

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
