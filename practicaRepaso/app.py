from flask import Flask, render_template,request, redirect,url_for,flash# render_template es la biblioteca/funcion que genera la vista para que se pueda ver
from flask_mysqldb import MySQL

app= Flask(__name__) #declaracion o inicializacion del servidor flask, se declara una variable app 


app.config['MYSQL_HOST']= "localhost" 
app.config['MYSQL_USER']= "root"
app.config['MYSQL_PASSWORD']= ""  
app.config['MYSQL_DB']= "db_fruteria" 

app.secret_key='mysecretkey'

mysql= MySQL(app)


@app.route('/')
def inicio():
   curSelect= mysql.connection.cursor()
   curSelect.execute('select * from tbfrutas')
   consulta= curSelect.fetchall() 

   return render_template('EditarEliminar.html' )



@app.route('/registrar',methods=['POST'])
def registrar():
    if request.method == 'POST':
        Vfruta= request.form['txtFruta']
        Vtemporada= request.form['txtTemporada']
        Vprecio= request.form['txtPrecio']
        Vstock= request.form['txtStock']
        CS= mysql.connection.cursor()
        CS.execute('insert into tbfrutas(fruta,temporada,precio,stock) values (%s,%s,%s,%s)',(Vfruta,Vtemporada,Vprecio,Vstock))
        mysql.connection.commit()

    flash('Datos agregados correctamente')
    return redirect(url_for('inicio'))


@app.route('/editar/<id>')
def editar(id): 
    curEditar=mysql.connection.cursor()
    curEditar.execute('select * from tbfrutas where id= %s ',(id,))
    consultaId= curEditar.fetchone()
    return render_template('EditarEliminar.html', fruta= consultaId)
    

@app.route('/actualizar/<id>',methods=['POST'])
def actualizar(id):
    if request.method == 'POST':
        Vfruta= request.form['txtFruta']
        Vtemporada= request.form['txtTemporada']
        Vprecio= request.form['txtPrecio']
        Vstock= request.form['txtStock']

        cursorCon= mysql.connection.cursor()
        cursorCon.execute('update tbfrutas set fruta=%s, temporada= %s, precio=%s, stock=%s where id= %s',(Vfruta,Vtemporada,Vprecio,Vstock,id))
        mysql.connection.commit()

    flash('Los datos se actualizaron en la BD')
    return redirect(url_for('consultas'))
    




#ejecucion del servidor
if __name__== '__main__':
    app.run(port= 5000,debug=True)
