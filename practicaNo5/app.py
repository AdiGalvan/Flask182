
from flask import Flask, render_template,request, redirect,url_for,flash# render_template es la biblioteca/funcion que genera la vista para que se pueda ver
from flask_mysqldb import MySQL

app= Flask(__name__) #declaracion o inicializacion del servidor flask, se declara una variable app 

#configuraciones para la base de datos
app.config['MYSQL_HOST']= "localhost" #en el localhost porque es dinde se coren los servicios que se quieren , se especifica a donde se quiere conectar
app.config['MYSQL_USER']= "root" #el usuario que se va a utilizar
app.config['MYSQL_PASSWORD']= ""  # la contraseña, y se esta por default va solo las comillas
app.config['MYSQL_DB']= "flask" #base de datos a la que se quiere conectar

app.secret_key='mysecretkey'

mysql= MySQL(app)

#declaracion de rutas

#ruta index http://localhost:5000
#la ruta se compone del nombre de la ruta y su funcion
@app.route('/')#busca la ruta principal, declaras la ruta quien tiene una diagonal, la diagonal esta por defaut
def index():#esa ruta necesita una funcion, aqui se llama index
   curSelect= mysql.connection.cursor()#objeto que va a hacer la selección
   curSelect.execute('select * from albums')#se usa el objeto creado arriba y esta es la consulta
   consulta= curSelect.fetchall() #se crea la variable consulta, contiene los elementos de la tabla en una lista
   print(consulta)

   return render_template('index.html',listAlbums=consulta )# aqui da lo que se quiere que hagas, tambien concatena la ruta que se le manda , lo que hace es abrir la ruta y llevarse la consulta



@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method == 'POST':
        Vtitulo= request.form['txtTitulo']
        Vartista= request.form['txtArtista']
        Vanio= request.form['txtAnio']
       # print(titulo,artista,anio)
        CS= mysql.connection.cursor()
        CS.execute('insert into albums(titulo,artista,anio) values (%s,%s,%s)',(Vtitulo, Vartista, Vanio))
        mysql.connection.commit()

    flash('Album Agregado correctamente')
    return redirect(url_for('index'))#redirecciona al index

@app.route('/editar/<id>')
def editar(id):
    curEditar=mysql.connection.cursor()
    curEditar.execute('select * from albums where id= %s ',(id,))
    consulId= curEditar.fetchone()
    return render_template('EditarAlbum.html', album= consulId)#render template muestra una vista
    

@app.route('/actualizar/<id>',methods=['POST'])#actualizar va a estar trabajando con un parametro que es id
def actualizar(id):#aqui se pasa el parametro id
    if request.method == 'POST':#se verifica si viene algo con post
        Vtitulo= request.form['txtTitulo']#despues se vacea en las variables vtitulo, vartista, vanio
        Vartista= request.form['txtArtista']
        Vanio= request.form['txtAnio']

        curAct= mysql.connection.cursor()
        curAct.execute('update albums set titulo=%s, artista= %s, anio=%s where id= %s',(Vtitulo,Vartista,Vanio,id))#procede a ejecutar el query
        mysql.connection.commit()#con esto se confirma la actualizacion para que sea un hecho que ya se actualizo 

    flash('Album ActualiZado en BD')
    return redirect(url_for('index'))




    

@app.route('/eliminar')
def eliminar():
    return "Se elimino el album de la BD"


#ejecucion del servidor
if __name__== '__main__':
    app.run(port= 5000,debug=True)
