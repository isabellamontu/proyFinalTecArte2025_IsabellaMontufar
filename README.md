Creamos una archivo csv con infomacion de 100 figuras diferentes (con Touch y lo editamos con nano) llamado figuras.csv

Con git innit iniciamos un repositorio de git vacio

Con git add agregamos figuras.csv al git

Tambien con touch creamos un archivo .py (figurasPrincipal.py)
 
Con nano editamos el archivo para que utiliza un for para mostrar que figura es y sus medidas
Con git add agregamos figurasPrincipal.py al git

Usamos git commit -m "mi primer commit" para agregar un mensaje a los cambios del git 

intalamos los comandos de github con brew install gh

Con gh auth login iniciamos sesion en github

Con git remote add orgin lo metemos a el repositorio en linea 

usamos git branch -M main para renombrar la rama master como main

Ahora utilizamoa git push-u origin main sube los archivos que ya teniamos a github

Ahora usamos pythin3 -m venv /Users/isabella/Desktop/proyectoFinalArte para crear un entorno virtual para instalar python

Y con source /Users/isabella/Desktop/proyectoFinalArte activamos el entorno virtual

Con python3 -m pip install pandas descargamos la libreria pandas

y con python3 figurasPrincipla.py corremos el archivo

Luego con touch creamos funciones.py donde hacemos funciones para calcular areas de triangulos, rectangulos y circulos

Con nano editamos figurasPrincipal.py para agregar las funciones

con git add . lo agregamos al git y con git commit-m agregamos un comentario y con git push -u origin main los subimos
