
from flask import Flask, render_template,request# render_template es la biblioteca/funcion que genera la vista para que se pueda ver

app= Flask(__name__) #declaracion o inicializacion del servidor flask, se declara una variable app 

#configuraciones para la base de datos
app.config['MYSQL_HOST']= "localhost" #en el localhost porque es dinde se coren los servicios que se quieren , se especifica a donde se quiere conectar
app.config['MYSQL_USER']= "root" #el usuario que se va a utilizar
app.config['MYSQL_PASSWORD']= ""  # la contraseña, y se esta por default va solo las comillas
app.config['MYSQL_BD']= "bdflask" #base de datos a la que se quiere conectar 

#declaracion de rutas

#ruta index http://localhost:5000
#la ruta se compone del nombre de la ruta y su funcion
@app.route('/')#busca la ruta principal, declaras la ruta quien tiene una diagonal, la diagonal esta por defaut
def index():#esa ruta necesita una funcion, qui se llama index
    return render_template('index.html')# aqui lo que se quiere que hagas



@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method == 'POST':
        titulo= request.form['txtTitulo']
        artista= request.form['txtArtista']
        anio= request.form['txtAnio']
        print(titulo,artista,anio)


    return "La info del Album llego a su ruta, Amigo ;)"

@app.route('/eliminar')
def eliminar():
    return "Se elimino el album de la BD"


#ejecucion del servidor
if __name__== '__main__':
    app.run(port= 5000,debug=True)
