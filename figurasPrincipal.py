import pandas as pd
#importar libreria pandas
from funciones import triangulo, circulo, rectangulo

#importar funciones de area

dataFile = pd.read_csv("figuras.csv")
#guardar la informacion de figuras en dataFile


print("Procesando Figuras...\n")
#imprimir mensaje de que esta procesando figuras

for index, row in dataFile.iterrows():
	print(f"Fila {index} : FIGURA= {row['FIGURA']}, Medida1 = {row['MEDIDA1']}, Medida2 ={row['MEDIDA2']}")
	if row['FIGURA'] == "t":
		area = triangulo(row['MEDIDA1'], row['MEDIDA2'])
	elif row['FIGURA'] == "c":
                area = circulo(row['MEDIDA1'])
	elif row['FIGURA'] == "r":
                area = rectangulo(row['MEDIDA1'], row['MEDIDA2'])
	print(f"Area = {area} ")
#imprime cada digura con sus medidas, identifica que figura es y dependiendo de que figura es utiliza diferente funcion para calcular el area 
