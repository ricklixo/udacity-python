import turtle


def quadrado(linhas):
    for i in range(1, 5):
        linhas.forward(100)
        linhas.right(90)

def triangulo(linhas):
    for t in range(1, 4):
        linhas.forward(100)
        linhas.right(120)

def desenhar():
    window = turtle.Screen()
    window.bgcolor('black')

    quad = turtle.Turtle() # Cria uma instância da classe Turtle
    quad.speed(2)
    quad.color('green')
    quadrado(quad)  # chama a função quadrado com os argumentos da variável QUAD.

    circulo = turtle.Turtle()
    circulo.shape('arrow')
    circulo.color('yellow')
    circulo.circle(100)
    quad.color('red')

    triangulo(quad) # chama a função quadrado utilizando as variáveis QUAD.

    window.exitonclick()
    return

desenhar()
