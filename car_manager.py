from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

'''a lógica do código é criar os carros no formato quadrado, nas medidas 2 por 1
 com a cores escolhidas
de forma randômica dentro do dicionário, o random_y determina a posição do carro
 na tela,
 também de forma randômica e o new_car.goto determina a posição inicial.
  Depois, a função: move_cars determina que os itens no dicionário vazio all_cars voltarão da distância inicial ao passo de 5 pixels por segundo. 
  A condição random_chance foi criada porque o código estava gerando os carros
   de maneira randômica com muita  frequência, assim, a lógica é que a cada
    seis ciclos que o jogo rodar, no novo ciclo (1) ele vai gerar novos carros,
     o que diminuiu a quantidade de carros gerado.'''
class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
