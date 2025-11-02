import math

def triangulo(b,a):
	area = (b * a)/ 2
	return area
#define funcion triangulo que pide 2 argumentos, calcula el area multiplicando las 2 medidas y dividiendolas entre 2 

def rectangulo(b,a):
        area = (b * a)
        return area
#define funcion rectangulo que pide 2 argumentos, calcula el area multiplicando las 2 medidas	


def circulo(r):
        area = math.pi * (r ** 2)
        return area
#define funcion circulo que pide 2 argumentos, calcula el area elevando el radio al cadrado y multiplicandolo por pi
